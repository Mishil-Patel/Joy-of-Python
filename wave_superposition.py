from manim import *

class WaveSuperposition(Scene):
    def construct(self):
        # Parameters of the waves
        amplitude1 = 1
        amplitude2 = 0.8
        wavelength1 = 2
        wavelength2 = 1.5
        phase_shift = PI / 2  # Phase difference between waves

        # Functions defining the waves
        def wave1(x):
            return amplitude1 * np.sin(2 * PI * x / wavelength1)

        def wave2(x):
            return amplitude2 * np.sin(2 * PI * x / wavelength2 + phase_shift)

        # Create axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )

        # Create waves as graphs
        graph1 = axes.get_graph(wave1, color=GREEN)
        graph2 = axes.get_graph(wave2, color=RED)

        # Display waves on the screen
        self.play(ShowCreation(graph1), ShowCreation(graph2))

        # Superposition of waves
        def superposed_wave(x):
            return wave1(x) + wave2(x)

        graph_superposed = axes.get_graph(superposed_wave, color=YELLOW)
        self.play(Transform(graph1.copy(), graph_superposed))
        
        self.wait(2)
