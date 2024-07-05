from web3 import Web3

ganacheUrl = "HTTP://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganacheUrl))

class Account():
    def __init__(self):
        self.account = web3.eth.account.create()
        self.address = self.account.address

# Create a Wallet class
class Wallet():
    # Define checkConnection() method
    def checkConnection(self):
        # Check if you are connected to the ganacheUrl
        if web3.is_connected():
           # Return True
           return True
        # Else 
        else:
            # Return False
            return False
    