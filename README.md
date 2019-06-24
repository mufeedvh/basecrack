<p align="center">
	<a href="https://github.com/mufeedvh/basecrack"><img src="https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-logo.png" title="BaseCrack" alt="basecrack"></a>
</p>
<h1 align="center">BaseCrack</h1>
<h4 align="center">Best Decoder Tool For Base Encoding Schemes</h4>
<p align="center">
	<img src="https://img.shields.io/badge/version-1.0.0-blue.svg" title="version" alt="version">
	<a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/mufeedvh/basecrack.svg"></a>
	<a href="https://twitter.com/intent/tweet?text=Check%20this%20out!%20A%20tool%20to%20decode%20all%20types%20of%20Base%20Encoding%20Schemes.%20Will%20be%20really%20useful%20for%20CTFs%20and%20Cryptography:&url=https%3A%2F%2Fgithub.com%2Fmufeedvh%2Fbasecrack"><img alt="Twitter" src="https://img.shields.io/twitter/url/https/github.com/mufeedvh/basecrack.svg?style=social"></a>
</p>
<p align="center">
	<img src="https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-tool.png" title="BaseCrack Tool" alt="basecrack tool">
</p>

------------

**BaseCrack** is a tool written in Python that can decode all alphanumeric base encoding schemes. This tool can accept single user input, multiple inputs from a file, input from argument and decode them incredibly fast.

Decode Base16, Base32, Base36, Base58, Base62, Base64, Base64Url, Base85, Base91, Base92 and more with the best base encoding scheme decoding tool in town. Mostly used for **CTFs** and **Cryptography**.

------------

## Supported Encoding Schemes
- Base16
- Base32
- Base36
- Base58
- Base62
- Base64
- Base64Url
- Base85
- Base91
- Base92

## Main Features
- Can decode multiple base encodings from a file
- Predicts the type of encoding scheme

## Screenshots
<p align="center">
<img src="https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/screenshot.png" title="Screenshot" alt="basecrack screenshot">
</p>

## Installation
    $ git clone https://github.com/mufeedvh/basecrack.git
    $ cd basecrack
    $ pip install -r requirements.txt
    $ python basecrack.py -h

## Usage
To decode a single base encoding from user input:

    python basecrack.py

To decode a single base encoding from argument:

    python basecrack.py -b SGVsbG8gV29ybGQh

To decode multiple base encodings from a file:

    python basecrack.py -f file.txt

## Contribution
Ways to contribute
- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word

## License
Licensed under the MIT License, see <a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE">LICENSE</a> for more information.

------------

***Support this project by starring, sharing, and contributing! :heart:***

------------
