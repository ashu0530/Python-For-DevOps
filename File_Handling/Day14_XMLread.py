'''
Another language widely used for representing structured data is Extensible Markup
Language (XML). It consists of hierarchical documents of tagged elements. Histori
cally, many web systems used XML to transport data. One such use is for Real Simple
Syndication (RSS) feeds. RSS feeds are used to track and notify users of updates to
websites and have been used to track the publication of articles from various sources.
RSS feeds use XML-formatted pages. Python offers the xml library for dealing with
XML documents. It maps the XML documents’ hierarchical structure to a tree-like
data structure. The nodes of the tree are elements, and a parent-child relationship is
used to model the hierarchy. The top parent node is referred to as the root element.
To parse an RSS XML document and get its root:
'''
import re
import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\app.xml')
print(tree,type(tree))

root = tree.getroot()
print(root)

for child in root:
    print(child.tag,child.attrib)