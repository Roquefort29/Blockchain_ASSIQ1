import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions=[]):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = (
            str(self.index) +
            str(self.previous_hash) +
            str(self.transactions) +
            str(self.timestamp) +
            str(self.nonce)
        )
        return hashlib.sha256(data.encode()).hexdigest()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)