import math
import io
from PIL import Image, ImageDraw
from sixel import SixelSerializer

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)

    def _generate_sixel(self) -> str:
        size = 300
        center = size // 2
        r_pixel = 100

        # Draw image with PIL
        img = Image.new("RGB", (size, size), color=(30, 30, 30))
        draw = ImageDraw.Draw(img)

        # Draw circle and radius line
        bbox = [center - r_pixel, center - r_pixel, center + r_pixel, center + r_pixel]
        draw.ellipse(bbox, outline=(0, 255, 128), width=3)
        draw.line([(center, center), (center + r_pixel, center)], fill=(255, 200, 0), width=2)

        # Labels
        draw.text((center + 20, center - 15), f"r = {self.radius}", fill=(255, 200, 0))
        draw.text((10, 10), f"Circumference: {self.circumference:.2f}", fill=(255, 255, 255))
        draw.text((10, 30), f"Area: {self.area:.2f}", fill=(255, 255, 255))

        # Convert PIL Image to Sixel via py-sixel
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        
        output = io.StringIO()
        serializer = SixelSerializer(output)
        serializer.write_bytes(buf.getvalue())
        
        return output.getvalue()

    def __str__(self) -> str:
        return self._generate_sixel()

c = Circle(5.0)
print(c)
