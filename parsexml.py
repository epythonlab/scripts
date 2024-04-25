# Converting XML into Pandas DataFrame

# import the necessary libraries
import pandas as pd
import xml.etree.ElementTree as et

# parse the xml file
tree = et.parse('book.xml')
root = tree.getroot()
#print(root)

# extract the data
books_list = []
for book_elem in root.findall('.//book'):
    book_dict = {}
    book_dict['id'] = book_elem.get('id')
    for child_elem in book_elem:
        book_dict[child_elem.tag] = child_elem.text
    books_list.append(book_dict)
print(books_list)

# convert to the dataframe 
df = pd.DataFrame(books_list) 
print(df)
