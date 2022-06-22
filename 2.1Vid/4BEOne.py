from manim import *

class BasicExample1(Scene):
    def construct(self):
        func = MathTex(r"f(x)", r"=", r"3x^{2}")
        derFunc1 = MathTex(r"f(x)", r"=", r"2 * ", r"3x^{2}")
        derFunc2 = MathTex(r"f(x)", r"=", r"6", r"x^{2}")
        derFunc3 = MathTex(r"f(x)", r"=", r"6x^{2", r"-1}")
        derFunc4 = MathTex(r"f(x)", r"=", r"6x", r"^{1}")
        derFunc5 = MathTex(r"f'(x)", r"=", r"6x")

        self.wait()

        #orig
        self.play(Write(func))
        self.wait()

        #s1
        self.play(
        ReplacementTransform(func[0], derFunc1[0]),
        ReplacementTransform(func[1], derFunc1[1]),
        ReplacementTransform(func[2], derFunc1[2:]))
        self.play(Indicate(derFunc1[2]))
        self.wait()

        #s2
        self.play(
        ReplacementTransform(derFunc1[0], derFunc2[0]), 
        ReplacementTransform(derFunc1[1], derFunc2[1]), 
        ReplacementTransform(derFunc1[2], derFunc2[2]), 
        ReplacementTransform(derFunc1[3], derFunc2[3]))
        self.play(Indicate(derFunc2[2]))

        #s3
        self.play(
        ReplacementTransform(derFunc2[0], derFunc3[0]),
        ReplacementTransform(derFunc2[1], derFunc3[1]),
        ReplacementTransform(derFunc2[2], derFunc3[2]),
        ReplacementTransform(derFunc2[3], derFunc3[3]))
        self.play(Indicate(derFunc3[3]))

        #s4
        self.play(
        ReplacementTransform(derFunc3[0], derFunc4[0]),
        ReplacementTransform(derFunc3[1], derFunc4[1]),
        ReplacementTransform(derFunc3[2], derFunc4[2]),
        ReplacementTransform(derFunc3[3], derFunc4[3]))
        self.play(Indicate(derFunc4[3]))

        #s5
        self.play(
        ReplacementTransform(derFunc4[0], derFunc5[0]),
        ReplacementTransform(derFunc4[1], derFunc5[1]),
        ReplacementTransform(derFunc4[2], derFunc5[2]),
        FadeOut(derFunc4[3]))
        self.play(Indicate(derFunc5[0]), Indicate(derFunc5[2]))

        self.wait()