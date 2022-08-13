from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class PRGeneralRule(Scene):
    def construct(self):

        pr = Text("Product Rule")

        self.play(Write(pr), run_time=0.5)
        self.wait(5)
        self.clear()

        #limitation = MathTex(r"f(x) = ", r"xy", r"* x")
        #limitation2 = MathTex(r"f(x) = ", r"xy", r"* x")
        #limitation2[1].set_color(RED)
#
        #goodEx = MathTex(r"f(x) = xy")
        #goodEx2 = MathTex(r"f(x) = xy")
        #goodEx2.set_color(GREEN)
#
        #self.wait()
#
        #self.play(Write(limitation), run_time=0.5)
#
        #self.wait()
#
        #self.play(ReplacementTransform(limitation, limitation2), run_time = 0.5)
#
        #self.wait()
#
        #self.play(FadeOut(limitation2, shift=UP*1.5))
        #self.play(FadeIn(goodEx, shift=UP*1.5))
#
        #self.wait()
#
        #self.play(ReplacementTransform(goodEx, goodEx2), run_time = 0.5)

        self.wait()

        generalFormula = MathTex(r"(fg)(x) = f(x)g(x)")
        generalFormula2 = MathTex(r"(fg)’(x) = f(x)g'(x) + f'(x)g(x)")

        #self.play(FadeOut(goodEx2, shift=UP*1.5))
        self.play(FadeIn(generalFormula, shift=UP*1.5))

        self.wait()

        self.play(ReplacementTransform(generalFormula, generalFormula2), run_time = 0.5)

        self.wait()

