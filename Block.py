import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions=[]):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.merkle_root = self.calculate_merkle_root()
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
    
    def calculate_merkle_root(self):
        if not self.transactions:
            return hashlib.sha256(b"").hexdigest()

        # Create a list of transaction hashes
        transaction_hashes = [transaction.calculate_hash() for transaction in self.transactions]

        # Build the Merkle tree
        while len(transaction_hashes) > 1:
            new_hashes = []
            for i in range(0, len(transaction_hashes), 2):
                left_hash = transaction_hashes[i]
                right_hash = transaction_hashes[i + 1] if i + 1 < len(transaction_hashes) else left_hash
                combined_hash = hashlib.sha256((left_hash + right_hash).encode('utf-8')).hexdigest()
                new_hashes.append(combined_hash)
            transaction_hashes = new_hashes

        return transaction_hashes[0]