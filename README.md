<p align="center">
	<a href="https://github.com/mufeedvh/basecrack"><img src="https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-logo.png" title="BaseCrack" alt="basecrack" height="100" width="325"></a>
</p>
<h1 align="center">BaseCrack</h1>
<h4 align="center">Decoder Tool For Base Encoding Schemes</h4>
<p align="center">
	<img src="https://img.shields.io/badge/version-3.0-blue.svg" title="version" alt="version">
	<a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/mufeedvh/basecrack.svg"></a>
	<a href="https://twitter.com/intent/tweet?text=Check%20this%20out!%20A%20tool%20to%20decode%20all%20types%20of%20Base%20Encoding%20Schemes.%20Will%20be%20really%20useful%20for%20CTFs%20and%20Cryptography:&url=https%3A%2F%2Fgithub.com%2Fmufeedvh%2Fbasecrack"><img alt="Twitter" src="https://img.shields.io/twitter/url/https/github.com/mufeedvh/basecrack.svg?style=social"></a>
</p>

![basecrack tool](https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-tool.png)

------------

**BaseCrack** is a tool written in Python that can decode all alphanumeric base encoding schemes. This tool can accept single user input, multiple inputs from a file, input from argument, **multi-encoded bases**, **bases in image EXIF data**, **bases on images with OCR** and decode them incredibly fast.

Decode Base16, Base32, Base36, Base58, Base62, Base64, Base64Url, Base85, Ascii85, Base91, Base92 and more with the best base encoding scheme decoding tool in town. It's useful for **CTFs**, **Bug Bounty Hunting**, and **Cryptography**.

<details>
  <summary>Fun Fact!</summary>
  <br>
  I initially made this after being fed up with lame AF CTF challenges with multi-encoded bases in Cryprography challenges and now some of them started doing that in Steganography challenges so I automated that too smh!
</details>

---

### Jump to [Usage](https://github.com/mufeedvh/basecrack#usage)

---

## Changelog

**What's new in v3.0:**

- **Decode bases in image EXIF data.** 📸
- **Decode bases on images with OCR detection.** 🔎
- Better Accuracy. (+added charset validation along with replacement char checks) 💯
- Magic Mode now works with File Read mode. :fire:
- Magic Mode now works with Wordlist Generator. :fire:

**What's new in v2.0:**

- Now BaseCrack supports both Python2 and Python3.

## Magic Mode 🪄

Now you can **decode multi-encoded bases** of any pattern in a single shot.

Have you ever stumbled upon that one lame CTF challenge that gives you an encoded string which is just encoded over and over with Base64, Base91, Base85 and so on? Just give that to BaseCrack and you're done with it! ;)

<details>
    <summary><b>Screenshot</b></summary>
    <br>
    <img src="https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-magic-mode.png" alt="basecrack magic mode">
</details>

Want to test it out? Just give it this input:

```
IX(Fp@nNG6ef<,*TFE]IT^zdINAb9EVbp,e<u=O6nN)/u+MTnU;Fo#VvQ&cK;mLZI#Jbdook<O{W#+gY%ooe#6pTkTa.9YPU8Uc=pl9BhSM9%kISw2k:8..u/6F2BwNndPZ2o#7NHNP3g,HlZu><*[Nv+T8
```

and see for yourself! :)

### BaseCrack API

BaseCrack can now be used as a library! Just import the `BaseCrack()` class and call the `decode()` function.

See [**API**](https://github.com/mufeedvh/basecrack#api).

**What's new in v1.1:**

I heard your feature requests, now you can generate a wordlist/output with the decoded bases! :)

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

## Main Features

- **Decode multi-encoded bases of any pattern.**
- **Decode bases in image EXIF data.**
- **Decode bases on images with OCR detection.**
- Dan decode multiple base encodings from a file.
- **Generate a wordlist/output with the decoded bases.**
- Predicts the type of encoding scheme.

------------

## Installation

    $ git clone https://github.com/mufeedvh/basecrack.git
    $ cd basecrack
    $ pip install -r requirements.txt
    $ python basecrack.py -h

📝 **NOTE:** Python3 is recommended to use!

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

📝 **NOTE:** I haven't completely tested this tool on Windows so if you stumble upon any issues, please [open an issue](https://github.com/mufeedvh/basecrack/issues/new).

## Usage

Get a list of all the arguments:

    python basecrack.py -h

To decode a single base encoding from user input:

    python basecrack.py

To decode a single base encoding from argument **(-b/--base)**:

    python basecrack.py -b SGVsbG8gV29ybGQh

To decode multiple base encodings from a file **(-f/--file)**:

    python basecrack.py -f file.txt

**Magic Mode:** To decode multi-encoded base of any pattern **(-m/--magic)**:

    python basecrack.py --magic

To input an image for **EXIF/OCR** detection mode **(-i/--image)**:

    python basecrack.py -i image.jpg (--exif/--ocr)

**EXIF Data Detection:** To decode bases in image EXIF data **(-e/--exif)**:

    python basecrack.py -i image.jpg --exif

**OCR Base Detection:** To decode bases on image with OCR detection **(-c/--ocr)**:

    python basecrack.py -i image.jpg --ocr

To generate a wordlist/output with the decoded bases **(-o/--output)**:

    python basecrack.py -f file.txt -o output-wordlist.txt

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

Time to integrate this into your automation tools! ;)

## Screenshots

## EXIF Data Detection 📸

![basecrack exif detection](https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-exif-detection.png)

**Try It Yourself!**

    python basecrack.py -i examples/exif-example.jpg --exif

## OCR Base Detection 🔎

![basecrack ocr detection](https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-ocr-detection.png)

**Try It Yourself!**

    python basecrack.py -i examples/ocr-example.jpg --ocr

## Contribution

Ways to contribute
- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word

Before you open a PR, make sure everything's good with a Unit Test:

**Unit Tests:** (Thanks [@FavasM](https://github.com/mufeedvh/basecrack/pull/8))

    python3 -m unittest discover -v -s tests

## License
Licensed under the MIT License, see <a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE">LICENSE</a> for more information.

## Liked the project?
Support the author by buying him a coffee!

<a href="https://www.buymeacoffee.com/mufeedvh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="51px" width="217px"></a>

------------

***Support this project by starring ⭐, sharing 📲, and contributing 👩‍💻! :heart:***

------------
