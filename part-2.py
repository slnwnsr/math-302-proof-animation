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


g = Graph(vertices, edges, layout='circular', layout_scale=3).scale(0.8)
redg = Graph(vertices, redes, layout='circular', layout_scale=3).set_color(color=RED).scale(0.8)
blueg = Graph(vertices, bluees, layout='circular', layout_scale=3).set_color(color=BLUE).scale(0.8)

# square = Square(fill_color=BLUE, fill_opacity=0.2)

# ANIMATIONS
# ----------------------------------------------------------

class main(Scene):
    def construct(self):
        # beginning text stuff
        starttext = Tex("R(4,4) $\leq$ 18").scale(1.5)
        self.play(FadeIn(starttext))
        self.play(starttext.animate.move_to(UP))
        self.wait(0.5)
        text17 = Tex("R(","4",",","4",") = 17?").scale(1.5).move_to(ORIGIN + DOWN)
        text17[1].set_color(RED)
        text17[3].set_color(BLUE)
        self.play(Write(text17))
        self.wait()
        self.play(Unwrite(starttext))
        self.play(text17.animate.move_to([0,3.3,0]).scale(0.8))
        self.wait()



# draws K17 into the scene
# class K17(Scene):
#     def construct(self):
        # k17text.to_corner(UP + LEFT)
        # self.play(Write(k17text))

        # construct the graph on the scene
        self.wait()
        self.play(ChangeSpeed(
                AnimationGroup(Create(g)),
                speedinfo={0.08: 0.08},
                affects_speed_updaters=True,
            ))
        self.wait()

        num = DecimalNumber(1, num_decimal_places=0)

        # numbers going around counting the vertices
        poly = RegularPolygon(n=17, radius=2.5).reverse_direction().rotate_about_origin(1)
        vertexList = poly.get_vertices()
        firstVertex = vertexList[0]
        num.move_to(Line(ORIGIN, firstVertex).scale(1.1, about_point=ORIGIN).get_end())
        vertexList = vertexList[1:]
        self.wait()
        for i, vertex in enumerate(vertexList):
            self.play(ChangeSpeed(
                AnimationGroup(
                num.animate.set_value(i+2).move_to(Line(ORIGIN, vertex).scale(1.1, about_point=ORIGIN).get_end())
                ),
                speedinfo={0.1: 1},
                affects_speed_updaters=True,
            ))

        self.wait()
        self.play(FadeOut(num))
        k17text = Tex(r"$K_{17}$").next_to(g, DOWN).scale(1.5)
        self.play(Write(k17text))
        self.wait()
        self.play(Unwrite(k17text))
        self.wait()

# # draws the red and blue edges of K17
# class colouredK17(Scene):
#     def construct(self):
        # self.play(FadeIn(g))
#         self.wait()
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{xcolor}")
        colourtext = Tex(r"$C(x,y) = \begin{cases} {\bullet} & \text{if}\ |y-x| \in \lbrace 1, 2, 4, 8, 9, 13, 15, 16 \rbrace \\ {\blacksquare} & \text{if}\ |y-x| \in \lbrace 3, 5, 6, 7, 10, 11, 12, 14 \rbrace \end{cases}$").scale(0.8)

        colourtext[0][8].set_color(RED)
        colourtext[0][37].set_color(BLUE)
        self.play(Write(colourtext.next_to(g, DOWN, buff=0.2)))

        # colour red lines
        self.play(ChangeSpeed(
                AnimationGroup(Create(redg), Create(blueg)),
                speedinfo={0.1: 0.1},
                affects_speed_updaters=True,
            ))
        # draw blue lines
        # self.play(ChangeSpeed(
        #         AnimationGroup(Create(blueg)),
        #         speedinfo={0.1: 0.1},
        #         affects_speed_updaters=True,
        #     ))
        # move them in and out
        self.play(FadeOut(g))
        self.play((redg.animate.move_to(RIGHT*2)), (blueg.animate.move_to(LEFT*2)))
        self.play((redg.animate.move_to([0,0,0])), (blueg.animate.move_to([0,0,0])))
        self.wait(0.3)
        self.play(Unwrite(colourtext), FadeOut(blueg)) #,Unwrite(text17))
        # self.play(Unwrite(starttext))

        self.wait()

