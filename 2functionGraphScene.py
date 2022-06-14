from manim import *


class Graph(Scene):
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
        graph_label = axes.get_graph_label(
            graph, label="f(x) = x^{2}", color=WHITE)
        graph_label.move_to([4, 2, 0])

        graph2 = axes.plot(lambda x: 2*x, color=RED)
        graph_label2 = axes.get_graph_label(
            graph2, label="f'(x) = 2x", color=RED).next_to(graph_label, DOWN)

        self.wait(2)
        self.play(Create(axes))
        self.play(Write(axis_labels))

        self.play(Create(graph), run_time=1)
        self.play(Write(graph_label))
        self.wait(2)

        self.play(Create(graph2), run_time=1)
        self.play(Write(graph_label2))
        self.wait(2)
