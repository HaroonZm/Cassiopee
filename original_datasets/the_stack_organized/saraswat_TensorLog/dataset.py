# (C) William W. Cohen and Carnegie Mellon University, 2016

import sys
import re
import math
import os.path
import collections
import scipy.sparse as SS
import scipy.io as SIO
import numpy as NP
import numpy.random as NR
import logging

from tensorlog import config
from tensorlog import mutil
from tensorlog import matrixdb
from tensorlog import declare
from tensorlog import util

conf = config.Config()
conf.normalize_outputs = True;  conf.help.normalize_outputs =  "In .exam files, l1-normalize the weights of valid outputs"

#
# dealing with labeled training data
#

class Dataset(object):

    def __init__(self,xDict,yDict):
        # dict which maps mode declaration to X matrices for training
        self.xDict = xDict
        # likewise for Y matrices
        self.yDict = yDict

    def isSinglePredicate(self):
        """Returns true if all the examples are for a single predicate."""
        return len(list(self.xDict.keys()))==1

    def extractMode(self,mode):
        """Return a new Dataset that just contains this mode."""
        assert mode in self.xDict, 'dataset does not contain mode %s' % str(mode)
        return Dataset({mode:self.xDict[mode]}, {mode:self.yDict[mode]})

    def modesToLearn(self):
        """Return list of modes associated with the data."""
        return list(self.xDict.keys())

    def hasMode(self,mode):
        """True if there are examples of the mode in the dataset."""
        return (mode in self.yDict and mode in self.xDict)

    def getX(self,mode):
        """Get a matrix of all inputs for the mode."""
        return self.xDict[mode]

    def getY(self,mode):
        """Get a matrix of all desired outputs for the mode."""
        return self.yDict[mode]

    def size(self):
        return sum([m.nnz for m in list(self.xDict.values())]) + sum([m.nnz for m in list(self.yDict.values())])

    def shuffle(self):
        for mode in self.xDict:
            shuffledRowNums = NP.arange(mutil.numRows(self.xDict[mode]))
            NR.shuffle(shuffledRowNums)
            self.xDict[mode] = mutil.shuffleRows(self.xDict[mode],shuffledRowNums)
            self.yDict[mode] = mutil.shuffleRows(self.yDict[mode],shuffledRowNums)

    def minibatchIterator(self,batchSize=100,shuffleFirst=True):
        """Iterate over triples (mode,X',Y') where X' and Y' are sets of
        batchSize rows from the full data for mode, randomly selected
        (without replacement) from the dataset."""
        # randomize the order of the examples
        if shuffleFirst: self.shuffle()
        # then sample an ordering of the modes
        modeList =  self.modesToLearn()
        modeSampleDict = {}
        for modeIndex,mode in enumerate(modeList):
            numBatches = int(math.ceil( mutil.numRows(self.getX(mode)) / float(batchSize) ))
            modeSampleDict[mode] = NP.ones(numBatches,dtype='int')*modeIndex
        modeSamples = NP.concatenate(list(modeSampleDict.values()))
        NR.shuffle(modeSamples)
        # finally produce the minibatches
        currentOffset = [0] * len(modeList)
        for modeIndex in modeSamples:
            mode = modeList[modeIndex]
            lo = currentOffset[modeIndex]
            bX = mutil.selectRows(self.getX(mode),lo,lo+batchSize)
            bY = mutil.selectRows(self.getY(mode),lo,lo+batchSize)
            currentOffset[modeIndex] += batchSize
            yield mode,bX,bY

    def pprint(self):
        return ['%s: X %s Y %s' % (str(mode),mutil.pprintSummary(self.xDict[mode]),mutil.pprintSummary(self.yDict[mode])) for mode in self.xDict]

    #
    # i/o and conversions
    #

    def serialize(self,dir):
        """Save the dataset on disk."""
        if not os.path.exists(dir):
            os.mkdir(dir)
        dx = dict([(str(k_v[0]),k_v[1]) for k_v in list(self.xDict.items())])
        dy = dict([(str(k_v[0]),k_v[1]) for k_v in list(self.yDict.items())])
        SIO.savemat(os.path.join(dir,"xDict"),dx,do_compression=True)
        SIO.savemat(os.path.join(dir,"yDict"),dy,do_compression=True)

    @staticmethod
    def deserialize(dir):
        """Recover a saved dataset."""
        logging.info('deserializing dataset file '+ dir)
        xDict = {}
        yDict = {}
        SIO.loadmat(os.path.join(dir,"xDict"),xDict)
        SIO.loadmat(os.path.join(dir,"yDict"),yDict)
        #serialization converts modes to strings so convert them
        #back.... it also converts matrices to csr
        for d in (xDict,yDict):
            for stringKey,mat in list(d.items()):
                del d[stringKey]
                if not stringKey.startswith('__'):
                   d[declare.asMode(stringKey)] = SS.csr_matrix(mat)
        dset = Dataset(xDict,yDict)
        logging.info('deserialized dataset has %d modes and %d non-zeros' % (len(dset.modesToLearn()), dset.size()))
        return dset


    @staticmethod
    def uncacheExamples(dsetFile,db,exampleFile,proppr=True):
        """Build a dataset file from an examples file, serialize it, and
        return the de-serialized dataset.  Or if that's not necessary,
        just deserialize it.
        """
        if not os.path.exists(dsetFile) or os.path.getmtime(exampleFile)>os.path.getmtime(dsetFile):
            logging.info('serializing examples in %s to %s' % (exampleFile,dsetFile))
            dset = Dataset.loadExamples(db,exampleFile,proppr=proppr)
            dset.serialize(dsetFile)
            os.utime(dsetFile,None) #update the modification time for the directory
            return dset
        else:
            return Dataset.deserialize(dsetFile)

    @staticmethod
    def uncacheMatrix(dsetFile,db,functorToLearn,functorInDB):
        """Build a dataset file from a DB matrix as specified with loadMatrix
        and serialize it.  Or if that's not necessary, just
        deserialize it.
        """
        if not os.path.exists(dsetFile):
            print(('preparing examples from',functorToLearn,'...'))
            dset = Dataset.loadMatrix(db,functorToLearn,functorInDB)
            print(('serializing dsetFile',dsetFile,'...'))
            dset.serialize(dsetFile)
            return dset
        else:
            print(('de-serializing dsetFile',dsetFile,'...'))
            return Dataset.deserialize(dsetFile)

    # TODO remove or make type-aware
    @staticmethod
    def loadMatrix(db,functorToLearn,functorInDB):
        """Convert a DB matrix containing pairs x,f(x) to training data for a
        learner.  For each row x with non-zero entries, copy that row
        to Y, and and also append a one-hot representation of x to the
        corresponding row of X.
        """
        assert db.isTypeless(),'cannot run loadMatrix on database with defined types'
        functorToLearn = declare.asMode(functorToLearn)
        xrows = []
        yrows = []
        m = db.matEncoding[(functorInDB,2)].tocoo()
        n = db.dim()
        for i in range(len(m.data)):
            x = m.row[i]
            xrows.append(SS.csr_matrix( ([1.0],([0],[x])), shape=(1,n) ))
            rx = m.getrow(x)
            yrows.append(rx * (1.0/rx.sum()))
        return Dataset({functorToLearn:mutil.stack(xrows)},{functorToLearn:mutil.stack(yrows)})

    @staticmethod
    def _parseLine(line,proppr=True):
        #returns mode, x, positive y's where x and ys are symbols
        if not line.strip() or line[0]=='#':
            return None,None,None
        parts = line.strip().split("\t")
        if not proppr:
            assert len(parts)>=2, 'bad line: %r parts %r' % (line,parts)
            return declare.asMode(parts[0]+"/io"),parts[1],parts[2:]
        else:
            regex = re.compile('(\w+)\((\w+),(\w+)\)')
            mx = regex.search(parts[0])
            if not mx:
                return None,None,None
            else:
                mode = declare.asMode(mx.group(1)+"/io")
                x = mx.group(2)
                pos = []
                for ans in parts[1:]:
                    label = ans[0]
                    my = regex.search(ans[1:])
                    assert my,'problem at line '+line
                    assert my.group(1)==mode.functor,'mismatched modes %s %s at line %s' % (my.group(1),mode,line)
                    assert my.group(2)==x,'mismatched x\'s at line '+line
                    if label=='+':
                        pos.append(my.group(3))
                return mode,x,pos

    @staticmethod
    def loadProPPRExamples(db,fileName):
        """Convert a proppr-style foo.examples file to a two dictionaries of
        modename->matrix pairs, one for the Xs, one for the Ys"""
        return Dataset.loadExamples(db,fileName,proppr=True)

    @staticmethod
    def loadExamples(db,fileName,proppr=False):
        """Convert foo.exam file, where each line is of the form

          functor <TAB> x <TAB> y1 ... yk

        to two dictionaries of modename->matrix pairs, one for the Xs,
        one for the Ys.

        """
        logging.info('loading examples from '+ str(fileName))

        # map from relation to lists that buffer data,row
        # index,colindex information for each of the X,Y matrices
        xDatabuf = collections.defaultdict(list)
        xRowbuf = collections.defaultdict(list)
        xColbuf = collections.defaultdict(list)
        yDatabuf = collections.defaultdict(list)
        yRowbuf = collections.defaultdict(list)
        yColbuf = collections.defaultdict(list)
        xsResult = {}
        ysResult = {}
        def getId(typeName,symbol):
          s = symbol if db.schema.hasId(typeName,symbol) else matrixdb.OOV_ENTITY_NAME
          return db.schema.getId(typeName,s)
        for line in util.linesIn(fileName):
          pred,x,ys = Dataset._parseLine(line,proppr=proppr)
          if pred:
            xType = db.schema.getDomain(pred.getFunctor(),2)
            yType = db.schema.getRange(pred.getFunctor(),2)
            row_index = len(xDatabuf[pred])
            xDatabuf[pred].append(1.0)
            xRowbuf[pred].append(row_index)
            xColbuf[pred].append(getId(xType,x))
            for y in ys:
              yDatabuf[pred].append( 1.0/len(ys) if conf.normalize_outputs else 1.0)
              yRowbuf[pred].append(row_index)
              yColbuf[pred].append(getId(yType,y))
        for pred in list(xDatabuf.keys()):
          xType = db.schema.getDomain(pred.getFunctor(),2)
          yType = db.schema.getRange(pred.getFunctor(),2)
          nrows = len(xDatabuf[pred])
          coo_x = SS.coo_matrix((xDatabuf[pred],(xRowbuf[pred],xColbuf[pred])), shape=(nrows,db.dim(xType)))
          xsResult[pred] = SS.csr_matrix(coo_x,dtype='float32')
          coo_y = SS.coo_matrix((yDatabuf[pred],(yRowbuf[pred],yColbuf[pred])), shape=(nrows,db.dim(yType)))
          ysResult[pred] = SS.csr_matrix(coo_y,dtype='float32')
        dset = Dataset(xsResult,ysResult)
        logging.info('loaded dataset has %d modes and %d non-zeros' % (len(dset.modesToLearn()), dset.size()))
        logging.info('in loaded dataset, example normalization (so sum_{y} score[pred(x,y)] == 1) is %r' % conf.normalize_outputs)
        return dset

    #TODO refactor to also save examples in form: 'functor X Y1
    #... Yk'
    def saveProPPRExamples(self,fileName,db,append=False,mode=None):
        """Convert X and Y to ProPPR examples and store in a file."""
        fp = open(fileName,'a' if append else 'w')
        modeKeys = [mode] if mode else list(self.xDict.keys())
        for mode in modeKeys:
            assert mode in self.yDict, "No mode '%s' in yDict" % mode
            functor,arity = mode.getFunctor(),mode.getArity()
            dx = db.matrixAsSymbolDict(self.xDict[mode],db.schema.getDomain(functor,arity))
            dy = db.matrixAsSymbolDict(self.yDict[mode],db.schema.getRange(functor,arity))
            theoryPred = mode.functor
            for i in range(max(dx.keys())+1):
                dix = dx[i]
                diy = dy[i]
                assert len(list(dix.keys()))==1,'X row %d is not onehot: %r' % (i,dix)
                x = list(dix.keys())[0]
                fp.write('%s(%s,Y)' % (theoryPred,x))
                for y in list(diy.keys()):
                    fp.write('\t+%s(%s,%s)' % (theoryPred,x,y))
                fp.write('\n')

if __name__ == "__main__":
    usage = 'usage: python -m dataset.py --serialize foo.cfacts|foo.db bar.exam|bar.examples glob.dset'
    if sys.argv[1]=='--serialize':
        assert len(sys.argv)==5,usage
        dbFile = sys.argv[2]
        examFile = sys.argv[3]
        dsetFile = sys.argv[4]
        if dbFile.endswith(".cfacts"):
            db = matrixdb.MatrixDB.loadFile(dbFile)
        elif dbFile.endswith(".db"):
            db = matrixdb.MatrixDB.deserialize(dbFile)
        else:
            assert False,usage
        assert examFile.endswith(".examples") or examFile.endswith(".exam"),usage
        dset = Dataset.loadExamples(db,examFile,proppr=examFile.endswith(".examples"))
        dset.serialize(dsetFile)
