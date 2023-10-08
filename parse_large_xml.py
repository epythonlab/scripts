import pandas as pd
import xml.etree.ElementTree as ET
# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
xml_file_path = 'STLD.xml'

try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    order_data = []

    for event in root.findall(".//TRX_Sale"):
        order = event.find("Order")

        if order is not None:
            order_row = order.attrib.copy()  # Copy attributes from <Order> element
            order_row["TRX_Sale_status"] = event.get("status")
            order_row["TRX_Sale_POD"] = event.get("POD")
            order_row["TRX_Sale_RemPOD"] = event.get("RemPOD")
            order_data.append(order_row)

    order_df = pd.DataFrame(order_data)

    print(order_df)

except ET.ParseError as e:
    print("Error parsing XML:", e)
