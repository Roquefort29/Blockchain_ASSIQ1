# -*- coding: utf-8 -*-
"""MerkleNode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YvxJonplAldRoEcf6CL9qm2-PG-Hd6pT
"""

import hashlib

class MerkleNode:
    def __init__(self):
        self.hash = None
        self.left_node = None
        self.right_node = None
        self.parent = None

    def is_leaf(self):
        return self.left_node is None and self.right_node is None

    def compute_hash(self, buffer):
        self.hash = hashlib.sha256(buffer).hexdigest()

    def set_left_node(self, node):
        if node.hash:
            self.left_node = node
            self.left_node.parent = self
            self.compute_hash(bytes.fromhex(self.left_node.hash) + bytes.fromhex(self.right_node.hash) if self.right_node else bytes.fromhex(self.left_node.hash))

    def set_right_node(self, node):
        if node.hash:
            self.right_node = node
            self.right_node.parent = self
            self.compute_hash(bytes.fromhex(self.left_node.hash) + bytes.fromhex(self.right_node.hash))

    def can_verify_hash(self):
        return (self.left_node is not None and self.right_node is not None) or (self.left_node is not None)

    def verify_hash(self):
        if self.left_node is None and self.right_node is None:
            return True

        if self.right_node is None:
            return self.hash == self.left_node.hash

        left_right_hash = hashlib.sha256(bytes.fromhex(self.left_node.hash) + bytes.fromhex(self.right_node.hash)).hexdigest()
        return self.hash == left_right_hash

    def equals(self, node):
        return self.hash == node.hash