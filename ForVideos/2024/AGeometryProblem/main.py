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

        # A point on each line
        A1point = Point(A1.get_bottom())

        # A Circle that makes the arcs mobjects
        A1mob = Circle.from_three_points(s.get_vertices()[0], s.get_vertices()[2], A1.get_top())

        # Shaded Area


        self.add(VGroup(s, A1, A2, A3, A4, A1mob))