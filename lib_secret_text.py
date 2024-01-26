# Import modules
import time
import datetime
import sys
from cryptography.fernet import Fernet
import hashlib
import os
from zipfile import ZipFile
import shutil
now = datetime.datetime.now()

# global variable :
code_text = " "
supercode = []
supertext = []
secondencrypt = []
path = os.getcwd()
global hashfilezip
global keyfilezip

# Dictnorary For Text-to-Secret text
key_dict = {
"a" : "**/**" ,
"b" : "/****" ,
"c" : "*/***" ,
"d" : "***/*" ,
"e" : "****/" ,
"f" : "**//*" ,
"g" : "//***" ,
"h" : "*//**" ,
"i" : "***//" ,
"j" : "**/*/" ,
"k" : "*/**/" ,
"l" : "*/*/*" ,
"m" : "/***/" ,
"n" : "/**/*" ,
"o" : "*///*" ,
"p" : "/*//*" ,
"q" : "/*/*/" ,
"r" : "*/*//" ,
"s" : "*//*/" ,
"t" : "**///" ,
"u" : "*////" ,
"v" : "////*" ,
"w" : "/*///" ,
"x" : "///*/" ,
"y" : "//*//" ,
"z" : "/////" ,
"?" : "|***|" ,
"." : "|///|" ,
"!" : "|/*/|" ,
"," : "|*/*|" ,
";" : "|//*|" ,
":" : "|*//|" ,
"(" : "||/||" ,
")" : "||*||" ,
"'" : "||-||" ,
""" " """: "||.||" ,

"A" : "..-.." ,
"B" : "-...." ,
"C" : "....-" ,
"D" : ".-..." ,
"E" : "...-." ,
"F" : ".--.." ,
"G" : "..--." ,
"H" : ".-..-" ,
"I" : "-...-" ,
"J" : "..-.-" ,
"K" : "-..-." ,
"L" : "-.-.." ,
"M" : ".---." ,
"N" : "-.--." ,
"O" : "--..-" ,
"P" : "--.-." ,
"Q" : ".-.--" ,
"R" : "..---" ,
"S" : "---@-" ,
"T" : "----@" ,
"U" : "-.---" ,
"V" : "--.--" ,
"W" : "---.-" ,
"X" : "----." ,
"Y" : "-*-*-" ,
"Z" : "*-*-*" ,

"1" : "|[]]|" ,
"2" : "|[[]|" ,
"3" : "/[[]/" ,
"4" : "/[]]/" ,
"5" : "!---!" ,
"6" : "!-*-!" ,
"7" : "!*-*!" ,
"8" : "!/*/!" ,
"9" : "!*/*!" ,
"0" : "@+++@" ,
"=" : "#---#" ,
"-" : "#-*-#" ,
"*" : "!.-.!" ,
"/" : "!-.-!" ,
"_" : "@@#@@" ,
'_' : "@@#@@" ,
"|" : "@!!!@" ,
"@" : "!...!" ,
"#" : "!#.#!" ,
"[" : "<<>>>" ,
"]" : ">><<<" ,
"{" : "<<<>>" ,
"}" : ">>><<" ,
">" : "<<>><" ,
"<" : ">><<>" ,
'\\': ".._.." ,
"+" : "_._._" ,
"&" : "._._." ,
"$" : "@@!@@" ,
"%" : "!!@!!" ,
"^" : "!@!@!" ,
"~" : "@!@!@" ,
"`" : "!!#!!" ,
"\n": "!!*!!" ,
"\t": "**!**" ,


}
# =====================================================================================================================

# =====================================================================================================================

