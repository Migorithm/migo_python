SOLUTION='{
    "ElasticSearch":{
        "ES_cluster1":["es1","es2","es3","es4"],
        "ES_cluster2":["node1","node2","node3","node4"]
},      
    "Redis":{
        "Redis_cluster1":["redis1-1","redis1-2","redis1-3","redis1-4"],
        "Redis_cluster2":["node2-1","node2-2","node2-3","node2-4"]
}
}'

FLASK_APP=test.py
FLASK_DEBUG=True
SECRET_KEY="You never know"