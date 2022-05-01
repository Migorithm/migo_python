import logging
import requests
import re
from typing import List, Optional, Tuple, Union, Mapping,Any
from contextlib import contextmanager
from pprint import pprint
import functools
import sys

logging.basicConfig(level=logging.DEBUG)

class CustomElasticsearch:
    def __new__(cls, hosts:Union[str,List[Union[str,Mapping[str,str]]]]=None,http_auth:Optional[Tuple[str,str]]=None ) -> "CustomElasticsearch":
        if hosts is None:
            raise ValueError("Hosts must be specified")
        cls.connection_fail=set()
        cls._hosts = hosts
        cls._http_auth=http_auth
        
        if isinstance(cls._hosts,str):
            match = re.search(r'(?P<protocol>https?://)?(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)',cls._hosts)
            if match.group("protocol") is None:
                raise ValueError("http(s) must be specified")
            cls._url = match.group(0)
        
        if isinstance(cls._hosts,list):
            url=cls._hosts[0]
            match = re.search(r'(?P<protocol>https?://)?(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)',url)
            if match.group("protocol") is None:
                raise ValueError("http(s) must be specified")
            cls._url = match.group(0)
        return cls          
    
    @classmethod
    @contextmanager
    def connector(cls):
        try:
            with requests.Session() as sock:
                yield sock
        finally:
            sock.close()
    
    @classmethod
    @property
    def get_host_len(cls):
        return len(cls._hosts)
    
    class ExceedNumberOfAttempt(Exception):
        pass
    
    class path_decorator:
        def __init__(self,func):
            self.func=func
            self.counter=0
            
            functools.update_wrapper(self,func) 
            
        def __call__(self, *args: Any, **kwargs: Any) -> Any:
            self.counter+=1
            if self.counter > CustomElasticsearch.get_host_len:
                raise CustomElasticsearch.ExceedNumberOfAttempt("No connection available for the given cluster.")
            
            path, body = self.func(*args,**kwargs)
            
            with CustomElasticsearch.connector() as con:
                try :
                    if body:
                        r: requests.models.Response = con.post(CustomElasticsearch._url + path,json=body,timeout=(2,5))
                        CustomElasticsearch.connection_fail.clear()
                        return r.json()
                    else:
                        r: requests.models.Response = con.get(CustomElasticsearch._url + path,json=body,timeout=(2,5))
                        CustomElasticsearch.connection_fail.clear()
                        return r.json()
                except requests.exceptions.ConnectionError as c:
                    logging.error(sys.exc_info())
                    
                    #Topology refresh requires the given hosts to be a cluster. 
                    if not isinstance(CustomElasticsearch._hosts,list):
                        raise ConnectionError("Connection to {} failed!".format(CustomElasticsearch._url))
                    
                    #Refresh
                    CustomElasticsearch.connection_fail.add(CustomElasticsearch._url)
                    for url in CustomElasticsearch._hosts[len(CustomElasticsearch.connection_fail):]:
                        if url not in CustomElasticsearch.connection_fail:
                            CustomElasticsearch._url=url
                            break
                    
                    #Resetting the target endpoint
                    match =  re.search(r'(?P<protocol>https?://)?(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)',CustomElasticsearch._url)
                    if match.group("protocol") is None:
                        raise ValueError("http(s) must be given")
                    
                    CustomElasticsearch._url = match.group(0)
                    
                    #Recursive call
                    function = getattr(CustomElasticsearch,"{}".format(self.func.__name__))
                    return function(*args[-1:],**kwargs)
                
    @classmethod
    @path_decorator
    def search(cls,index=None,body=None):
        path = f'/{index}/_search'
        return path,body
    
    
    @classmethod
    @path_decorator
    def health(cls):
        path = f'/_cluster/health'
        return path,None
    
es = CustomElasticsearch(["http://10.107.11.66:9200"])
a:dict = es.search("heartbeat-7.16.3-2022.03.15-000001")
b:dict = es.health()
pprint(a)
pprint(b)
    
                     
                    