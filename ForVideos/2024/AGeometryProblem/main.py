from manim import *

# The Thumbnail
class ThumbNail(Scene):
    def construct(self):
        s = Square().scale(2)

        # Length of a side of a square
        side = Line(s.get_vertices()[2], s.get_vertices()[3])

        # Makes a point on each of the verticies
        VertA = Point(s.get_vertices()[2])
        VertB = Point(s.get_vertices()[3])
        VertC = Point(s.get_vertices()[0])
        VertD = Point(s.get_vertices()[1])

        # Label for each of the verticies
        A = Tex("A").next_to(VertA, LEFT)
        B = Tex("B").next_to(VertB, RIGHT)
        C = Tex("C").next_to(VertC, RIGHT)
        D = Tex("D").next_to(VertD, LEFT)
        
        # Side Length
        M = Point(side.get_midpoint())
        slength = Tex("12").move_to(2.5*LEFT)

        # Quarter Circles
        A1 = ArcBetweenPoints(s.get_vertices()[0], s.get_vertices()[2])
        A2 = ArcBetweenPoints(s.get_vertices()[1], s.get_vertices()[3])
        A3 = ArcBetweenPoints(s.get_vertices()[2], s.get_vertices()[0])
        A4 = ArcBetweenPoints(s.get_vertices()[3], s.get_vertices()[1])

        # A Circle that makes the arcs mobjects
        A1mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[0])
        A2mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[1])
        A3mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[2])
        A4mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[3])

        # Shaded Area
        ShadedArea = Intersection(A1mob, A2mob, A3mob, A4mob, color = WHITE, fill_opacity = 0.5)

        # Questions
        q = Tex("What is the area of the shaded reigon?").to_edge(UP, buff=0.5)


        self.add(VGroup(s, A1, A2, A3, A4))
        self.add(ShadedArea, q)
        self.add(A, B, C, D, slength)

class ProblemInfo(Scene):
    def construct(self):
        s = Square().scale(1)

        # Length of a side of a square
        side = Line(s.get_vertices()[2], s.get_vertices()[3])

        # Makes a point on each of the verticies
        VertA = Point(s.get_vertices()[2])
        VertB = Point(s.get_vertices()[3])
        VertC = Point(s.get_vertices()[0])
        VertD = Point(s.get_vertices()[1])

        # Label for each of the verticies
        A = Tex("A").next_to(VertA, LEFT)
        B = Tex("B").next_to(VertB, RIGHT)
        C = Tex("C").next_to(VertC, RIGHT)
        D = Tex("D").next_to(VertD, LEFT)
        
        # Side Length
        M = Point(side.get_midpoint())
        slength = Tex("12").move_to(2.5*LEFT)

        # Quarter Circles
        A1 = ArcBetweenPoints(s.get_vertices()[0], s.get_vertices()[2])
        A2 = ArcBetweenPoints(s.get_vertices()[1], s.get_vertices()[3])
        A3 = ArcBetweenPoints(s.get_vertices()[2], s.get_vertices()[0])
        A4 = ArcBetweenPoints(s.get_vertices()[3], s.get_vertices()[1])

        # A Circle that makes the arcs mobjects
        A1mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[0])
        A2mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[1])
        A3mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[2])
        A4mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[3])

        # Shaded Area
        ShadedArea = Intersection(A1mob, A2mob, A3mob, A4mob, color = WHITE, fill_opacity = 0.5)

        self.play(Create(s))
        self.play(Create(VGroup(A1, A2, A3, A4)))
        self.play(Create(ShadedArea))
        self.play(Write(A, run_time=0.5))
        self.play(Write(B, run_time=0.5))
        self.play(Write(C, run_time=0.5))
        self.play(Write(D, run_time=0.5))