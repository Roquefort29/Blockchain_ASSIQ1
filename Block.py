import hashlib


class Block:
    def __init__(self, index, previous_hash, transactions, merkle_root):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = merkle_root
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self.index).encode('utf-8'))
        sha256.update(str(self.previous_hash).encode('utf-8'))
        sha256.update(str(self.merkle_root).encode('utf-8'))
        return sha256.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)

    def get_latest_block(self):
        return self.chain[-1]

    def is_valid(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            previous_block = self.chain[i - 1]
            if block.previous_hash != previous_block.hash:
                return False
            merkle_tree = MerkleTree(block.transactions)
            if block.merkle_root != merkle_tree.root:
                return False
        return True


class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_merkle_tree()

    def build_merkle_tree(self):
        if not self.transactions:
            return hashlib.sha256(b"").hexdigest()
        if len(self.transactions) == 1:
            return hashlib.sha256(str(self.transactions[0]).encode('utf-8')).hexdigest()
            # Recursive construction of the Merkle tree
        hashes = [hashlib.sha256(str(tx).encode('utf-8')).hexdigest() for tx in self.transactions]
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])
            new_hashes = []
            for i in range(0, len(hashes), 2):
                combined = hashlib.sha256((hashes[i] + hashes[i + 1]).encode('utf-8')).hexdigest()
                new_hashes.append(combined)
            hashes = new_hashes
        return hashes[0]


blockchain = Blockchain()
genesis_block = Block(0, "0", [], "")
blockchain.add_block(genesis_block)

for block in blockchain.chain:
    print(f"Block Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Merkle Root: {block.merkle_root}")
    print(f"Block Hash: {block.hash}\n") 