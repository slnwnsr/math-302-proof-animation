from manim import *
from itertools import combinations


# scene just to try out stuff
class MovingVertices2(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)]
        g = Graph(vertices, edges).move_to(LEFT)
        self.play(Create(g))
        self.wait()
        g2 = g.copy().set_color(color=RED).move_to(RIGHT)
        g_group = Group(g, g2).move_to(LEFT * 3)
        self.play(FadeIn(g_group))
        self.play(g2.animate.next_to(g, RIGHT, buff=1))
        self.wait()

# GRAPHS------------------------------------------------------
# edges in K17
vertices = list(range(0,17))
arr = []
for x in range(0,17):
    arr.append(x)
edges = list(combinations(arr, 2))

# edges coloured red
redes = []
reddiffs = [1, 2, 4, 8, 9, 13, 15, 16]
for x in edges:
    if (x[1] - x[0]) in reddiffs:
        redes.append(x)

# edges coloured blue
bluees = []
for x in edges:
    if x not in redes:
        bluees.append(x)

g = Graph(vertices, edges, layout='circular', layout_scale=3)
redg = Graph(vertices, redes, layout='circular', layout_scale=3).set_color(color=RED)
blueg = Graph(vertices, bluees, layout='circular', layout_scale=3).set_color(color=BLUE)
# ----------------------------------------------------------

# draws K17 into the scene
class K17(Scene):
    def construct(self):

        self.wait()
        self.play(ChangeSpeed(
                AnimationGroup(Create(g)),
                speedinfo={0.08: 0.08},
                affects_speed_updaters=True,
            ))
        # self.play(g.animate.next_to(g, LEFT, buff=-3.3))
        self.wait()


# draws the red and blue edges of K17 then merges them
class colouredK17(Scene):
    def construct(self):
        self.play(FadeIn(g))
        self.wait()

        self.play(ChangeSpeed(
                AnimationGroup(Create(redg)),
                speedinfo={0.1: 0.1},
                affects_speed_updaters=True,
            ))
        # self.play(Create(redg))
        self.wait()
        self.play(redg.animate.scale(0.6).move_to(RIGHT*4.8))
        self.wait()

        self.play(ChangeSpeed(
                AnimationGroup(Create(blueg)),
                speedinfo={0.1: 0.1},
                affects_speed_updaters=True,
            ))
        # self.play(Create(blueg))
        self.wait()
        self.play(blueg.animate.scale(0.6).move_to(LEFT*4.8))
        self.wait()

        self.play(FadeOut(g))
        self.wait()


        self.play(redg.animate.scale(1.6).move_to([0,0,0]))
        self.play(blueg.animate.scale(1.6).move_to([0,0,0]))
        self.wait()

class sampleScene(Scene):
    def construct(self):
        blob = Circle(1.5)
        self.wait()
        self.play(blob.animate.move_to(RIGHT*4))
        self.wait()
        self.play(blob.animate.move_to([0,0,0]))
