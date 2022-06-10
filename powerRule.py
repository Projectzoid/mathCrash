from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class PowerRule(Scene):
    def construct(self):
        mathCrash = MarkupText(
            f'math<span fgcolor="{WHITE}">Crash</span>', color=BLUE
        )

        section = Text(
            "Section 2.1", color=WHITE
        )

        topic = MarkupText(
            f'Derivitives <span fgcolor="{WHITE}">and</span> The Power Rule', color=RED
        )

        section.next_to(mathCrash, DOWN)
        
        self.play(Write(mathCrash), Write(section))
        self.wait(3)
        self.play(ReplacementTransform(mathCrash, topic), FadeOut(section))
        self.wait(5)
        self.clear()

        t1 = MarkupText(
            f'<span fgcolor="{WHITE}">What is a</span> derivative<span fgcolor="{WHITE}">?</span> ', color=RED
        )

        self.play(Write(t1))
        self.wait(3)

        
      
  
