#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Mufeed VH"
__version__ = "1.0.0"
__email__   = "contact@mufeedvh.com"
__github__  = "https://github.com/mufeedvh"

# importing some required stuff
import re
import argparse
from termcolor import colored
import base36
import base58
import base62
import base64
import base91

# compatibility handling
try:
	import base92
except ImportError:
	print(colored("\nBaseCrack is not compatible with Python3, use Python2.\n", "red"))
	quit()


# basecrack class containing all the base decoding methods
class BaseCrack:
	def __init__(self, encoded_base):
		self.encoded_base = encoded_base

	# decoding a single encoded base 
	def decode_base(self):
		# declaring the encoding type array to store encoding types which haven't caused errors
		encoding_type = []

		# declaring the results array to store results which haven't caused errors
		results = []

		# checking if input is not empty
		if len(self.encoded_base) > 1:
			# decoding as base16
			try:
				base16_decode = base64.b16decode(self.encoded_base, casefold=False)
				encoding_type.append("Base16")
				results.append(base16_decode)
				print(colored("\n[>] Decoding as Base16: ", "blue")+colored(str(base16_decode), "green"))
			except:
				pass

			# decoding as base32
			try:
				base32_decode = base64.b32decode(self.encoded_base, casefold=False, map01=None)
				encoding_type.append("Base32")
				results.append(base32_decode)
				print(colored("\n[>] Decoding as Base32: ", "blue")+colored(str(base32_decode), "green"))
			except:
				pass

			# decoding as base36
			try:
				base36_decode = base36.dumps(self.encoded_base)
				encoding_type.append("Base36")
				results.append(base36_decode)
				print(colored("\n[>] Decoding as Base36: ", "blue")+colored(str(base36_decode), "green"))
			except:
				pass

			# decoding as base58
			try:
				base58_decode = base58.b58decode(self.encoded_base)
				encoding_type.append("Base58")
				results.append(base58_decode)
				print(colored("\n[>] Decoding as Base58: ", "blue")+colored(str(base58_decode), "green"))
			except:
				pass

			# decoding as base62
			try:
				base62_decode = base62.encode(int(self.encoded_base))
				encoding_type.append("Base62")
				results.append(base62_decode)
				print(colored("\n[>] Decoding as Base62: ", "blue")+colored(str(base62_decode), "green"))
			except:
				pass

			# decoding as base64
			try:
				base64_decode = base64.b64decode(self.encoded_base)
				encoding_type.append("Base64")
				results.append(base64_decode)
				print(colored("\n[>] Decoding as Base64: ", "blue")+colored(str(base64_decode), "green"))
			except:
				pass

			# decoding as base64url
			try:
				base64url_decode = base64.urlsafe_b64decode(self.encoded_base + '=' * (4 - len(self.encoded_base) % 4))
				encoding_type.append("Base64Url")
				results.append(base64url_decode)
				print(colored("\n[>] Decoding as Base64Url: ", "blue")+colored(str(base64url_decode), "green"))
			except:
				pass

			# decoding as base85
			try:
				base85_decode = base64.b85decode(self.encoded_base)
				encoding_type.append("Base85")
				results.append(base85_decode)
				print(colored("\n[>] Decoding as Base85: ", "blue")+colored(str(base85_decode), "green"))
			except:
				pass

			# decoding as base91
			try:
				base91_decode = base91.decode(self.encoded_base)
				encoding_type.append("Base91")
				results.append(base91_decode)
				print(colored("\n[>] Decoding as Base91: ", "blue")+colored(str(base91_decode), "green"))
			except:
				pass

			# decoding as base92
			try:
				base92_decode = base92.decode(self.encoded_base)
				encoding_type.append("Base92")
				results.append(base92_decode)
				print(colored("\n[>] Decoding as Base92: ", "blue")+colored(str(base92_decode), "green"))
			except:
				pass

			# algorithm to identify which type of base encoding the input is
			for x in range(len(results)):
				# identifying the encoding type with regex pattern matching
				if re.match("^[A-Za-z0-9_ ]*$", results[x]):
					# printing the predicted encoding type
					print(colored("\nThe accurate base encoding type is probably ", "red")+colored(encoding_type[x], "green"))

	# fetching a set of base encodings from input file and passing it to 'decode_base' function to decode it all
	def decode_base_from_file(self):
		# opening the input file
		with open(self.encoded_base) as input_file:
			# reading each line from file
			for line in input_file:
				# declaring current line as the encoded_base value
				self.encoded_base = line

				# checking if input is not empty
				if len(line) > 1:
					# printing encoded base
					print(colored("\nEncoded Base: ", "yellow")+str(line))

					# calling the 'decode_base' function to decode the current line
					self.decode_base()

					# separating each decode results with some lines yo
					print(colored("\n{{<<", "red")+colored("="*70, "yellow")+colored(">>}}", "red"))
	

def main():
	# print this kickass banner
	print(colored('''
███   ██      ▄▄▄▄▄   ▄███▄   ▄█▄    █▄▄▄▄ ██   ▄█▄    █  █▀ 
█  █  █ █    █     ▀▄ █▀   ▀  █▀ ▀▄  █  ▄▀ █ █  █▀ ▀▄  █▄█   
█ ▀ ▄ █▄▄█ ▄  ▀▀▀▀▄   ██▄▄    █   ▀  █▀▀▌  █▄▄█ █   ▀  █▀▄   
█  ▄▀ █  █  ▀▄▄▄▄▀    █▄   ▄▀ █▄  ▄▀ █  █  █  █ █▄  ▄▀ █  █  
███      █            ▀███▀   ▀███▀    █      █ ▀███▀    █   
		█                             ▀      █          ▀    
	   ▀                                    ▀                
		''', 'red')+colored("python basecrack.py -h [FOR HELP]\n", "green"))

	# setting up argparse module to accept arguments
	parser = argparse.ArgumentParser()
	# to accept argument '-b' or '--base' to decode a single encoded base from the value of argument '-b' or '--base'
	parser.add_argument('-b', '--base', help='Decode a single encoded base from argument')
	# to accept argument '-f' or '--file' to decode multiple encoded bases from a file
	parser.add_argument('-f', '--file', help='Decode multiple encoded bases from a file')
	args = parser.parse_args()

	# decodes base encodings from file if argument is given, else it accepts a single encoded base from user
	if args.file:
		print(colored("Decoding Base Data From ", "green")+colored(str(args.file), "red"))
		# triggering the 'decode base from file' function from basecrack class with the input file
		BaseCrack(str(args.file)).decode_base_from_file()
	elif args.base:
		print(colored("Encoded Base: ", "yellow")+colored(str(args.base), "red"))
		# triggering the 'decode base' function directly from basecrack class with the base argument
		BaseCrack(str(args.base)).decode_base()
	else:
		encoded_base = raw_input(colored("Enter Encoded Base: ", "yellow"))
		# triggering the 'decode base' function directly from basecrack class with the user input
		BaseCrack(encoded_base).decode_base()


if __name__ == '__main__':
	main()
