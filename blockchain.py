import datetime as _dt
import hashlib as _hashlib
import json as _json


class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(data="Vote Number: 000", proof=1, previous_hash="0", index=1)
        self.chain.append(genesis_block)

    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = self._proof_of_stake(previous_proof, index, data)
        previous_hash = self._hash(block=previous_block)
        block = self._create_block(data=data, proof=proof, previous_hash=previous_hash, index=index)
        self.chain.append(block)
        return block

    def _hash(self, block: dict) -> str:
        encoded_block = _json.dumps(block, sort_keys=True).encode()

        return _hashlib.sha256(encoded_block).hexdigest()

    def _to_digest(self, new_proof: int, previous_proof: int, index: str, data: str) -> bytes:
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index) + data

        return to_digest.encode()

    def _proof_of_stake(self, previous_proof: str, index: int, data: str) -> int:
        new_proof = 1
        check_proof = False

        while not check_proof:
            # print(new_proof)
            to_digest = self._to_digest(new_proof=new_proof, previous_proof=previous_proof, index=index, data=data)
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            if hash_value[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash,
        }

        return block

    def vote(self, **kwargs) -> str:
        candidate1 = input("Enter 1st candidate name:")
        candidate2 = input("Enter 2nd candidate name:")

        candidate1_votes = 0
        candidate2_votes = 0

        voters_id = [101, 102, 103, 104, 105, 106]
        number_of_voters = len(voters_id)

        voted = []

        while True:
            if not voters_id:
                print("Voting is over")

                if candidate1_votes > candidate2_votes:
                    print(f"{candidate1} won the election with {candidate1_votes}")

                elif candidate1_votes < candidate2_votes:
                    print(f"{candidate2} won the election with {candidate2_votes}")

                else:
                    print("Tied!!!")
            else:
                voter = int(input("Enter your voter ID: "))

                if voter in voted:
                    print("You already voted!!")
                else:
                    if voter in voters_id:
                        print(f"1.{candidate1}\n2.{candidate2}")
                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            candidate1_votes += 1
                            print(f"You voted {candidate1}")
                        else:
                            candidate2_votes += 1
                            print(f"You voted {candidate2}")

                        voters_id.remove(voter)
                        voted.append(voter)
                    else:
                        print("You are not allowed to vote")

    """
    This method checks if the next block's previous hash value is same
    current block's hash value.
    If not, then return false which determine the ledger / chain is not
    valid.
    
    """

    def is_chain_valid(self) -> bool :
        current_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            if next_block["previous_hash"] != self._hash(current_block)
                return False

            current_proof = current_block["proof"]
            next_index, next_data, next_proof = (
                next_block["index"],
                next_block["data"],
                next_block["proof"],
            )

            hash_value = _hashlib.sha256(
                self._to_digest(
                    new_proof=next_proof,
                    previous_proof=current_proof,
                    index=next_index,
                    data=next_data,
                )
            ).hexdigest()

            if hash_value[:4] != "0000":
                return False

            current_block = next_block
            block_index += 1

        return True
