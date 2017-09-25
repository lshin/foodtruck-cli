"""Packaging settings."""
from setuptools import Command, find_packages, setup
from src import __version__

setup(
    name = 'food truck',
    version = __version__,
    description = 'A command line program that display a list of food trucks that are open at the current date',
    url = 'https://github.com/lshin/foodtruck-cli',
    author = 'Leo Shin',
    author_email = 'leo@sh1n.com',
    license = 'MIT',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'requests', 'requests_cache'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'show_open_food_trucks=src.cli:main',
        ],
    }
)