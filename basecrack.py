#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, sys, time, argparse
from colorama import init
from termcolor import colored

import base36, base58, base62, base64, base91
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import base92


class BaseCrack:
    def __init__(self, output=None, magic_mode_call=False):
        self.output = output
        # initial bools
        self.api_call = False
        self.magic_mode_call = magic_mode_call
        self.b64_once = False

    # main decode function
    def decode_base(self, encoded_base):
        def contains_replacement_char(res):
            """
            `contains_replacement_char()` checks whether the decoded base
            contains an unknown unicode, ie: invalid character.
            these are replaced with 'replacement character',
            which is '�' and 'U+FFFD' in unicode and
            also checks for unicode chars after `127`.
            """
            if u'\ufffd' in res: return True
            else:
                count = 0
                for char in res:
                    if ord(char) > 127: count += 1
                return True if count > 0 else False

        # to store the encoding schemes which haven't caused errors
        encoding_type = []

        # to store the decoded results which haven't caused errors
        results = []

        def process_decode(decode_string, scheme):
            """
            `process_decode()` stores the result if the encoding is valid
            after checks from `contains_replacement_char()` and
            prints the output if it isn't an API call
            """
            if not contains_replacement_char(decode_string):
                # don't repeat `base64url` when `base64` has already passed
                if scheme == 'Base64': self.b64_once = True
                if self.b64_once and (scheme == 'Base64URL'): return
                
                # append results to the respective lists
                encoding_type.append(scheme)
                results.append(decode_string)

                if not self.api_call:
                    print(colored('\n[>] Decoding as {}: '.format(scheme), 'blue')+colored(decode_string, 'green'))


        # checking if input is not empty
        if len(encoded_base) != 0:
            # decoding as base16
            try:
                process_decode(
                    base64.b16decode(encoded_base, casefold=False).decode('utf-8', 'replace'),
                    'Base16'
                )
            except: pass
            # decoding as base32
            try:
                process_decode(
                    base64.b32decode(encoded_base, casefold=False, map01=None).decode('utf-8', 'replace'),
                    'Base32'
                )
            except: pass
            # decoding as base36
            try:
                process_decode(
                    base36.dumps(int(encoded_base)),
                    'Base36'
                )
            except: pass
            # decoding as base58
            try:
                process_decode(
                    base58.b58decode(encoded_base.encode()).decode('utf-8', 'replace'),
                    'Base58'
                )
            except: pass
            # decoding as base62
            try:
                process_decode(
                    base62.decodebytes(encoded_base).decode('utf-8', 'replace'),
                    'Base62'
                )
            except: pass
            # decoding as base64
            try:
                process_decode(
                    base64.b64decode(encoded_base).decode('utf-8', 'replace'),
                    'Base64'
                )
            except: pass            
            # decoding as base64url
            try:
                process_decode(
                    base64.urlsafe_b64decode(encoded_base + '=' * (4 - len(encoded_base) % 4)).decode('utf-8', 'replace'),
                    'Base64URL'
                )
            except: pass
            # decoding as base85
            try:
                process_decode(
                    base64.b85decode(encoded_base).decode('utf-8', 'replace'),
                    'Base85'
                )
            except: pass
            # decoding as ascii85
            try:
                process_decode(
                    base64.a85decode(encoded_base).decode('utf-8', 'replace'),
                    'Ascii85'
                )
            except: pass
            # decoding as base91
            try:
                process_decode(
                    base91.decode(encoded_base).decode('utf-8', 'replace'),
                    'Base91'
                )
            except: pass
            # decoding as base92
            try:
                process_decode(
                    base92.decode(encoded_base),
                    'Base92'
                )
            except: pass

            if not results and not self.api_call:
                quit(colored('\n[!] Not a valid encoding.\n', 'red'))

            # print/return the results
            for x in range(len(results)):
                if not self.api_call:
                    print(colored('\n[-] The Encoding Scheme Is ', 'blue')+colored(encoding_type[x], 'green'))                    
                    # generating the wordlist/output file with the decoded base
                    if self.output != None:
                        open(self.output, 'a').write(results[x]+'\n')
                else:
                    return results[x], encoding_type[x]


    def decode_base_from_file(self, file):
        """
        this function fetches the set of base encodings from the input file
        and passes it to 'decode_base()' function to decode it all
        """
        print(colored('[-] Decoding Base Data From ', 'cyan')+colored(file, 'yellow'))
        # opening the input file
        with open(file) as input_file:
            # reading each line from the file
            for line in input_file:
                # checking if the line/base is not empty
                if len(line) > 1:
                    # printing the encoded base
                    print(colored('\n[-] Encoded Base: ', 'yellow')+str(line.strip()))

                    if self.magic_mode_call: self.magic_mode(line)
                    else: self.decode_base(line)

                    # separating each decode results with some lines yo
                    print(colored('\n{{<<', 'red')+colored('='*70, 'yellow')+colored('>>}}', 'red'))


    def decode(self, encoded_base):
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
        self.api_call = True
        # api calls returns a tuple with the decoded base and the encoding scheme
        return self.decode_base(encoded_base)

    # magic mode tries to decode multi-encoded bases
    def magic_mode(self, encoded_base):
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

            # generating the wordlist/output file with the decoded base
            if self.output != None:
                open(self.output, 'a').write(decoded_string+'\n')

            completion_time = str(end_time-start_time)[:6]
            print(colored('\n[-] Finished in ', 'green')+colored(completion_time, 'cyan', attrs=['bold'])+colored(' seconds\n', 'green'))
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
            BaseCrack(output=args.output, magic_mode_call=True).decode_base_from_file(str(args.file))
        else:
            BaseCrack(output=args.output).decode_base_from_file(str(args.file))    

    elif args.base:
        print(colored('[-] Encoded Base: ', 'yellow')+colored(str(args.base), 'red'))

        if args.magic: BaseCrack().magic_mode(str(args.base))
        else: BaseCrack().decode_base(str(args.base))

    else:
        # input() for python2 is actually eval() :face_palm:
        if sys.version_info >= (3, 0):
            encoded_base = input(colored('[>] Enter Encoded Base: ', 'yellow'))
        else:
            encoded_base = raw_input(colored('[>] Enter Encoded Base: ', 'yellow'))

        if args.magic: BaseCrack().magic_mode(encoded_base)
        else: BaseCrack().decode_base(encoded_base)

    if args.output:
        print(colored('\n[-] Output Generated Successfully > ', 'green')+colored(args.output+'\n', 'yellow'))        

if __name__ == '__main__':
    init()
    main()
