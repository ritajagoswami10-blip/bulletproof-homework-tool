#!/usr/bin/env python3
"""
Math Problem Solver
Template for solving math problems step by step.
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 10


class MathSolver:
    """
    Helper class for solving math problems.
    """
    
    @staticmethod
    def quadratic_formula(a, b, c):
        """
        Solve quadratic equation ax^2 + bx + c = 0
        
        Args:
            a, b, c: Coefficients
            
        Returns:
            tuple: (x1, x2) - Two solutions
        """
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return None  # Complex roots
        
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        
        return (x1, x2)
    
    @staticmethod
    def linear_system_2x2(a1, b1, c1, a2, b2, c2):
        """
        Solve 2x2 linear system:
        a1*x + b1*y = c1
        a2*x + b2*y = c2
        
        Args:
            Coefficients for two equations
            
        Returns:
            tuple: (x, y) - Solution
        """
        det = a1*b2 - a2*b1
        
        if det == 0:
            return None  # No unique solution
        
        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det
        
        return (x, y)
    
    @staticmethod
    def solve_problem(problem_description):
        """
        Main problem solver function.
        Override this for specific problems.
        
        Args:
            problem_description: Description of the problem
            
        Returns:
            Solution
        """
        print(f"Problem: {problem_description}")
        print("\nStep 1: Identify given information")
        print("Step 2: Determine what to find")
        print("Step 3: Select appropriate formula/method")
        print("Step 4: Solve step by step")
        print("Step 5: Check answer")
        
        return None


def main():
    """
    Example problems
    """
    solver = MathSolver()
    
    # Example 1: Quadratic equation
    print("=== Example: Quadratic Equation ===")
    print("Solve: 2x² + 5x - 3 = 0")
    x1, x2 = solver.quadratic_formula(2, 5, -3)
    print(f"Solutions: x₁ = {x1}, x₂ = {x2}\n")
    
    # Example 2: Linear system
    print("=== Example: Linear System ===")
    print("Solve: 2x + 3y = 8")
    print("       x - y = 1")
    x, y = solver.linear_system_2x2(2, 3, 8, 1, -1, 1)
    print(f"Solution: x = {x}, y = {y}\n")


if __name__ == "__main__":
    main()
