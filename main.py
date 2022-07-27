from hashlib import sha256
import json #text written with java script object notations
# The SHA-256 is a hashing algorithm created by the NSA back in 2001 which takes an input
# of any size and converts it to an output of fixed size. The beauty of the SHA-256 is t
# hat the Output is close to impossible to decode thus ensuring security.

sender='sender'
genesis_block={
    'previous_hash':'XYZ', 'index':0, 'transaction': [], 'proof':0
}
blockchain=[genesis_block]
open_transactions=[]
def get_transcation():
    recipient= input('Enter your recipient:')
    amount=input('Enter ypur amount:')
    return (recipient, amount)
while True:
    I=input('Enter your choice:')
    if I=='1':
        data= get_transcation()
        recipient, amount= data
        transaction={'sender':sender, 'recipient': recipient, 'amount': amount}
        open_transactions.append(transaction)
        print(open_transactions)

def hash_block(last_block):
    previous_hash=''
    for keys in last_block:
        previous_hash= previous_hash+ str(last_block[keys])
        hash = sha256(json.dumps(previous_hash).encode('utf-8')).hexdigest()
    return hash

def proof_of_work():
    previous_hash=''
    proof=0
    last_block=blockchain[-1]
    for keys in last_block:
        previous_hash= previous_hash + str(last_block[keys])

    guess_hash= previous_hash+ str(proof)
    hash= sha256(hash.encode('utf-8')).hexdigest()
    proof= proof+ 1
    while hash[0:2]!= '00':
        guess_hash = previous_hash + str(proof)
        hash = sha256(hash.encode('utf-8')).hexdigest()
        proof = proof + 1
        print(hash)
    return proof

def hash_block(last_block):
    previous_hash=''

    for keys in last_block:
        previous_hash= previous_hash+ str(last_block[keys])
    hash= sha256(json.dumps(previous_hash).encode('utf-8')).hexdigest()
    return hash

def mine_block():
    last_block= blockchain[-1]
    hashed_block= hash_block(last_block)
    proof= proof_of_work()

    block={
        'previous_hash': hashed_block ,
        'index':len(blockchain),
    'transaction': open_transactions
        , 'proof': proof
    }
    blockchain.append(block)
    print(blockchain)
    print(hashed_block)
    print(proof)
    return True
def verify_chain():
    for(index, block) in enumerate(blockchain):
        if index== 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index- 1]):
            print(block['previous_hash'])
            print(hash_block(blockchain[index-1]))
            print(block)
            print(blockchain[index- 1])
            return False
    return True


while True:
    I = input('Enter your choice')
    print('1 to recieve transactions')
    print('2 to mine block')
    print('3 to alter block')
    if I == '1':
        data = get_transaction()
        recipient, amount = data
        transaction = {'sender': owner,
                       'recipient': recipient,
                       'amount': amount}

        open_transactions.append(transaction)
        print(open_transactions)
        save_data()

    if I == '2':
        mine_block()
        open_transactions = []

    if I == '3':
        alter_block()

    if not verify_chain():
        print('Invalid block')
        break






