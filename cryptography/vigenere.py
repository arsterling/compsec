#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Given function
def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

#Use this function to get an idea of the pop var for an independent caesar cipher.
def CaesarPopVar(cipher, key):
    CaesarIndex = 0
    Caesars = []
    i = 0
    #Take the cipher and break it up into chunks less than the key length.
    while CaesarIndex < key:
        Independent = ""
        while(i+CaesarIndex < len(cipher)):
            Independent += cipher[i+CaesarIndex]
            i += key
        i = 0
        #Now put it all together
        Caesars.append(Independent)
        CaesarIndex += 1
    return sum(pop_var(Independent) for Independent in Caesars)/key

#Use this function to determine the frequency at which letters occur and if it resembles an English phrase.
def FindLetterFreqs(s):
    English = True
    DecryptedFreqs = Counter(s)
    DifferentSum = 0
    #Determine how different the decrytped letter frequencies are from the letter frequencies in the english language.
    for letter in letter_freqs:
        DifferentSum += abs((DecryptedFreqs[letter]/len(s)) - letter_freqs[letter])
    #Averaging the findings against the total length of the alphabet
    DifferentAvg = DifferentSum/26
    #Figure out if the average is in an appropriate range.
    English = (DifferentAvg < 0.025)
    return English

#Figure out what the appropriate shift is for each caesar cipher (and potentially for the entire cipher if it works out)
def CaesarDecoder(key, s):
    #Decode the shift for a given block given key length.
    Decoded = list(s)
    i = 0
    shift = alphabet.index(key)
    while(i < len(s)):
        Decoded[i] = alphabet[(alphabet.index(s[i]) + 26 - shift)%26]
        i += 1
    return "".join(Decoded)

#Primary function used to figure out the key.
def KeyFinder(cipher, KeyLen):
    Caesars = []
    CaesarIndex = 0
    i = 0
    #Breaking everything up into chunks from the size of the key length to the max 
    while CaesarIndex < KeyLen:
        Indpendent = ""
        while(i+CaesarIndex < len(cipher)):
            Indpendent += cipher[i+CaesarIndex]
            i += KeyLen
        i = 0
        Caesars.append(Indpendent)
        CaesarIndex += 1
    CaesarIndex = 0
    key = list("")

    for Indpendent in Caesars:
        for letter in alphabet:
            if(FindLetterFreqs(CaesarDecoder(letter, Indpendent))): 
                key.append(letter)
                break
        CaesarIndex += 1
    return key

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case

    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    #################################################################

    # Your code to determine the key and decrypt the ciphertext here

    KeyLen = 2
    #Use this loop to repeatedly break up the cipher into blocks to try different keys.
    while(KeyLen <= 13):
        #Evaluate the individual caesar cipher pop var; if the popvar is greater than .001 (from english letter pop var), then this is most likely the key
        if(CaesarPopVar(cipher, KeyLen) >= 0.001): break
        KeyLen += 1
    print("".join(KeyFinder(cipher, KeyLen)))