<h1 align="center">BaseCrack</h1>
<h4 align="center">Decoder For Base Encoding Schemes</h4>
<p align="center">
	<img src="https://img.shields.io/badge/version-4.0-blue.svg" title="version" alt="version">
	<a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/mufeedvh/basecrack.svg"></a>
</p>

**BaseCrack** is a tool written in Python that can decode all alphanumeric base encoding schemes. This tool can accept single user input, multiple inputs from a file, input from argument, **multi-encoded bases**, **bases in image EXIF data**, **bases on images with OCR** and decode them incredibly fast.

For a basic demo, try the [Web Interface](https://basecrack.herokuapp.com/) that uses BaseCrack's [API](#api).

<details>
	<summary><strong>Fun Fact!</strong></summary>
  	<br>
  	I initially made this after being fed up with lame CTF challenges with multi-encoded bases. Now some of them started doing that in Steganography challenges so I automated that too smh!
</details>

## Table of Contents
- [Features](#features)
- [Supported Encoding Schemes](#supported-encoding-schemes)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Contribution](#contribution)
- [License](#license)

## Features

- Decode multi-encoded bases of any pattern.
- Decode bases in image EXIF data.
- Decode bases on images with OCR detection.
- Can decode multiple base encodings from a file.
- Generate a wordlist/output with the decoded bases.
- Predicts the type of encoding scheme.

## Supported Encoding Schemes
- Base16
- Base32
- Base36
- Base58
- Base62
- Base64
- Base64Url
- Base85
- Ascii85
- Base91
- Base92
- [Base100](https://github.com/AdamNiederer/base100) ([#14](https://github.com/mufeedvh/basecrack/issues/14))

## Installation

    $ git clone https://github.com/mufeedvh/basecrack.git
    $ cd basecrack
    $ pip3 install -r requirements.txt
    $ python3 basecrack.py -h

**NOTE:** Python3 is recommended to use!

**Linux:**

    $ sudo apt-get update
    $ sudo apt-get install tesseract-ocr libtesseract-dev

**MacOS:**

    $ brew install tesseract

**Windows:**

OCR Detection is implemented with [Tesseract](https://github.com/tesseract-ocr/tesseract) and Windows requires installation of the Tesseract executable. Installing the dependencies from `requirements.txt` which includes `pytesseract` should install it. If in case it doesn't, here's how you can set it up:

1. First check whether you have it installed or not in the `Program Files`/`Program Files (x86)` under the `Tesseract-OCR` directory.
2. If there is, give that path in the `config.json` and you're all set! If you don't have it, install it from [here](https://github.com/UB-Mannheim/tesseract/wiki) and set the path in `config.json`.

**Tesseract Docs:** https://tesseract-ocr.github.io/

**NOTE:** I haven't completely tested this tool on Windows so if you stumble upon any issues, please [open an issue](https://github.com/mufeedvh/basecrack/issues/new).

## Usage

Get a list of all the arguments:

    python3 basecrack.py -h

To decode a single base encoding from user input:

    python3 basecrack.py

To decode a single base encoding from argument **(-b/--base)**:

    python3 basecrack.py -b SGVsbG8gV29ybGQh

To decode multiple base encodings from a file **(-f/--file)**:

    python3 basecrack.py -f file.txt

**Magic Mode:** To decode multi-encoded base of any pattern **(-m/--magic)**:

    python3 basecrack.py --magic

To input an image for **EXIF/OCR** detection mode **(-i/--image)**:

    python3 basecrack.py -i image.jpg (--exif/--ocr)

**EXIF Data:** To decode bases in image EXIF data **(-e/--exif)**:

    python basecrack.py -i image.jpg --exif

**OCR Base Detection:** To decode bases on image with OCR detection **(-c/--ocr)**:

    python basecrack.py -i image.jpg --ocr

To generate a wordlist/output with the decoded bases **(-o/--output)**:

    python basecrack.py -f file.txt -o output-wordlist.txt
    
## Magic Mode

Now you can **decode multi-encoded bases** of any pattern in a single shot.

Have you ever stumbled upon that one lame CTF challenge that gives you an encoded string which is just encoded over and over with Base64, Base91, Base85 and so on? Just give that to BaseCrack and you're done with it! ;)

Want to test it out? Just give it this input:

```
IX(Fp@nNG6ef<,*TFE]IT^zdINAb9EVbp,e<u=O6nN)/u+MTnU;Fo#VvQ&cK;mLZI#Jbdook<O{W#+gY%ooe#6pTkTa.9YPU8Uc=pl9BhSM9%kISw2k:8..u/6F2BwNndPZ2o#7NHNP3g,HlZu><*[Nv+T8
```

and see for yourself! :)

### BaseCrack API

BaseCrack can now be used as a library! Just import the `BaseCrack()` class and call the `decode()` function.

See [**API**](https://github.com/mufeedvh/basecrack#api).

## API

Want to use BaseCrack as a library? We got you covered!

Just put `basecrack` in your project's directory and you're ready to go!

**Example:**

```python
# import the BaseCrack class from basecrack.py
from basecrack import BaseCrack

# calling the api function decode() with the encoded base
result = BaseCrack().decode('c3BhZ2hldHRp')

# printing the output
"""
result is tuple where:
result[0] = DECODED STRING
result[1] = ENCODING SCHEME
"""
print('Decoded String: {}'.format(result[0]))
print('Encoding Scheme: {}'.format(result[1]))
```

**Output:**

```
Decoded String: spaghetti
Encoding Scheme: Base64
```

## Contribution

Ways to contribute
- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word

Before you open a PR, make sure everything's good by running the tests:

**Unit Tests:** (Thanks [@FavasM](https://github.com/mufeedvh/basecrack/pull/8))

    python3 -m unittest discover -v -s tests

## License
Licensed under the MIT License, see <a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE">LICENSE</a> for more information.