ssign_dic = {
"**/** " : "a"  ,
"/**** " : "b",
"*/*** " : "c",
"***/* " : "d",
"****/ " : "e",
"**//* " : "f",
"//*** " : "g",
"*//** " : "h",
"***// " : "i",
"**/*/ " : "j",
"*/**/ " : "k",
"*/*/* " : "l",
"/***/ " : "m",
"/**/* " : "n",
"*///* " : "o",
"/*//* " : "p",
"/*/*/ " : "q",
"*/*// " : "r",
"*//*/ " : "s",
"**/// " : "t",
"*//// " : "u",
"////* " : "v",
"/*/// " : "w",
"///*/ " : "x",
"//*// " : "y",
"/////| " : "z",
"|***| " : "?",
"|///| " : ".",
"|/*/| " : "!",
"|*/*| " : ",",
"|//*| " : ";",
"|*//| " : ":",
"||/|| " : "(",
"||*|| " : ")",
"||-|| " : "'",
"||.|| " : """ " """  ,

"..-.. " : "A",
"-.... " : "B",
"....- " : "C",
".-... " : "D",
"...-. " : "E",
".--.. " : "F",
"..--. " : "G",
".-..- " : "H",
"-...- " : "I",
"..-.- " : "J",
"-..-. " : "K",
"-.-.. " :"L",
".---. " : "M",
"-.--. " : "N",
"--..- " : "O",
"--.-. " : "P",
".-.-- " : "Q",
"..--- " : "R",
"---@- " : "S",
"----@ " : "T",
"-.--- " : "U",
"--.-- " : "V",
"---.- " : "W",
"----. " : "X",
"-*-*- " : "Y",
"*-*-* " : "Z",

"|[]]| " : "1",
"|[[]| " : "2",
"/[[]/ " : "3",
"/[]]/ " : "4",
"!---! " : "5",
"!-*-! " : "6",
"!*-*! " : "7",
"!/*/! " : "8",
"!*/*! " : "9",
"@+++@ " : "0",
"#---# " : "=",
"||||| " : " ",
"#-*-# " : "-",
"!.-.! " : "*",
"!-.-! " : "/",
"@@#@@ " : "_",
"@!!!@ " : "|",
"!...! " : "@",
"!#.#! " : "#",
"<<>>> " : "[",
">><<< " : "]",
"<<<>> " : "{",
">>><< " : "}",
"<<>>< " : ">",
">><<> " : "<",
".._.. " : '\\',
"_._._ " : "+",
"._._. " : "&",
"@@!@@ " : "$",
"!!@!! " : "%",
"!@!@! " : "^",
"@!@!@ " : "~",
"!!#!! " : "`",
"!!*!! ": "\n",
"**!** ": "\t",

}


#==============================DOT DICT.=====================================







#==============================DOT DICT.=====================================

#==============================CORE DEFINATIONS=================================

def seperate() :
    print("====================")
    time.sleep(0.3)
    print("====================")
    print()


def decode(cipher) :
    seperate()
    plain_text = ''
    citext = ''
    for sign in cipher :
        if sign !=  ' ':
            citext += sign

        else :
            if sign != ' ' :
                plain_text += sign_dic[citext]

            else :
                plain_text += ' '
    print(citext)
    return plain_text


def cipher(code_text):

    # its Lv.2 encoding
    list = []
    codelist = (code_text)

    while True:
        try:

            for aaa in range(0,len(codelist)):
                d1 = codelist[aaa * 5 + 0]
                d2 = codelist[aaa * 5 + 1]
                d3 = codelist[aaa * 5 + 2]
                d4 = codelist[aaa * 5 + 3]
                d5 = codelist[aaa * 5 + 4]
                #d6 = codelist[aaa * 5 + 5]
                #d7 = codelist[aaa * 5 + 6]
                #d8 = codelist[aaa * 5 + 7]

                www = d3 + d2 + d5 + d1 + d4 #+ d7 + d8 + d6

                supercode.append(www)

        except IndexError :
            print(supercode)
def decipher(cipher) :
    text = []
    while True:
        try:

            for aaa in range(0, len(cipher)):
                d1 = cipher[aaa * 6 + 0]
                d2 = cipher[aaa * 6 + 1]
                d3 = cipher[aaa * 6 + 2]
                d4 = cipher[aaa * 6 + 3]
                d5 = cipher[aaa * 6 + 4]
                d6 = cipher[aaa * 6 + 5]
                # d7 = cipher[aaa * 5 + 6]
                # d8 = cipher[aaa * 5 + 7]

                www = d1 + d2 + d3 + d4 + d5 + d6 #+ d7 + d8

            
                zzz = ssign_dic[www]

          

                text.append(zzz)
           
        except IndexError:
      
            puretext = ''.join(map(str, text))
            return puretext
            break


