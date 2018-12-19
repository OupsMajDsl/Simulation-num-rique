from string import ascii_lowercase
from unidecode import unidecode
import projet2_1 as rand_gen

class Vernam: #vernam2.0
    
    def __init__(self, key):
        self.table         = {letters : index for index, letters in enumerate(' ' + ascii_lowercase, start = 0)}
        self.reverse_table = {letters : index for letters, index in enumerate(' ' + ascii_lowercase, start = 0)}
        self.key           = [self.table[letter] for letter in key if letter in self.table]

    def encrypt(self, msg, keygen = False):
        if keygen:
            key      = rand_gen.key(len(msg))
            self.key = [self.table[letter] for letter in key if letter in self.table]
        msg  = unidecode(msg)
        char = [self.table[letter] for letter in msg if letter in self.table]
        for i in range(len(char)):
            if len(self.key) == len(char):
                if char[i] != 0:
                    char[i] += self.key[i]
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
            if len(self.key) == len(char):
                if char[i] != 0:
                    char[i] -= self.key[i]
                    if char[i] < 0:
                        char[i] += 26
            else: 
                print("Les longueurs de la clé et du message à encrypter doivent être identiques")
                break
        char = [self.reverse_table[nb] for nb in char if nb in self.reverse_table]
        msg = ''.join(char[i] for i in range(len(char)))
        return msg
        

        
if __name__ == "__main__":
    test = Vernam('ibchntmaqf')
    crypt = test.encrypt('helloworld', keygen = True)
    print(crypt)
#    decrypt = test.decrypt('qgotcqbscj')
#    print(decrypt)



# class Vernam1: #vernam1.0
    
#     def __init__(self, key):
#         self.table         = {letters : index for index, letters in enumerate(' ' + ascii_lowercase, start = 0)}
#         self.reverse_table = {letters : index for letters, index in enumerate(' ' + ascii_lowercase, start = 0)}
#         self.key           = [self.table[letter] for letter in key if letter in self.table]

#     def encrypt(self, msg):
#         msg  = unidecode(msg)
#         char = [self.table[letter] for letter in msg if letter in self.table]
#         for i in range(len(char)):
#             if len(self.key) == len(char):
#                 if char[i] != 0:
#                     char[i] += self.key[i]
#                     if char[i] > 26:
#                         char[i] -= 26
#             else: 
#                 print("Les longueurs de la clé et du message à encrypter doivent être identiques")
#                 break
#         char = [self.reverse_table[nb] for nb in char if nb in self.reverse_table]
#         enc_msg = ''.join(char[i] for i in range(len(char)))
#         return enc_msg
                    
#     def decrypt(self, enc_msg):
#         enc_msg  = unidecode(enc_msg)
#         char     = [self.table[letter] for letter in enc_msg if letter in self.table]
#         for i in range(len(char)):
#             if len(self.key) == len(char):
#                 if char[i] != 0:
#                     char[i] -= self.key[i]
#                     if char[i] < 0:
#                         char[i] += 26
#             else: 
#                 print("Les longueurs de la clé et du message à encrypter doivent être identiques")
#                 break
#         char = [self.reverse_table[nb] for nb in char if nb in self.reverse_table]
#         msg = ''.join(char[i] for i in range(len(char)))
#         return msg