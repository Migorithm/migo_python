import socket
import json
import base64
import sys
import ssl
#  HTTP is based on TCP, and TCP is based on IP. This means HTTP is stream-oriented(TCP) and wants an IP address to work(IP)
#  Those requirements are fulfilled by picking
#   -  AF_INET for socket family 
#   - SOCK_STREAM for socket type

context =ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    # We have now a working socket object configured for HTTP transmission. This type of socket is also known as stream socket.

    #For TLS
    sock = ssl.wrap_socket(sock,keyfile=None,certfile=None,server_side=False,cert_reqs=ssl.CERT_NONE,ssl_version=ssl.PROTOCOL_SSLv23)
    sock.settimeout(3)

    # The next step is to choose a web address to connect t

    sock.connect((sys.argv[1],9200))

# We have now a working socket object configured for HTTP transmission. This type of socket is also known as stream socket.


# Sending data to the server
#
#  An HTTP communication always starts with a request made by the client (i.e. us!) with the page we want to obtain,
#  followed by some additional information. Such request is sent as a normal text string and looks like this:
    path = '/_cluster/health'
    host = sys.argv[1]
    token = base64.b64encode(sys.argv[2].encode("ascii"))
    lines = [
        'GET %s HTTP/1.1' % path,
        'Host: %s' % host,
        'Authorization: Basic %s' % token.decode(),
    ]

#sock.send(b"GET / HTTP/1.1\r\nContent-Type: application/json\r\nHost:10.107.11.66\r\n\r\n")
    sock.send(("\r\n".join(lines) + "\r\n\r\n").encode())

    response=sock.recv(4096).decode()

    separator = response.index("{")
    result = json.loads(response[separator:])

    print(result)




