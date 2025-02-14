from simple_blockchain import block, block_1, block_2, generate_block_hash

def is_valid_chain(blockchain):
    previous_block = blockchain[0]
    for current_block in blockchain[1:]:
        if current_block.block_hash != generate_block_hash(current_block.block_id, previous_block.block_hash, current_block.timestamp, current_block.content):
            return False
        previous_block = current_block
    return True

blockchain = [block, block_1, block_2]
print(f"Is the blockchain valid? {is_valid_chain(blockchain)}")

print(f"Block Hash: {block.block_hash}")
print(f"Block 1 Hash: {block_1.block_hash}")
print(f"Block 2 Hash: {block_2.block_hash}")
