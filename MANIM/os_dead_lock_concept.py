
from manim import *

class OSDeadlockConcept(Scene):
    def construct(self):
        # Deadlock Definition
        definition_text = Text("OS Deadlock:", font_size=48).to_edge(UP).set_color_by_gradient(RED, YELLOW, BLUE)
        definition_explanation = Text(
            "A state where two or more processes are blocked\\n"
            "indefinitely, waiting for resources held by others.",
            font_size=28,
        ).next_to(definition_text, DOWN)

        self.play(Write(definition_text))
        self.play(FadeIn(definition_explanation, shift=DOWN))
        self.wait(1);

        self.play(FadeOut(VGroup(definition_text, definition_explanation)))
        self.wait(0.5)

        # Dining Philosophers Setup
        title = Text("Dining Philosophers Deadlock", font_size=36).to_edge(UP).set_color_by_gradient(RED, YELLOW, BLUE)
        self.play(Write(title))
        self.wait(0.5)

        table = Circle(radius=2, color="#A52A2A")
        self.play(Create(table))

        philosophers = VGroup()
        forks = VGroup()
        num_philosophers = 5
        philosopher_color = BLUE
        fork_color = GREY

        # Positions around the table
        angles = [n * 2 * PI / num_philosophers for n in range(num_philosophers)]
        philosopher_positions = [table.point_at_angle(angle) * 1.2 for angle in angles] # Philosophers slightly outside the table
        fork_positions = [table.point_at_angle(angle + PI / num_philosophers) * 0.8 for angle in angles] # Forks between philosophers, closer to center

        # Create philosophers and forks
        for i in range(num_philosophers):
            # Philosophers
            philosopher = Dot(philosopher_positions[i], color=philosopher_color, radius=0.15);
            philosopher_label = Text(f"P{i+1}", font_size=20).next_to(philosopher, philosopher_positions[i] - ORIGIN) # Label next to philosopher, facing away from center
            philosophers.add(VGroup(philosopher, philosopher_label))

            # Forks
            # Forks are positioned between philosophers, pointing towards the center
            fork = Line(fork_positions[i], ORIGIN, color=fork_color, stroke_width=5);
            forks.add(fork)

        self.play(FadeIn(philosophers, shift=UP))
        self.play(Create(forks))
        self.wait(0.5)

        # Deadlock Scenario
        explanation_deadlock = Text(
            "Each philosopher tries to pick up their right fork...",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(explanation_deadlock))
        self.wait(0.5)

        # Simulate each philosopher picking up their right fork
        # P1 picks up fork 1 (index 0), P2 picks up fork 2 (index 1), etc.
        fork_movements = []
        philosopher_texts = VGroup(*[p[1] for p in philosophers]); #

        for i in range(num_philosophers):
            # Fork i is to the right of philosopher i
            philosopher_dot = philosophers[i][0];
            fork_to_pickup = forks[i];
            # Move the fork to appear held by the philosopher
            # Target position: near the philosopher's sphere, lifted slightly
            # Move the fork towards the philosopher's position (linear interpolation)
            held_pos = fork_positions[i] * 0.3 + philosopher_dot.get_center() * 0.7;
            fork_movements.append(fork_to_pickup.animate.move_to(held_pos).set_color(YELLOW)); # Indicate held

        self.play(LaggedStart(*fork_movements, lag_ratio=0.5))
        self.wait(0.5); # Reduced wait after picking up forks

        # Show the deadlock state
        explanation_wait = Text(
            "...and then waits for their left fork,\n"
            "which is held by the philosopher on their left.",
            font_size=24
        ).to_edge(DOWN);

        self.play(Transform(explanation_deadlock, explanation_wait))
        self.wait(2); # Wait during the deadlock state

        # Highlight the waiting state (optional, could add pulsating)
        # For simplicity, just show the held forks and the explanation

        # Indicate deadlock
        deadlock_indicator = Text("DEADLOCK!", font_size=72).set_color_by_gradient(RED, WHITE, RED);
        self.play(Write(deadlock_indicator))
        self.wait(1.5);

        # Fade out
        self.play(FadeOut(VGroup(title, table, philosophers, forks, explanation_deadlock, deadlock_indicator)))
        self.wait(1)
