from manim import *

# The Thumbnail
class ThumbNail(Scene):
    def construct(self):
        s = Square().scale(2)
        side = Line(s.get_vertices()[1], s.get_vertices()[2])
        SideLength = Tex("4").move_to(2.25*LEFT)
        q = ArcBetweenPoints(s.get_vertices()[3], s.get_vertices()[1])
        

        self.add(s)
        self.add(q)
        self.add(SideLength)