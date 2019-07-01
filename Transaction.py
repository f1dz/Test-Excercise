import web3
from eth_account import Account
from web3 import Web3


class Transaction:

  testnet = 'https://ropsten.infura.io/v3/35dc5ccc706a4d3497a88028b65aa127'
  chainId = 3 # 1 : mainnet, 3 : ropsten 
  debug = False
  gas = 2000000

  def __init__(self, private_key, to, value):
    self.private_key = private_key
    self.to = to
    self.value = value
    self.w3 = Web3(Web3.HTTPProvider(self.testnet))
    self.account = Account.privateKeyToAccount(private_key)
    self.gas_price = self.w3.eth.gasPrice
    self.nonce = self.w3.eth.getTransactionCount(self.account.address)

  def send(self):
    signed = self.sign()
    tx = self.w3.eth.sendRawTransaction(signed)
    return tx.hex()
  
  def sign(self):
    detail = {
      'to': self.to,
      'value': (self.value - self.gas_price),
      'gasPrice': self.gas_price,
      'gas': self.gas,
      'nonce': self.nonce,
      'chainId': self.chainId
    }

    if(self.debug):
      print(detail)

    signed = self.w3.eth.account.signTransaction(detail, self.private_key)
    return signed.rawTransaction.hex()