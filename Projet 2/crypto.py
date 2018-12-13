import random
from string import ascii_lowercase
from unidecode import unidecode

def key(nb):
    return ''.join(random.choice(ascii_lowercase) for i in range(nb))


romnum_dict = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), 
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}     

def arabic2roman(num):
    roman = ''
    while num > 0:
        for nb, rom in romnum_dict:
            while num >= nb:
                num -= nb
                roman += rom
    return roman

def roman2arabic(roman):
    num = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and rom_dict[roman[i]] < rom_dict[roman[i + 1]]:
            num -= rom_dict[roman[i]]
        else:
            num += rom_dict[roman[i]]
    return num

def ROT13(txt, n = 13, way = 'encrypt'):
    output_string = ''
    txt = unidecode(txt)
    if n > 26 or n < 1:
        print("La valeur de n est invalide")
    else:
        for i in range(len(txt)):
            char = ord(txt[i].lower())
            if char != 32:                  #gestion des espaces
                if way == 'encrypt':
                    char += n
                elif way == 'decrypt':
                    char -= n
                if char > 122:              #z --> 122
                    char -= 26
                elif char < 97:             #a --> 97  
                    char += 26
            output_string += chr(char)
        print(output_string)
        
        
class Vernam:
    
    def __init__(self, cle):
        self.table         = {letters : index for index, letters in enumerate(' ' + ascii_lowercase, start = 0)}
        self.reverse_table = {letters : index for letters, index in enumerate(' ' + ascii_lowercase, start = 0)}
        self.cle           = [self.table[letter] for letter in cle if letter in self.table]

    def encrypt(self, msg, keygen = False):
        if keygen:
            cle      = key(len(msg))
            self.cle = [self.table[letter] for letter in cle if letter in self.table]
        msg  = unidecode(msg)
        char = [self.table[letter] for letter in msg if letter in self.table]
        for i in range(len(char)):
            if len(self.cle) == len(char):
                if char[i] != 0:
                    char[i] += self.cle[i]
                    if char[i] > 26:
                        char[i] -= 26
            else: 
                print("Les longueurs de la clé et du message à encrypter doivent être identiques")
                break
        char = [self.reverse_table[nb] for nb in char if nb in self.reverse_table]
        enc_msg = ''.join(char[i] for i in range(len(char)))
        return enc_msg
                    
    def decrypt(self, enc_msg):
        enc_msg  = unidecode(enc_msg)
        char     = [self.table[letter] for letter in enc_msg if letter in self.table]
        for i in range(len(char)):
            if len(self.cle) == len(char):
                if char[i] != 0:
                    char[i] -= self.cle[i]
                    if char[i] < 0:
                        char[i] += 26
            else: 
                print("Les longueurs de la clé et du message à encrypter doivent être identiques")
                break
        char = [self.reverse_table[nb] for nb in char if nb in self.reverse_table]
        msg = ''.join(char[i] for i in range(len(char)))
        return msg