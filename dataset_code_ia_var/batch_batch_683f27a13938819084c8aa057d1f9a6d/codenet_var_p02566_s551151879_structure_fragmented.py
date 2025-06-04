import os
import sys

def write_code_file(filename, code):
    with open(filename, 'w') as f:
        f.write(code)

def run_cythonize(filename):
    os.system(f'cythonize -i -3 -b {filename}')

def should_compile():
    return sys.argv[-1] == 'ONLINE_JUDGE'

def trigger_compile_if_needed(code):
    if should_compile():
        filename = 'solve.pyx'
        write_code_file(filename, code)
        run_cythonize(filename)

def import_solve():
    import solve

def main():
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
    trigger_compile_if_needed(code)
    import_solve()

main()