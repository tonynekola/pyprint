from setuptools import setup, find_packages
import platform

if platform.system() == "Windows":
    libraries = [
        'win32print'
    ]
else:
    libraries = [
        'pycups>=2.0.1'
    ]
setup(
    name='pyprint',
    version='1.0',
    packages=find_packages(),
    install_requires=libraries,
    entry_points={
        'console_scripts': [
            'pyprint = src.printer.air_printer:main'
        ]
    },
    author='Tony Nekola',
    author_email='nekolaton11@gmail.com',
    description='A unified printer script for both Windows and Unix system',
    url='https://github.com/tonynekola/pyprint',
)