def level2(code_text):

    codelist = code_text
    len(codelist)
    supercode = []
    while True:
        try:

            for aaa in range(0, len(codelist)):
                d1 = codelist[aaa * 6 + 0]
                d2 = codelist[aaa * 6 + 1]
                d3 = codelist[aaa * 6 + 2]
                d4 = codelist[aaa * 6 + 3]
                d5 = codelist[aaa * 6 + 4]
                d6 = codelist[aaa * 6 + 5]
                # d7 = codelist[aaa * 5 + 6]
                # d8 = codelist[aaa * 5 + 7]

                #www = d3 + d2 + d5 + d1 + d4 + d7 + d8 + d6
                www = d4 + d1 + d3 + d6 + d5 + d2
                
                supercode.append(www)

        except IndexError:
     
            puretext = ''.join(map(str, supercode))
            #print(puretext)
            return puretext
            break


def level3(cipher):
    supertext = []
    while True:
        try:

            for aaa in range(0,len(cipher)):

                d1 = cipher[aaa * 6 + 0]
                d2 = cipher[aaa * 6 + 1]
                d3 = cipher[aaa * 6 + 2]
                d4 = cipher[aaa * 6 + 3]
                d5 = cipher[aaa * 6 + 4]
                d6 = cipher[aaa * 6 + 5]
                # d7 = cipher[aaa * 5 + 6]
                # d8 = cipher[aaa * 5 + 7]

                #www = d4 + d2 + d1 + d5 + d3 + d6 + d8 + d6 + d7
                www = d2 + d6 + d3 + d1 + d5 + d4


                supertext.append(www)
                

        except IndexError :
            puretext = ''.join(map(str, supertext))
 

            secondencrypt.append(puretext)
            return puretext

            break

#==============================SECOND LEVEL DEFINATIONS=========================

def std_encode(plain_text) :
    #seperate()
    #print(plain_text," --> Your plain text")
    code_text = ''
    for letter in plain_text :

        if letter != ' ':

            code_text += key_dict[letter] + ' '

        else :
            code_text += '|||||' + ' '
    if code_text == '':
        code_text = '|*| ERROR NO INPUT IS GIVEN !! \n|*| Enter Some Text To Encode It.'
        print("ERROR 444 : NO ENTRY GIVEN")
        return code_text
    else:
        
        return code_text
    #END !


def std_decode(arg):
    code_text = " "
    supercode = []
    supertext = []
    secondencrypt = []

    
    while True:
        try:

 
            cipher = list(arg)
            if cipher[-1] == " ":

                output = decipher(cipher)
                if output == '' :
                    output = "|*| INVALID CIPHER ERROR !! \n|*| Enter A Valid Cipher Made By This Program"
                else:
                    pass
            else :
                cipher.append(" ")
                output = decipher(cipher)
  
            return output
            break
  
        except KeyError:
            print("ERROR 404: INVALID CIPHER ERROR")
            print()
            output = "|*| INVALID CIPHER ERROR !! \n|*| Enter A Valid Cipher Made By This Program"
            return output
            break
            
        except IndexError:
            print("ERROR 444 : NO ENTRY GIVEN")
            print()
            output = "|*| NO INPUT GIVEN TO PROGRAM !! \n|*| Enter A Cipher To Decode It."
            return output
            break


def adv_encode(arg):
    
    output = std_encode(arg)
    code_text  = list(output)

    output2 = level2(code_text)

    if output2 == '|*E| RORN  RONPI TSUIGI NE!V  \n!|*E| tenS mro TetxTe  EoocendIt ':
        output5 = '|*| ERROR NO INPUT IS GIVEN !! \n|*| Enter Some Text To Encode It.'
        print("ERROR 444 : NO ENTRY GIVEN")
        return output5
    else:
        
        return output2

def adv_decode(arg):

 
        while True:
            try:

  
                cipher = list(arg)
                if cipher[-1] == " ":

   
                    print("===============")
                    output4 = level3(cipher)

                    output = decipher(output4)
                    
                    return output
                    break
                else :
                    cipher.append(" ")
                    output4 = level3(cipher)
                    output = decipher(output4)
                    return output
                    break
                #break
            except KeyError :
                print("ERROR 404 : INVALID CIPHER ERROR")
                print()
                output = "|*| INVALID CIPHER ERROR !! \n|*| Enter A Valid Cipher Made By This Program"
                return output
                break
            except IndexError :
                print("ERROR 444 : NO ENTRY GIVEN")
                print()
                output = "|*| NO INPUT GIVEN TO PROGRAM !! \n|*| Enter A Cipher To Decode It."
                return output
                break

