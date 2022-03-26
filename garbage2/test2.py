import requests
import os




dir= os.path.abspath(os.path.dirname(__file__))
print(dir)


files=os.listdir(dir)
print(files)
url = "http://127.0.0.1:50001/file_upload"
test_files ={
    str(_) : open(os.path.join(dir,file),"rb") for _,file in zip(range(10000),files)
}

test_files["token"] = 1
print(test_files)

res=requests.post(url,files=test_files)
if res.ok:
    print("Uplload completed successfully")
    print(res.text)
else:
    print("Something went wrong")
    
#url = "http://127.0.0.1:50001/"
#res= requests.get(url)
#print(res.json().get("version"))
    

