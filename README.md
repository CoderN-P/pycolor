# pycolor
## Installation
Due to `pycolor` already being used, the actual package name is `pycolor-codern`

```bash
$ pip install pycolor-codern
```

## About
Pycolor uses thecolorapi to to get useful information about colors in a pythonic way.
## Usage

```py
from pycolor import Color

rgb = (1, 233, 123)
color = Color(rgb)
# Returns a color object
# Color(color_input=(1, 233, 123), input_type='rgb', hex='#01E97B', cmyk='100, 0, 47, 9', name='Spring Green', hsl='152, 99, 46', xyz='42, 69, 57', image='https://singlecolorimage.com/get/01E97B/400x100.png', hsv='152, 100, 91', rgb='1, 233, 123')
name = color.name
image_url = color.image
color_hex = color.hex
# etc.
```
More examples can be seen in [/examples](/examples)
## Contributing

If you have any questions or concerns feel free to make a pull request or open an issue.