#==============================SECOND LEVEL DEFINATIONS===============================
            
#==============================FERNET DEFINATIONS START===============================

global bytekey
global bytehash

def byte_string(arg):
     
    #arg = barg

    sarg = str(arg)

    sarg = sarg[2:len(sarg)-1]

    return sarg

def byte_string_adv(arg):
    
    #arg = barg

    sarg = str(arg)

    sarg = sarg[2:len(sarg)-1]

    a = sarg.replace('\\n','\n')
    b = a.replace('\\a','\a')
    c = b.replace("\\'","'")
    d = c.replace('\\','\\')
    e = d.replace('\\t','    ')

    return e

def string_byte(arg):
   
    sarg = arg

    barg = bytes(sarg,'utf-8')

    return barg

def generate_key():

    global bytekey

    bkey = Fernet.generate_key()

    skey = byte_string(bkey)

    secretkey = adv_encode(skey)

    bytekey = bkey

    return secretkey

def generate_hash_secretkey(string , secretkey):

    global bytekey

    global bytehash

    skey = adv_decode(secretkey)

    bkey = string_byte(skey)

    bstring = string_byte(string)

    #bkey = bytekey

    f = Fernet(bkey)

    bhash = f.encrypt(bstring)

    bytehash = bhash

    shash = byte_string(bhash)

    secrethash = std_encode(shash)

    return secrethash

def decode_hash_secretkey(secrethash , secretkey):

    skey = adv_decode(secretkey)

    bkey = string_byte(skey)

    shash = std_decode(secrethash)

    bhash = string_byte(shash)

    f = Fernet(bkey)

    bstr = f.decrypt(bhash)

    sstr = byte_string_adv(bstr)

    return sstr

def generate_hash_bytekey(string , bytekey):
    
    #skey = adv_decode(secretkey)

    #bkey = string_byte(skey)

    bstring = string_byte(string)

    #bkey = bytekey

    f = Fernet(bytekey)

    bhash = f.encrypt(bstring)

    bytehash = bhash

    shash = byte_string(bhash)

    secrethash = std_encode(shash)

    return secrethash

def decode_hash_bytekey(secrethash , bytekey):

    #skey = adv_decode(key)

    #bkey = string_byte(skey)

    shash = std_decode(secrethash)

    bhash = string_byte(shash)

    f = Fernet(bytekey)

    bstr = f.decrypt(bhash)

    sstr = byte_string_adv(bstr)

    return sstr

    

#==============================FERNET DEFINATIONS END===============================

#==============================SECOND LAYER ENCRYPTION START========================

def second_encrypt_std_adv(string):

    std = std_encode(string)

    adv = adv_encode(std)

    return adv

def second_decrypt_std_adv(secretext):

    adv = adv_decode(secretext)

    std = std_decode(adv)

    return std

def second_encrypt_adv_std(string):

    adv = adv_encode(string)

    std = std_encode(adv)

    return std

def second_decrypt_adv_std(secrettext):

    std = std_decode(secrettext)

    adv = adv_decode(std)

    return adv

#==============================SECOND LAYER ENCRYPTION END==========================

#==============================CREATE & LOAD HASH KEY FILE==========================

def generate_keyfile(filename):

    bkey = Fernet.generate_key()

    skey = byte_string(bkey)

    secretkey = second_encrypt_std_adv(skey)

    filename1 = filename + '.key'

    ppath = f'{path}\\keys\\{filename1}'

    f = open(ppath,'w')

    f.truncate(00)

    f.seek(0,0)

    keyhash = str(hashlib.md5(bkey).hexdigest())
    keyhash2 = str(hashlib.sha512(bkey).hexdigest())
    
    #f.write(secretkey)
    keylist = [secretkey , keyhash]
    f.write(secretkey + '\n')
    #f.write('\n')
    f.write(keyhash)
    f.write(keyhash2)

    #f.writelines(keylist)
    
    f.close()

    exitstatus = f'The Key file is saved with name : {filename1} \n Saved In Location: \n {ppath}'

    return print(exitstatus)


