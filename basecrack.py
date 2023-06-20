#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__  = 'Mufeed VH'
__version__ = '4.0'
__email__   = 'contact@mufeedvh.com'
__github__  = 'https://github.com/mufeedvh/basecrack'

import os
import re
import sys
import time
import platform
import json
import argparse
from colorama import init
from termcolor import colored
from pathlib import Path

from src.base_chain import DecodeBase
from src.messages import push_error, print_line_separator

class BaseCrack:
    def __init__(self, output=None, magic_mode_call=False, quit_after_fail=True):
        self.output = output
        # initial bools
        self.api_call = False
        self.magic_mode_call = magic_mode_call
        self.image_mode_call = False
        self.quit_after_fail = quit_after_fail

    # main decode function
    def decode_base(self, encoded_base):
        if len(encoded_base) > 3:
            # execute decode chain
            encoding_type, results = DecodeBase(
                encoded_base,
                api_call = self.api_call,
                image_mode = self.image_mode_call
            ).decode()

            if not results and not self.api_call:
                if not self.image_mode_call:
                    push_error('Not a valid encoding.')

                if self.quit_after_fail:
                    quit()

            # print/return the results
            for x in range(len(results)):          
                if not self.api_call:
                    print(
                        colored('\n[-] The Encoding Scheme Is ', 'blue') +
                        colored(encoding_type[x], 'green')
                    )

                    # generating the wordlist/output file with the decoded base
                    if self.output != None:
                        open(self.output, 'a').write(results[x]+'\n')
                else:
                    return results[x].strip(), encoding_type[x]

            if self.image_mode_call and results:
                print_line_separator()
        else:
            push_error("Found no valid base encoded strings.")


    def decode_from_file(self, file):
        """
        `decode_from_file()` fetches the set of base encodings from the input file
        and passes it to 'decode_base()' function to decode it all
        """

        print(colored('[-] Decoding Base Data From ', 'cyan') + colored(file, 'yellow'))

        # check whether file exists
        if not Path(file).is_file():
            push_error('File does not exist.')
            quit()

        with open(file) as input_file:
            # reading each line from the file
            for line in input_file:
                # checking if the line/base is not empty
                if len(line) > 1:
                    line = line.strip()
                    print(colored('\n[-] Encoded Base: ', 'yellow')+str(line))
                    
                    if self.magic_mode_call:
                        self.magic_mode(line)
                    else:
                        self.decode_base(line)

                    print_line_separator()


    def decode(self, encoded_base):
        """
        API FUNCTION
        ------------
        the `decode()` function returns a tuple
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


    def magic_mode(self, encoded_base):
        """
        `magic_mode()` tries to decode multi-encoded bases of any pattern
        """
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

            print(
                colored('\n[-] Magic Decode Finished With Result: ', 'green') +
                colored(decoded_string, 'yellow', attrs=['bold'])
            )

            # generating the wordlist/output file with the decoded base
            if self.output != None:
                open(self.output, 'a').write(decoded_string+'\n')

            completion_time = str(end_time-start_time)[:6]

            print(
                colored('\n[-] Finished in ', 'green') +
                colored(completion_time, 'cyan', attrs=['bold']) +
                colored(' seconds\n', 'green')
            )
        else:
            quit(colored('\n[!] Not a valid encoding.\n', 'red'))


    def decode_from_image(self, image, mode):
        """
        `decode_from_image()` AKA "lame_steganography_challenge_solving_automated()" has two modes:
            - OCR Detection Mode: dectects base encodings in images
            - EXIF Data Mode: detects base encodings in an image's EXIF data
        """
        self.image_mode_call = True

        # check whether file exists
        if not Path(image).is_file():
            push_error('File does not exist.')
            quit()

        if mode == 'exif':
            import exifread

            read_image = open(image, 'rb')
            exif_tags = exifread.process_file(read_image)

            for tag in exif_tags:
                split_tag = str(exif_tags[tag]).split(' ')

                for base in split_tag:
                    if len(base) < 3 or '\\x' in base: continue

                    for base in base.splitlines():
                        if self.magic_mode_call:
                            self.magic_mode(base)
                        else:
                            self.decode_base(base)
        elif mode == 'ocr':
            import cv2, pytesseract

            # import tesseract for windows
            if platform.system() == 'Windows':
                load_config = json.loads(open('config.json', 'r').read())

                if len(load_config) > 0:
                    # load 32/64 bit executables
                    if sys.maxsize > 2**32:
                        # 64 bit
                        tesseract_path = load_config['tesseract_path']['32bit']
                    else:
                        # 32 bit
                        tesseract_path = load_config['tesseract_path']['64bit']

                # raw string to treat `\` as a literal character
                pytesseract.pytesseract.tesseract_cmd = r'{}'.format(tesseract_path)

            read_image = cv2.imread(image)
            get_text = pytesseract.image_to_string(read_image)
            strings_from_img = str(get_text).replace(' ', '')

            # cleaning the detected string with valid base chars for accurary
            base = re.sub('[^A-Za-z0-9+/=@]', '', strings_from_img)

            if self.magic_mode_call: self.magic_mode(base)
            else: self.decode_base(base)


# print a banner to look cool
def banner():
    banner = '''
██████╗  █████╗ ███████╗███████╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║███████╗█████╗  ██║     ██████╔╝███████║██║     █████╔╝ 
██╔══██╗██╔══██║╚════██║██╔══╝  ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██████╔╝██║  ██║███████║███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ v4.0
    '''
    print(colored(banner, 'red')+colored('\n\t\tpython basecrack.py -h [FOR HELP]\n', 'green'))

def main():
    banner()

    # setting up argparse module to accept arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--base', help='Decode a single encoded base from argument.')
    parser.add_argument('-f', '--file', help='Decode multiple encoded bases from a file.')
    parser.add_argument('-m', '--magic', help='Decode multi-encoded bases in one shot.', action='store_true')
    parser.add_argument('-i', '--image', help='Decode base encodings from image with OCR detection or EXIF data.')
    parser.add_argument('-c', '--ocr', help='OCR detection mode.', action='store_true')
    parser.add_argument('-e', '--exif', help='EXIF data detection mode. (default)', action='store_true')
    parser.add_argument('-o', '--output', help='Generate a wordlist/output with the decoded bases, enter filename as the value.')
    args = parser.parse_args()

    if args.output:
        print(
            colored('\n[>] ', 'yellow') +
            colored('Enabled Wordlist Generator Mode :: ', 'green') +
            colored(args.output+'\n', 'blue')
        )

    """
    decodes base encodings from file if argument is given
    else it accepts a single encoded base from user
    """
    if args.file:
        if args.magic:
            BaseCrack(
                output=args.output,
                magic_mode_call=True
            ).decode_from_file(str(args.file))
        else:
            BaseCrack(output=args.output).decode_from_file(str(args.file))

    elif args.base:
        print(colored('[-] Encoded Base: ', 'yellow')+colored(str(args.base), 'red'))

        if args.magic:
            BaseCrack().magic_mode(str(args.base))
        else:
            BaseCrack().decode_base(str(args.base))

    elif args.image:
        print(colored('[-] Input Image: ', 'yellow')+colored(str(args.image), 'red'))

        if args.ocr:
            mode = 'ocr'
        elif args.exif:
            mode = 'exif'
        # default
        else:
            mode = 'exif'

        if args.magic:
            BaseCrack(
                output=args.output, magic_mode_call=True, quit_after_fail=False
            ).decode_from_image(str(args.image), mode)
        else:
            BaseCrack(
                quit_after_fail=False
            ).decode_from_image(str(args.image), mode)

    else:
        if sys.version_info >= (3, 0):
            encoded_base = input(colored('[>] Enter Encoded Base: ', 'yellow'))
        else:
            encoded_base = raw_input(colored('[>] Enter Encoded Base: ', 'yellow'))

        if args.magic:
            BaseCrack().magic_mode(encoded_base)
        else:
            BaseCrack().decode_base(encoded_base)

    if args.output:
        print(
            colored('\n[-] Output Generated Successfully > ', 'green') +
            colored(args.output+'\n', 'yellow')
        )

if __name__ == '__main__':
    init()
    main()
