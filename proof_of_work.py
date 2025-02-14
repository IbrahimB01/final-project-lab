from simple_blockchain import block_2, generate_block_hash

def mine_block(block, difficulty):
    prefix = '0' * difficulty
    while not block.block_hash.startswith(prefix):
        block.timestamp += 1
        block.block_hash = generate_block_hash(block.block_id, block.previous_block_hash, block.timestamp, block.content)
    return block

difficulty = 4
mined_block = mine_block(block_2, difficulty)
print(f"Mined block hash: {mined_block.block_hash}")