def generate_keyfile_pathgiven(filename , givenpath):
    bkey = Fernet.generate_key()

    skey = byte_string(bkey)

    secretkey = second_encrypt_std_adv(skey)

    filename1 = filename + '.key'

    ppath = f'{givenpath}\\{filename1}'

    f = open(ppath, 'w')

    f.truncate(00)

    f.seek(0, 0)

    keyhash = str(hashlib.md5(bkey).hexdigest())
    keyhash2 = str(hashlib.sha512(bkey).hexdigest())

    # f.write(secretkey)
    keylist = [secretkey, keyhash]
    f.write(secretkey + '\n')
    # f.write('\n')
    f.write(keyhash)
    f.write(keyhash2)

    # f.writelines(keylist)

    f.close()

    exitstatus = f'The Key file is saved with name : {filename1} \n Saved In Location: \n {ppath}'

    return print(exitstatus)


def snipper(listvar):
    listvar1 = listvar[:len(listvar)-1]
    return listvar1

def verify(key , hash1 , hash2):
    #key = int(key)
    hash1 = str(hash1)          #md5 = hash1
    hash2 = str(hash2)          #sha512 = hash2

    a = str(hashlib.md5(key).hexdigest())
    aa = str(hashlib.sha512(key).hexdigest())
    b = hash1
    c = hash2

    if a == b :
        if aa == c :
            
            return True
        else:
            print('Hash 2 Incorrect . Failed Validitaing Key')
            return False
    elif aa == c :
        if a == b :

            return True
        else:
            print('Hash 1 Incorrect . Failed Validitaing Key')
            return False
    else:
        return False


def load_keyfile(keyfile):
    keyfile = str(keyfile)
    filename = keyfile + '.key'

    ppath = f'{path}\\keys\\{filename}'

    #print(ppath)

    #FileNotFound = True

    #FileNotFound = False
            
    
    while True:
        try:
            
            f = open(ppath,'r')
            f.seek(0,0)
            sys = f.readlines()
            a = sys[0]
            b = sys[1]
            #print('b :',len(b))
            md5 = b[:len(b)-128]
            #print('md5 :',len(md5))
            #print(md5)
            #print(type(md5))
            sha = b[32:]
            #print('sha :',len(sha))
            #print(sha)
            #print(type(sha))
            readyhash = snipper(a)
            skey = second_decrypt_std_adv(readyhash)
            bkey = string_byte(skey)
            #print('bkey :',bkey)
            #ikey = int(bkey)
            verification = verify(bkey , md5 , sha)
            exitss = "Your Key Does Not Match With Hash. Your Key Is Tampered."
            if verification:
                return bkey
                break
            else:
                print(exitss)
                return True
                break

        except FileNotFoundError:
            
            #FileNotFound = True
            print("File Not Found. Please Give path.\n Keys Are Stored In Root Directory in Sub-Directory keys\n Also your Key file not in current working directory.")
            print("Your Current Directory Is : \n",path)
            return True
            break


def load_keyfile_path(keyfile):
    keyfile = str(keyfile)
    #filename = keyfile + '.key'

    ppath = keyfile

    # print(ppath)

    # FileNotFound = True

    # FileNotFound = False

    while True:
        try:

            f = open(ppath, 'r')
            f.seek(0, 0)
            sys = f.readlines()
            a = sys[0]
            b = sys[1]
            # print('b :',len(b))
            md5 = b[:len(b) - 128]
            # print('md5 :',len(md5))
            # print(md5)
            # print(type(md5))
            sha = b[32:]
            # print('sha :',len(sha))
            # print(sha)
            # print(type(sha))
            readyhash = snipper(a)
            skey = second_decrypt_std_adv(readyhash)
            bkey = string_byte(skey)
            # print('bkey :',bkey)
            # ikey = int(bkey)
            verification = verify(bkey, md5, sha)
            exitss = "Your Key Does Not Match With Hash. Your Key Is Tampered."
            if verification:
                return bkey
                break
            else:
                print(exitss)
                return True
                break

        except FileNotFoundError:

            # FileNotFound = True
            print(
                "File Not Found. Please Give path.\n Keys Are Stored In Root Directory in Sub-Directory keys\n Also your Key file not in current working directory.")
            print("Your Current Directory Is : \n", path)
            return True
            break

