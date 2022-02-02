from src.pycolor.main import Color

color = Color('hsl', (0, 100, 50))
print(color.get_raw())
color2 = Color('hsl', '0, 100, 50')
color3 = Color('hSl', '0_100_50')
print(color)
print(color2)
print(color3)