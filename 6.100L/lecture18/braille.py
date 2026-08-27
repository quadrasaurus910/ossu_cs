import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)

    def _generate_braille_art(self, width: int = 40, height: int = 20) -> str:
        # Braille sub-pixel dimensions (2 wide x 4 high per character block)
        canvas_w = width * 2
        canvas_h = height * 4
        
        grid = [[False for _ in range(canvas_w)] for _ in range(canvas_h)]
        
        center_x = canvas_w / 2
        center_y = canvas_h / 2
        r_x = (canvas_w / 2) - 4
        r_y = (canvas_h / 2) - 2

        # 1. Plot Circle outline
        steps = 120
        for i in range(steps):
            theta = (2 * math.pi * i) / steps
            x = int(center_x + r_x * math.cos(theta))
            y = int(center_y + r_y * math.sin(theta))
            if 0 <= x < canvas_w and 0 <= y < canvas_h:
                grid[y][x] = True

        # 2. Plot Radius line (center to right edge)
        for x in range(int(center_x), int(center_x + r_x)):
            grid[int(center_y)][x] = True

        # 3. Convert grid of sub-pixels into Unicode Braille characters
        # Braille bit positions:
        # (0,0)->1, (0,1)->2, (0,2)->4, (1,0)->8, (1,1)->16, (1,2)->32, (0,3)->64, (1,3)->128
        braille_dot_map = [
            [0x01, 0x08],
            [0x02, 0x10],
            [0x04, 0x20],
            [0x40, 0x80]
        ]

        lines = []
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
            lines.append("".join(line))

        # Add text measurements around the graphic using ANSI color formatting
        output = [
            f"\033[1;36mCircumference: {self.circumference:.2f}\033[0m",
            f"\033[1;36mArea:          {self.area:.2f}\033[0m",
            ""
        ]
        
        # Inject the "r = X" label next to the radius line in the middle of the diagram
        mid = len(lines) // 2
        for idx, line in enumerate(lines):
            if idx == mid:
                output.append(f"{line} \033[1;33mr = {self.radius}\033[0m")
            else:
                output.append(line)

        return "\n".join(output)

    def __str__(self) -> str:
        return self._generate_braille_art()

c = Circle(5.0)
print(c)
