# PyColor
## Installation
```pip install pycolor```

##About
Pycolor is an extremely simple library, I wrote in like an hour. It uses thecolorapi to get info on inputted hex/rgb strings 
##Usage
```py
from pycolor import Color
rgb = '1, 233, 123'
color = Color(rgb)
#Returns a color object
#Example Color Object 
#Color(color_input='1, 233, 123', input_type='rgb', hex='#01E97B', cmyk='100, 0, 47, 9', name='Spring Green', hsl='152, 99, 46', xyz='42, 69, 57', image='https://singlecolorimage.com/get/01E97B/400x100.png', hsv='152, 100, 91', rgb='1, 233, 123')
name = color.name
image_url = color.image
color_hex = color.hex
#etc.



```


