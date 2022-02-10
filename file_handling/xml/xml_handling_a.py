from xml.dom.minidom import parse   
#https://docs.python.org/3/library/xml.dom.minidom.html


dom = parse('../files/xmlfile_name.xml') #Render into DOM tree
for name in dom.getElementsByTagName('name'):
    print(name.firstChild.data)

print('==============================================')
datasource = open('../files/xmlfile_name.xml') #파일로 읽어와서 파싱한다.
dom2 = parse(datasource)
for name in dom.getElementsByTagName('addr'):
    print(name.firstChild.data)