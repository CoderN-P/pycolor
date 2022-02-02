from src.pycolor.main import Color

color = Color('cmyk', (0, 0, 0, 0))
print(color.get_raw())
color2 = Color('cmyk', '0, 0, 0, 0')
color3 = Color('cmyk', '0-0-0-0')
print(color)
print(color2)
print(color3)
