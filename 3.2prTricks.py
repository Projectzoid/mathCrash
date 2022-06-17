from re import S
from idna import InvalidCodepoint
from manim import *


class solvingDerivative(Scene):
    def construct(self):
        t1 = MarkupText(
            f'<span fgcolor="{WHITE}">How do you get the </span>derivative function<span fgcolor="{WHITE}">?</span> ', color=RED
        )

        f1 = MathTex(r"f(x)", r"=", r"2", r"x")
        f2 = MathTex(r"f(x)", r"=", r"2", r"x", r"^{1}")
        f3 = MathTex(r"f'(x)", r"=", r"1", r"*", r"2", r"x", r"^{1", r"-1}")
        f4 = MathTex(r"f'(x)", r"=", r"2", r"x", r"^{0}")
        f5 = MathTex(r"f'(x)", r"=", r"2")

        self.wait()
        
        self.play(Write(f1), run_time = 0.5)

        self.wait()        

        self.play(
        ReplacementTransform(f1[0], f2[0]),
        ReplacementTransform(f1[1], f2[1]),
        ReplacementTransform(f1[2], f2[2]),
        ReplacementTransform(f1[3], f2[3:]), run_time = 0.5
        )
        #self.play(Indicate(f2[4]))

        self.wait()

        self.play(
        ReplacementTransform(f2[0], f3[0]),
        ReplacementTransform(f2[1], f3[1]),
        ReplacementTransform(f2[2], f3[2:5]),
        ReplacementTransform(f2[3], f3[5]),
        ReplacementTransform(f2[4], f3[6:8]), run_time = 0.5
        )
        #self.play(
        #    Indicate(f3[0]),
        #    Indicate(f3[2]),
        #    Indicate(f3[7])
        #)
        self.wait()

        self.play(
            ReplacementTransform(f3[0],f4[0]),
            ReplacementTransform(f3[1],f4[1]),
            ReplacementTransform(f3[2:5],f4[2]),
            ReplacementTransform(f3[5],f4[3]),
            ReplacementTransform(f3[6:],f4[4]), run_time = 0.5
        )
        #self.play(
        #    Indicate(f4[2]),
        #    Indicate(f4[4]), run_time = 0.5
        #)
        
        self.wait()

        self.play(
            ReplacementTransform(f4[0],f5[0]),
            ReplacementTransform(f4[1],f5[1]),
            ReplacementTransform(f4[2],f5[2:]),
            FadeOut(f4[3:]), run_time = 0.5
        )
        #self.play(
        #    Indicate(f5[2])            
        #)

        self.wait()

        self.clear()

        self.wait()

        f1 = MathTex(r"f(x)", r"=", r"5")
        f2 = MathTex(r"f(x)", r"=", r"5", r"x^{0}")
        f3 = MathTex(r"f'(x)", r"=", r"0", r"*5", r"x^{0", r"-1}")
        f4 = MathTex(r"f'(x)", r"=", r"0", r"x^{-1}")
        f5 = MathTex(r"f'(x)", r"=", r"0")

        self.wait()

        self.play(
            Write(f1), run_time = 0.5
        )

        self.wait()

        self.play(
            ReplacementTransform(f1[0], f2[0]),
            ReplacementTransform(f1[1], f2[1]),
            ReplacementTransform(f1[2], f2[2:]), run_time = 0.5
        )
        #self.play(
        #    Indicate(f2[3])
        #)

        self.wait()

        self.play(
            ReplacementTransform(f2[0], f3[0]),
            ReplacementTransform(f2[1], f3[1]),
            ReplacementTransform(f2[2], f3[2:4]),
            ReplacementTransform(f2[3], f3[4:]), run_time = 0.5
        )

        #self.play(
        #    Indicate(f3[2]),
        #    Indicate(f3[5]),
        #)

        self.wait()

        self.play(
            ReplacementTransform(f3[0], f4[0]),
            ReplacementTransform(f3[1], f4[1]),
            ReplacementTransform(f3[2], f4[2]),
            FadeOut(f3[3]),
            ReplacementTransform(f3[4:], f4[3]), run_time = 0.5
        )   
        
        self.wait()

        self.play(
            ReplacementTransform(f4[0], f5[0]),
            ReplacementTransform(f4[1], f5[1]),
            ReplacementTransform(f4[2], f5[2]),
            FadeOut(f4[3]), run_time = 0.5
        )
        #self.play(
        #    Indicate(f5[2])
        #)
        
        self.wait