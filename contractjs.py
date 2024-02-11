# This is a simple example StarkNet smart contract

from starkware.starkware_utils.serialize import deserialize, serialize

# StarkNet contract state
@storage_var
def counter() -> felt:
    pass

# Initialize the counter
@public
@init
def initialize(initial_value: felt):
    self.counter = initial_value

# Increase the counter value
@public
@external
def increase(value: felt):
    self.counter += value

# Decrease the counter value
@public
@external
def decrease(value: felt):
    self.counter -= value

# Get the current counter value
@public
@external
def get_counter() -> felt:
    return self.counter