def load_keyfile_path(keyfile):
    keyfile = str(keyfile)
    #filename = keyfile + '.key'

    ppath = keyfile

    # print(ppath)

    # FileNotFound = True

    # FileNotFound = False

    while True:
        try:

            f = open(ppath, 'r')
            f.seek(0, 0)
            sys = f.readlines()
            a = sys[0]
            b = sys[1]
            # print('b :',len(b))
            md5 = b[:len(b) - 128]
            # print('md5 :',len(md5))
            # print(md5)
            # print(type(md5))
            sha = b[32:]
            # print('sha :',len(sha))
            # print(sha)
            # print(type(sha))
            readyhash = snipper(a)
            skey = second_decrypt_std_adv(readyhash)
            bkey = string_byte(skey)
            # print('bkey :',bkey)
            # ikey = int(bkey)
            verification = verify(bkey, md5, sha)
            exitss = "Your Key Does Not Match With Hash. Your Key Is Tampered."
            if verification:
                return bkey
                break
            else:
                print(exitss)
                return True
                break

        except FileNotFoundError:

            # FileNotFound = True
            print(
                "File Not Found. Please Give path.\n Keys Are Stored In Root Directory in Sub-Directory keys\n Also your Key file not in current working directory.")
            print("Your Current Directory Is : \n", path)
            return True
            break


#==============================CREATE & LOAD HASH KEY FILE==========================

#==============================CREATE & LOAD HASH FILE==========================

def generate_hashfile(hashfilename , string , keyfile):

    string = str(string)

    hashfilename = str(hashfilename)

    key = load_keyfile(keyfile)

    filename1 = hashfilename + '.hash'

    ppath = f'{path}\\hash\\{filename1}'

    if key == True:

        print('Invalid Key Error or  Key file Tampred')

        pass

    else:

        hashh = generate_hash_bytekey(string , key)

        f = open(ppath , 'w')

        f.write(hashh)

        f.close()

        exitstatus = print(f'The hash file is saved with name : {filename1} \n Saved In Location: \n {ppath}')

        print(exitstatus)

def generate_hashfile_pathgiven(hashfilename , string , keyfile , path):

    string = str(string)

    hashfilename = str(hashfilename)

    poo = str(path)

    key = load_keyfile_path(keyfile)

    filename1 = hashfilename + '.hash'

    #ppath = f'{path}\\hash\\{filename1}'
    ppath = f'{poo}\\{filename1}'

    if key == True:

        print('Invalid Key Error or  Key file Tampred')

        pass

    else:

        hashh = generate_hash_bytekey(string , key)

        f = open(ppath , 'w')

        f.write(hashh)

        f.close()

        exitstatus = print(f'The hash file is saved with name : {filename1} \n Saved In Location: \n {ppath}')

        print(exitstatus)


def load_hashfile(filename , keyfile):

    filename1 = filename + '.hash'
    ppath = f'{path}\\hash\\{filename1}'

    key = load_keyfile(keyfile)

    if key == True:
        print('Invalid Key Error or  Key file Tampred')
        return KeyError
        pass

    else:

        while True :
            try:

                f = open(ppath,'r')
                hashh = f.read()

                string = decode_hash_bytekey(hashh , key)

                return string
                break
            except FileNotFoundError:
                
                #FileNotFound = True
                print("File Not Found. Please Give path.\n Keys Are Stored In Root Directory in Sub-Directory keys\n Also your Key file not in current working directory.")
                print("Your Current Directory Is : \n",path)
                return FileNotFoundError
                break


def load_hashfile_path(filename, keyfile):
    #filename1 = filename + '.hash'
    #ppath = f'{path}\\hash\\{filename1}'

    ppath = str(filename)

    key = load_keyfile_path(keyfile)

    if key == True:
        print('Invalid Key Error or  Key file Tampred')
        return KeyError
        pass

    else:

        while True:
            try:

                f = open(ppath, 'r')
                hashh = f.read()

                string = decode_hash_bytekey(hashh, key)

                return string
                break
            except FileNotFoundError:

                # FileNotFound = True
                print(
                    "File Not Found. Please Give path.\n Keys Are Stored In Root Directory in Sub-Directory keys\n Also your Key file not in current working directory.")
                print("Your Current Directory Is : \n", path)
                return FileNotFoundError
                break


#==============================CREATE & LOAD ZIP FILES=============================


