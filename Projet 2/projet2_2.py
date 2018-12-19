romnum_dict = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), 
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def arabic2roman(num):
    roman = ''
    while num > 0:
        for nb, rom in romnum_dict:
            while num >= nb:
                num -= nb
                roman += rom
    return roman

def roman2arabic(roman):
    roman = list(roman)
    num   = []
    for n in range(len(roman)):
        for nb, rom in romnum_dict:
            if rom in roman[n]:
                num.append(nb)
                if num[n] > num[n - 1]:
                    num[n - 1] -= 2*num[n-1]
    return sum(num)


if __name__ == "__main__":
    print(arabic2roman(4999))
    print(roman2arabic('MMMMCMXCIX'))
    print(roman2arabic('MMDXCVII'))
    print(roman2arabic('MMMMMDXCVII'))
    print(roman2arabic('CMXCIX'))