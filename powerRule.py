from manim import *
from sympy import * 

#config.frame_width = 37.9391100703
#config.frame_height = 32

class PowerRule(MovingCameraScene):
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

        #equation1 = MathTex("y", "=", "x^2")

        #self.add(equation1)
        #self.play(self.camera.frame.animate.move_to(equation1[0]).set(width=equation1[0].width*2))
        #self.wait(1)
        #self.play(self.camera.frame.animate.move_to(equation1[2]).set(width=equation1[2].width*2))
        

        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )

        graph1 = axes.get_graph(lambda x: x**2, RED)
        graph2 = axes.get_graph(lambda x: x*2, GREEN)
        graph_label1 = axes.get_graph_label(graph1, label='x^{2}')
        graph_label2 = axes.get_graph_label(graph2, label='2x')

        self.play(Create(axes), Create(graph1), Write(graph_label1))
        self.wait(5)
        self.play(Create(graph2), Write(graph_label2))
      
  
