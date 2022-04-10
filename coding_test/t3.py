from  string import Formatter
from functools import partial

def solution(tstring:str, variables):
  
    #extract circular 
    hash :dict[str,str]={}
    for key,value in variables:
        hash[key] = value
        
    circular = set()
    for key,value in hash.items():
        if value.startswith('{') and value.endswith('}'):
            search_for= hash.get(value[1:-1])
            if search_for and search_for == "{" + key +"}":
                circular.add(key)
                circular.add(value[1:-1])
    
    keywords = {fname for _,fname,_,_ in Formatter().parse(tstring)}
    if circular:
        dic ={}
        for cir in circular:
            dic[cir] = r"{"+cir +r"}"
            del hash[cir]
            keywords.discard(cir)    
        tstring = tstring.format(**dic)
        if not keywords :
            return tstring
    
    answer = tstring.format(**hash)     
    keywords = {fname for _,fname,_,_ in Formatter().parse(answer)}
    if not None in keywords:
        vars= [ [keyword,hash[keyword]] for keyword in keywords]
        return  solution(answer,vars)

    return answer
    





ts1 = "this is {template} {template} is {state}"
var1 =[["template", "string"], ["state", "changed"]]


ts2= "this is {template} {template} is {state}"
var2 = [["template", "string"], ["state", "{template}"]]

ts3 = "this is {template} {template} is {state}"
var3 = [["template", "{state}"], ["state", "{template}"]]

print(solution(ts1,var1))
print(solution(ts2,var2))
print(solution(ts3,var3))
