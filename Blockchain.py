
from Block import Block
from MerkleNodes import MerkleNodes

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0")
        self.mine_block(genesis_block)  # Mining the genesis block
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_block(self, block, difficulty=2):
        while block.hash[:difficulty] != '0' * difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index + 1, previous_block.hash, transactions)
        self.mine_block(new_block)  # Mining the new block
        self.chain.append(new_block)

    def view_blockchain(self):
        for block in self.chain:
            print("Block #", block.index)
            print("Previous Hash: ", block.previous_hash)
            print("Timestamp: ", block.timestamp)
            print("Transactions: ", block.transactions)
            print("Hash: ", block.hash)
            print("\n")

    def create_merkle_tree(self, transactions):
        if len(transactions) == 0:
            return None

        if len(transactions) == 1:
            return MerkleNodes(data=transactions[0].to_dict())

        leaves = [MerkleNodes(data=tx.to_dict()) for tx in transactions]

        while len(leaves) > 1:
            new_leaves = []
            for i in range(0, len(leaves), 2):
                left = leaves[i]
                right = leaves[i + 1] if i + 1 < len(leaves) else left
                parent = MerkleNodes(left=left, right=right)
                new_leaves.append(parent)
            leaves = new_leaves

        return leaves[0]

    def verify_transaction(self, transaction):
        merkle_root = self.create_merkle_tree(self.get_latest_block().transactions).calculate_hash()
        if merkle_root == transaction.to_dict()['merkle_root']:
            return True
        return False