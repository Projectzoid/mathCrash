from manim import *


class solvingDerivative(Scene):
    def construct(self):
        t1 = MarkupText(
            f'<span fgcolor="{WHITE}">How do you get the </span>derivative function<span fgcolor="{WHITE}">?</span> ', color=RED
        )

        func = MathTex(r"f(x)", r"=", r"x^n")
        derFunc = MathTex(r"f'(x)", r"=", r"n", r"x", r"^{n", r"-1}")

        self.wait()

        self.play(Write(t1), run_time=0.5)
        self.play(ApplyWave(
            t1,
            direction=UP,
            time_width=0.5,
            amplitude=0.1
        ))

        self.wait()

        self.play(ReplacementTransform(t1, func))
        self.wait(2)

        self.play(
            ReplacementTransform(func[0], derFunc[0]),
            ReplacementTransform(func[1], derFunc[1]),
            ReplacementTransform(func[2], derFunc[2:]))

        self.wait()

        self.play(Indicate(derFunc[2]))

        self.wait()

        self.play(Indicate(derFunc[5]))

        self.wait()
