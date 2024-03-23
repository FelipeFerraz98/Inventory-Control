import json
import os

class Data:
    json_file = 'data.json'

    def load_json(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                return json.load(file)
        else:
            print("JSON file not found. Creating a new file.")
            with open(self.json_file, 'w') as file:
                json.dump({}, file)
            return {}

    def save_json(self, data):
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=4)