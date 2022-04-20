import re

# "abcabcdefabc"


def solution(call:str):
    hash ={}
    for i in range(1,len(call)): # 1,2 ... max_length  
        idx=0
        while True:
            if len(call[idx:i+idx]) != i:
                break
            if call[idx:i+idx] =="":
                break
            #print(call[idx:i+idx])
            if hash.get(call[idx:i+idx].lower()):
                # print(call[idx:i+idx])
                hash[call[idx:i+idx].lower()] +=1 
            else :
                hash[call[idx:i+idx].lower()] = 1
            if idx >= len(call):
                break
            idx +=1
            
    hash= sorted(hash.items(),key=lambda x:x[1],reverse=True)
    hash = sorted(filter(lambda x: x[1]==hash[0][1],hash),key=lambda x: len(x[0]),reverse=True)
    hash = list(filter(lambda x:len(x[0]) == len(hash[0][0]),hash))
    
    for word,_ in hash:
        case_insensitive = re.compile(word,re.IGNORECASE)
        call = case_insensitive.sub("",call)
        
    return call

print(solution("abcabcdefabc"))
print(solution("abxdeydeabz"))
print(solution("ABCabcA"))
print(solution("abcabca"))

# occurrence