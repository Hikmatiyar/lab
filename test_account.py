import pytest
from account import Account


def test_account_init():
    account_one = Account('John')
    assert account_one.get_name() == 'John'
    assert account_one.get_balance() == 0


def test_account_deposit():
    account_one = Account('John')
    assert
