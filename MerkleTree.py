# -*- coding: utf-8 -*-
"""MerkleTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YvxJonplAldRoEcf6CL9qm2-PG-Hd6pT
"""

import hashlib

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def calculate_hash(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self.sender).encode('utf-8'))
        sha256.update(str(self.recipient).encode('utf-8'))
        sha256.update(str(self.amount).encode('utf-8'))
        return sha256.hexdigest()


class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = self.calculate_merkle_root()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self.index).encode('utf-8'))
        sha256.update(str(self.previous_hash).encode('utf-8'))
        sha256.update(str(self.merkle_root).encode('utf-8'))
        return sha256.hexdigest()

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


class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        if len(self.chain) > 0:
            previous_block = self.chain[-1]
            if block.previous_hash != previous_block.hash:
                raise Exception("Invalid block: Previous hash does not match")
        self.chain.append(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

blockchain = Blockchain()

genesis_block = Block(0, "0", [])
blockchain.add_block(genesis_block)

transactions = [
    Transaction("Dana", "Dias", 1),
    Transaction("Syrym", "Asel", 2),
    Transaction("Syrym", "Dias", 0.5),
]

new_block = Block(1, blockchain.chain[-1].hash, transactions)
blockchain.add_block(new_block)

if blockchain.is_chain_valid():
    print("Transaction is valid.")
else:
    print("Transaction is not valid.")