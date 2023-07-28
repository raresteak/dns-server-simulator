# dns-server-simulator
Python 3 implementation of a dns server.  Responds with random ip address


Usage(server)
```
$ python3 ./dns_server_simulator.py
```


Usage(client)
```
$ dig @127.0.0.1 -p 7753 foo.bar.com +short
10.12.28.17
```
