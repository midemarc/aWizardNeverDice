from typing import Dict
import yaml


def read_config() -> Dict:
    with open("config.yml") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