# class textstuff(Scene):
#     def construct(self):
#         mytext = Tex(r"$K_{17}$")
#         self.play(Write(mytext))
#         self.wait()

# class redK17(Scene):
#     def construct(self):
        # text17 = Tex("R(4,4) = 17?").move_to([0,3.3,0])
        # self.play(Write(text17))
        k4text = Tex(r"$K_{4}$?").set_color(RED).scale(1.5)
        k4text.next_to(redg, DOWN)
        # self.play(FadeIn(redg))
        # self.wait()
        self.play(Write(k4text))
        self.wait()
        self.play(redg.animate.move_to(RIGHT*3))

        # first mini
        mini = redg.copy().set_color(WHITE)
        mini.remove_vertices(1,2,3,4,6,7,11,12,13,14,15,16,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to([-2.6,0,0]))
        p = mini.copy().add_edges((5, 8), (5,10)).set_color(PINK)
        self.play(ChangeSpeed(
                AnimationGroup((FadeIn(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(ChangeSpeed(
                AnimationGroup((FadeOut(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(FadeOut(mini))

        # second mini
        mini = redg.copy().set_color(WHITE)
        mini.remove_vertices(1,2,3,6,8,9,11,12,13,14,15,16,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to([-2.1,0,0]))
        p = mini.copy().add_edges((10, 4), (10,5), (10,7), (4,7)).set_color(PINK)
        self.play(ChangeSpeed(
                AnimationGroup((FadeIn(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(ChangeSpeed(
                AnimationGroup((FadeOut(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(FadeOut(mini))

        # third mini
        mini = redg.copy().set_color(WHITE)
        mini.remove_vertices(2,3,4,5,6,8,10,11,12,13,14,15,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to([-1.3,-0.3,0]))
        p = mini.copy().add_edges((9,16), (1,7)).set_color(PINK)
        self.play(ChangeSpeed(
                AnimationGroup((FadeIn(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(ChangeSpeed(
                AnimationGroup((FadeOut(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(FadeOut(mini))
        self.wait()
        self.play(Unwrite(k4text))
        self.play(FadeOut(redg))
        self.wait()

# class blueK17(Scene):
#     def construct(self):
        k4text = Tex(r"$K_{4}$?").set_color(BLUE).scale(1.5)
        k4text.next_to(blueg, DOWN)
        self.play(FadeIn(blueg))
        self.wait()
        self.play(Write(k4text))
        self.wait()
        self.play(blueg.animate.move_to(RIGHT*3))

        self.wait()

        # first mini
        mini = blueg.copy().set_color(WHITE)
        mini.remove_vertices(1,2,3,5,6,7,9,10,11,12,13,15,16)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to([-1.7,-0.5,0]))
        p = mini.copy().add_edges((4,8), (4,17), (8,17)).set_color(PINK)
        self.play(ChangeSpeed(
                AnimationGroup((FadeIn(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(ChangeSpeed(
                AnimationGroup((FadeOut(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        # self.wait()
        self.play(FadeOut(mini))

        # second mini
        mini = blueg.copy().set_color(WHITE)
        mini.remove_vertices(1,2,3,6,8,9,11,12,13,14,15,16,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to([-2.2,-0.2,0]))
        p = mini.copy().add_edges((4,5), (5,7)).set_color(PINK)
        self.play(ChangeSpeed(
                AnimationGroup((FadeIn(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(ChangeSpeed(
                AnimationGroup((FadeOut(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        # self.wait()
        self.play(FadeOut(mini))

        #third mini
        mini = blueg.copy().set_color(WHITE)
        mini.remove_vertices(2,3,4,5,6,8,10,11,12,13,14,15,17)
        self.play(FadeIn(mini))
        self.play(mini.animate.change_layout("circular").move_to([-1.6,-0.3,0]))
        p = mini.copy().add_edges((7,9), (7,16), (9,1), (16,1)).set_color(PINK)
        self.play(ChangeSpeed(
                AnimationGroup((FadeIn(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        self.play(ChangeSpeed(
                AnimationGroup((FadeOut(p)),),
                speedinfo={0.3: 1},
                affects_speed_updaters=True,
            )
        )
        # self.wait()
        self.play(FadeOut(mini))

        self.wait()
        self.play(Unwrite(k4text))
        # self.play(Write(text17))
        # self.play(FadeOut(blueg))
        self.wait()


# merges colours together to show 2-coloured K17 that has no monochromatic K4
# class mergeColours(Scene):
#     def construct(self):
        # text17 = Tex("R(","4",",","4",") = 17?").move_to([0,3.3,0])
        # text17[1].set_color(RED)
        # text17[3].set_color(BLUE)

        self.play(blueg.animate.move_to([-3,0,0]), FadeIn(redg))

        self.wait(0.1)
        bluetext = Tex(r"No $K_{4}$").set_color(BLUE).next_to(blueg, DOWN)
        redtext =Tex(r"No $K_{4}$").set_color(RED).next_to(redg, DOWN)
        self.wait()
        self.play(Write(bluetext), Write(redtext))
        self.wait()
        self.play(Unwrite(bluetext), Unwrite(redtext),)
        self.wait()

        self.play(redg.animate.move_to([0,0,0]),blueg.animate.move_to([0,0,0]))
        mergetext = Tex(r"$K_{17}$").next_to(redg, DOWN, buff=0.5).set_color(WHITE).scale(1.5)
        self.play(Write(mergetext))
        mergegroup = Group(blueg, redg, mergetext)
        self.wait()
        # self.play(Unwrite(mergetext))
        self.wait()
        # self.play(myredg.animate.move_to([3.2,0,0]), myblueg.animate.move_to([3.2,0,0]), mergetext.animate.next_to([3.2,0,0], DOWN))
        self.play(mergegroup.animate.move_to(RIGHT*3)) #, myblueg.animate.move_to([3.2,0,0]), mergetext.animate.next_to([3.2,0,0], DOWN))

        self.play(text17.animate.move_to([0,0,0] + LEFT*3 + UP))

        mytext0 =Tex("R(","4",",","4",") $\\neq$ 17 ").move_to(LEFT*3 + UP)
        mytext0[1].set_color(RED)
        mytext0[3].set_color(BLUE)


        mytext1 = Tex("R(","4",",","4",") $>$ 17").move_to(LEFT*3)
        mytext1[1].set_color(RED)
        mytext1[3].set_color(BLUE)

        mytext2 = Tex("R(","4",",","4",") $\\leq$ 18").move_to(LEFT*3 + DOWN)
        mytext2[1].set_color(RED)
        mytext2[3].set_color(BLUE)

        mytext4 = Tex("R(","4",",","4",") = 18").move_to(LEFT*3 + DOWN*2)
        mytext4[1].set_color(RED)
        mytext4[3].set_color(BLUE)

        # write the text
        self.play(Transform(text17, mytext0))
        staytext17 = text17.copy()
        self.wait()

        self.play(Transform(staytext17, mytext1))

        self.wait()
        self.play(Write(mytext2))
        self.wait()
        copymytext2 = mytext2.copy()
        copytext17 = staytext17.copy()
        self.play(Transform(copytext17, mytext4), Transform(copymytext2, mytext4))
        self.wait()

        box = Rectangle(width=3, height=1).move_to(LEFT*3 + DOWN*2)
        self.play(Create(box))
        mygroup = Group(copytext17, box)
        self.wait()

        slowrectangle = ChangeSpeed(
                AnimationGroup((mygroup.animate.move_to([0,0,0]).scale(2.5)),),
                speedinfo={0.4: 0.2},
                affects_speed_updaters=True,
                rate_func=linear,
            )

        empty = Circle(1).set_color(BLACK).move_to([10,0,0])
        # textsgroup = Group(Unwrite(mytext1), Unwrite(mytext2), Unwrite(mytext3), FadeOut(myredg, myblueg))

        self.play(LaggedStart(
            Unwrite(text17),
            Unwrite(staytext17),
            Unwrite(mytext2),
            Unwrite(mergetext),
            FadeOut(copymytext2),
            FadeOut(redg, blueg),
            FadeOut(empty),
            FadeOut(empty),
            slowrectangle,
            lag_ratio=0.25,
            run_time=4
            )
        )

        self.wait()
        self.wait()
        self.wait()
