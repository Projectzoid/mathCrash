from manim import *

class BasicExample1(Scene):
    def construct(self):
        func = MathTex(r"f(x)", r"=", r"x^n")
        derFunc = MathTex(r"f'(x)", r"=", r"n", r"x", r"^{n", r"-1}")

        self.wait(1)
        self.play(Write(func))
        self.wait(3)
        self.play(ReplacementTransform(func[0], derFunc[0]))
        self.play(ReplacementTransform(func[1], derFunc[1]))
        self.play(ReplacementTransform(func[2], derFunc[2:]))
        self.wait(1)
        self.play(Indicate(derFunc[2]))
        self.wait(1)
        self.play(Indicate(derFunc[5]))
        self.wait(1)