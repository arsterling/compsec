import etherscan
import sys
import hashlib
from const import *

def normalize(b):
    return b.replace(b'\r\n', b'\n').replace(b' ', b'').strip() #.replace(b'\n', b'') ?

eth = etherscan.Etherscan(API_KEY, net="ropsten")
with open(sys.argv[1], "rb") as f:
    byte_file = f.read()
    with open(sys.argv[2]) as contract:
        contract_source = contract.read().strip()
        res = eth.get_contract_source_code(contract_source)

        remix_source = normalize(res[0]['SourceCode'].encode('utf-8'))
        provided_source = normalize(byte_file)

        remix_hash = hashlib.sha256(remix_source).hexdigest()
        provided_hash = hashlib.sha256(provided_source).hexdigest()

        if(remix_hash == provided_hash):
            print("passed")
        else:
            print("source code of contract at " + contract_source + "and attack.sol dont match")
            print('Remix: (%s)\n%s' % (remix_hash, remix_source))
            print('==============================')
            print('attack.sol: (%s)\n%s' % (provided_hash, provided_source))
