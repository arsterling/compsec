#!/usr/bin/python3

import requests
import sys

def check(oracle_url, ciphertext):
    r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(ciphertext).hex()))
    r.raise_for_status()
    obj = r.json()
    # print(obj)
    return obj

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: %s ORACLE_URL CIPHERTEXT_HEX" % (sys.argv[0]), file=sys.stderr)
        sys.exit(-1)
    oracle_url = sys.argv[1]
    ciphertext = sys.argv[2]


    # Example check of ciphertext at the oracle URL:
    r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(ciphertext).hex()))
    r.raise_for_status()
    obj = r.json()
    print(obj)
    print(obj['status'])

    cnt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    split = []

    for index in range(0, len(ciphertext),2):
        split.append(ciphertext[index:index+2])
    
    print(split)
    for index,n in enumerate(split):

        last_byte = ciphertext.strip()[-index:]
        stripped = ciphertext[:-index]
        for i in cnt:
            for j in cnt:
                attack = i + j
                manipulated = stripped + attack
                # print(attack)
                obj = check(oracle_url, manipulated)
                obj_stat = obj['status']
                print(obj_stat)
                if (obj_stat == 'invalid_mac'):
                    zeroOne = cnt[0]+cnt[1]
                    c_lastByte = int(attack,16) ^ int(zeroOne,16)
                    pad = int(c_lastByte,16) ^ int(last_byte,16)
