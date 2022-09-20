from pymd5 import md5
from random import getrandbits

def main():
    j = 0
    string = "'='"
    final_string = ""
    for k in string:
        final_string += hex(ord(k))[2:]
    print(final_string)
    while(True):
        temp = getrandbits(64)
        if(j % 1000000 == 0):
            print(temp)
        h = md5()
        h.update(str(temp))
        if(h.hexdigest()[0:6] == final_string[0:6]):
            print("Voila~!")
            print(temp)
            return
        j += 1


if __name__ == '__main__':
    main()
