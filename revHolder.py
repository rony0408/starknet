from starkware.starkware_utils.serialize import serialize, deserialize

# StarkNet contract state
@storage_var
def user_holdings(user: felt) -> (felt, felt):
    pass

# StarkNet contract constants
HOLDING_NFT = 1
HOLDING_TOKEN = 2

# Initialize user holdings
@public
@external
def initialize():
    self.user_holdings[msg.sender] = (0, 0)

# Function to check and update user holdings
@private
@nonreentrant("update_holdings")
def update_holdings(user: address, holding_type: felt, duration: felt):
    holding_nft, holding_token = self.user_holdings[user]
    
    # Update holding based on duration
    if holding_type == HOLDING_NFT:
        holding_nft = duration
    elif holding_type == HOLDING_TOKEN:
        holding_token = duration
    
    # Calculate total holdings based on conditions
    if holding_nft < 6 and holding_token < 6:
        total_holdings = 20000
    elif holding_nft < 6 or holding_token < 6:
        total_holdings = 5000
    elif holding_nft < 3:
        total_holdings = 5000
    elif holding_nft < 1:
        total_holdings = 1000
    else:
        total_holdings = 0
    
    self.user_holdings[user] = (holding_nft, holding_token)

    # Transfer tokens to the user
    transfer(msg.sender, total_holdings)

# External function for NFT holding
@public
@external
def holdNFT(duration: felt):
    update_holdings(msg.sender, HOLDING_NFT, duration)

# External function for Token holding
@public
@external
def holdToken(duration: felt):
    update_holdings(msg.sender, HOLDING_TOKEN, duration)
