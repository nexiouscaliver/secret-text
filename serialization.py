#including main lib
import lib_secret_text as sc

#global var:
global ssa_key 
global serdict
global serdict2
global serdict3

#default values:
ssa_key = "ABCDE.123456789"

#============================================================================

#serial num table


serdict = {
"!" : "1",
"." : "2",
"|" : "3",
"_" : "4",
"@" : "5",
"#" : "6",
"-" : "7",
"+" : "8",
"*" : "9",
"/" : "0",
"[" : ".",
"]" : "A",
"<" : "B",
">" : "C",

}

serdict2 = {
"1" : "!",
"2" : ".",
"3" : "|",
"4" : "_",
"5" : "@",
"6" : "#",
"7" : "-",
"8" : "+",
"9" : "*",
"0" : "/",
"." : "[",
"A" : "]",
"B" : "<",
"C" : ">",
"D" : " ",
}

serdict3 = {
"!" : "1",
"." : "2",
"|" : "3",
"_" : "4",
"@" : "5",
"#" : "6",
"-" : "7",
"+" : "8",
"*" : "9",
"/" : "0",
"[" : ".",
"]" : "A",
"<" : "B",
">" : "C",
"D" : " ",
}


#============================================================================


#serial engine start :

default_key = "1234567890.ABCD"    #15dig-code

def check_key(k):
    if(k=='default'):
        return True
    else:
        k1 = list(k)
        k2 = set(k)
        if(len(k1) != len(k2)):
            return False
        else: return True

def change_key(k):
    global ssa_key
    if(k == 'default'):
        ssa_key = default_key
    else:
        if(len(k) == 15):
            ssa_key = k
            return True
        else:
            return False

def set_tables():
    global serdict
    global serdict2
    global serdict3
    global ssa_key

    a1 = ssa_key[0]
    a2 = ssa_key[1]
    a3 = ssa_key[2]
    a4 = ssa_key[3]
    a5 = ssa_key[4]
    a6 = ssa_key[5]
    a7 = ssa_key[6]
    a8 = ssa_key[7]
    a9 = ssa_key[8]
    a10 = ssa_key[9]
    a11 = ssa_key[10]
    a12 = ssa_key[11]
    a13 = ssa_key[12]
    a14 = ssa_key[13]
    a15 = ssa_key[14]

    
    serdict = {
    "!" : a1,
    "." : a2,
    "|" : a3,
    "_" : a4,
    "@" : a5,
    "#" : a6,
    "-" : a7,
    "+" : a8,
    "*" : a9,
    "/" : a10,
    "[" : a11,
    "]" : a12,
    "<" : a13,
    ">" : a14,

    }

    serdict2 = {
    a1 : "!",
    a2 : ".",
    a3 : "|",
    a4 : "_",
    a5 : "@",
    a6 : "#",
    a7 : "-",
    a8 : "+",
    a9 : "*",
    a10 : "/",
    a11 : "[",
    a12 : "]",
    a13 : "<",
    a14 : ">",
    a15 : " ",
    }

    serdict3 = {
    "!" : a1,
    "." : a2,
    "|" : a3,
    "_" : a4,
    "@" : a5,
    "#" : a6,
    "-" : a7,
    "+" : a8,
    "*" : a9,
    "/" : a10,
    "[" : a11,
    "]" : a12,
    "<" : a13,
    ">" : a14,
    "D" : a15,
    }

    



#============================================================================

def ser_decode(cipherd):
    text = []
    cipher = []
    for i in cipherd:
        cipher.append(i)
        cipher.append(' ')
    #print(cipher)
    while True:
        try:

            for aaa in range(0, len(cipher)):
                d1 = cipher[aaa * 2 + 0]
                #d2 = cipher[aaa * 2 + 1]
                #d3 = cipher[aaa * 5 + 2]
                #d4 = cipher[aaa * 5 + 3]
                #d5 = cipher[aaa * 5 + 4]
                #d6 = cipher[aaa * 8 + 5]
                #d7 = cipher[aaa * 8 + 6]
                #d8 = cipher[aaa * 8 + 7]

                #www = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8
                www = d1 

            
                zzz = serdict2[www]

          

                text.append(zzz)
           
        except IndexError:
      
            puretext = ''.join(map(str, text))
            return puretext
            break

def ser_encode(plain_text):
    code_text = ''
    for letter in plain_text :

        if letter != ' ':

            code_text += serdict[letter] + ' '

        else :
            code_text += 'D' + ' '
    if code_text == '':
        code_text = '|*| ERROR NO INPUT IS GIVEN !! \n|*| Enter Some Text To Encode It.'
        print("ERROR 444 : NO ENTRY GIVEN")
        return code_text
    else:
        z = code_text.replace(' ','')
        return z

#============================================================================

def std_serial_encode(plain_text,ssa=default_key):
    A = check_key(ssa)
    if A:
        a0 = change_key(ssa)
    else : return 0
    
    if a0 : set_tables()
    else : return 0
    
    a1 = sc.std_encode(plain_text)
    a2 = ser_encode(a1)

    return a2

def std_serial_decode(cipherd,ssa=default_key):
    A = check_key(ssa)
    if A:
        a0 = change_key(ssa)
    else : return 0

    if a0 : set_tables()
    else: return 0

    a1 = ser_decode(cipherd)
    a2 = sc.std_decode(a1)

    return a2

def adv_serial_encode(plain_text,ssa=default_key):
    A = check_key(ssa)
    if A:
        a0 = change_key(ssa)
    else : return 0
    
    if a0 : set_tables()
    else : return 0
    
    a1 = sc.adv_encode(plain_text)
    a2 = ser_encode(a1)

    return a2

def adv_serial_decode(cipherd,ssa=default_key):
    A = check_key(ssa)
    if A:
        a0 = change_key(ssa)
    else : return 0

    if a0 : set_tables()
    else: return 0

    a1 = ser_decode(cipherd)
    a2 = sc.adv_decode(a1)

    return a2


#============================================================================










