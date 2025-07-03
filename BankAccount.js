// BankAccount.js
// Simple checking account with deposit and withdraw methods (ES2022)

class BankAccount {
  #balance;
  constructor(name, balance = 0.0) {
    this.name = name;
    this.#balance = balance;
  }

  deposit(amount) {
    if (amount <= 0) {
      throw new Error('Deposit must be positive');
    }
    this.#balance += amount;
  }

  withdraw(amount) {
    if (amount <= 0) {
      throw new Error('Withdraw must be positive');
    }
    if (amount > this.#balance) {
      throw new Error('Insufficient funds');
    }
    this.#balance -= amount;
    return amount;
  }

  toString() {
    return `${this.name}: $${this.#balance.toFixed(2)}`;
  }
}

export default BankAccount;
