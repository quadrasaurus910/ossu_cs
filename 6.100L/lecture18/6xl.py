import math
import io
from PIL import Image, ImageDraw, ImageFont
import libsixel

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)

    def _generate_sixel(self) -> str:
        # Create canvas
        size = 300
        center = size // 2
        r_pixel = 100
        img = Image.new("RGB", (size, size), color=(30, 30, 30))
        draw = ImageDraw.Draw(img)

        # Draw circle outline
        bbox = [center - r_pixel, center - r_pixel, center + r_pixel, center + r_pixel]
        draw.ellipse(bbox, outline=(0, 255, 128), width=3)

        # Draw radius line (center to right edge)
        draw.line([(center, center), (center + r_pixel, center)], fill=(255, 200, 0), width=2)

        # Labels
        draw.text((center + 20, center - 15), f"r = {self.radius}", fill=(255, 200, 0))
        draw.text((10, 10), f"Circumference: {self.circumference:.2f}", fill=(255, 255, 255))
        draw.text((10, 30), f"Area: {self.area:.2f}", fill=(255, 255, 255))

        # Encode image buffer to Sixel string
        output = io.StringIO()
        sixel_output = libsixel.sixel_output_new(lambda s, _: output.write(s.decode('ascii')), None)
        
        # Save PIL image to raw bytes and pass to libsixel
        img_bytes = img.tobytes()
        libsixel.sixel_output_encode_palette(
            sixel_output, img_bytes, size, size, 3, img.getpalette() or []
        )
        return output.getvalue()

    def __str__(self) -> str:
        return self._generate_sixel()

# Usage
c = Circle(5.0)
print(c)
