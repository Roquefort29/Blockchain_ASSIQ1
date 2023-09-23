import hashlib
from Block import Block


# class Block:
#     def __init__(self, index, previous_hash, data):
#         self.index = index
#         self.previous_hash = previous_hash
#         self.data = data
#         self.nonce = 0
#         self.hash = self.calculate_hash()


#     def calculate_hash(self):
#         data = str(self.index) + self.previous_hash + str(self.data) + str(self.nonce)
#         return hashlib.sha256(data.encode()).hexdigest()


class Blockchain():
    def __init__(self):
        self.chain = []
        self.add_genesis_block()
        self.data = data
        self.nonce = 0


    def add_genesis_block(self):
        genesis_block = Block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        return self.chain[-1]


    def add_block(self, data):
        previous_block = self.chain[-1]


        index = previous_block.index + 1
        new_block = Block(index, previous_block.hash, data)
        self.mine_block(new_block)
        self.chain.append(new_block)


    def mine_block(self, block, difficulty=2):
        while block.hash[:difficulty] != '0' * difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
            print(f"Block mined: {block.hash}")


    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            return True

my_blockchain = Blockchain()
my_blockchain.add_block("Transaction 1")
my_blockchain.add_block("Transaction 2")
print("Blockchain is valid:", my_blockchain.is_chain_valid())