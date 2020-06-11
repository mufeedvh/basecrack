<p align="center">
	<a href="https://github.com/mufeedvh/basecrack"><img src="https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-logo.png" title="BaseCrack" alt="basecrack" height="100" width="320"></a>
</p>
<h1 align="center">BaseCrack</h1>
<h4 align="center">Best Decoder Tool For Base Encoding Schemes</h4>
<p align="center">
	<img src="https://img.shields.io/badge/version-2.0-blue.svg" title="version" alt="version">
	<a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/mufeedvh/basecrack.svg"></a>
	<a href="https://twitter.com/intent/tweet?text=Check%20this%20out!%20A%20tool%20to%20decode%20all%20types%20of%20Base%20Encoding%20Schemes.%20Will%20be%20really%20useful%20for%20CTFs%20and%20Cryptography:&url=https%3A%2F%2Fgithub.com%2Fmufeedvh%2Fbasecrack"><img alt="Twitter" src="https://img.shields.io/twitter/url/https/github.com/mufeedvh/basecrack.svg?style=social"></a>
</p>

![basecrack tool](https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-tool.png)

------------

**BaseCrack** is a tool written in Python that can decode all alphanumeric base encoding schemes. This tool can accept single user input, multiple inputs from a file, input from argument, **multi-encoded bases** and decode them incredibly fast.

Decode Base16, Base32, Base36, Base58, Base62, Base64, Base64Url, Base85, Base91, Base92 and more with the best base encoding scheme decoding tool in town. It's useful for **CTFs**, **Bug Bounty Hunting**, and **Cryptography**.

**What's new in v1.1:** I heard your feature requests, now you can generate a wordlist/output with the decoded bases! :)

## What's new in v2.0:

_**Now BaseCrack supports both Python2 and Python3**_

## Magic Mode

Now you can **decode multi-encoded bases** of any pattern in a single shot.

Have you ever stumbled upon that one lame CTF challenge that gives you an encoded string which is just encoded over and over with Base64, Base91, Base85 and so on? Just give that to BaseCrack and you're done with it! ;)

![basecrack magic mode](https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-magic-mode.png)

Want to test it out? Just give it this input:
```
IX(Fp@nNG6ef<,*TFE]IT^zdINAb9EVbp,e<u=O6nN)/u+MTnU;Fo#VvQ&cK;mLZI#Jbdook<O{W#+gY%ooe#6pTkTa.9YPU8Uc=pl9BhSM9%kISw2k:8..u/6F2BwNndPZ2o#7NHNP3g,HlZu><*[Nv+T8
```
and see for yourself! :)

**API:** BaseCrack can now be used as a library! Just import the `BaseCrack()` class and call the `decode()` function. See example below.

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
- **Can decode multi-encoded bases of any pattern.**
- Can decode multiple base encodings from a file.
- **Generate a wordlist/output with the decoded bases.**
- Predicts the type of encoding scheme.

## Screenshots

![basecrack screenshot](https://raw.githubusercontent.com/mufeedvh/basecrack/master/assets/basecrack-screenshot.png)

## Installation
    $ git clone https://github.com/mufeedvh/basecrack.git
    $ cd basecrack
    $ pip install -r requirements.txt
    $ python basecrack.py -h

## Usage
To decode a single base encoding from user input:

    python basecrack.py

To decode a single base encoding from argument **(-b/--base)**:

    python basecrack.py -b SGVsbG8gV29ybGQh

To decode multiple base encodings from a file **(-f/--file)**:

    python basecrack.py -f file.txt

**Magic Mode:** To decode multi-encoded base of any pattern **(-m/--magic)**:

    python basecrack.py --magic

To generate a wordlist/output with the decoded bases **(-o/--output)**:

    python basecrack.py -f file.txt -o output-wordlist.txt


## API

Want to use BaseCrack as a library? We got you covered!

Just put `basecrack` in your project's folder and you're ready to go!

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

## Contribution
Ways to contribute
- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word

## License
Licensed under the MIT License, see <a href="https://github.com/mufeedvh/basecrack/blob/master/LICENSE">LICENSE</a> for more information.

## Liked the project?
Support the author by buying him a coffee!

<a href="https://www.buymeacoffee.com/mufeedvh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="51px" width="217px"></a>

------------

***Support this project by starring ⭐, sharing 📲, and contributing 👩‍💻! :heart:***

------------
