import hashlib
import time
import json


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generate hash for block"""
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Proof of Work: find hash with leading zeros"""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        """Genesis block = first block"""
        return Block(0, [], time.time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        """Add a new transaction to pending list"""
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        """Mine all pending transactions into a block"""
        block = Block(
            len(self.chain),
            self.pending_transactions,
            time.time(),
            self.get_latest_block().hash,
        )
        block.mine_block(self.difficulty)

        self.chain.append(block)
        print("Block added to chain!")

        # Reward miner
        self.pending_transactions = [
            {"sender": "SYSTEM", "receiver": miner_address, "amount": self.mining_reward}
        ]

    def is_chain_valid(self):
        """Check if blockchain is valid"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print("Invalid block hash at index", i)
                return False
            if current.previous_hash != prev.hash:
                print("Invalid previous hash at index", i)
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print("\n======================")
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Hash: {block.hash}")
            print(f"Prev Hash: {block.previous_hash}")


def menu():
    blockchain = Blockchain()

    while True:
        print("\n=== Simple Blockchain CLI ===")
        print("1. Add Transaction")
        print("2. Mine Pending Transactions")
        print("3. View Blockchain")
        print("4. Validate Blockchain")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sender = input("Sender: ")
            receiver = input("Receiver: ")
            amount = float(input("Amount: "))
            blockchain.add_transaction(sender, receiver, amount)
            print("Transaction added!")

        elif choice == "2":
            miner = input("Enter miner address: ")
            blockchain.mine_pending_transactions(miner)

        elif choice == "3":
            blockchain.print_chain()

        elif choice == "4":
            valid = blockchain.is_chain_valid()
            print("Blockchain valid?" , valid)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()