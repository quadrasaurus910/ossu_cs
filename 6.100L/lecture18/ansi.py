import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)

    def __str__(self) -> str:
        return (
            f"\033[1;34m┌─────────────────────────────────────────┐\033[0m\n"
            f"\033[1;34m│\033[0m  \033[1;32mCircumference:\033[0m {self.circumference:<8.2f}               \033[1;34m│\033[0m\n"
            f"\033[1;34m│\033[0m  \033[1;32mArea:         \033[0m {self.area:<8.2f}               \033[1;34m│\033[0m\n"
            f"\033[1;34m├─────────────────────────────────────────┤\033[0m\n"
            f"          . - ~ - .\n"
            f"      . '           ' .\n"
            f"    .                   .\n"
            f"   .          ●───────•  \033[1;33mr = {self.radius:<5}\033[0m.\n"
            f"    .                   .\n"
            f"      . '           ' .\n"
            f"          ' - ~ - '\n"
            f"\033[1;34m└─────────────────────────────────────────┘\033[0m"
        )

c = Circle(5.0)
print(c)
