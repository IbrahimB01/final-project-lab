import hashlib
import time

class SimpleBlock:
    def __init__(self, block_id, previous_block_hash, timestamp, content, block_hash):
        self.block_id = block_id
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.content = content
        self.block_hash = block_hash

def generate_block_hash(block_id, previous_block_hash, timestamp, content):
    block_data = f"{block_id}{previous_block_hash}{timestamp}{content}"
    return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

def create_block():
    return SimpleBlock(0, "0", int(time.time()), "Block", generate_block_hash(0, "0", int(time.time()), "Block"))

def create_new_block(last_block, content):
    block_id = last_block.block_id + 1
    timestamp = int(time.time())
    block_hash = generate_block_hash(block_id, last_block.block_hash, timestamp, content)
    return SimpleBlock(block_id, last_block.block_hash, timestamp, content, block_hash)

block = create_block()
block_1 = create_new_block(block, "Block 1 content")
block_2 = create_new_block(block_1, "Block 2 content")

print(f"Block Hash: {block.block_hash}")
print(f"Block 1 Hash: {block_1.block_hash}")
print(f"Block 2 Hash: {block_2.block_hash}")
