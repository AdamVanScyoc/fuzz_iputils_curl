import socket
import sys

PING_TARGET="::1"

source_ip = "::1"
addresses = [addr for addr in socket.getaddrinfo(source_ip, None) if socket.AF_INET6 == addr[0]]
src_address = addresses[0][-1][0]
print("Source addr: " +repr(src_address))

# A minimal ICMP6-echo message
#data = b'\x80\0\0\0\0\0\0\0'

data = open("./crash1", "rb").read()

sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW, socket.getprotobyname('ipv6-icmp'))
#sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW, socket.getprotobyname('ipv6'))
sock.bind((src_address, 0))
sent = sock.sendto(data, (PING_TARGET, 0, 0, 0))
print("send: " + repr(sent))

receive = sock.recv(65536, 0)
#receive = sock.recv(9, 0)
print("recv: " + str(receive))

data = open("./id:000001,sig:11,src:000004,time:23071,op:arith8,pos:0,val:+17", "rb").read()
sent = sock.sendto(data, (PING_TARGET, 0, 0, 0))
print("send: " + repr(sent))

sock.close()
