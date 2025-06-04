from abc import ABC, abstractmethod
from typing import List, Tuple
import math
import cmath

class Polynomial(ABC):
    def __init__(self, coefficients: List[float]):
        self.coefficients = coefficients
    
    @abstractmethod
    def degree(self) -> int:
        pass
    
    @abstractmethod
    def roots(self) -> List[complex]:
        pass
    
    def real_roots(self) -> List[float]:
        """Filter roots to return only real roots (including repeated)."""
        eps = 1e-12
        return [r.real for r in self.roots() if abs(r.imag) < eps]

class CubicPolynomial(Polynomial):
    def __init__(self, a: float, b: float, c: float, d: float):
        super().__init__([a, b, c, d])
        if abs(a) < 1e-15:
            raise ValueError("Leading coefficient a must not be zero for cubic polynomial")
    
    def degree(self) -> int:
        return 3
    
    def roots(self) -> List[complex]:
        # Solve cubic equation a*x^3 + b*x^2 + c*x + d = 0 using Cardano's method
        
        a, b, c, d = self.coefficients
        
        # Depress cubic: x = t - b/(3a)
        p = (3*a*c - b**2) / (3 * a**2)
        q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27 * a**3)
        
        discriminant = (q/2)**2 + (p/3)**3
        
        roots = []
        
        if abs(p) < 1e-15 and abs(q) < 1e-15:
            # triple root
            root = -b/(3*a)
            roots = [complex(root)] * 3
        elif discriminant > 1e-15:
            # one real root and two complex conjugates
            sqrt_disc = math.sqrt(discriminant)
            u_cubed = -q/2 + sqrt_disc
            v_cubed = -q/2 - sqrt_disc
            u = CubicPolynomial._cubic_root_real(u_cubed)
            v = CubicPolynomial._cubic_root_real(v_cubed)
            root1 = u + v - b/(3*a)
            root2 = -(u+v)/2 - b/(3*a) + 1j * (u - v) * math.sqrt(3)/2
            root3 = root2.conjugate()
            roots = [complex(root1), root2, root3]
        elif abs(discriminant) <= 1e-15:
            # multiple roots, all real
            u_cubed = -q/2
            u = CubicPolynomial._cubic_root_real(u_cubed)
            root1 = 2*u - b/(3*a)
            root2 = -u - b/(3*a)
            roots = [complex(root1), complex(root2), complex(root2)]
        else:
            # three distinct real roots
            r = math.sqrt(- (p**3)/27)
            phi = math.acos(-q/(2*r))
            t = 2 * (-p/3)**0.5
            root1 = t * math.cos(phi/3) - b/(3*a)
            root2 = t * math.cos((phi + 2*math.pi)/3) - b/(3*a)
            root3 = t * math.cos((phi + 4*math.pi)/3) - b/(3*a)
            roots = [complex(root1), complex(root2), complex(root3)]
        
        return roots
    
    @staticmethod
    def _cubic_root_real(x: float) -> float:
        # real cubic root, handling negative numbers properly
        if x >= 0:
            return x ** (1/3)
        else:
            return - (-x) ** (1/3)
    
class RootCounter:
    def __init__(self, polynomial: Polynomial):
        self.polynomial = polynomial
    
    def count_positive_and_negative_real_roots(self) -> Tuple[int,int]:
        real_roots = self.polynomial.real_roots()
        # Count roots including multiplicities - roots() returns all multiplicities inherently
        pos_count = sum(1 for r in real_roots if r > 1e-15)
        neg_count = sum(1 for r in real_roots if r < -1e-15)
        # roots close to zero considered neither positive nor negative
        return pos_count, neg_count

class InputReader:
    def __init__(self):
        self.test_cases = []
    
    def read(self):
        t = int(input().strip())
        for _ in range(t):
            a,b,c,d = map(int, input().strip().split())
            self.test_cases.append((a,b,c,d))
        return self.test_cases

class OutputWriter:
    @staticmethod
    def write(results: List[Tuple[int,int]]):
        for pos, neg in results:
            print(pos, neg)

class EquationSolverFacade:
    def __init__(self):
        self.reader = InputReader()
    
    def execute(self):
        coefficients_list = self.reader.read()
        results = []
        for coeffs in coefficients_list:
            cubic = CubicPolynomial(*coeffs)
            counter = RootCounter(cubic)
            results.append(counter.count_positive_and_negative_real_roots())
        OutputWriter.write(results)

if __name__ == "__main__":
    EquationSolverFacade().execute()