def generate_zip(zipname , keyfile , hashfile):

    filename1 = zipname + '.ZipHash'
    keyfile1 = keyfile + '.key'
    hashfile1 = hashfile + '.hash'

    shutil.move(f'{path}\\keys\\{keyfile1}' , f'{path}\\temp')
    shutil.move(f'{path}\\hash\\{hashfile1}' , f'{path}\\temp')
    
    ppath = f'{path}\\zip\\{filename1}' 
    z = ZipFile(f'{path}\\temp\\{filename1}' , 'w')

    os.chdir(f'{path}\\temp')
    
    keypath = f'{path}\\keys\\{keyfile1}'
    hashpath = f'{path}\\hash\\{hashfile1}'

    z.write(keyfile1)
    z.write(hashfile1)

    z.close()

    shutil.move(f'{path}\\temp\\{keyfile1}',f'{path}\\keys')
    shutil.move(f'{path}\\temp\\{hashfile1}' , f'{path}\\hash')
    shutil.move(f'{path}\\temp\\{filename1}' , f'{path}\\zip')

    os.chdir(path)

    exitstatus = print(f'The ZIP file is saved with name : {filename1} \n Saved In Location: \n {ppath}')

    return exitstatus


def generate_zip_path(zipname, keyfile, hashfile , zippath):

    zipname = str(zipname)
    zippath = str(zippath)
    keyp = str(keyfile)
    hashp = str(hashfile)
    zipfile = f'{zipname}.ZipHash'
    zippath = f'{zippath}\\{zipfile}'


    keyy = keyp.split("\\")
    keyname = keyy[-1]

    hashh = hashp.split("\\")
    hashname = hashh[-1]

    Z = ZipFile(zippath,'w')

    Z.write(keyp,arcname=keyname)
    Z.write(hashp,arcname=hashname)

    Z.close()

    while True:
        try:
            z = ZipFile(zippath,'r')
            aa = z.namelist()

            if aa[0] == keyname:
                if aa[1] == hashname:
                    return True
                else:
                    print('2nd name not match')
                    return False
            else:
                print('1st name not match')
                return False

        except FileNotFoundError:
            print('File Not Found')
            return False
    

def load_zip_path(zippath,keypath,hashpath):

    zippath = str(zippath)
    keypath = str(keypath)
    hashpath = str(hashpath)
    
            
    Z = ZipFile(zippath,'r')

    namelist = Z.namelist()

    keyname = namelist[0]

    hashname = namelist[1]

    Z.extract(keyname , path=keypath)
    Z.extract(hashname , path=hashpath)

    finalkey = f'{keypath}\\{keyname}'
    finalhash = f'{hashpath}\\{hashname}'

    while True:
        try:

            f = open(finalkey , 'r')
            f.close()
            print('KEYFILE > OK')
            F = open(finalhash,'r')
            F.close()
            print('HASHFILE > OK')
            return True

        except FileNotFoundError:
            return False



    

def load_zip(zipname):
    ziplist = []

    filename1 = zipname + '.ZipHash'

    ppath = f'{path}\\zip\\{filename1}'

    z = ZipFile(ppath , 'r')

    print("The Contentes Of This Zip Files Are :")
    
    ziplist = z.namelist()
    print(f' 1) {ziplist[0]} \n 2) {ziplist[1]}')
    z.close()
    shutil.move(f'{path}\\zip\\{filename1}' , f'{path}\\temp\\{filename1}')
    #time.sleep(3)
    os.chdir(f'{path}\\temp')
    #time.sleep(3)

    z = ZipFile(f'{path}\\temp\\{filename1}' , 'r')
    
    z.extractall()
    z.close()
    #time.sleep(3)
    shutil.move(f'{path}\\temp\\{ziplist[0]}' , f'{path}\\keys')
    shutil.move(f'{path}\\temp\\{ziplist[1]}' , f'{path}\\hash')
    shutil.move(f'{path}\\temp\\{filename1}' , f'{path}\\zip')
                
    exitstatus = f'All Files are extracted. They are as follows \n1) {ziplist[0]} saved at {path}\\keys\\{ziplist[0]}\n2){ziplist[1]} saved at {path}\\hash\\{ziplist[1]}'

    return print(exitstatus)

#==============================ZIP & LOAD FILES=================================

#==============================AUTOMATE ZIPPING=================================

