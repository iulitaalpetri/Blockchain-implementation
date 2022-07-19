from hashlib import sha256
# The SHA-256 is a hashing algorithm created by the NSA back in 2001 which takes an input
# of any size and converts it to an output of fixed size. The beauty of the SHA-256 is t
# hat the Output is close to impossible to decode thus ensuring security.
sender = 'Moeed'
genesis_block = {'previous_hash': 'XYZ',
                 'index': 0,
                 'transactions': [], 'proof': 0}
blockchain = [genesis_block]
open_transactions = []

def get_transaction():# the sender introduces the transaction amount and the receiver
    recipient = input('Enter your recipient')
    amount = input('Enter your amount')
    return (recipient,amount)

while True:
    I = input('Enter your choice')
    if I == '1':
        data = get_transaction()
        recipient, amount = data
        transaction = {'sender': sender,
                      'recipient': recipient,
                      'amount': amount}
        open_transactions.append(transaction)
        print(open_transactions)

def hash_block(last_block):
    previous_hash = ''

    for keys in last_block:
        previous_hash = previous_hash + str(last_block[keys])
    hash = sha256(json.dumps(previous_hash).encode('utf-8')).hexdigest()
    return hash