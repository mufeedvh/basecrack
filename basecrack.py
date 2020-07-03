#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__  = 'Mufeed VH'
__version__ = '2.0'
__email__   = 'contact@mufeedvh.com'
__github__  = 'https://github.com/mufeedvh/basecrack'

# importing some required stuff
import os
import re
import sys
import time
import argparse
from colorama import init
from termcolor import colored

import base36
import base58
import base62
import base64
import base91
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import base92


class BaseCrack:
    def __init__(self, output=None):
        self.output = output
        # initial bools
        self.api_call = False

    # main decode function
    def decode_base(self, encoded_base):
        """
        contains_replacement_char() checks whether the decoded base
        contains an unknown unicode, ie: invalid character.
        these are replaced with 'replacement character',
        which is '�' and 'U+FFFD' in unicode.
        """
        def contains_replacement_char(res):
            return True if u'\ufffd' in res else False

        # to store the encoding schemes which haven't caused errors
        encoding_type = []

        # to store the decoded results which haven't caused errors
        results = []

        # checking if input is not empty
        if len(encoded_base) != 0:
            # decoding as base16
            try:
                base16_decode = base64.b16decode(encoded_base, casefold=False).decode('utf-8', 'replace')
                if not contains_replacement_char(base16_decode):
                    encoding_type.append('Base16')
                    results.append(base16_decode)				
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base16: ', 'blue')+colored(base16_decode, 'green'))
            except:
                pass

            # decoding as base32
            try:
                base32_decode = base64.b32decode(encoded_base, casefold=False, map01=None).decode('utf-8', 'replace')
                if not contains_replacement_char(base32_decode):
                    encoding_type.append('Base32')
                    results.append(base32_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base32: ', 'blue')+colored(base32_decode, 'green'))
            except:
                pass

            # decoding as base36
            try:
                base36_decode = base36.dumps(encoded_base).decode('utf-8', 'replace')
                if not contains_replacement_char(base36_decode):
                    encoding_type.append('Base36')
                    results.append(base36_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base36: ', 'blue')+colored(base36_decode, 'green'))
            except:
                pass

            # decoding as base58
            try:
                base58_decode = base58.b58decode(encoded_base.encode()).decode('utf-8', 'replace')
                if not contains_replacement_char(base58_decode):
                    encoding_type.append('Base58')
                    results.append(base58_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base58: ', 'blue')+colored(base58_decode, 'green'))
            except:
                pass

            # decoding as base62
            try:
                base62_decode = base62.encode(int(encoded_base)).decode('utf-8', 'replace')
                if not contains_replacement_char(base62_decode):
                    encoding_type.append('Base62')
                    results.append(base62_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base62: ', 'blue')+colored(base62_decode, 'green'))
            except:
                pass		

            # decoding as base64
            try:
                base64_decode = base64.b64decode(encoded_base).decode('utf-8', 'replace')
                if not contains_replacement_char(base64_decode):
                    encoding_type.append('Base64')
                    results.append(base64_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base64: ', 'blue')+colored(base64_decode, 'green'))
            except:
                pass

            # decoding as base64url
            try:
                base64url_decode = base64.urlsafe_b64decode(encoded_base + '=' * (4 - len(encoded_base) % 4)).decode('utf-8', 'replace')
                if not contains_replacement_char(base64url_decode):
                    encoding_type.append('Base64URL')
                    results.append(base64url_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base64URL: ', 'blue')+colored(base64url_decode, 'green'))
            except:
                pass

            # decoding as base85
            try:
                base85_decode = base64.b85decode(encoded_base).decode('utf-8', 'replace')
                if not contains_replacement_char(base85_decode):
                    encoding_type.append('Base85')
                    results.append(base85_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base85: ', 'blue')+colored(base85_decode, 'green'))
            except:
                pass

            # decoding as base91
            try:
                base91_decode = base91.decode(encoded_base).decode('utf-8', 'replace')
                if not contains_replacement_char(base91_decode):
                    encoding_type.append('Base91')
                    results.append(base91_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base91: ', 'blue')+colored(base91_decode, 'green'))
            except:
                pass

            # decoding as base92
            try:
                base92_decode = base92.decode(encoded_base)
                if not contains_replacement_char(base92_decode):
                    encoding_type.append('Base92')
                    results.append(base92_decode)
                    if not self.api_call:
                        print(colored('\n[>] Decoding as Base92: ', 'blue')+colored(base92_decode, 'green'))
            except:
                pass

            if not results and not self.api_call:
                quit(colored('\n[!] Not a valid encoding.\n', 'red'))

            # algorithm to identify which type of base encoding the input is
            for x in range(len(results)):
                """
                It runs through all the results and compares them
                with a regex pattern of 'alphabets, numbers, and special characters'
                thus ending up with the right result as false results will
                contain invalid characters.
                """
                if re.match('[A-Za-z0-9$&+,:;=?@#|\'<>.^*()%!_-]', results[x]):
                    if not self.api_call:
                        # printing the predicted encoding type
                        print(colored('\n[-] The Encoding Scheme Is ', 'blue')+colored(encoding_type[x], 'green')) 
                        # generating the wordlist/output file with the decoded bases
                        if self.output != None:
                            open(self.output, 'a').write(results[x]+'\n')
                    else:
                        # return a tuple with the decoded base and encoding scheme if it's an api call
                        return (results[x], encoding_type[x])
    
    """
    this function fetches the set of base encodings from the input file
    and passes it to 'decode_base()' function to decode it all
    """
    def decode_base_from_file(self, file):
        print(colored('[-] Decoding Base Data From ', 'cyan')+colored(file, 'yellow'))
        # opening the input file
        with open(file) as input_file:
            # reading each line from the file
            for line in input_file:
                # checking if the line/base is not empty
                if len(line) > 1:
                    # printing the encoded base
                    print(colored('\n[-] Encoded Base: ', 'yellow')+str(line.strip()))

                    # calling the 'decode_base()' function to decode the current line
                    self.decode_base(line)

                    # separating each decode results with some lines yo
                    print(colored('\n{{<<', 'red')+colored('='*70, 'yellow')+colored('>>}}', 'red'))

    # api decode function
    """
    API FUNCTION
    ------------
    the decode() function returns a tuple
    with the structure:
        ('DECODED_STRING', 'ENCODING SCHEME')
        For example:
            >> from basecrack import BaseCrack
            >> BaseCrack().decode('c3BhZ2hldHRp')
            ('spaghetti', 'Base64')
        ie:
            result[0] is the decoded string
            result[1] is the encoding scheme
    """	
    def decode(self, encoded_base):
        self.api_call = True
        # api calls returns a tuple with the decoded base and the encoding scheme
        return self.decode_base(encoded_base)

    # magic mode tries to decode multi-encoded bases
    def magic_mode(self, encoded_base):
        # magic mode uses the api function to decode every iteration
        self.api_call = True

        iteration = 0
        result = None
        encoding_pattern = []
        start_time = time.time()

        while True:
            if self.decode(encoded_base) is not None:
                iteration += 1
                result = self.decode(encoded_base)
                decoded_string = result[0]
                encoding_scheme = result[1]
                encoding_pattern.append(encoding_scheme)
                print(colored('\n[-] Iteration: ', 'green')+colored(iteration, 'blue'))
                print(colored('\n[-] Heuristic Found Encoding To Be: ', 'yellow')+colored(encoding_scheme, 'green'))
                print(colored('\n[-] Decoding as {}: '.format(encoding_scheme), 'blue')+colored(decoded_string, 'green'))
                print(colored('\n{{<<', 'red')+colored('='*70, 'yellow')+colored('>>}}', 'red'))
                # setting the encoded bases and the current result for the next iteration
                encoded_base = decoded_string
            else:
                break

        if result is not None:
            end_time = time.time()
            print(colored('\n[-] Total Iterations: ', 'green')+colored(iteration, 'blue'))
            # show the encoding pattern in order and comma-seperated
            pattern = ' -> '.join(map(str, encoding_pattern))
            print(colored('\n[-] Encoding Pattern: ', 'green')+colored(pattern, 'blue'))
            print(colored('\n[-] Magic Decode Finished With Result: ', 'green')+colored(decoded_string, 'yellow', attrs=['bold']))
            completion_time = str(end_time-start_time)[:6]
            print(colored('\n[-] Finished in ', 'green')+colored(completion_time, 'cyan', attrs=['bold'])+colored(' seconds\n', 'green'))
            quit()
        else:
            quit(colored('\n[!] Not a valid encoding.\n', 'red'))

# print a kickass banner to look cool
def banner():
    banner = '''
██████╗  █████╗ ███████╗███████╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║███████╗█████╗  ██║     ██████╔╝███████║██║     █████╔╝ 
██╔══██╗██╔══██║╚════██║██╔══╝  ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██████╔╝██║  ██║███████║███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    '''
    print(colored(banner, 'red')+colored('\n\t\tpython basecrack.py -h [FOR HELP]\n', 'green'))

def main():
    banner()
    # setting up argparse module to accept arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--base', help='Decode a single encoded base from argument.')
    parser.add_argument('-f', '--file', help='Decode multiple encoded bases from a file.')
    parser.add_argument('-m', '--magic', help='Decode multi-encoded bases in one shot.', action='store_true')
    parser.add_argument('-o', '--output', help='Generate a wordlist/output with the decoded bases, enter filename as the value.')
    args = parser.parse_args()

    if args.output:
        print(colored('\n[>] ', 'yellow')+colored('Enabled Wordlist Generator Mode :: ', 'green')+colored(args.output+'\n', 'blue'))

    """
    decodes base encodings from file if argument is given
    else it accepts a single encoded base from user
    """
    if args.file:
        if args.magic:
            quit(colored('\n[!] Magic Mode doesn\'t work with DECODE_FROM_FILE mode.\n', 'red'))
        # calling the 'decode_base_from_file()' with the input file
        BaseCrack(args.output).decode_base_from_file(str(args.file))
        if args.output:
            print(colored('\n[-] Output Generated Successfully > ', 'green')+colored(args.output+'\n', 'yellow'))
    elif args.base:
        print(colored('[-] Encoded Base: ', 'yellow')+colored(str(args.base), 'red'))

        if args.magic:
            BaseCrack().magic_mode(str(args.base))
        else:
            BaseCrack().decode_base(str(args.base))
    else:
        # input() for python2 is actually eval() :face_palm:
        if sys.version_info >= (3, 0):
            encoded_base = input(colored('[>] Enter Encoded Base: ', 'yellow'))
        else:
            encoded_base = raw_input(colored('[>] Enter Encoded Base: ', 'yellow'))

        if args.magic:
            BaseCrack().magic_mode(encoded_base)
        else:
            BaseCrack().decode_base(encoded_base)

if __name__ == '__main__':
    init()
    main()
