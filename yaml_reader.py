import yaml
import os

def read_yaml_file(file_name):
    imported_data = {}
    path = os.getcwd() + os.path.sep + "Brick_Breaker" + os.path.sep + file_name
    with open(path, "rt", encoding="utf-8") as file:
        imported_data.update(yaml.load(stream = file, Loader = yaml.FullLoader))
    return imported_data
