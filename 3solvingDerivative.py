from manim import *
from sympy import *


class solvingDerivative(Scene):
    def construct(self):
        derFunc = MathTex(
            r"f'(x) = x^2"
        )
        derFunc.set_color_by_tex("x", WHITE)

        solvedDerFunc = MathTex(
            r"f'(x) = 2x"
        )
        derFunc.set_color_by_tex("x", WHITE)

        self.add(derFunc)
        self.wait(3)
        self.play(ReplacementTransform(derFunc, solvedDerFunc))