def auto_create_zip(zipname , string):

    mastername = str(zipname)
    string = str(string)
    
    #Generate keyfile :

    print('Generating Keyfile...')

    keyname = f'{zipname}keyfile'

    generate_keyfile(keyname)

    #Load keyfile:

    print('Loading Keyfile...')

    key = load_keyfile(keyname)

    #Generate hashfile:

    print('Generating Hashfile...')

    hashname = f'{zipname}hashfile'

    generate_hashfile(hashname , string , keyname)

    #Generate zipfile :

    print('Compressing Keyfile and Hashfile to ZipHash file...')

    generate_zip(mastername , keyname , hashname)

    
    return print('ZIPHASH File Created Successfully !!')


def auto_load_zip(zipname):
    mastername = str(zipname)
    filename1 = zipname + '.ZipHash'
    ppath = f'{path}\\zip\\{filename1}'
    
    while True :
        try:
                 
            #Extract zip :
            
            z = ZipFile(ppath , 'r')

            print("The Contents Of This Zip Files Are :")
            
            ziplist = z.namelist()
            print(f' 1) {ziplist[0]} \n 2) {ziplist[1]}')
            z.close()

            print('Extracting Files...')
            
            shutil.move(f'{path}\\zip\\{filename1}' , f'{path}\\temp\\{filename1}')
            time.sleep(3)
            os.chdir(f'{path}\\temp')
            time.sleep(3)

            z = ZipFile(f'{path}\\temp\\{filename1}' , 'r')
            
            z.extractall()
            z.close()
            time.sleep(3)

            while True:
                try:
                    
                    shutil.move(f'{path}\\temp\\{ziplist[0]}' , f'{path}\\keys')
                    break
                except shutil.Error:
                    os.remove(f'{path}\\temp\\{ziplist[0]}')
                    break

            while True:
                try:
                    
                    shutil.move(f'{path}\\temp\\{ziplist[1]}' , f'{path}\\hash')
                    break
                except shutil.Error:
                    os.remove(f'{path}\\temp\\{ziplist[1]}')
                    break
                
            while True:
                try:
                    
                    shutil.move(f'{path}\\temp\\{filename1}' , f'{path}\\zip')
                    break
                except shutil.Error:
                    os.remove(f'{path}\\temp\\{filename1}')
                    break



                
            keyfilezip = ziplist[0][:-4]
            print(f'The key : {ziplist[0]}')

            hashfilezip = ziplist[1][:-5]
            print(f'The key : {ziplist[1]}')

            #Load keyfile :
            print('Validating Key Hash...')
            key = load_keyfile(keyfilezip)

            #print(key)

            
            print('Decoding Hash with Key...')

            #Load hashfile :

            string = load_hashfile(hashfilezip , keyfilezip)

            #Return string obtained :

            print('Your Text Retrieved From .ZipHash File Is : ')
            print()

            return string
            break

        except FileNotFoundError :
            print("The .ZipHash File is not in The 'zip' Directory.")
            print('Please Place The .ZipHash file in the following path: ')
            print(ppath)
            print('Check For Any Name Spelling Errors if any...')
            break

            
            
#==============================AUTOMATE ZIPPING=================================

#==============================INFLATE SIZE=====================================



def inflatesize(data , inflatesize):
    sdata = str(data)
    size = int(inflatesize)
    start = time.time()
    while True:
        try:
            
            if size > 7:
                print('Max. Inflate Size Is 7')
                return False
            else:
        
                rawdata = sdata
                processeddata = ""
                for i in range(size):
        
                    a = std_encode(rawdata)
                    rawdata = a
                    print(f'Number Of Times Encoded Text : {i+1}')
                    #print(a)
                else:
                    return rawdata
                    break
        except KeyboardInterrupt:
            return rawdata
            break

def deflatesize(cipher , deflatesize):
    scipher = str(cipher)
    size = int(deflatesize)

    if size > 7:
        print('Max. Deflate Size is 7')
        return False
    else:
        rawdata = scipher
        processeddata = ""
        while True:
            try:
                
                for i in range(size):

                    a = std_decode(rawdata)
                    if a == "|*| INVALID CIPHER ERROR !! \n|*| Enter A Valid Cipher Made By This Program" :
                        return rawdata
                    else:
                    
                        rawdata = a
                        print(f'Number Of Times Decoded Text : {i+1}')
                    
                else:
                        return rawdata
            except KeyError:
                print('Returned An Error While Processing !!\nGiving Last Decoded Text')
                return rawdata

#==============================INFLATE SIZE=====================================



#=====================================END!!=====================================


#FOR DEBUGGING AND TEST ONLY !!!
#import Shahils_secret_text as sc
