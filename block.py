from shared import Shared


class Block(object):
    def __init__(
        self,
        index: int,
        transactions: list,
        difficulty: int,
        previous_block_hash: str,
        mined_by: str,
        block_data_hash: str,
        nonce: int,
        date_created: int
    ):
        # validate input data
        if Shared.Defined(index) is False:
            print(__name__, "index was not defined!")
            return False
        if isinstance(index, int) is False:
            print(__name__, "index was not an integer!")
            return False
        if index < 0:
            print(__name__, "index was a negative integer!")
            return False
        if Shared.Defined(transactions) is False:
            print(__name__, "transactions was not defined!")
            return False
        if isinstance(transactions, list) is False:
            print(__name__, "transactions was not a list!")
            return False
        if Shared.Defined(difficulty) is False:
            print(__name__, "difficulty was not defined!")
            return False
        if isinstance(difficulty, int) is False:
            print(__name__, "difficulty was not an integer!")
            return False
        if Shared.Defined(previous_block_hash) is False:
            print(__name__, "previous_block_hash was not defined!")
            return False
        if isinstance(previous_block_hash, str) is False:
            print(__name__, "previous_block_hash was not a string!")
            return False
        if Shared.Defined(mined_by) is False:
            print(__name__, "mined_by was not defined!")
            return False
        if isinstance(mined_by, str) is False:
            print(__name__, "mined_by was not a string!")
            return False
        if Shared.Defined(block_data_hash) is False:
            print(__name__, "block_data_hash was not defined!")
            return False
        if isinstance(block_data_hash, str) is False:
            print(__name__, "block_data_hash was not a string!")
            return False
        if Shared.Defined(nonce) is False:
            print(__name__, "nonce was not defined!")
            return False
        if isinstance(nonce, int) is False:
            print(__name__, "nonce was not an integer!")
            return False
        if nonce < 0:
            print(__name__, "nonce was a negative integer!")
            return False
        if Shared.Defined(date_created) is False:
            print(__name__, "date_created was not defined!")
            return False
        if isinstance(date_created, int) is False:
            print(__name__, "date_created was not an integer!")
            return False
        if date_created < 0:
            print(__name__, "date_created was a negative integer!")
            return False
        # assign values to the new object
        self.index = index
        self.transactions = transactions
        self.difficulty = difficulty
        self.previous_block_hash = previous_block_hash
        self.mined_by = mined_by
        # self.block_data_hash = block_data_hash
        self.nonce = nonce
        self.date_created = date_created

    def get_block_header_hash(self):
        # The block header consists of three sets of block metadata. First,
        # there is a reference to a previous block hash, which connects this
        # block to the previous block in the blockchain. The second set of
        # metadata, namely the difficulty, timestamp and nonce, relate to the
        # mining competition. The third piece of metadata is the Merkle Tree
        # root, a data structure used to efficiently summarize all the
        # transactions in the block.
        pass
