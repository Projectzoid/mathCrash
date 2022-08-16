from manim import *


class Graph(MovingCameraScene):
    def construct(self):
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            tips=False,
            axis_config={
                "color": BLUE,
                "numbers_to_include": np.arange(-6, 7),
                "font_size": 24,
            }
        )

        axis_labels = axes.get_axis_labels()

        graph = axes.plot(lambda x: x**2, color=WHITE)
        graph.arrange(DOWN, center=False, aligned_edge=LEFT) 

        graph_label = axes.get_graph_label(
            graph, label="f(x) = x^{2}", color=WHITE)
        graph_label.move_to([4, 2, 0])


        self.wait(2)
        self.play(Create(axes))
        self.play(Write(axis_labels))

        self.play(Create(graph), run_time=1)
        self.play(Write(graph_label))
        self.wait(2)

        dot = Dot()
        dot.move_to(graph.coords_to_point(2,4))


        #e1 = MathTex(r"f'(x)", r"=", r"2x")
        #e2 = MathTex(r"f'(2)", r"=", r"2(2)")
        #e3 = MathTex(r"f'(2)", r"=", r"4")

        #self.play(Write(e1))
#
        #self.play(
        #ReplacementTransform(e1[0],e2[0]),
        #ReplacementTransform(e1[1],e2[1]),
        #ReplacementTransform(e1[2],e2[2]))
#
        #self.wait()
#
        #self.play(
        #ReplacementTransform(e2[0],e3[0]),
        #ReplacementTransform(e2[1],e3[1]),
        #ReplacementTransform(e2[2],e3[2]))
#
        #self.wait()
        #self.clear()
        #self.wait()

        #axes2 = Axes(
            #x_range=[-12, 12, 1],
            #y_range=[-12, 12, 1],
            #tips=False,
            #axis_config={
                #"color": BLUE,
                #"numbers_to_include": np.arange(-12, 13),
                #"font_size": 16,
            #}
        #)
        #axis_labels2 = axes2.get_axis_labels()
#
        #graph4 = axes2.plot(lambda x: x**2, color=WHITE)
        #graph_label4 = axes2.get_graph_label(
            #graph4, label="f(x) = x^{2}", color=WHITE)
        #graph_label4.move_to([4, 2, 0])
#
        #graph3 = axes2.plot(lambda x: 4*x-4, color=YELLOW)
        #graph_label3 = axes2.get_graph_label(
            #graph3, label="g(x) = 4x-4", color=YELLOW).next_to(graph_label, DOWN)
#
        #self.play(
        #Create(axes2, run_time=0.5),
        #Write(axis_labels2),
        #Create(graph4, run_time=0.5),
        #Write(graph_label4))
        #self.wait()
#
        #self.play(Create(graph3), run_time=1)
        #self.play(Write(graph_label3))
        #self.wait(2)

        self.wait()