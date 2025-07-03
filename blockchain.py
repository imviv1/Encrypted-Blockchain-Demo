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
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

# Example usage
bc = Blockchain()
bc.add_block("Transaction 1")