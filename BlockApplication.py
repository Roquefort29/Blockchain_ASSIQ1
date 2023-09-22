from BlockValidation import Blockchain
from Block import Block
from Transactions import Transaction
import time

class BlockchainApp:
    def __init__(self):
        self.blockchain = Blockchain()

    def start(self):
        while True:
            print("Choose Action:")
            print("1. Create new block")
            print("2. Send transaction")
            print("3. Show blockchain")
            print("4. Exit")

            choice = int(input())

            if choice == 1:
                self.create_new_block()
            elif choice == 2:
                self.send_transaction()
            elif choice == 3:
                self.view_blockchain()
            elif choice == 4:
                print("Exit.")
                break
            else:
                print("Wrong Input. Please, choose action from 1 to 6.")

    def create_new_block(self):
        print("Add data for new block:")
        data = input()

        new_block = Block(
            self.blockchain.get_latest_block().index + 1,
            self.blockchain.get_latest_block().hash,
            data, int(time.time()),
            self.blockchain
        )
        # new_block.mine_block(4)

        self.blockchain.add_block(new_block)
        print("Added new block.")

    def send_transaction(self):
        print("Input index, which you want to add transaction:")
        index = int(input())
        print("Input Sender:")
        sender = input()
        print("Input Recipient:")
        recipient = input()
        print("Input amount:")
        amount = float(input())

        transaction = Transaction(index, sender, recipient, amount)

        if 0 <= index <= len(self.blockchain.chain):
            block = self.blockchain.chain[index]
            block.add_transaction(transaction)
            block.update_merkle_tree()
            block.recalculate_hash()
            print(f"Transaction added to index {index}")
        else:
            print("Block index does not exist.")

    def view_blockchain(self):
        for block in self.blockchain.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Merkle Root: {block.merkle_root()}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")

            transactions = block.transactions
            if transactions:
                print("Transactions:")
                for transaction in transactions:
                    print(f"  Sender: {transaction.sender}")
                    print(f"  Recipient: {transaction.recipient}")
                    print(f"  Amount: {transaction.amount}")
                    print(f"  Hash: {transaction.hash}")

            print()

    def view_specific_block(self):
        print("Input block index to view:")
        block_index = int(input())

        block = self.blockchain.get_block_by_index(block_index)

        if block:
            print(f"Block Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Merkle Root: {block.calculate_merkle_root()}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")

            transactions = block.transactions
            if transactions:
                print("Transactions:")
                for transaction in transactions:
                    print(f"  Sender: {transaction.sender}")
                    print(f"  Recipient: {transaction.recipient}")
                    print(f"  Amount: {transaction.amount}")
                    print(f"  Hash: {transaction.hash}")
        else:
            print("Block not found.")

    def check_blockchain_integrity(self):
        is_chain_valid = self.blockchain.is_chain_valid()
        if is_chain_valid:
            print("Blockchain is valid.")
        else:
            print("Blockchain is defective.")


if __name__ == "__main__":
    blockchain_app = BlockchainApp()
    blockchain_app.start()
