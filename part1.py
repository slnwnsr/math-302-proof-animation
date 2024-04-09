from manim import *
from itertools import combinations
from itertools import permutations
import random
import networkx

#Testing....
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


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


# BEGINNING OF ANIMATION !!!
class Intro(Scene):
    def construct(self):
        introText = MarkupText("<big>Proof of R(4,4) = 18 </big> \n <small>without words</small>")
        authors = MarkupText("By: Sloane Wensauer and Max Liu")
        self.wait()

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


class testClass(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        G = Graph(vertices, edges, layout=lt)
        self.add(G)
        self.wait()
        self.play(
            ChangeSpeed(
                AnimationGroup(G.animate.add_edges((2,4))), 
                speedinfo = {0.0: 0.5},
                affects_speed_updaters = True,
            )
        )
        self.play(G.animate.add_edges((2,4), (1,3)))
        self.play(G.edges[2,4].animate.set_color(RED), G.edges[1,3].animate.set_color(RED))
        self.wait()
        p = Polygon(*[[-1, -1, 0], [-0.5, -1.5, 0], [0.5, -1.5, 0]], color=RED_B)
        p.set_fill(RED,opacity=0.5)
        self.play(Create(p))
        self.wait()

        self.play(G.animate.remove_edges((2,4), (1,3)))
        self.play(FadeOut(p))


class K18(Scene):

    def construct(self):

        #----------------------------------------------------------- PART 1 --------------------------------------------------------------------

        #----creation of K9 graph----- 
        
        # preamble...
        vertices = list(range(1,10))
        arr = list(range(1,10))
        labels = {}
        edges = list(combinations(arr,2))

        # colouring the edges randomly... 
        numReds = random.randint(0, 9*(9-1)/2)
        redEdges = []
        blueEdges = list(edges)

        for i in range(numReds):
            colouredEdge = random.choice(blueEdges)
            redEdges.append(colouredEdge)
            blueEdges.remove(colouredEdge)
        
        # finding a K3 or K4 subgraph of any colouring.... .
            
        # --- checking for red... ----

        GRed = networkx.Graph()
        GBlue = networkx.Graph()

        GRed.add_edges_from(redEdges)
        GBlue.add_edges_from(blueEdges)


        redK4 = [i for i in networkx.enumerate_all_cliques(GRed) if len(i) == 4]        # cliques <==> complete graphs
        redK3 = [i for i in networkx.enumerate_all_cliques(GRed) if len(i) == 4]

        #--- checking for blue... -----
        
        blueK4 = [i for i in networkx.enumerate_all_cliques(GBlue) if len(i) == 4]
        blueK3 = [i for i in networkx.enumerate_all_cliques(GBlue) if len(i) == 4]
        

        redEdgeDict = {}
        for edge in redEdges:
            redEdgeDict.update({edge: {"stroke_color": RED}})

        blueEdgeDict = {}
        for edge in blueEdges:
            blueEdgeDict.update({edge: {"stroke_color": BLUE}})

        colorDict = redEdgeDict | blueEdgeDict


        k9 = Graph(vertices, edges, edge_config = colorDict,layout = 'circular', layout_scale = 3)

        # ---- displaying graph----- 
        self.wait()
        self.play(ChangeSpeed(
                AnimationGroup(Create(k9)), 
                speedinfo = {0.10: 0.10},
                affects_speed_updaters = True,
            ))
        self.wait(2)
        
        # enumeration. 
        # displaying da numbers
        num = DecimalNumber(1, num_decimal_places=0)
        poly = RegularPolygon(n=9, radius=3.1).reverse_direction().rotate_about_origin(-2.965)

        vertexList = poly.get_vertices()
        firstVertex = vertexList[0]
        num.move_to(Line(ORIGIN, firstVertex).scale(1.1, about_point=ORIGIN).get_end())
        vertexList = vertexList[1:]

        for i, vertex in enumerate(vertexList):
            self.play(ChangeSpeed(
                AnimationGroup(num.animate.set_value(i+2).move_to(Line(ORIGIN, vertex).scale(1.1, about_point=ORIGIN).get_end())),
                speedinfo = {0.08:1},
                affects_speed_updaters=True,
                )
            )
        self.play(FadeOut(num))
        self.wait()

        self.play(k9.animate.scale(0.7))
        self.play(k9.animate.move_to([-4,0,0]))

        #----------------------------------------------------------- PART 2 --------------------------------------------------------------------

        if (len(redK4) != 0):
            vertices = [i for i in redK4[0]]
            edges = list(combinations(vertices, 2))
            redLabels = {}
            redEdgesDict = {}
            for vertex in vertices:
                redLabels.update({vertex : str(vertex)})
            
            for edge in edges:
                redEdgesDict.update({edge: {"stroke_color": RED}})

            redSubGraph = Graph(vertices, edges, labels = redLabels, edge_config = redEdgesDict, layout = 'circular', layout_scale = 2)
            self.play(ChangeSpeed(
                AnimationGroup(Create(redSubGraph)), 
                speedinfo = {0.1: 0.3},
                affects_speed_updaters = True,
            ))
        else:
            vertices = [i for i in blueK3[0]]
            edges = list(combinations(vertices, 2))
            blueLabels = {}
            blueEdgesDict = {}

            for vertex in vertices:
                blueLabels.update({vertex : str(vertex)})

            for edge in edges:
                blueEdgesDict.update({edge: {"stroke_color": BLUE}})

            blueSubGraph = Graph(vertices, edges, labels = blueLabels, edge_config = blueEdgesDict, layout = 'circular', layout_scale = 2)
            self.play(ChangeSpeed(
                AnimationGroup(Create(blueSubGraph)), 
                speedinfo = {0.1: 0.3},
                affects_speed_updaters = True,
            ))
            print(blueLabels)
            print(blueEdgesDict)    
        
        self.wait()
