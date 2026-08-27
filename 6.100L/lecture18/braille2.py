import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.diameter = 2 * radius
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)

    def _generate_braille_art(self, width: int = 28, height: int = 14) -> str:
        # Sub-pixel dimensions (2 wide x 4 high per character block)
        canvas_w = width * 2
        canvas_h = height * 4
        
        grid = [[False for _ in range(canvas_w)] for _ in range(canvas_h)]
        
        center_x = canvas_w // 2
        center_y = canvas_h // 2
        
        # Radii adjusted for standard terminal character height-to-width ratio (~2:1)
        r_x = canvas_w / 2 - 3
        r_y = canvas_h / 2 - 1

        # 1. Plot Tight Circle Outline
        steps = 160
        for i in range(steps):
            theta = (2 * math.pi * i) / steps
            x = int(round(center_x + r_x * math.cos(theta)))
            y = int(round(center_y + r_y * math.sin(theta)))
            if 0 <= x < canvas_w and 0 <= y < canvas_h:
                grid[y][x] = True

        # 2. Plot Radius Line (Center to Right Edge)
        for x in range(int(center_x), int(center_x + r_x)):
            grid[int(center_y)][x] = True

        # 3. Convert grid of sub-pixels into Unicode Braille characters
        # Braille bit positions mapping
        braille_dot_map = [
            [0x01, 0x08],
            [0x02, 0x10],
            [0x04, 0x20],
            [0x40, 0x80]
        ]

        braille_lines = []
        for row in range(0, canvas_h, 4):
            line = []
            for col in range(0, canvas_w, 2):
                code = 0x2800  # Base Braille Unicode offset
                for dy in range(4):
                    for dx in range(2):
                        if row + dy < canvas_h and col + dx < canvas_w:
                            if grid[row + dy][col + dx]:
                                code |= braille_dot_map[dy][dx]
                line.append(chr(code))
            braille_lines.append("".join(line))

        # 4. Define the Metadata List (Easy to append new items here in the future)
        metrics_list = [
            f"\033[1;33mr            = {self.radius}\033[0m",
            f"\033[1;36mdiameter     = {self.diameter:.2f}\033[0m",
            f"\033[1;36mcircumference = {self.circumference:.2f}\033[0m",
            f"\033[1;36marea         = {self.area:.2f}\033[0m",
            # Add future items here, e.g.:
            # f"\033[1;36msphere vol   = {(4/3)*math.pi*(self.radius**3):.2f}\033[0m",
        ]

        # 5. Merge the Braille Graphic with the Side List
        mid_row = len(braille_lines) // 2
        # Align list start so radius label sits right at the center line level
        list_start_row = mid_row

        final_output = []
        max_rows = max(len(braille_lines), list_start_row + len(metrics_list))

        for r in range(max_rows):
            # Get Braille line or blank spacing if out of bounds
            b_line = braille_lines[r] if r < len(braille_lines) else " " * width
            
            # Match metadata items to corresponding rows
            list_idx = r - list_start_row
            if 0 <= list_idx < len(metrics_list):
                metric_text = metrics_list[list_idx]
                # Insert connecting line symbol on the center row
                prefix = " ──► " if r == mid_row else "     "
                combined = f"{b_line}{prefix}{metric_text}"
            else:
                combined = b_line
                
            final_output.append(combined)

        return "\n".join(final_output)

    def __str__(self) -> str:
        return self._generate_braille_art()


# Demo Output
c = Circle(5.0)
print(c)
