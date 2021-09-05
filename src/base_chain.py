import anybase32
import base36
import base58
import base62
import base64
import base91
import src.base92 as base92
import pybase100

from termcolor import colored

class DecodeBase:
    def __init__(self, encoded_base, api_call=False, image_mode=False):
        self.encoded_base = encoded_base
        self.b32_once = False
        self.b64_once = False
        self.b64_url = False
        self.encoding_type = []
        self.results = []

        # state conditions
        self.api_call = api_call
        self.image_mode_call = image_mode

    def decode(self):
        self.decode_base()
        return (
            self.encoding_type,
            self.results
        )

    def contains_replacement_char(self, res):
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

    def process_decode(self, decode_string, scheme):
        """
        `process_decode()` stores the result if the encoding is valid
        after checks from `contains_replacement_char()` and
        prints the output if it isn't an API call
        """
        encoding_type = self.encoding_type
        results = self.results

        if len(decode_string) < 3: return
        if not self.contains_replacement_char(decode_string):
            # don't repeat `base64url` when `base64` has already passed and it's not a URL
            if scheme == 'Base64' and '://' not in decode_string:
                self.b64_once = True
                
            if self.b64_once and (scheme == 'Base64URL'):
                return
            
            # append results to the respective lists
            encoding_type.append(scheme)
            results.append(decode_string)

            if not self.api_call:
                if self.image_mode_call:
                    print(
                        colored('\n[-] Attempting Base: ', 'yellow') +
                        colored(self.encoded_base, 'red')
                    )

                print(
                    colored('\n[>] Decoding as {}: '.format(scheme), 'blue') +
                    colored(decode_string, 'green')
                )

    def decode_base(self):
        encoded_base = self.encoded_base
        process_decode = self.process_decode

        # decoding as base16
        try:
            process_decode(
                base64.b16decode(encoded_base, casefold=False).decode('utf-8', 'replace'),
                'Base16'
            )
        except Exception as _: pass

        # decoding as base32
        try:
            process_decode(
                base64.b32decode(
                    encoded_base, casefold=False, map01=None
                ).decode('utf-8', 'replace'),
                'Base32'
            )
            self.b32_once = True
        except Exception as _: pass

        # decoding as base32 (RFC 3548)
        if not self.b32_once:
            try:
                """
                Base32 charset can differ based on their spec, this requires stripping
                the padding or changing charsets to get the correct results.
                By default this `anybase32` implementation follows the RFC 3548 spec.
                """
                temp_clean_base = str.encode(encoded_base.replace('=', ''))
                process_decode(
                    anybase32.decode(temp_clean_base).decode('utf-8', 'replace'),
                    'Base32'
                )
            except Exception as _: pass                

        # decoding as base36
        try:
            process_decode(
                base36.dumps(int(encoded_base)),
                'Base36'
            )
        except Exception as _: pass

        # decoding as base58
        try:
            process_decode(
                base58.b58decode(encoded_base.encode()).decode('utf-8', 'replace'),
                'Base58'
            )
        except Exception as _: pass

        # decoding as base62
        try:
            process_decode(
                base62.decodebytes(encoded_base).decode('utf-8', 'replace'),
                'Base62'
            )
        except Exception as _: pass

        # decoding as base64
        try:
            process_decode(
                base64.b64decode(encoded_base).decode('utf-8', 'replace'),
                'Base64'
            )
        except Exception as _: pass

        # decoding as base64url
        try:
            process_decode(
                base64.urlsafe_b64decode(
                    encoded_base + '=' * (4 - len(encoded_base) % 4)
                ).decode('utf-8', 'replace'),
                'Base64URL'
            )
        except Exception as _: pass

        # decoding as base85
        try:
            process_decode(
                base64.b85decode(encoded_base).decode('utf-8', 'replace'),
                'Base85'
            )
        except Exception as _: pass

        # decoding as ascii85
        try:
            process_decode(
                base64.a85decode(encoded_base).decode('utf-8', 'replace'),
                'Ascii85'
            )
        except Exception as _: pass

        # decoding as base91
        try:
            process_decode(
                base91.decode(encoded_base).decode('utf-8', 'replace'),
                'Base91'
            )
        except Exception as _: pass

        # decoding as base92
        try:
            process_decode(
                base92.decode(encoded_base),
                'Base92'
            )
        except Exception as _: pass

        # decoding as base100 lol why??!!
        try:
            process_decode(
                pybase100.decode(encoded_base).decode(),
                'Base100'
            )
        except Exception as _:
            pass