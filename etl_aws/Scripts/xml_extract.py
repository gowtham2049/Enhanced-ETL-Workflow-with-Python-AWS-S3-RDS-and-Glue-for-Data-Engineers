import pandas as pd 
import xml.etree.ElementTree as et
import glob
import logging


def extract_xml(path):
    logging.info("xml reading")

    xml_file_list=glob.glob(f'{path}\*.xml')
    data=[]
    for file in xml_file_list:
        tree=et.parse(file)
        root=tree.getroot()
        for person in root.findall('person'):
            name=person.find('name').text
            height=person.find('height').text
            weight=person.find('weight').text
            data.append([name,height,weight])
    xml_df=pd.DataFrame(data)
    xml_df.columns = ['name', 'height', 'weight']

    return xml_df
