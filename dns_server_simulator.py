#!/usr/bin/env python3
import dnslib
import socket
import random
import time

# generate random IP from 10.0.0.0/8 range
def random_ip():
    return "10." + ".".join(str(random.randint(0, 255)) for _ in range(3))

def log_request(source, request, response):
    with open("dns.log", "a") as f:
        f.write(f"{time.asctime()} {source} {request} {response}\n")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# change the port below in sock.bind
sock.bind(("0.0.0.0", 7753))

while True:
    data, addr = sock.recvfrom(1024)
    request = dnslib.DNSRecord.parse(data)
    response = dnslib.DNSRecord(dnslib.DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
    response.add_answer(dnslib.RR(request.q.qname, dnslib.QTYPE.A, rdata=dnslib.A(random_ip())))
    sock.sendto(response.pack(), addr)
    log_request(addr[0], request.q.qname, response.a.rdata)
