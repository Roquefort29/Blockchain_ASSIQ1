from Blockchain import Blockchain
from Transaction import Transaction

class BlockchainApp:
    def __init__(self):
        self.blockchain = Blockchain()

    def start(self):
        while True:
            print("Choose Action:")
            print("1. Create new block")
            print("2. Add transaction")
            print("3. Show blockchain")
            print("4. Chain validation")
            print("5. Verify transaction")
            print("6. Exit")

            choice = input()

            if choice == "1":
                self.create_new_block()
            elif choice == "2":
                self.add_transaction()
            elif choice == "3":
                self.view_blockchain()
            elif choice == "4":
                self.is_chain_valid()
            elif choice == "5":
                self.verify_transaction()
            elif choice == "6":
                print("Exit.")
                break
            else:
                print("Wrong Input. Please, choose action from 1 to 6.")

    def create_new_block(self):
        self.blockchain.add_block([])  # Create a new block with no transactions
        print("Added new block.")

    def add_transaction(self):
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        amount = float(input("Amount: "))

        transaction = Transaction(sender, recipient, amount)
        latest_block = self.blockchain.get_latest_block()
        latest_block.add_transaction(transaction)
        print("Transaction added.")

    def view_blockchain(self):
       self.blockchain.view_blockchain()

    def verify_transaction(self):
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        amount = float(input("Amount: "))
        merkle_root = input("Merkle Root: ")

        transaction = Transaction(sender, recipient, amount, merkle_root)
        result = self.blockchain.verify_transaction(transaction)

        if result:
            print("Transaction is valid.")
        else:
            print("Transaction is not valid.")

    def is_chain_valid(self):
        print(self.blockchain.is_chain_valid())

if __name__ == "__main__":
    blockchain_app = BlockchainApp()
    blockchain_app.start()