from manim import *

class MovingVertices2(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)]
        g = Graph(vertices, edges).move_to(LEFT)
        # self.play(Create(g))
        self.wait()
        g2 = g.copy().set_color(color=RED).move_to(RIGHT)
        g_group = Group(g, g2).move_to(LEFT * 3)
        self.play(FadeIn(g_group))
        self.play(g2.animate.next_to(g, RIGHT, buff=1))
        self.wait()
