class Account:
    def __init__(self, name: str) -> None:
        """
        This should be used to set the default values for each account object. It should contain 2 private variables
        (account name, account balance), that should hold the account name and a balance of 0 respectively.

        Example: account_one = Account('John') is an account object whose account name = John and account balance = 0.
        """
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This should increment the account balance by the specified amount. If the amount is a negative number or 0,
        nothing should happen to the account balance (since you cannot deposit a negative amount of money or $0).
        Return the Boolean value True if the deposit transaction is successful and False if the transaction is
        unsuccessful (didn't change account balance).
        """
        if amount <= 0:
            return False
        else:
            self.__balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        This should decrement the account balance by the specified amount. If the amount is a negative number, 0,
        or more than the current account balance, nothing should happen to the account balance (since you cannot withdraw
        a negative amount, $0, and you cannot withdraw more than your current account balance).
        Return the Boolean value True if the deposit transaction is successful and False if the transaction is
        unsuccessful (didn't change account balance).
        """
        if amount <= 0 or self.__balance < amount:
            return False
        else:
            self.__balance -= amount
            return True

    def get_balance(self) -> float:
        """
        This should return the account balance.
        """
        return self.__balance

    def get_name(self) -> str:
        """
        This should return the account name.
        """
        return self.__name
