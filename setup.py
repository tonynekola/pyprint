from setuptools import setup, find_packages
import platform
import os
import subprocess


libraries = ['PyMuPDF>=1.22.1']
if platform.system() == "Windows":
    libraries.append(
        'win32print'
    )
else:
    libraries.append(
        'pycups>=2.0.1'
    )


# if platform.system() == "Darwin":
#     try:
#         subprocess.run(["brew", "install", "unoconv"])
#     except subprocess.CalledProcessError as e:
#         print("Error installing missing library:", e)

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
    scripts=['src/printer/air_printer.py'],
    author='Tony Nekola',
    author_email='nekolaton11@gmail.com',
    description='A unified printer script for both Windows and Unix system',
    url='https://github.com/tonynekola/pyprint',
)