import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pycolor-codern",
    packages=["pycolor"],
    package_dir={"": "src"},
    version="1.1",
    description="Pycolor uses thecolorapi to to get useful information about colors in a pythonic way.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/CoderN-P/pycolor",
    author="Neel Parpia",
    author_email="neel.parpia@gmail.com",
    license="MIT",
    keywords=['color', 'colorapi', 'python'],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)