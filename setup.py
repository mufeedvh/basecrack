from setuptools import setup

setup(
    name='basecrack',
    version=4.0 ,
    description='Decode All Bases - Base Scheme Decoder',
    author='Mufeed VH',
    url='https://github.com/mufeedvh/basecrack',
    license='MIT',
    packages=[
        'src'
    ],
    py_modules=[
        'basecrack'
    ],
    install_requires=[
        'argparse',
        'colorama',
        'termcolor',
        'pathlib',
        'anybase32',
        'base36',
        'base58',
        'pybase62',
        'base91',
        'pybase100',
        'exifread',
        'opencv-python',
        'pytesseract'
    ],
    python_requires='>=3.0.0',
    entry_points={
        'console_scripts': [
            'basecrack = basecrack:main'
        ]
    }
)
