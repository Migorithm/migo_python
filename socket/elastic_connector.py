import socket
import json
import base64
import time
from typing import List, Optional,Tuple,Union,Mapping
import random
from contextlib import contextmanager
from pprint import pprint
from functools import wraps

class Custom_Elasticsearch:
    def __new__(cls,hosts:Union[str, List[Union[str,Mapping[str,str]]]] =None, http_auth:Optional[Tuple[str,str]] = None) -> "Custom_Elasticsearch": 
        if hosts is None:
            raise ValueError("hosts must be specified")
        cls._hosts = hosts
        if isinstance(cls._hosts,str):
            ip, port = cls._hosts.split(":")
            cls._ip = ip
            cls._port = port
        if isinstance(cls._hosts,list):
            ip,port = random.choice(cls._hosts).split(":")
            cls._ip = ip
            cls._port=port
        cls._http_auth=http_auth
        return cls
        
    
    @classmethod
    @contextmanager
    def connector(cls):
        try :
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
                sock.settimeout(3)
                sock.connect((cls._ip,int(cls._port)))
                yield sock
        finally:
            sock.close()
    
    
    class path_decorator:
        def __init__(self,func):
            self.func=func
        
        def __call__(self,*args,**kwargs):
            lines = self.func(*args,**kwargs)
            with Custom_Elasticsearch.connector() as con: #As it's classmethod, you can call connector this way.
                # Make the socket non-blocking. 
                # By doing this, the socket won't wait if there is no data in recv calls.
                # It will continue if there is no data available.
                con.setblocking(0) 
                total_data =[]
                begin = time.time()
                con.send(("\r\n".join(lines) + "\r\n\r\n" + kwargs.get("body","")).encode())
                while True:
                    if total_data and time.time() - begin > 2:
                        print("time - begin > 2secs")
                        break
                    elif time.time()-begin > 4:
                        print("time - begin > 4secs")
                        break
                    
                    #Recv something
                    try:
                        response=con.recv(4096)
                        if response:
                            total_data.append(response.decode())
                            print("Dd")
                            begin = time.time()
                        else:
                            print("dd")
                            time.sleep(0.1)
                    except Exception as e:
                        pass
                json_string = "".join(total_data)
                separator = json_string.index("{")
                end_index = json_string.rindex("}") +1
                result = json.loads(json_string[separator:end_index])
                return result

    @classmethod
    @path_decorator
    def search(cls,index,body=None):
        path = f'/{index}/_search'
        host = cls._ip
        if body:
            body = json.dumps(body)
        token ="".encode()
        if cls._http_auth:
            token:bytes = base64.b64decode(":".join(cls._http_auth).encode("ascii"))
        lines = [
            'GET %s HTTP/1.1' % path,
            'Host: %s' % host,
            'Authorization: Basic %s' % token.decode(),
            'Content-Type: application/json',
            "Content-Length: %d" % len(body) if body else ""
        ]
        return lines
    
    @classmethod
    @path_decorator
    def health(cls):
        path =f"/_cluster/health"
        host = cls._ip
        token ="".encode()
        if cls._http_auth:
            token:bytes = base64.b64decode(":".join(cls._http_auth).encode("ascii"))
        lines = [
            'GET %s HTTP/1.1' % path,
            'Host: %s' % host,
            'Authorization: Basic %s' % token.decode()
        ]
        return lines    

es= Custom_Elasticsearch("10.107.11.66:9200")
pprint(es.search("heartbeat-7.16.3-2022.03.15-000001"))
pprint(es.health())


