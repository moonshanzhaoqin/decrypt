

from Crypto.Cipher import AES
from Crypto import Random
import base64

block_size = AES.block_size
def pad(plain_text):
    """
    func to pad cleartext to be multiples of 8-byte blocks.
    If you want to encrypt a text message that is not multiples of 8-byte blocks,
    the text message must be padded with additional bytes to make the text message to be multiples of 8-byte blocks.
    """
    number_of_bytes_to_pad = block_size - len(plain_text) % block_size
    ascii_string = chr(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string
    padded_plain_text =  plain_text + padding_str
    print type(padded_plain_text)
    return padded_plain_text


key='anytime_exchange'
plain="{\"name\": \"Silent\",\"age\": 30}"
plain = pad(plain)
iv = 'anytime_exchange'

cipher = AES.new(key, AES.MODE_CBC, iv )
encrypted_text = cipher.encrypt( plain )
print type(encrypted_text)
print str(encrypted_text)
encrypted_text2="piAqI2W4b144j1UPu5wvloKszvuD6wRCSs9qAqEGX3Y="
obj2 = AES.new(key, AES.MODE_CBC, iv)
print obj2.decrypt(encrypted_text)

