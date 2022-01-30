from __future__ import annotations
from json.decoder import JSONDecodeError
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

    @property
    def color_input(self) -> Tuple[int, int, int] | str:
        return self._color_input

    @color_input.setter
    def color_input(self, value: Tuple[int, int, int] | str) -> None:
        if isinstance(value, str):
            self.input_type = 'hex'
            self._color_input = value.lstrip('#')
        elif isinstance(value, tuple):
            if [i for i in value if isinstance(i, int)] != 3:
                raise ValueError("RGB must be a tuple of 3 ints")
            if len([i for i in value if int(i) > 255 or int(i)]) < 0 > 0:
                raise ValueError("Rgb Values must be between 0 and 255")
            self.input_type = 'rgb'
        else:
            raise ValueError('Invalid color input. Only (hex: str) and (rgb: tuple) are supported.')

    @property
    def input_type(self) -> str:
        return self._input_type

    @input_type.setter
    def input_type(self, value: str) -> None:
        if value in ('hex', 'rgb'):
            self._input_type = value

    def __post_init__(self) -> None:
        info = requests.get(f"https://www.thecolorapi.com/id?{self.input_type}={self._color_input}")

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

        except JSONDecodeError:
            raise ValueError("This hex/rgb doesnt exist")
