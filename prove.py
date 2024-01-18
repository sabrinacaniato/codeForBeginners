import base64

def hex2string(text):
    ascii_string =  bytes.fromhex(text).decode('utf-8', errors="ignore") 
    return ascii_string


def binary2string(text):
    return''.join(chr(int(text[i*8:i*8+8],2)) for i in range(len(text)//8))


def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")


text='000111010101'
sol=binary2string(text)
print(sol)
