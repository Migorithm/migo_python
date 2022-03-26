import json
import re
SOLUTION='''{
    "ElasticSearch":{
        "ES_cluster1":["http://10.107.11.66:9200","http://10.107.11.56:9200","http://10.107.11.59:9200"],
        "ES_cluster2":["http://10.107.11.66:9200","http://10.107.11.59:9200","http://10.107.11.56:9200"]
},      
    "Redis":{
        "Redis_cluster1":["10.107.11.66:6379","10.107.11.56:6379","10.107.11.59:6379",
                          "10.107.11.66:6380","10.107.11.56:6380","10.107.11.59:6380"],
        "Redis_cluster2":["node2-1","node2-2","node2-3","node2-4"]
}
}'''

a = json.loads(SOLUTION)

# for i in a.values():
#     print(i.keys())

b= [(node,node) 
    for clusters in a.values()
    for node in clusters.keys()]
# print(b)

c= [(ids,node) for ids,node in zip(range(1000,),*[ clusters.get("ES_cluster1") for clusters in a.values() if clusters.get("ES_cluster1")])]

for b in a.values():
    a=b.get("ES_cluster1")
    if a :
        
        
        regex = re.compile(r"\d+.\d+.\d+.\d+")
        search = list(map(lambda x: "http://"+regex.search(x).group()+":5000",a))
        print(search)
        
        # print(a)