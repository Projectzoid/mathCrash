from manim import *

class BasicExample1(Scene):
    def construct(self):
        func = MathTex(r"f(x)", r"=", r"6x", r"+", r"4x^{1/2}", r"+", r"6", r"+", r"2x^{-1}")
        derFunc1 = MathTex(r"f(x)", r"=", r"(1)" , r"6x", r"^{1", r"-1}", r"+", r"(1/2)", r"4x^{1/2", r"-1}", r"+", r"(0)", r"6x^{0", r"-1}", r"+", r"(-1)", r"2x^{-1", r"-1}")
        derFunc2 = MathTex(r"f(x)", r"=", r"6x", r"^{0}", r"+", r"2x", r"^{-1/2}", r"+", r"0^{-1}", r"+", r"-2x", r"^{-2}")
        derFunc3 = MathTex(r"f'(x)", r"=", r"6", r"+", r"\frac{2}{x^{1/2}}", r"+", r"\frac{-2}{x^{2}}")

        #6x + 4x^½  + 6 + 2x^-1

        self.wait()

        #orig
        self.play(Write(func))
        self.wait()

        #s1
        self.play(
        ReplacementTransform(func[0], derFunc1[0]),
        ReplacementTransform(func[1], derFunc1[1]),
        ReplacementTransform(func[2], derFunc1[2:6]),
        ReplacementTransform(func[3], derFunc1[6]),
        ReplacementTransform(func[4], derFunc1[7:10]),
        ReplacementTransform(func[5], derFunc1[10]),
        ReplacementTransform(func[6], derFunc1[11:14]),
        ReplacementTransform(func[7], derFunc1[14]),
        ReplacementTransform(func[8], derFunc1[15:]))
        self.play(
        Indicate(derFunc1[2]),
        Indicate(derFunc1[5]),
        Indicate(derFunc1[7]),
        Indicate(derFunc1[9]),
        Indicate(derFunc1[11]),
        Indicate(derFunc1[13]),
        Indicate(derFunc1[15]),
        Indicate(derFunc1[17]))
        self.wait()

        #s2
        self.play(
        ReplacementTransform(derFunc1[0], derFunc2[0]), 
        ReplacementTransform(derFunc1[1], derFunc2[1]), 
        ReplacementTransform(derFunc1[2:4], derFunc2[2]), 
        ReplacementTransform(derFunc1[4:6], derFunc2[3]),
        ReplacementTransform(derFunc1[6], derFunc2[4]),
        ReplacementTransform(derFunc1[7:9], derFunc2[5]),
        ReplacementTransform(derFunc1[9], derFunc2[6]),
        ReplacementTransform(derFunc1[10], derFunc2[7]),
        ReplacementTransform(derFunc1[11:14], derFunc2[8]),
        ReplacementTransform(derFunc1[14], derFunc2[9]),
        ReplacementTransform(derFunc1[15:17], derFunc2[10]),
        ReplacementTransform(derFunc1[17], derFunc2[11]))
        self.wait(2)
        
        #s3
        self.play(
        ReplacementTransform(derFunc2[0], derFunc3[0]),
        ReplacementTransform(derFunc2[1], derFunc3[1]),
        ReplacementTransform(derFunc2[2:4], derFunc3[2]),
        ReplacementTransform(derFunc2[4], derFunc3[3]),
        ReplacementTransform(derFunc2[5:7], derFunc3[4]),
        ReplacementTransform(derFunc2[7:], derFunc3[5:8]))
        self.wait(2)

        self.wait()