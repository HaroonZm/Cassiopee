code = r"""
# distutils: language=c++
# distutils: include_dirs=[/home/contestant/.local/lib/python3.8/site-packages/numpy/core/include, /opt/atcoder-stl]
from libcpp.vector cimport vector
from libcpp.string cimport string
cdef extern from "<atcoder/string>" namespace "atcoder" nogil:
    cdef vector[int] suffix_array(string s)
    cdef vector[int] suffix_array[T](vector[T] s)
    cdef vector[int] suffix_array(vector[int] s, int upper)
    cdef vector[int] lcp_array(string s, vector[int] sa)
    cdef vector[int] lcp_array[T](vector[T] s, vector[int] sa)
    cdef vector[int] z_algorithm(string s)
    cdef vector[int] z_algorithm[T](vector[T] s)
cdef string s = input().encode()
cdef long n = s.length()
cdef vector[int] sa = suffix_array(s)
cdef vector[int] la = lcp_array(s, sa)
cdef long a = n * (n + 1) // 2
for i in range(n - 1): a -= la[i]
print(a)
"""
import os, sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    open('solve.pyx', 'w').write(code)
    os.system('cythonize -i -3 -b solve.pyx')
import solve