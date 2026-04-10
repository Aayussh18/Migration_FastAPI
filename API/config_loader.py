import yaml

_config = None  # Singleton instance

def load_config():
    global _config

    if _config is None:
        with open("config.yaml", "r") as f:
            _config = yaml.safe_load(f)

    return _config