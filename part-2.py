from manim import *
from itertools import combinations


# GRAPHS------------------------------------------------------

# edges in K17
vertices = list(range(1,18))
arr = []
for x in range(1,18):
    arr.append(x)
edges = list(combinations(arr, 2))

# edges coloured red
redes = []
reddiffs = [1, 2, 4, 8, 9, 13, 15, 16]
for x in edges:
    if ((x[1]-1) - (x[0]-1)) in reddiffs:
        redes.append(x)

# edges coloured blue
bluees = []
for x in edges:
    if x not in redes:
        bluees.append(x)

# vertex labels
labels = []
for i in range(1,18):
    labels.append(str(i))


g = Graph(vertices, edges, layout='circular', layout_scale=3)
redg = Graph(vertices, redes, layout='circular', layout_scale=3).set_color(color=RED)
blueg = Graph(vertices, bluees, layout='circular', layout_scale=3).set_color(color=BLUE)

# square = Square(fill_color=BLUE, fill_opacity=0.2)

# ANIMATIONS
# ----------------------------------------------------------

# draws K17 into the scene
class K17(Scene):
    def construct(self):
        k17text = MarkupText("K17")
        k17text.to_corner(UP + LEFT)
        self.play(Write(k17text))

        self.wait()
        self.play(ChangeSpeed(
                AnimationGroup(Create(g)),
                speedinfo={0.08: 0.08},
                affects_speed_updaters=True,
            ))
        self.wait()

        num = DecimalNumber(0, num_decimal_places=0)
        poly = RegularPolygon(n=17, radius=3.1).reverse_direction().rotate_about_origin(1)
        # self.add(poly)
        for i, vertex in enumerate(poly.get_vertices()):
            self.play(
                num.animate.set_value(i+1).move_to(Line(ORIGIN, vertex).scale(1.1, about_point=ORIGIN).get_end())
            )
        self.play(FadeOut(num))
        self.wait()


class redK17(Scene):
    def construct(self):
        k4text = MarkupText("K4?").set_color(RED)
        k4text.to_corner(UP + LEFT)
        self.play(FadeIn(redg))
        self.wait()
        self.play(Write(k4text))
        self.wait()
        self.play(redg.animate.move_to(RIGHT*3))
        self.wait()

        mini = redg.copy().set_color(WHITE)
        mini.remove_vertices(1,2,3,4,6,7,11,12,13,14,15,16,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to(LEFT*2.5))
        self.wait()
        minitxt = MarkupText("<s>K4</s>").next_to(mini, DOWN)
        self.play(Write(minitxt))
        self.play(FadeOut(mini, minitxt))
        # self.play(FadeOut(minitxt))

        mini = redg.copy().set_color(WHITE)
        mini.remove_vertices(1,2,3,6,8,9,11,12,13,14,15,16,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to(LEFT*2.5))
        self.wait()
        self.play(FadeOut(mini))

        mini = redg.copy().set_color(WHITE)
        mini.remove_vertices(2,3,4,5,6,8,10,11,12,13,14,15,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to(LEFT*2.5))
        self.wait()
        self.play(FadeOut(mini))



# draws the red and blue edges of K17
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
        self.play(redg.animate.scale(0.5).move_to(RIGHT*4.8))
        self.wait()

        self.play(ChangeSpeed(
                AnimationGroup(Create(blueg)),
                speedinfo={0.1: 0.1},
                affects_speed_updaters=True,
            ))
        # self.play(Create(blueg))
        self.wait()
        self.play(blueg.animate.scale(0.5).move_to(LEFT*4.8))

        self.play(FadeOut(g))

        self.play(redg.animate.scale(1.6).move_to([0,0,0]), FadeOut(blueg))
        # self.play(FadeOut(blueg))
        # self.play(blueg.animate.scale(1.6).move_to([0,0,0]))
        self.wait()
