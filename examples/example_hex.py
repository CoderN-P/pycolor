from src.pycolor.main import Color
color = Color('hEx', 'FFFFFF')
print(color.get_raw())
color2 = Color('hex', '#FFFFFF')
color3 = Color('hex', '#ffffff')
# returns: Color(color_input='FFFFFF', input_type='hex', hex='#FFFFFF', cmyk='0, 0, 0, 0', name='White', hsl='0, 0, 100', xyz='95, 100, 108.883', image='https://singlecolorimage.com/get/FFFFFF/400x100.png', hsv='0, 0, 100', rgb=(255, 255, 255))
print(color)
print(color2)
print(color3)