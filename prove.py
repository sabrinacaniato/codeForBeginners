import base64

def ceasar_cracker(text, from_ = -30, to_=+30):
    for i in range(from_, to_): #possible keys [-30, 30]
        #decode
        curr_step = ''.join([chr(ord(c) + i) for c in text])

        #print
        print(f"Step={i}\t{curr_step}")

def hex2string(text):
    ascii_string =  bytes.fromhex(text).decode('utf-8', errors="ignore") 
    return ascii_string
    
# decode the flag from hex to ascii
decoded = binascii.unhexlify(hex_encrypted)
decoded = decoded.decode('ascii')

def binary2string(text):
    return''.join(chr(int(text[i*8:i*8+8],2)) for i in range(len(text)//8))


def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")


text='000111010101'
sol=binary2string(text)
print(sol)
