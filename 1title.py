from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class LimitsTitle(Scene):
    def construct(self):
        mathCrash = MarkupText(
            f'math<span fgcolor="{WHITE}">Crash</span>', color=BLUE
        )

        section = Text(
            "Section 1.1", color=WHITE
        )

        topic = Text(
            f'What is a limit? \nHow do you determine if a limit exists? \nHow do you graphically solve for a limit?', color=WHITE
        )
        topic.arrange(center=True)  

        section.next_to(mathCrash, DOWN)
        
        self.play(Write(mathCrash), Write(section), run_time = 1)
        self.wait(3)
        self.play(ReplacementTransform(mathCrash, topic), FadeOut(section), run_time = 0.5)

        self.play(ApplyWave(
            topic[0:13],
            direction=UP,
            time_width=0.5,
            amplitude=0.1
        ))

        self.wait()

        self.play(ApplyWave(
            topic[15:45],
            direction=UP,
            time_width=0.5,
            amplitude=0.1
        ))

        self.wait()

        self.play(ApplyWave(
            topic[45:85],
            direction=UP,
            time_width=0.5,
            amplitude=0.1
        ))
    
        self.wait(3)

        t1 = MarkupText(
            f'<span fgcolor="{WHITE}">What is a</span> limit<span fgcolor="{WHITE}">?</span> ', color=RED
        )

        self.play(ReplacementTransform(topic, t1), run_time = 1)
        self.play(ApplyWave(
            t1,
            direction=UP,
            time_width=0.5,
            amplitude=0.1
        ))
        self.wait(3)

  
        
      
