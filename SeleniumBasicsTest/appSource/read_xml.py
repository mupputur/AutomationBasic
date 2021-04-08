from xml.etree import ElementTree as et

file_path = "D:\\xml_file.xml"
tree = et.parse(file_path)
#print(et.dump(tree))

books = tree.findall("book")
for c in books:
    titles = c.find("title").text
    desc = c.find("description").text
    #print(titles,desc)


