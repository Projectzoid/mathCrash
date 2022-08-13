from lib2to3.pgen2.token import LEFTSHIFT
from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class BasicExampleTwo(Scene):
    def construct(self):

        beStart = MathTex(r"h(x) = \frac{x^2}{3x^3+2x}")
        beF1 = MathTex(r"f(x) = x^2")
        beF2 = MathTex(r"f'(x) = 2x")
        beG1 = MathTex(r"g(x) = 3x^3+2x")
        beG2 = MathTex(r"g'(x) = 9x^2+2")

        beF2.next_to(beF1, DOWN)
        beG1.next_to(beF2, DOWN)
        beG2.next_to(beG1, DOWN)
        

        self.wait()

        self.play(Write(beStart), run_time=0.5)

        self.wait()

        self.play(beStart.animate.move_to(UP+UP+UP+LEFT+LEFT+LEFT+LEFT+LEFT), run_time=0.5)
        self.play(AnimationGroup(Write(beF1), Write(beF2), Write(beG1), Write(beG2)), run_time=0.5)

        self.wait()

        twoBeF1 = MathTex(r"f(x) = x^2")
        twoBeF2 = MathTex(r"f'(x) = 2x")
        twoBeG1 = MathTex(r"g(x) = 3x^3+2x")
        twoBeG2 = MathTex(r"g'(x) = 9x^2+2")

        twoBeF1.scale(0.5)
        twoBeF2.scale(0.5)
        twoBeG1.scale(0.5)
        twoBeG2.scale(0.5)

        twoBeF1.next_to(beStart, DOWN, aligned_edge=LEFT)
        twoBeF2.next_to(twoBeF1, DOWN, aligned_edge=LEFT)
        twoBeG1.next_to(twoBeF2, DOWN, aligned_edge=LEFT)
        twoBeG2.next_to(twoBeG1, DOWN, aligned_edge=LEFT)

        self.play(AnimationGroup(Write(twoBeF1), Write(twoBeF2), Write(twoBeG1), Write(twoBeG2)), FadeOut(beF1, beF2, beG1, beG2), run_time=0.5)

        self.wait()

        generalFormula1 = MathTex(r"(f/g)'(x)", r"=", r"\frac{g(x)f'(x)-f(x)g'(x)}{g(x)^2}")   
        generalFormula2 = MathTex(r"h'(x)", r"=", r"\frac{(3x^3+2x)f'(x)-f(x)g'(x)}{(3x^3+2x)^2}")
        generalFormula3 = MathTex(r"h'(x)", r"=", r"\frac{(3x^3+2x)(2x)-f(x)g'(x)}{(3x^3+2x)^2}")
        generalFormula4 = MathTex(r"h'(x)", r"=", r"\frac{(3x^3+2x)(2x)-(x^2)g'(x)}{(3x^3+2x)^2}")
        generalFormula5 = MathTex(r"h'(x)", r"=", r"\frac{(3x^3+2x)(2x)-(x^2)(9x^2+2)}{(3x^3+2x)^2}")

        solvedGF1 = MathTex(r"h'(x)", r"=", r"\frac{(18x^3+3x)-(6x^3+3x)}{9x^2}")
        solvedGF2 = MathTex(r"h'(x)", r"=", r"\frac{(12x^3)}{9x^2}")
        solvedGF3 = MathTex(r"h'(x)", r"=", r"\frac{4x}{3}")

        self.play(Write(generalFormula1), run_time=0.5)
        
        self.wait()

        self.play(ReplacementTransform(generalFormula1, generalFormula2), run_time=0.5)
        self.play(Indicate(generalFormula2[2][0:8]), Indicate(generalFormula2[2][24:32]), Indicate(twoBeG1), run_time=0.5)

        self.wait()

        self.play(ReplacementTransform(generalFormula2, generalFormula3), run_time=0.5)
        self.play(Indicate(generalFormula3[2][8:12]), Indicate(twoBeF2), run_time=0.5)

        self.wait()
        
        self.play(ReplacementTransform(generalFormula3, generalFormula4), run_time=0.5)
        self.play(Indicate(generalFormula4[2][13:17]), Indicate(twoBeF1), run_time=0.5)
        

        self.wait()

        self.play(ReplacementTransform(generalFormula4,generalFormula5), run_time=0.5)
        self.play(Indicate(generalFormula5[2][17:24]), Indicate(twoBeG2), run_time=0.5)

        self.wait()

        self.play(ReplacementTransform(generalFormula5, solvedGF1), run_time=0.5)
        
        self.wait()

        self.play(ReplacementTransform(solvedGF1, solvedGF2), run_time=0.5)

        self.wait()

        self.play(ReplacementTransform(solvedGF2, solvedGF3), run_time=0.5)
        #self.play(Indicate(solvedGF3), run_time=0.5)

        self.wait()

