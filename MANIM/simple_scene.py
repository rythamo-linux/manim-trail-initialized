from manim import *

class SimpleScene(Scene):
    def construct(self):
        # Create text
        hello_text = Text("Hello, Manim!").set_color_by_gradient([RED, YELLOW, BLUE{{INSERTED_CODE}}
]])
        hello_text.to_edge(UP) # Position text at the top

        # Create a square
        my_square = Square(side_length=2, fill_opacity=0.5, fill_color=BLUE, stroke_color=WHITE)

        # Arrange objects
        VGroup(hello_text, my_square).arrange(DOWN)

        # Add objects to the scene with animation
        self.play(Write(hello_text)) # Write the text
        self.play(FadeIn(my_square, shift=UP)) # Fade in the square from below

        # Wait for a moment
        self.wait(2)

        # Transform the square into a circle
        my_circle = Circle(radius=1.5, fill_opacity=0.5, fill_color=GREEN, stroke_color=WHITE)
        self.play(Transform(my_square, my_circle)) # Transform the square to a circle

        # Wait again
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(VGroup(hello_text, my_circle)))
