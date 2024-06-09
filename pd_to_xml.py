# Transforming Pandas DataFrame to XML
import pandas as pd

data ={
    'Name': ['asibeh', 'alice', 'tenager'],
    'age': [23, 40, 34],
    'city':['addis ababa', 'bahirdar', 'db']
}
df = pd.DataFrame(data)
print(df)


import xml.etree.ElementTree as ET

def df_to_xml(df, root_name, row_name):
    root = ET.Element(root_name)
    for _, row in df.iterrows():
        item = ET.SubElement(root, row_name)
        for col_name, col_value in row.items():
            sub_item = ET.SubElement(item, col_name)
            sub_item.text = str(col_value)
    return ET.tostring(root, encoding='unicode')

xml_data = df_to_xml(df, 'Data', 'Person')
print(xml_data)
