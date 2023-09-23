import hashlib

class MerkleNodes:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def calculate_hash(self):
        if self.data is not None:
            return hashlib.sha256(self.data.encode()).hexdigest()
        left_hash = self.left.calculate_hash()
        right_hash = self.right.calculate_hash()
        combined = left_hash + right_hash
        return hashlib.sha256(combined.encode()).hexdigest()