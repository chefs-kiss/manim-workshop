from manim import *

class BubbleSort(Scene):
    def construct(self):
        # Array to sort
        arr = [8, 3, 7, 4, 9, 2, 6, 5]
        n = len(arr)
        
        # Title
        title = Text("Bubble Sort Visualization", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create bars representing array elements
        bars = VGroup()
        bar_width = 0.6
        max_height = 4
        colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, BLUE_C, BLUE_D, BLUE_E]
        
        for i, val in enumerate(arr):
            bar = Rectangle(
                width=bar_width,
                height=(val / max(arr)) * max_height,
                fill_opacity=0.8,
                fill_color=colors[i % len(colors)],
                stroke_width=2,
                stroke_color=WHITE
            )
            label = Text(str(val), font_size=24)
            label.next_to(bar, DOWN, buff=0.2)
            
            bar_group = VGroup(bar, label)
            bars.add(bar_group)
        
        bars.arrange(RIGHT, buff=0.3)
        bars.move_to(ORIGIN)
        
        self.play(LaggedStart(*[FadeIn(bar) for bar in bars], lag_ratio=0.1))
        self.wait(0.5)
        
        # Bubble sort algorithm with animation
        for i in range(n):
            for j in range(n - i - 1):
                # Highlight bars being compared
                bar1 = bars[j][0]
                bar2 = bars[j + 1][0]
                
                self.play(
                    bar1.animate.set_stroke(color=ORANGE, width=4),
                    bar2.animate.set_stroke(color=ORANGE, width=4),
                    run_time=0.3
                )
                
                # Compare and swap if needed
                if arr[j] > arr[j + 1]:
                    # Swap in array
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    
                    # Animate swap
                    pos1 = bars[j].get_center()
                    pos2 = bars[j + 1].get_center()
                    
                    self.play(
                        bars[j].animate.move_to(pos2),
                        bars[j + 1].animate.move_to(pos1),
                        run_time=0.5
                    )
                    
                    # Swap in VGroup
                    bars.submobjects[j], bars.submobjects[j + 1] = \
                        bars.submobjects[j + 1], bars.submobjects[j]
                
                # Reset stroke
                self.play(
                    bar1.animate.set_stroke(color=WHITE, width=2),
                    bar2.animate.set_stroke(color=WHITE, width=2),
                    run_time=0.2
                )
            
            # Mark sorted element with green stroke
            sorted_bar = bars[n - i - 1][0]
            self.play(
                sorted_bar.animate.set_stroke(color=PURE_GREEN, width=3),
                run_time=0.3
            )
        
        # Final message
        sorted_text = Text("Sorted!", font_size=48, color=WHITE)
        sorted_text.next_to(bars, DOWN, buff=1)
        self.play(Write(sorted_text))
        self.wait(2)
        