from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import requests


@dataclass
class Color:
    color_input: Tuple[int, int, int] | str
    input_type: str = 'none'
    hex: str = 'none'
    cmyk: str = 'none'
    name: str = 'none'
    hsl: str = 'none'
    xyz: str = 'none'
    image: str = 'none'
    hsv: str = 'none'
    rgb: str = 'none'

    def __post_init__(self):
        if isinstance(self.color_input, str):
            self.input_type = 'hex'
        elif isinstance(self.color_input, tuple):
            self.input_type = 'rgb'
        else:
            raise ValueError('Invalid color input. Only hex: str and rgb: tuple are supported.')

        if self.input_type == 'hex':
            self.color_input = self.color_input.lstrip('#')
            info = requests.get(f"https://www.thecolorapi.com/id?hex={self.color_input}")

        else:
            data = self.color_input


            for i in data:
                if int(i) > 255 or int(i) < 0:
                    raise ValueError("Rgb Values must be between 0 and 255")
                else:
                    continue


            info = requests.get(f"https://www.thecolorapi.com/id?rgb={self.color_input}")

        try:
            info = info.json()
            cmyk = info["cmyk"]["value"][5:][:-1]
            self.cmyk = cmyk.replace('NaN', '0')
            hsl = info['hsl']['value'][4:][:-1]

            self.hsl = hsl.replace('%', '')

            rgb1 = info['rgb']['value'][:-1]
            self.rgb = rgb1[4:]

            self.hsv = info['hsv']['value'][4:][:-1].replace('%', '')
            hex1 = info['hex']['value']
            self.hex = info['hex']['value']
            self.name = info['name']['value']
            self.xyz = info['XYZ']['value'][4:][:-1]
            self.image = f'https://singlecolorimage.com/get/{hex1[1:]}/400x100.png'

        except KeyError:
            raise ValueError("This hex/rgb doesnt exist")
