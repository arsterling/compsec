from scapy.all import *
import sys

ipDict = dict()

# Complete this function!
def process_pcap(pcap_fname):
    for pkt in PcapReader(pcap_fname):
        # Your code here

        #ignore if not using IP
        if not pkt.haslayer(IP):
            continue

        #ignore if not using Ether
        if not pkt.haslayer(Ether):
            continue

        #ignore if not using TCP
        if not pkt.haslayer(TCP):
            continue

        #if SYN then put IP source into ipDict, if already in ipDict, increment S value (S = SYN)
        if pkt['TCP'].flags == 'S':
            if pkt['IP'].src not in ipDict:
                ipDict[pkt['IP'].src] = {'S' : 0, 'SA' : 0}
            ipDict[pkt['IP'].src]['S'] += 1
        #if SYN+ACK then put IP destination into ipDict, if already in ipDict, increment SA value (SA = SYN+ACK)
        elif pkt['TCP'].flags == 'SA':
            if pkt['IP'].dst not in ipDict:
                ipDict[pkt['IP'].dst] = {'S' : 0, 'SA' : 0}
            ipDict[pkt['IP'].dst]['SA'] += 1
    #go through ipDict to find when SYN packets are more than 3 times SYN+ACK then print the IP address
    for ip in ipDict.keys():
            if ipDict[ip]['S'] > (ipDict[ip]['SA']*3):
                print(ip)

if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Use: python3 detector.py file.pcap')
        sys.exit(-1)
    process_pcap(sys.argv[1])
    
