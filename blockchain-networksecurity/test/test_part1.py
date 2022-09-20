import etherscan
import sys
import json
from const import *
from datetime import datetime

WEI_PER_ETH = float(10**18)

eth = etherscan.Etherscan(API_KEY, net="ropsten")
with open(sys.argv[1]) as f:
    student_addr = str(f.read().strip().lower())
    
    res = eth.get_internal_txs_by_address(student_addr, 10308757, 'latest', 'desc')

    from_contract = list(filter(lambda x: x['from'] == CONTRACT.lower() and x['to'] == student_addr, res))
    to_contract = [obj for obj in res if (obj['from'] == student_addr and obj['to'] == CONTRACT.lower())]

    sum_in = 0
    for i in range(len(to_contract)):
        sum_in += int(to_contract[i]['value'])
    sum_out = 0
    for j in range(len(from_contract)):
        sum_out += int(from_contract[j]['value'])

    if sum_out > sum_in:
        print("passed")
    else:
        print("amount receieved is not greater than amount sent")
        print('In: %.6f Rop' % (float(sum_in)/WEI_PER_ETH))
        print('Out: %.6f Rop' % (float(sum_out)/WEI_PER_ETH))
        blocks = [int(x['blockNumber']) for x in res]
        times = [int(x['timeStamp']) for x in res]

        print('Searched blocks %d - %d' % (min(blocks), max(blocks)))
        print('(oldest block: %s)' % (datetime.utcfromtimestamp(min(times)).strftime('%Y-%m-%d %H:%M:%S')))
        #print(json.dumps(res))

