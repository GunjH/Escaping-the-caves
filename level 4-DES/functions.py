import numpy as np

def hexCipher(ciphertext,mapping):
    hex_cipher=[]
    for i in ciphertext:
        
        hex=[]
        if len(i) == 16:
            for j in range(16):
                hex.extend(mapping[i[j]])
            hex_cipher.extend([hex])    
    return hex_cipher

def ITFP(hexcipher, RFP):
    invres = []
    for i in hexcipher:
        temp = [i[RFP[j]-1] for j in range(64)]
        invres.append(temp)
    return invres   

def Xor_cipher(invres):
    resxor = [list(np.bitwise_xor(invres[2*i], invres[2*i+1])) for i in range(len(invres)//2)]
    return resxor  
     

def Expanded(invres, E):
    expanded = []

    for i in invres:
        temp = [i[E[j]-1] for j in range(48)]
        expanded.append(temp)

    return expanded
    
def Xor_sbox(inxor, INVP):
    sxor = []
    for i in inxor:
        temp = [i[INVP[j]-1] for j in range(32)]
        sxor.append(temp)
    return sxor


def Xor_e_sbox(expanded):
    sin = [list(np.bitwise_xor(expanded[2*i], expanded[2*i+1])) for i in range(len(expanded)//2)]
    return sin


def keys_6(sin,sxor,expanded,sbox):
    keys = np.zeros((8,64))

    for i in range(len(sin)):
        if sin[i]=="":
            continue 
        for j in range(0,8):
            inx = int(''.join([str(s) for s in sin[i][j*6:j*6+6]]),2)
            outx = int(''.join([str(s) for s in sxor[i][j*4:j*4+4]]),2)
            inp = int(''.join([str(s) for s in expanded[2*i+1][j*6:j*6+6]]),2)

            for k in range(0,64):
                a = bin(k)[2:].zfill(6)
                b = bin(k^inx)[2:].zfill(6)
                if outx == sbox[j][int(a[0])*2 + int(a[5])][int(a[4]) + 2 *int(a[3]) + int(a[2]) * 4 + int(a[1])*8]^sbox[j][int(b[0])*2 + int(b[5])][int(b[4]) + 2 *int(b[3]) + int(b[2]) * 4 + int(b[1])*8]:
                    keys[j][k^inp]+=1
    return keys  

def xor_l5_l6(resxor, L5):
    inxor = [list(np.bitwise_xor(i[32:64], L5)) for i in resxor]
    return inxor

def max_mean_key_value(keys):
    mean_v = [int(np.mean(k)) for k in keys]
    max_v = [max(k) for k in keys]
    key_v = [np.where(k == max(k))[0][0] for k in keys]
    return max_v, mean_v, key_v

def find_key(PC2,sbkey,shift_table):
    key = ['X']*56
    for i in range(48):
       key[PC2[i]-1] = sbkey[i]
    for i in range(0,6):
        for j in range(shift_table[i]):
            x = key[27]
            y = key[55]
            for k in range(27,0,-1):
                key[k] = key[k-1]
                key[k+28] = key[k+27]
            key[0] = x
            key[28] = y
    return key

 
def permute(k, arr, n): 
    permutation = "" 
    for i in range(0, n): 
        permutation = permutation + k[arr[i] - 1] 
    return permutation 
   
def shift(k, n): 
    return k[n:] + k[0:n]


def roundkey(k,rno,shift_table,key_comp):
    
    binkey = []

    for i in range(rno):
            
        key = shift(k[0:28],shift_table[i]) + shift(k[28:56],shift_table[i])
        binkey.extend([permute(key,key_comp,48)])

    return binkey


def encryption(mess,key,rno,initial_perm,E,sbox,sboxper,final_perm):

  mess = permute(mess,initial_perm,64)

  left = mess[:32]
  right = mess[32:]

  for i in range(rno):
   
    expmess = permute(right,E,48)
    inxor = str(bin(np.bitwise_xor(int(expmess,2),int(key[i],2)))[2:])
    if(len(inxor)!=48):
      inxor= ('0'*(48-len(inxor)))+inxor
    sout = ''
    for j in range(8):
      temp = (bin(sbox[j][int(inxor[j*6]+inxor[j*6+5],2)][int(inxor[j*6+1:j*6+5],2)])[2:])
      sout+= ('0'*(4-len(temp))+temp)
    sout = permute(sout,sboxper,32)

    roundxor = str(bin(np.bitwise_xor(int(left,2),int(sout,2)))[2:])
    if(len(roundxor)!=32):
      roundxor= ('0'*(32-len(roundxor)))+roundxor
    left = roundxor

    if(i!=5):
      t = left
      left = right
      right = t

    
  outmess = left + right
  cipher = permute(outmess,final_perm,64)

  return cipher
    
  