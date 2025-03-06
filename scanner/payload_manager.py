import os

class PayloadManager:
    def __init__(self, payload_dir):
        self.payload_dir = payload_dir

    def get_payloads(self, attack_type):
        file_path = os.path.join(self.payload_dir, f"{attack_type}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        return []