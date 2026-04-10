from jsonschema import validate, ValidationError
import json
from config_loader import load_config

config= load_config()

# Load Schema directly from YAML config

with open (config['schema_path'], 'r') as f:
    schema = json.load(f)

def validate_json(data: dict):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return False, e.message
    
    return True, "JSON is valid"

    