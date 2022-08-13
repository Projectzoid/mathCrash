from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class QRGeneralRule(Scene):
    def construct(self):

        pr = Text("Quotient Rule")

        self.play(Write(pr), run_time=0.5)
        self.wait()
        self.clear()

        generalFormula = MathTex(r"(f/g)(x) = f(x)/g(x)")
        generalFormula2 = MathTex(r"(f/g)’(x) = \frac{g(x)f'(x) - f(x)g'(x)}{g(x)^2}")

        self.wait()

        self.play(Write(generalFormula), run_time=0.5)

        self.wait()

        self.play(ReplacementTransform(generalFormula, generalFormula2), run_time=0.5)

        self.wait()

