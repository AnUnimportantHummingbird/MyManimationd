from manim import *

# The Thumbnail
class ThumbNail(Scene):
    def construct(self):
        s = Square().scale(2.5)

        self.add(VGroup(s))