class Account:
    def __init__(self, name: str) -> None:
        self._name = name
        self._balance = 0

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self._balance:
            return False
        else:
            self._balance -= amount
            return True

    def get_balance(self) -> float:
        return self._balance

    def get_name(self) -> str:
        
        return self._name
