import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_timestamp = int(time.time())
        new_hash = previous_block.hash

        new_block = Block(new_index, new_hash, new_timestamp, data)
        self.chain.append(new_block)

def main():
    my_blockchain = Blockchain()

    # Adding blocks to the blockchain
    my_blockchain.add_block("Transaction Data 1")
    my_blockchain.add_block("Transaction Data 2")
    my_blockchain.add_block("Transaction Data 3")

    # Printing the blockchain
    for block in my_blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("\n")

if __name__ == "__main__":
    main()