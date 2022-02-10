#unpcaking dictionary -- value passing
def myfunc(x,y,z):
    print(x,y,z)

dict_vec={'x':1,"y":0,"z":1}

myfunc(**dict_vec)

#unpacking dictionary -- key passing
def myfunc2(a,b,c):
    print(a,b,c)

myfunc2(*dict_vec)