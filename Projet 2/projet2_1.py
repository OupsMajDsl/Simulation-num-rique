import random, string

def key(nb):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(nb))

def key_dev(nb):
    char = ''
    for i in range(nb):
        char = char + random.choice(string.ascii_lowercase) 
    return char

def key2(nb):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(nb))

if __name__ == "__main__":
    for i in range(15):
        print(key(15))
    print(5* '-')
    for i in range(15):
        print(key2(15))
    print(key_dev(20))