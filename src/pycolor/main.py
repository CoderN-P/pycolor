from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple, List, Union
import re
import requests

rgb_hsl = Union[Tuple[int, int, int], List[int], str]
cmyk = Union[Tuple[int, int, int, int], List[int], str]
hex = str
@dataclass
class Color:
    color_type: str
    color: rgb_hsl | cmyk | hex
    hex: str = field(init=False, default_factory=str)
    cmyk: str = field(init=False, default_factory=str)
    name: str = field(init=False, default_factory=str)
    hsl: str = field(init=False, default_factory=str)
    xyz: str = field(init=False, default_factory=str)
    image: str = field(init=False, default_factory=str)
    hsv: str = field(init=False, default_factory=str)
    rgb: str = field(init=False, default_factory=str)
    contrast: str = field(init=False, default_factory=str)
    raw_data: dict = field(init=False, repr=False,  default_factory=dict)


    @property
    def color(self) -> rgb_hsl | cmyk | hex:
        return self._color

    @color.setter
    def color(self, value: rgb_hsl | cmyk | hex) -> None:

        if isinstance(value, str):
            if self.color_type.lower() != 'hex':
                value = [i for i in re.split(r'\D', value) if i]
            else:
                if len(value) not in [6, 7]:
                    raise ValueError("Hex must be a string of 6-7 chars. The '#' is optional")
                value = value.lstrip('#')
                if not all(i in '0123456789abcdef' for i in value.lower()):
                    raise ValueError("Hex must only contain hex chars")
            self._color = value

        if isinstance(value, tuple) or isinstance(value, list):
            if len([i for i in value if str(i).isdigit()]) not in [3, 4]:
                if self.color_type == 'cmyk':
                    raise ValueError("CMYK must be a tuple of 4 ints")
                else:
                    raise ValueError("RGB/HSL must be a tuple or string of 3 ints")
            else:
                value = tuple(map(int, list(value)))
            if self.color_type == 'hsl':
                if value[0] < 0 or value[0] > 360:
                    raise ValueError("Hue must be between 0 and 360")
                if value[1] < 0 or value[1] > 100:
                    raise ValueError("Saturation must be between 0 and 100")
                if value[2] < 0 or value[2] > 100:
                    raise ValueError("Lightness must be between 0 and 100")
            elif self.color_type == 'cmyk':
                if value[0] < 0 or value[0] > 100:
                    raise ValueError("Cyan must be between 0 and 100")
                if value[1] < 0 or value[1] > 100:
                    raise ValueError("Magenta must be between 0 and 100")
                if value[2] < 0 or value[2] > 100:
                    raise ValueError("Yellow must be between 0 and 100")
                if value[3] < 0 or value[3] > 100:
                    raise ValueError("Key must be between 0 and 100")
            elif self.color_type == 'rgb':
                if value[0] < 0 or value[0] > 255:
                    raise ValueError("Red must be between 0 and 255")
                if value[1] < 0 or value[1] > 255:
                    raise ValueError("Green must be between 0 and 255")
                if value[2] < 0 or value[2] > 255:
                    raise ValueError("Blue must be between 0 and 255")

            self._color = value

    @property
    def color_type(self) -> str:
        return self._color_type

    @color_type.setter
    def color_type(self, value: str) -> None:
        if value.lower() in ('hex', 'rgb', 'cmyk', 'hsl'):
            self._color_type = value.lower()
        else:
            raise ValueError('Invalid input type. Only hex, rgb, cmyk, and hsl are supported. ')

    def __post_init__(self) -> None:
        self.raw_data = requests.get(f"https://www.thecolorapi.com/id?{self.color_type}={self.color}").json()
        cmyk = self.raw_data["cmyk"]["value"][5:][:-1]
        self.cmyk = cmyk.replace('NaN', '0')
        hsl = self.raw_data['hsl']['value'][4:][:-1]

        self.hsl = hsl.replace('%', '')

        rgb1 = self.raw_data['rgb']['value'][:-1]
        self.rgb = tuple(int(i) for i in rgb1[4:].split(','))

        self.hsv = self.raw_data['hsv']['value'][4:][:-1].replace('%', '')
        hex1 = self.raw_data['hex']['value']
        self.hex = self.raw_data['hex']['value']
        self.name = self.raw_data['name']['value']
        self.xyz = self.raw_data['XYZ']['value'][4:][:-1]
        self.image = f'https://singlecolorimage.com/get/{hex1[1:]}/400x100.png'
        self.contrast = self.raw_data['contrast']['value']

    def get_raw(self) -> dict:
        return self.raw_data

