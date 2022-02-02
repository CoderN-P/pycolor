from src.pycolor.main import Color

color = Color('RGB', (1, 2, 3))
print(color.get_raw())
color2 = Color('RGB', '1 2 3')
color3 = Color('RGB', '1/2/3')
color4 = Color('RGB', '1,2,3')
#You can split the rgb in different ways
# returns: Color(color_input=(1, 2, 3), input_type='rgb', hex='#010203', cmyk='67, 33, 0, 99', name='Ebony', hsl='210, 50, 1', xyz='1, 1, 1', image='https://singlecolorimage.com/get/010203/400x100.png', hsv='210, 67, 1', rgb=(1, 2, 3))
print(color)
print(color2)
print(color3)
print(color4)
