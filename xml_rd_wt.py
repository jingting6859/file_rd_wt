import xml.dom.minidom as xmldom
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
