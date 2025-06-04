from abc import ABC, abstractmethod
from typing import List, Optional

class Mora(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def is_voiceless_consonant(self) -> bool:
        pass
    
    @abstractmethod
    def get_vowel(self) -> Optional[str]:
        pass
    
    @abstractmethod
    def is_voiced_consonant(self) -> bool:
        pass
    
    @abstractmethod
    def is_sokuon(self) -> bool:
        pass
    
    @abstractmethod
    def is_choon(self) -> bool:
        pass
    
    @abstractmethod
    def is_hatsuon(self) -> bool:
        pass
    
    @abstractmethod
    def original_text(self) -> str:
        pass

class SimpleMora(Mora):
    _voiceless_consonants = {'k', 's', 't', 'h', 'p'}
    _allowed_y_vowels = {'a','u','o'}
    _allowed_w_vowels = {'a'}
    
    def __init__(self, text:str, consonant:Optional[str], y_char:bool, vowel:Optional[str]):
        self.text = text
        self.consonant = consonant  # None if no consonant (vowel only)
        self.y_char = y_char        # True if has 'y' between consonant and vowel
        self.vowel = vowel          # vowel can be None only for special mora
        # Checks done outside
    def is_voiceless_consonant(self) -> bool:
        # voiceless consonants and their 'y'-variants are considered voiceless
        if self.consonant is None:
            return False
        if self.consonant in self._voiceless_consonants:
            # If y_char true, still voiceless
            return True
        return False
    
    def is_voiced_consonant(self) -> bool:
        # voiced consonants not in voiceless list
        if self.consonant is None:
            return False
        return not self.is_voiceless_consonant()
    
    def get_vowel(self) -> Optional[str]:
        return self.vowel
    
    def is_sokuon(self) -> bool:
        return False
    
    def is_choon(self) -> bool:
        return False
    
    def is_hatsuon(self) -> bool:
        return False
    
    def __str__(self):
        return self.text
    
    def original_text(self) -> str:
        return self.text

class Sokuon(Mora):
    # 促音 (small tsu)
    def __init__(self):
        self.text = 'っ'  # representation internally
    
    def is_voiceless_consonant(self) -> bool:
        return False
    
    def get_vowel(self) -> Optional[str]:
        return None
    
    def is_voiced_consonant(self) -> bool:
        return False
    
    def is_sokuon(self) -> bool:
        return True
    
    def is_choon(self) -> bool:
        return False
    
    def is_hatsuon(self) -> bool:
        return False
    
    def __str__(self):
        return self.text
    
    def original_text(self) -> str:
        return ''
    

class Hatsuon(Mora):
    # 撥音 ('n' or n')
    def __init__(self, text:str):
        self.text = text  # 'n' or "n'"
    
    def is_voiceless_consonant(self) -> bool:
        return False
    
    def get_vowel(self) -> Optional[str]:
        return None
    
    def is_voiced_consonant(self) -> bool:
        return False
    
    def is_sokuon(self) -> bool:
        return False
    
    def is_choon(self) -> bool:
        return False
    
    def is_hatsuon(self) -> bool:
        return True
    
    def __str__(self):
        return self.text
    
    def original_text(self) -> str:
        return self.text

class Choon(Mora):
    # 長音 (長音符号) always a vowel repeated: 'aa','ii','uu'
    def __init__(self, text:str):
        self.text = text  # doubled vowel like 'aa'
        # Text length is 2
    
    def is_voiceless_consonant(self) -> bool:
        return False
    
    def get_vowel(self) -> Optional[str]:
        # The 'vowel' of the mora is the second vowel (long vowel)
        # but long vowels do not form a vowel sound alone, they are treated specially
        return self.text[1]
    
    def is_voiced_consonant(self) -> bool:
        return False
    def is_sokuon(self) -> bool:
        return False
    def is_choon(self) -> bool:
        return True
    def is_hatsuon(self) -> bool:
        return False
    
    def __str__(self):
        return self.text
    def original_text(self) -> str:
        return self.text

# Parsing class that decomposes input into morae
class MoraParser:
    # All lower-case passed
    _mother_vowels = {'a','i','u','e','o'}
    _consonants = {'k','s','t','n','h','m','y','r','w','g','z','d','b','p'}
    _voiceless = {'k','s','t','h','p'}
    
    def __init__(self, text:str):
        self.text = text
        self.pos = 0
        self.length = len(text)
    
    def parse(self)->List[Mora]:
        morae: List[Mora] = []
        while self.pos < self.length:
            mora = self._parse_one()
            if mora is not None:
                morae.append(mora)
            else:
                # Invalid but ignore
                self.pos += 1
        return morae
    
    def _peek(self, ahead=0) -> Optional[str]:
        if self.pos + ahead >= self.length:
            return None
        return self.text[self.pos + ahead]
    
    def _parse_one(self) -> Optional[Mora]:
        c = self._peek()
        if c is None:
            return None
        
        # 促音 (sokuon) 'っ' are represented in romaji by doubling consonant.
        # The problem states input uses romaji only, so sokuon appears as doubled consonant, e.g. 'kk'.
        # We parse doubled consonant as sokuon + next mora
        
        # Check for sokuon:
        # If next two chars are consonants same and in allowed list?
        # But making sure second consonant is really part of next mora
        # So sokuon consumes one consonant which is doubled. To code this, 
        # we will detect double consonant and parse sokuon mora before next mora.
        
        # But the problem examples show sokuon is implicit in doubled consonants
        
        # So approach:
        # If next two chars are same consonant and in _voiceless and not 'n','y','w' after (since sokuon not before those)
        # then sokuon mora is constructed and pos advances by 1, the next mora is parsed at next loop iteration
        
        # Check if next two chars are same consonant and sokuon allowed
        c2 = self._peek(1)
        if c2 and c==c2 and c in self._voiceless:
            # sokuon found
            self.pos += 1  # consume first one as sokuon representation
            return Sokuon()
        
        # Check for hatsoon 'n' or n'
        # 'n' mora is single 'n' but if next char is vowel or 'y' it's ambiguous, so an apostrophe is added to 'n' -> "n'"
        # parse 'n'' or 'n'
        
        if c=='n':
            next_c = self._peek(1)
            next_next_c = self._peek(2)
            # Check if 'n\'' sequence
            if next_c == "'":
                self.pos += 2
                return Hatsuon("n'")
            # If next char is not None and not apostrophe, disambiguate:
            # If next char is vowel or y, then 'n'' notation must appear,
            # so without apostrophe 'n' before vowel or y is used as consonant + vowel
            # so here just parse it if next is not vowel or y
            if next_c is None:
                # n is end of word, normal hatsoon
                self.pos += 1
                return Hatsuon("n")
            if next_c in self._mother_vowels or next_c=='y':
                # Actually these cases required apostrophe, so 'n' alone not valid before vowel or y
                # Not supposed to appear alone, parse as part of consonant+vowel syllable
                pass
            else:
                # safe to parse as hatsoon
                self.pos += 1
                return Hatsuon("n")
        
        # Check for choon (long vowel)
        # In problem statement, long vowel is represented by doubling vowels a,i,u
        # So if current char is vowel and next char is same vowel and vowel in {a,i,u} then choon
        if c in {'a','i','u'}:
            next_c = self._peek(1)
            if next_c == c:
                # long vowel mora
                self.pos += 2
                return Choon(c+c)
        
        # Now parse 1 mora normal
        # Mora may be:
        # 1) vowel only
        # 2) consonant + vowel
        # 3) consonant + y + vowel (exceptionally certain vowel sets)
        # consonant is in _consonants (except y and w have special rule)
        
        # Check if c is vowel only mora
        if c in self._mother_vowels:
            self.pos += 1
            return SimpleMora(c, None, False, c)
        
        # If c is consonant, decide next part
        if c in self._consonants:
            # One or two mora chars
            consonant = c
            next_c = self._peek(1)
            next_next_c = self._peek(2)
            if consonant == 'y' or consonant == 'w':
                # 'y' and 'w' can be consonants only followed by limited vowels
                # but 'y' or 'w' alone is never a mora, always followed by vowel
                # 'y' in _consonants but must be handled as middle char, thus not initial consonant here
                # so must parse composite mora if previous consonant + y + vowel? No here c is 'y' or 'w'
                # No valid for single consonant 'y' or 'w' mora, skip
                pass
            # Check for consonant + y + vowel variant
            if next_c == 'y' and next_next_c in {'a','u','o'}:
                # Consonant + y + vowel
                if consonant in self._consonants and consonant not in {'y','w'}:
                    text = c + next_c + next_next_c
                    self.pos += 3
                    return SimpleMora(text, consonant, True, next_next_c)
            
            # Otherwise, consonant + vowel mora
            if next_c in self._mother_vowels:
                # check 'w' only can be followed by 'a'
                if consonant == 'w' and next_c != 'a':
                    # invalid, skip one char and parse as vowel next round
                    self.pos += 1
                    return SimpleMora(c, None, False, c) if c in self._mother_vowels else None
                # check 'y' only can be followed by a,u,o but we treat 'y' as middle char only not consonant here
                
                text = c + next_c
                self.pos += 2
                return SimpleMora(text, consonant, False, next_c)
            
            # If consonant alone or invalid combos: treat as vowel only if c is vowel else None
            # But consonant alone invalid here
            # consume one char to avoid infinite loop
            self.pos += 1
            return SimpleMora(c, None, False, c) if c in self._mother_vowels else None
        
        # Otherwise unknown char, consume one char and skip
        self.pos += 1
        return None

class VoicingRules:
    voiceless_consonants = {'k','s','t','h','p'}
    # voiceless + y variants handled in SimpleMora.is_voiceless_consonant
    vowels_for_i_u = {'i','u'}
    vowels_for_a_o = {'a','o'}
    
    @staticmethod
    def can_be_voiceless_consonant(mora:Mora)->bool:
        return mora.is_voiceless_consonant()
    
    @staticmethod
    def is_vowel_i_u(mora:Mora) -> bool:
        v = mora.get_vowel()
        return v in VoicingRules.vowels_for_i_u
    
    @staticmethod
    def is_vowel_a_o(mora:Mora) -> bool:
        v = mora.get_vowel()
        return v in VoicingRules.vowels_for_a_o
    
    @staticmethod
    def is_choon(mora:Mora)->bool:
        return mora.is_choon()
    
    @staticmethod
    def is_sokuon(mora:Mora)->bool:
        return mora.is_sokuon()

class VowelDevoiceDecorator:
    def __init__(self, original_text:str):
        self.original_text = original_text
        self.is_devoiced = False
    
    def mark_devoiced(self):
        self.is_devoiced = True
    
    def __str__(self):
        if self.is_devoiced:
            return '(' + self.original_text + ')'
        return self.original_text

class VowelDevoiceProcessor:
    def __init__(self, morae:List[Mora]):
        self.morae = morae
        # Decorator wrappers for each mora original text
        self.decorated = [VowelDevoiceDecorator(mora.original_text()) for mora in morae]
    
    def process(self)->List[str]:
        # apply devoicing rules in order
        self._apply_rule_i_u()
        self._apply_rule_a_o()
        # return decorated text
        return [str(d) for d in self.decorated]
    
    def _apply_rule_i_u(self):
        # Rule 1:
        # 母音「i」「u」の短音について，その母音が無声子音にはさまれたとき，
        # または無声子音の直後でしかも語句の末尾にあるとき。
        # This applies also if next mora after the i/u mora is sokuon.
        
        n = len(self.morae)
        for i, mora in enumerate(self.morae):
            if not VoicingRules.is_vowel_i_u(mora):
                continue
            if self.decorated[i].is_devoiced:
                continue
            
            # check preceding mora voiceless consonant
            prev_voiceless = i>0 and VoicingRules.can_be_voiceless_consonant(self.morae[i-1])
            # check following mora voiceless consonant or sokuon + next mora voiceless consonant
            next_voiceless = False
            
            if i+1<n:
                next_m = self.morae[i+1]
                # If next is sokuon, look 2 ahead
                if next_m.is_sokuon():
                    if i+2<n:
                        next_m2 = self.morae[i+2]
                        if VoicingRules.can_be_voiceless_consonant(next_m2):
                            next_voiceless = True
                else:
                    if VoicingRules.can_be_voiceless_consonant(next_m):
                        next_voiceless = True
            
            # Also condition: "無声子音の直後でしかも語句の末尾にある"
            voiceless_prev_and_last_pos = (prev_voiceless and i == n -1)
            
            if (prev_voiceless and next_voiceless) or voiceless_prev_and_last_pos:
                self.decorated[i].mark_devoiced()
    
    def _apply_rule_a_o(self):
        # Rule 2:
        # 母音「a」「o」について，同一の母音が無声子音とともに連続する2つ以上の拍で現れたとき．
        # ただし，最後のものは無声化されない．
        # 促音及び長音があってはならない連続．
        # 複数無声化は連続しないことから最初か直近未無声化のみ無声化
        
        # We look for runs of morae that have same vowel (a or o),
        # accompanied by voiceless consonants, no sokuon or choon inside the run,
        # and with length >= 2.
        
        n = len(self.morae)
        i = 0
        while i < n:
            mora = self.morae[i]
            if not VoicingRules.is_vowel_a_o(mora):
                i += 1
                continue
            if self.decorated[i].is_devoiced:
                i += 1
                continue
            if mora.is_sokuon() or mora.is_choon():
                i += 1
                continue
            # Verify mora has a voiceless consonant
            if not VoicingRules.can_be_voiceless_consonant(mora):
                # no voiceless consonant with vowel a or o, skip
                i += 1
                continue
            # Try to find consecutive run
            run_start = i
            run_vowel = mora.get_vowel()
            run_end = run_start + 1
            while run_end < n:
                m2 = self.morae[run_end]
                if m2.is_sokuon() or m2.is_choon():
                    break
                if not VoicingRules.can_be_voiceless_consonant(m2):
                    break
                if m2.get_vowel() != run_vowel:
                    break
                run_end += 1
            run_len = run_end - run_start
            
            if run_len >= 2:
                # Mark first or if previous vowel devoiced no mark, mark current first in run
                if not self.decorated[run_start].is_devoiced:
                    self.decorated[run_start].mark_devoiced()
                # Other vowels in run except last not devoiced
                # None other marked for devoicing
                # skip next run_len
                i = run_end
            else:
                i += 1

class PrincessJapaneseCorrector:
    def __init__(