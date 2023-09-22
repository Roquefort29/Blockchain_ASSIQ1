import hashlib
import time


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        try:
            input_data = str(self.sender) + str(self.recipient) + str(self.amount)
            sha256 = hashlib.sha256()
            sha256.update(input_data.encode('utf-8'))
            return sha256.hexdigest()
        except Exception as e:
            raise RuntimeError(e)


class Block:
    def __init__(self, timestamp, transactions, previous_hash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        try:
            input_data = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
            sha256 = hashlib.sha256()
            sha256.update(input_data.encode('utf-8'))
            return sha256.hexdigest()
        except Exception as e:
            raise RuntimeError(e)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(time.time(), [], '0')

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


my_blockchain = Blockchain()
transactions = [Transaction("Dana", "Dias", 10),
                Transaction("Asel", "Syrym", 5), ]

new_block = Block(time.time(), transactions)
my_blockchain.add_block(new_block)

for block in my_blockchain.chain:
    print(f"Block Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Transactions: {len(block.transactions)}\n")
