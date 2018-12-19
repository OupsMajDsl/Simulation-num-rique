import random, string

def key(nb):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(nb))

if __name__ == "__main__":
    for i in range(15):
        print(key(15))