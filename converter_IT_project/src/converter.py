import json
import yaml
from lxml import etree
import os


def convert_file(input_path, output_path):
    _, in_ext = os.path.splitext(input_path)
    _, out_ext = os.path.splitext(output_path)

    # Wczytywanie danych
    if in_ext == '.json':
        with open(input_path, 'r') as f:
            data = json.load(f)
    elif in_ext in ['.yml', '.yaml']:
        with open(input_path, 'r') as f:
            data = yaml.safe_load(f)
    elif in_ext == '.xml':
        tree = etree.parse(input_path)
        root = tree.getroot()
        data = xml_to_dict(root)

    # Zapis danych
    if out_ext == '.json':
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
    elif out_ext in ['.yml', '.yaml']:
        with open(output_path, 'w') as f:
            yaml.dump(data, f)
    elif out_ext == '.xml':
        root = dict_to_xml(data)
        tree = etree.ElementTree(root)
        tree.write(output_path, pretty_print=True)


# Funkcje pomocnicze do konwersji XML
def xml_to_dict(element):
    return {child.tag: xml_to_dict(child) for child in element}


def dict_to_xml(data, root_tag='root'):
    element = etree.Element(root_tag)
    for key, value in data.items():
        child = etree.SubElement(element, key)
        child.text = str(value)
    return element