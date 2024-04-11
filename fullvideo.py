from manim import *
from itertools import combinations
from itertools import permutations
import random
import networkx

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


class Intro(Scene):
    def construct(self):
        introText = MarkupText('<big>R(<span foreground="#FC6255">4</span>,<span foreground="#58C4DD">4</span>) = 18 </big> \n<small>A proof without words</small>')
        authors = MarkupText('By: <span foreground="#58C4DD">Sloane Wensauer</span> and <span foreground="#FC6255">Max Liu</span>')

        generalEquation = Tex("R(", "s", ",", "t", ")", " $\leq$ R(", "s-1", ",", "t", ")", " + R(", "s", ",", "t-1", ")")
        equation = Tex("R(", "4", ",", "4", ")", " $\leq$ ", "R(", "3", ",", "4", ")", " + ", "R(", "4", ",", "3", ")")


        self.play(DrawBorderThenFill(introText))
        self.wait()
        self.play(FadeOut(introText))

        self.play(Write(authors))
        self.wait()
        self.play(FadeOut(authors))


        # fancy colouring woahh
        generalEquation.set_color_by_tex("s", RED)
        generalEquation.set_color_by_tex("s-1", RED)
        generalEquation.set_color_by_tex("t", BLUE)
        generalEquation.set_color_by_tex("t-1", BLUE)


        equation[1].set_color(RED)
        equation[3].set_color(BLUE)
        equation[7].set_color(RED)
        equation[9].set_color(BLUE)
        equation[13].set_color(RED)
        equation[15].set_color(BLUE)


        self.play(Write(generalEquation))
        self.wait()
        self.play(generalEquation.animate.move_to(UP))

        # create copy of equation
        equationCopy = generalEquation.copy()
        self.add(equationCopy)
        self.play(equationCopy.animate.move_to(ORIGIN))
        self.wait(0.5)

        self.play(Transform(equationCopy, equation))
        self.wait()

        # create copy of R(4,3), R(3,4) for future use
        textGroup  = equation[6::].copy()
        self.add(textGroup)

        # adding braces
        b1 = Brace(equation[6:11], DOWN)
        br1 = b1.get_text("R(3,4) = ?")

        b2 = Brace(equation[12::], DOWN)
        br2 = b2.get_text("R(4,3) = ?")

        self.add(b1)
        self.play(Write(br1))
        self.wait(1)
        self.play(FadeOut(br1), FadeOut(b1))


        self.add(b2)
        self.play(Write(br2))
        self.wait(1)
        self.play(FadeOut(br2), FadeOut(b2))
        self.wait(0.75)
        self.play(FadeOut(equationCopy), FadeOut(generalEquation))

        # preparing for k9 scene
        # self.add(NumberPlane())

        self.play(Transform(textGroup[5], Tex("=").move_to(RIGHT)))

        self.play(textGroup.animate.move_to(3.25*UP).shift(0.5*LEFT))
        equals = Tex(" = ?").next_to(textGroup, RIGHT)
        self.play(Write(equals))


        #------------------------------------------------------- PART 1 ---------------------------------------------
        self.k9Scene()
        self.play(Transform(equals, Tex(" = 9").next_to(textGroup, RIGHT)))
        newGroup = VGroup(textGroup, equals)
        self.play(newGroup.animate.move_to(ORIGIN).scale(1.5))
        self.wait()
        bruh = Tex("R(4,4) $\leq$ 9 + 9").scale(1.5)
        self.play(Transform(newGroup, bruh))
        self.play(Transform(newGroup, Tex("R(4,4) $\leq$ 18").scale(1.5)))
        self.wait(2)
        self.play(FadeOut(newGroup))

    def k9Scene(self):
        vertices = list(range(0,9))
        arr = list(range(0,9))
        edges = list(combinations(arr,2))

        k9 = Graph(vertices, edges,layout = 'circular', layout_scale = 2)

          # ---- displaying graph-----
        self.wait()
        self.play(ChangeSpeed(
                AnimationGroup(Create(k9)),
                speedinfo = {0.10: 0.10},
                affects_speed_updaters = True,
            ))
        self.wait()

        # enumeration.
        # displaying da numbers
        num = DecimalNumber(1, num_decimal_places=0)
        poly = RegularPolygon(n=9, radius=2.1).reverse_direction().rotate_about_origin(-2.965)

        vertexList = poly.get_vertices()
        firstVertex = vertexList[0]
        num.move_to(Line(ORIGIN, firstVertex).scale(1.1, about_point=ORIGIN).get_end())
        vertexList = vertexList[1:]

        for i, vertex in enumerate(vertexList):
            self.play(ChangeSpeed(
                AnimationGroup(num.animate.set_value(i+2).move_to(Line(ORIGIN, vertex).scale(1.1, about_point=ORIGIN).get_end())),
                speedinfo = {0.1:1},
                affects_speed_updaters=True,
                )
            )
        self.play(FadeOut(num))

        b3 = Brace(k9, 0.6*DOWN)
        br3 = b3.get_tex(r"K_{9}")
        self.play(Write(br3))
        self.wait(0.5)
        self.play(FadeOut(br3))


        self.wait()

        self.play(k9.animate.scale(0.8))
        self.play(k9.animate.move_to([5,0,0]))
        self.wait()


        mini = k9.copy().set_color(GREEN)
        for edge in edges:
            if (edge[0] != 7 and edge[1] != 7):
                mini.remove_edges(edge)
        self.play(FadeIn(mini))
        # self.wait()
        # self.play(mini.animate.shift(DOWN))
        self.play(mini.animate.move_to([-6, 1, 0])
                  .scale(0.5)
                  .set_color(WHITE))
        # self.play(mini.animate.scale(0.5))
        self.play(Rotate(mini, 170*DEGREES))
        self.wait()

        miniCopyList = []
        blueCopies = []
        redCopies = []
        for i in range(8):
            graph = mini.copy()
            redEdges = []
            blueEdges = []
            redEdgeDict = {}
            blueEdgeDict = {}

            edgeList = graph.edges
            counter = 0

            for edge in edgeList:
                if (counter < (7-i)):
                    redEdges.append(edge)
                else:
                    blueEdges.append(edge)
                counter += 1

            if (counter < 5):
                blueCopies.append(graph)
            else:
                redCopies.append(graph)

            for edge in redEdges:
                redEdgeDict.update({edge: {"stroke_color": RED}})

            for edge in blueEdges:
                blueEdgeDict.update({edge: {"stroke_color": BLUE}})

            colorDict = redEdgeDict | blueEdgeDict
            g = Graph(graph.vertices, graph.edges, edge_config=colorDict, layout= 'circular', layout_scale= 0.8)
            g.rotate(170*DEGREES)


            if (i < 4):
                g.shift((6-2.5*i)*LEFT + UP)
            else:
                g.shift((6-2.5*(i-4))*LEFT + 2*DOWN)

            miniCopyList.append(g)
            self.play(ChangeSpeed(
                AnimationGroup(Create(g)),
                speedinfo = {0.0: 0.5},
                affects_speed_updaters = True,
            ))
            self.wait(0.5)
            self.remove(mini)

        self.wait(1.2)
        lt = {0: [-0.75, 1, 0], 1: [0, 1, 0], 2: [0.75, 1, 0], 3: [-1.5, -2, 0], 4: [-0.5, -2.35, 0], 5: [0, -3, 0], 6: [0.5, -2.35, 0], 7: [0, 0, 0], 8:[1.5, -2, 0]}                          # general case
        redTrivial = {0: [-0.5, 1, 0], 1: [0.5, 1, 0], 2: [-1.5, -1.5, 0], 3: [-1, -2, 0], 4: [-.5, -2.5, 0], 5: [0.5, -2.5, 0], 6: [1, -2.0, 0], 7: [0, 0, 0], 8:[1.5, -1.5, 0]}             # trivial case for red
        blueTrivial = {0: [-1, 1, 0], 1: [-0.5, 1, 0], 2: [0.5, 1, 0], 3: [1, 1, 0], 4: [-1, -1, 0], 5: [-0.5, -1.5, 0], 6: [0.5, -1.5, 0], 7: [0, 0, 0], 8:[1, -1, 0]}                        # trivial case for blue

        # general case
        whiteListGeneral = [0, 1, 2]
        edgeColouringGeneral = {}
        for edge in mini.edges:
            if (edge[0] in whiteListGeneral or edge[1] in whiteListGeneral):
                edgeColouringGeneral.update({edge: {"stroke_color": WHITE}})
            else:
                edgeColouringGeneral.update({edge: {"stroke_color": RED}})

        whiteListRed = [0,1]
        edgeColouringRed = {}
        for edge in mini.edges:
            if (edge[0] in whiteListRed or edge[1] in whiteListRed):
                edgeColouringRed.update(({edge: {"stroke_color": WHITE}}))
            else:
                edgeColouringRed.update({edge: {"stroke_color": RED}})


        whiteListBlue = [0, 1, 2, 3]
        edgeColouringBlue = {}
        for edge in mini.edges:
            if (edge[0] in whiteListBlue or edge[1] in whiteListBlue):
                edgeColouringBlue.update({edge: {"stroke_color": WHITE}})
            else:
                edgeColouringBlue.update({edge: {"stroke_color": BLUE}})



        proofRed = Graph(mini.vertices, mini.edges, edge_config = edgeColouringRed, layout=redTrivial)
        proofBlue = Graph(mini.vertices, mini.edges, edge_config = edgeColouringBlue, layout=blueTrivial)
        proofGeneral = Graph(mini.vertices, mini.edges, edge_config=edgeColouringGeneral, layout=lt)

        proofBlue.shift(UP)
        proofRed.shift(UP)
        proofGeneral.shift(UP)

        # -------------------------------------------------------------- PROOF OF R(3,3) OR SOMETHING IDK -------------------------------------------------------------------

        grouping = VGroup()
        for g in miniCopyList:
            grouping.add(g)

        self.play(grouping.animate.scale(0.5))
        self.play(grouping.animate.to_corner(LEFT + DOWN))
        self.play(FadeOut(k9))

        # >= 6 red edges..
        for i in range(2):
            self.play(Transform(grouping[i], proofRed))
            self.wait()


        self.play(proofRed.animate.add_edges((4,5), (3,4), (3,5)))
        self.add(proofRed)
        self.remove(*grouping[0:2])
        self.play(proofRed.edges[4,5].animate.set_color(RED), proofRed.edges[3,4].animate.set_color(RED), proofRed.edges[3,5].animate.set_color(RED))
        p = Polygon(*[[0,1,0], [-1, -1, 0], [-0.5, -1.5, 0], [0.5, -1.5, 0]], color=RED_B)
        p.set_fill(RED,opacity=0.5)
        self.play(Create(p))
        self.wait()

        self.play(proofRed.animate.remove_edges((4,5), (3,4), (3,5)))
        self.play(FadeOut(p))
        self.wait()


        self.play(proofRed.animate.add_edges((4,5), (3,4), (3,5)))
        # self.add(proofRed)
        self.play(proofRed.edges[4,5].animate.set_color(BLUE), proofRed.edges[3,4].animate.set_color(BLUE), proofRed.edges[3,5].animate.set_color(BLUE))
        p = Polygon(*[[-1, -1, 0], [-0.5, -1.5, 0], [0.5, -1.5, 0]], color=BLUE_B)
        p.set_fill(BLUE,opacity=0.5)
        self.play(Create(p))
        self.wait()

        self.play(FadeOut(p))
        self.play(FadeOut(proofRed))


        self.wait()

        # >= 4 blue edges..
        for i in range(3,8):
            self.play(Transform(grouping[i], proofBlue))

        self.play(proofBlue.animate.add_edges((5,6)))
        self.add(proofBlue)
        self.remove(*grouping[3::])
        self.play(proofBlue.edges[5,6].animate.set_color(BLUE))
        p = Polygon(*[[0, 1, 0], [-0.5, -0.5, 0], [0.5, -0.5, 0]], color=BLUE_B)

        p.set_fill(BLUE,opacity=0.5)
        self.play(Create(p))
        self.wait()


        self.play(proofBlue.animate.remove_edges((5,6)))
        self.play(FadeOut(p))
        self.wait()


        self.play(proofBlue.animate.add_edges((4,5), (4,6), (4,8), (5,8), (5,6), (6,8)))
        # self.add(proofBlue)
        self.play(proofBlue.edges[4,5].animate.set_color(RED), proofBlue.edges[4,8].animate.set_color(RED), proofBlue.edges[4,6].animate.set_color(RED),
                  proofBlue.edges[5,8].animate.set_color(RED), proofBlue.edges[5,6].animate.set_color(RED), proofBlue.edges[6,8].animate.set_color(RED))
        p = Polygon(*[[-1, 0, 0], [-0.5, -0.5, 0], [0.5, -0.5, 0], [1, 0, 0]], color=RED_B)
        p.set_fill(RED,opacity=0.5)
        self.play(Create(p))
        self.wait()

        self.play(FadeOut(p))
        self.play(FadeOut(proofBlue))


        arr = list(range(3,9))
        arr = [x for x in arr if x != 7]
        edges = list(permutations(arr,2))
        edges = list(set((min(a, b), max(a, b)) for a, b in edges))

        # general case...
        for i in range(2,3):
            self.play(Transform(grouping[i], proofGeneral))

        for edge in edges:
            self.play(
                ChangeSpeed(
                AnimationGroup(proofGeneral.animate.add_edges(edge)),
                speedinfo = {0.0: 0.5},
                affects_speed_updaters = True,
                ),
                run_time = 0.25
            )

        self.play(proofGeneral.edges[3,8].animate.set_color(RED), proofGeneral.edges[5,8].animate.set_color(BLUE), proofGeneral.edges[4,6].animate.set_color(RED),
                  proofGeneral.edges[4,5].animate.set_color(BLUE), proofGeneral.edges[5,6].animate.set_color(RED), proofGeneral.edges[4,8].animate.set_color(BLUE),
                  proofGeneral.edges[3,4].animate.set_color(RED), proofGeneral.edges[3,6].animate.set_color(BLUE), proofGeneral.edges[6,8].animate.set_color(RED),
                  proofGeneral.edges[3,5].animate.set_color(BLUE))

        self.wait()
        self.remove(*grouping[2:4])
        p = Polygon(*[[-0.5, -1.35, 0], [0, -2, 0], [1.5, -1, 0]], color=BLUE_B)

        p.set_fill(BLUE,opacity=0.5)
        self.play(Create(p))
        self.wait()

        self.play(FadeOut(p))
        self.play(proofGeneral.animate.remove_edges((3, 8), (3, 4), (5, 8), (6, 8), (4, 6), (4, 5), (5, 6), (4, 8), (3, 6), (3, 5)))
        self.wait()

        for edge in edges:
            self.play(
                ChangeSpeed(
                AnimationGroup(proofGeneral.animate.add_edges(edge)),
                speedinfo = {0.0: 0.5},
                affects_speed_updaters = True,
                ),
                run_time = 0.25
            )


        self.play(proofGeneral.edges[3,8].animate.set_color(RED), proofGeneral.edges[5,8].animate.set_color(BLUE), proofGeneral.edges[4,6].animate.set_color(RED),
            proofGeneral.edges[4,5].animate.set_color(BLUE), proofGeneral.edges[5,6].animate.set_color(RED), proofGeneral.edges[4,8].animate.set_color(RED),
            proofGeneral.edges[3,4].animate.set_color(RED), proofGeneral.edges[3,6].animate.set_color(BLUE), proofGeneral.edges[6,8].animate.set_color(RED),
            proofGeneral.edges[3,5].animate.set_color(BLUE))

        p = Polygon(*[[0, 1, 0], [-1.5, -1, 0], [-0.5, -1.35, 0], [1.5, -1, 0]], color=RED_B)
        p.set_fill(RED,opacity=0.5)
        self.play(Create(p))
        self.wait()

        self.play(FadeOut(p))
        self.play(FadeOut(proofGeneral))
        self.wait()

        # PART 2 ------------------------------------------------------------

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
