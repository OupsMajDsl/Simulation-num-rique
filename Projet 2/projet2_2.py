#def arabic2roman(nb):
#    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#    numbers = numbers[::-1]
#    romans  = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
#    romans = romans[::-1]
#    i = 0
#    nb_rom  = ""
#    while  nb > 0:
#        for j in range(nb // numbers[i]):           #compte le nombre de chaque élément du type i dans nb
#            nb_rom += romans[i]
#            nb -= numbers[i]
#        i += 1
#    return nb_rom

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


if __name__ == "__main__":
    print(arabic2roman(4999))
    print(roman2arabic('MMMMCMXCIX'))
    print(roman2arabic('MMDXCVII'))
    print(roman2arabic('MMMMMDXCVII'))
    print(roman2arabic('CMXCIX'))
