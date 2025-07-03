class BankAccount:
    """Simple checking account with deposit and withdraw."""
    def __init__(self, name: str, balance: float = 0.0):
        self._name = name
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return amount

    def __repr__(self) -> str:
        return f"{self._name}: ${self._balance:.2f}"

import pytest

def test_deposit_valid():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc._balance == 150
    acc.deposit(0.01)
    assert acc._balance == 150.01

def test_deposit_invalid():
    acc = BankAccount("Bob", 10)
    with pytest.raises(ValueError, match="Deposit must be positive"):
        acc.deposit(0)
    with pytest.raises(ValueError, match="Deposit must be positive"):
        acc.deposit(-5)

def test_withdraw_valid():
    acc = BankAccount("Carol", 200)
    amt = acc.withdraw(50)
    assert amt == 50
    assert acc._balance == 150
    amt2 = acc.withdraw(150)
    assert amt2 == 150
    assert acc._balance == 0

def test_withdraw_invalid():
    acc = BankAccount("Dan", 100)
    with pytest.raises(ValueError, match="Withdraw must be positive"):
        acc.withdraw(0)
    with pytest.raises(ValueError, match="Withdraw must be positive"):
        acc.withdraw(-1)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(101)
    acc.withdraw(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(1)

def test_repr():
    acc = BankAccount("Eve", 42.5)
    assert repr(acc) == "Eve: $42.50"
    acc2 = BankAccount("Zed")
    assert repr(acc2) == "Zed: $0.00"