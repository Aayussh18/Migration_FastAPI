from dicttoxml import dicttoxml
from config_loader import load_config

config= load_config()   

def convert_json_to_xml(data: dict):    
    return dicttoxml(data, custom_root=config['xml_root'],attr_type=config['attr_type'])

