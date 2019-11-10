import xml.dom.minidom as xmldom
from xml.dom.minidom import Document
# 获得dom 对象
domobj = xmldom.parse('test.xml')
data_ele = domobj.childNodes[0]
country_eles = data_ele.getElementsByTagName('country')
for country in country_eles:
    print(country.getAttribute('name'))
    rank = country.getElementsByTagName('rank')[0]
    year = country.getElementsByTagName('year')[0]
    gdppc = country.getElementsByTagName('gdppc')[0]
    neighbors = country.getElementsByTagName('neighbor')
    for neighbor in neighbors:
        name = neighbor.getAttribute('name')
        direction = neighbor.getAttribute('direction')
    print(rank.childNodes[0].data,year.childNodes[0].data,gdppc.childNodes[0].data,name,direction)
    print('===========================================')


########################################xml 写操作#######################################
doc = Document()
root = doc.createElement('data')
root_node = doc.appendChild(root)
print(root_node)
# 记录每层节点的最新元素
level_note = doc.createElement('level')
level_note.setAttribute('name','1')
root_node.appendChild(level_note)
nodes = {0: root}


with open('create.xml', 'w') as f:
    f.write(doc.toprettyxml(indent='\t'))
