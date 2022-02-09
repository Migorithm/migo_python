import xml.etree.ElementTree as et  

def Test():
    friend = et.parse('../files/myfriend.xml')
    friends = friend.findall("address")
    for res in friends :
        print(res.find("name").text , ",",res.find("addr").text)

    print('============================')

def Test01():
    tree = et.ElementTree(file='../files/fruit.xml') 
    root =tree.getroot() #get root address

    for child in root:
        print("tag:", child.tag,
              "attributes:", child.attrib)  
        for grandchild in child:
            if grandchild.text != None:
                print("\ttag:",grandchild.tag, grandchild.text,
                    "attributes:",grandchild.attrib)
            else:
                print("\ttag:", grandchild.tag,
                      "attributes:", grandchild.attrib)

if __name__ == '__main__':
    Test()
