import math
import io
from PIL import Image, ImageDraw

class PureSixelEncoder:
    """Lightweight, pure-Python Sixel encoder for RGB Pillow Images."""
    
    @staticmethod
    def encode(img: Image.Image) -> str:
        # Convert image to 256-color palette mode for efficient Sixel encoding
        paletted = img.convert("P", palette=Image.Palette.ADAPTIVE, colors=256)
        width, height = paletted.size
        pixels = paletted.load()
        palette = paletted.getpalette()

        out = []
        # Sixel Header: Start Sixel sequence (\x1bPq)
        out.append("\x1bPq")

        # 1. Define Color Palette (#N;2;R%;G%;B%)
        # Extract RGB triplets and scale 0-255 values to 0-100 percentages
        num_colors = len(palette) // 3
        for i in range(num_colors):
            r = int((palette[i * 3 + 0] / 255.0) * 100)
            g = int((palette[i * 3 + 1] / 255.0) * 100)
            b = int((palette[i * 3 + 2] / 255.0) * 100)
            out.append(f"#{i};2;{r};{g};{b}")

        # 2. Encode pixels in 6-pixel high horizontal bands
        for y_band in range(0, height, 6):
            # Process each color present in the band separately
            for color_idx in range(num_colors):
                sixel_line = []
                has_pixels = False

                for x in range(width):
                    # Build a 6-bit mask representing vertical pixels (top bit = lowest row)
                    bitmask = 0
                    for bit in range(6):
                        py = y_band + bit
                        if py < height and pixels[x, py] == color_idx:
                            bitmask |= (1 << bit)

                    if bitmask > 0:
                        has_pixels = True

                    # Map bitmask (0-63) to ASCII character starting at '?' (ASCII 63)
                    sixel_line.append(chr(63 + bitmask))

                # If this color has pixels in this 6-row band, emit color select + characters
                if has_pixels:
                    # Trim trailing empty '?' characters for efficiency
                    line_str = "".join(sixel_line).rstrip("?")
                    out.append(f"#{color_idx}{line_str}$")

            # Move to next 6-row line
            out.append("-")

        # Sixel Footer: End of String (\x1b\)
        out.append("\x1b\\")
        return "".join(out)


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)

    def __str__(self) -> str:
        # Create image using Pillow
        size = 300
        center = size // 2
        r_pixel = 100

        img = Image.new("RGB", (size, size), color=(20, 20, 25))
        draw = ImageDraw.Draw(img)

        # Draw circle and radius line
        bbox = [center - r_pixel, center - r_pixel, center + r_pixel, center + r_pixel]
        draw.ellipse(bbox, outline=(0, 255, 128), width=3)
        draw.line([(center, center), (center + r_pixel, center)], fill=(255, 200, 0), width=2)

        # Draw labels
        draw.text((center + 15, center - 15), f"r = {self.radius}", fill=(255, 200, 0))
        draw.text((15, 15), f"Circumference: {self.circumference:.2f}", fill=(255, 255, 255))
        draw.text((15, 35), f"Area: {self.area:.2f}", fill=(255, 255, 255))

        # Encode directly with our custom encoder
        return PureSixelEncoder.encode(img)


# Test Output
c = Circle(5.0)
print(c)
