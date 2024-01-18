
def rule9b0(b):
    row=int(b[0])
    col=int(b[1:],2)

    matrix=[['101','010','001','110','011','100','111','000'],['001','100','110','010','000','111','101','011']]
    return matrix[row][col]

def rule9b1(b):
    row=int(b[0])
    col=int(b[1:],2)

    matrix=[['100','000','110','101','111','001','011','010'],['101','011','000','111','110','010','001','100']]
    return matrix[row][col]

def string2binary(text):
    return''.join(f"{ord(c):08b}"for c in text)

def binary2string(text):
    return''.join(f"{ord(c):08b}" for c in text)

def splitblock(text):
    L=text[:6]
    R=text[6:]
    return L, R

def expand_miniblock(b):
    return b[0]+b[1]+b[3]+b[2]+b[3]+b[2]+b[4]+b[5]

def xor(a,b):
    res=int(a,2)^int(b,2)

    return f"{res:08b}"

def encrypt(text, key, R):
    text_encr=''

    #R1
    text_bin=string2binary(text)
    if(len(text_bin)%12!=0):
        raise Exception(f'Rule 1 not respected.')
    
    #R2
    key_bin=string2binary(key)
    if(len(key_bin)<8):
        raise Exception(f'Rule 2 not respected.')
    
    #R3
    for bnum in range(len(text_bin)//12):
        i=bnum

        #define the block
        from_=0+12*bnum
        to_=12*(bnum+1)
        block=text_bin[from_:to_]

        #R4
        for r in range(R):
            #R5
            Lr,Rr=splitblock(block)

            #R6
            Rr_expand=expand_miniblock(Rr)

            #R7
            curr_key=key_bin[(i*R+r):((i*R+r)+8)]
            Rr_exp_xor_key=xor(Rr_expand, curr_key)

            #R8
            Rr_exp_0=Rr_exp_xor_key[:4]
            Rr_exp_1=Rr_exp_xor_key[4:]

            #R9
            Rr_exp_sol_0=rule9b0(Rr_exp_0)
            Rr_exp_sol_1=rule9b1(Rr_exp_1)

            #R10
            Rr_exp_sol=Rr_exp_sol_0+Rr_exp_sol_1
            if(len(Rr_exp_sol) !=6):
                raise Exception("Error on Rule 10")
            
            #R11
            Res=xor(Lr,Rr_exp_sol)[2:]

            #R12
            block=Rr+Res

        text_encr+=block

    return text_encr

def decrypt(text, key, R):
    text_dec=''

    text_bin=text
    key_bin=string2binary(key)
    if (len(text_bin) < 8):
        raise Exception('Rule 2 not respected')
  
    #R3
    for bnum in range(len(text_bin)//12):
        i=bnum

        #define the block
        from_=0+12*bnum
        to_=12*(bnum+1)
        block=text_bin[from_:to_]

        for r in range(R-1,-1,-1):
            Rr, Rr_alt=splitblock(block)
            #rule6
            Rr_expanded = expand_miniblock(Rr)
            #Rule7
            curr_key = key_bin[(i* R + r) : ((i* R + r)+8)]
            Rr_exp_xor_key = xor(Rr_expanded, curr_key)
            #Rule8
            Rr_exp_xor_key_0 = Rr_exp_xor_key[:4]
            Rr_exp_xor_key_1 = Rr_exp_xor_key[4:]
            #Rule9
            Rr_exp_xor_key_0_conv = rule9b0(Rr_exp_xor_key_0)
            Rr_exp_xor_key_1_conv = rule9b1(Rr_exp_xor_key_1)
            Rr_sboxes = Rr_exp_xor_key_0_conv + Rr_exp_xor_key_1_conv
            #Rule10
            if len(Rr_sboxes) != 6:
                raise Exception("Error on Rule 10")
            
            Lr = xor(Rr_alt, Rr_sboxes)
            Lr = Lr[2:]
            block = Lr + Rr

        new_block = Lr + Rr
        text_dec += new_block
    res = ''
    for i in range(len(text_dec) // 8):
        res += chr(int(text_dec[(i * 8): ((i+1) * 8)] ,2))
    print(res)


puzzle = "011001010010001010001100010110000001000110000101"
key_ex = 'Mu'
R_ex = 2

decrypt(puzzle, key_ex, R_ex)
#flag: Min0n!

decrypt(encrypt('Min0n!', 'Mu', 2), 'Mu', 2)

