from manim import *

# The Thumbnail
class ThumbNail(Scene):
    def construct(self):
        s = Square().scale(2.5)

        # Quarter Circles
        A1 = ArcBetweenPoints(s.get_vertices()[0], s.get_vertices()[2])
        A2 = ArcBetweenPoints(s.get_vertices()[1], s.get_vertices()[3])
        A3 = ArcBetweenPoints(s.get_vertices()[2], s.get_vertices()[0])
        A4 = ArcBetweenPoints(s.get_vertices()[3], s.get_vertices()[1])

        # Makes a point on each of the verticies
        A = Point(s.get_vertices()[0])
        B = Point(s.get_vertices()[1])
        C = Point(s.get_vertices()[2])
        D = Point(s.get_vertices()[3])
        

        # Length of a side of a square
        side = Line(s.get_vertices()[0], s.get_vertices()[1])

        # A Circle that makes the arcs mobjects
        A1mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[0])
        A2mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[1])
        A3mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[2])
        A4mob = Circle(radius = side.get_length()).move_to(s.get_vertices()[3])

        # Shaded Area
        ShadedArea = Intersection(A1mob, A2mob, A3mob, A4mob, color = WHITE, fill_opacity = 0.5)

        # The question
        q = Tex("Can you solve this?").to_edge(UP, buff=0.5)

        self.add(VGroup(s, A1, A2, A3, A4))
        self.add(ShadedArea, q, A)