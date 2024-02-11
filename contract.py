@storage_var
def balances(account: felt) -> felt:
    pass

@public
@external
def transfer(receiver: address, amount: felt):
    self.balances[msg.sender] -= amount
    self.balances[receiver] += amount

@storage_var
def balances(account: felt) -> felt:
    pass

@public
@external
def transfer(receiver: address, amount: felt):
    self.balances[msg.sender] -= amount
    self.balances[receiver] += amount

@storage_var
def escrowed_amount(depositor: address) -> felt:
    pass

@public
@external
def deposit():
    self.escrowed_amount[msg.sender] += msg.value

@public
@external
def withdraw(amount: felt):
    assert self.escrowed_amount[msg.sender] >= amount
    self.escrowed_amount[msg.sender] -= amount
    send(msg.sender, amount)


@storage_var
def escrowed_amount(depositor: address) -> felt:
    pass

@public
@external
def deposit():
    self.escrowed_amount[msg.sender] += msg.value

@public
@external
def withdraw(amount: felt):
    assert self.escrowed_amount[msg.sender] >= amount
    self.escrowed_amount[msg.sender] -= amount
    send(msg.sender, amount)


@storage_var
def highest_bidder() -> address:
    pass

@storage_var
def highest_bid() -> felt:
    pass

@public
@external
def bid():
    assert msg.value > self.highest_bid()
    send(self.highest_bidder(), self.highest_bid())
    self.highest_bidder = msg.sender
    self.highest_bid = msg.value


