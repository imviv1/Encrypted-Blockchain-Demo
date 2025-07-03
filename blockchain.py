class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return "hash"  # Dummy hash for now
class Block:
    def __init__(self, data, previous_hash):
        self.original_data = data
        self.data = self.encrypt_data(data)  # Encrypt before storing
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return "hash"  # Dummy hash

    def encrypt_data(self, data):
        return data + 10  # Dummy encryption (FHE-inspired)