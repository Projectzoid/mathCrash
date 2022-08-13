from lib2to3.pgen2.token import LEFTSHIFT
from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class BasicExampleOne(Scene):
    def construct(self):

        beStart = MathTex(r"h(x) = (x+2)(2x+1)")
        beF1 = MathTex(r"f(x) = x+2")
        beF2 = MathTex(r"f'(x) = 1")
        beG1 = MathTex(r"g(x) = 2x+1")
        beG2 = MathTex(r"g'(x) = 2")

        beF2.next_to(beF1, DOWN)
        beG1.next_to(beF2, DOWN)
        beG2.next_to(beG1, DOWN)
        

        self.wait()

        self.play(Write(beStart), run_time=0.5)

        self.wait()

        self.play(beStart.animate.move_to(UP+UP+UP+LEFT+LEFT+LEFT+LEFT), run_time=0.5)
        self.play(AnimationGroup(Write(beF1), Write(beF2), Write(beG1), Write(beG2)), run_time=0.5)

        self.wait()

        twoBeF1 = MathTex(r"f(x) = x+2")
        twoBeF2 = MathTex(r"f'(x) = 1")
        twoBeG1 = MathTex(r"g(x) = 2x+1")
        twoBeG2 = MathTex(r"g'(x) = 2")

        twoBeF1.scale(0.75)
        twoBeF2.scale(0.75)
        twoBeG1.scale(0.75)
        twoBeG2.scale(0.75)

        twoBeF1.next_to(beStart, DOWN, aligned_edge=LEFT)
        twoBeF2.next_to(twoBeF1, DOWN, aligned_edge=LEFT)
        twoBeG1.next_to(twoBeF2, DOWN, aligned_edge=LEFT)
        twoBeG2.next_to(twoBeG1, DOWN, aligned_edge=LEFT)

        self.play(AnimationGroup(Write(twoBeF1), Write(twoBeF2), Write(twoBeG1), Write(twoBeG2)), FadeOut(beF1, beF2, beG1, beG2), run_time=0.5)

        self.wait()

        generalFormula1 = MathTex(r"f'(x)g'(x)", r"=", r"f(x)",  r"g'(x)", r"+", r"g(x)", r"f'(x)")
        generalFormula2 = MathTex(r"h'(x)", r"=", r"(x+2)",  r"g'(x)", r"+", r"g(x)", r"f'(x)")
        generalFormula3 = MathTex(r"h'(x)", r"=", r"(x+2)",  r"(2)", r"+", r"g(x)", r"f'(x)")
        generalFormula4 = MathTex(r"h'(x)", r"=", r"(x+2)",  r"(2)", r"+", r"(2x+1)", r"f'(x)")
        generalFormula5 = MathTex(r"h'(x)", r"=", r"(x+2)",  r"(2)", r"+", r"(2x+1)", r"(1)")

        solvedGF1 = MathTex(r"h'(x)", r"=", r"2x+4", r"+", r"2x+1",)
        solvedGF2 = MathTex(r"h'(x)", r"=", r"4x+5")

        self.play(Write(generalFormula1), run_time=0.5)
        
        self.wait()

        self.play(ReplacementTransform(generalFormula1, generalFormula2), run_time=0.5)
        self.play(Indicate(generalFormula2[2]), Indicate(twoBeF1), run_time=0.5)

        self.wait()

        self.play(ReplacementTransform(generalFormula2, generalFormula3), run_time=0.5)
        self.play(Indicate(generalFormula3[3]), Indicate(twoBeG2), run_time=0.5)

        self.wait()
        
        self.play(ReplacementTransform(generalFormula3, generalFormula4), run_time=0.5)
        self.play(Indicate(generalFormula4[5]), Indicate(twoBeG1), run_time=0.5)
        

        self.wait()

        self.play(ReplacementTransform(generalFormula4,generalFormula5), run_time=0.5)
        self.play(Indicate(generalFormula5[6]), Indicate(twoBeF2), run_time=0.5)

        self.wait()

        self.play(ReplacementTransform(generalFormula5, solvedGF1), run_time=0.5)
        
        self.wait()

        self.play(ReplacementTransform(solvedGF1, solvedGF2), run_time=0.5)
        self.play(Indicate(solvedGF2), run_time=0.5)

        self.wait()

