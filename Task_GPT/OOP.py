# ────────────────────────────────────────────────────────────────
# Файл: bank_account.py — Класс банковского аккаунта
# ────────────────────────────────────────────────────────────────

class BankAccount:
    """Класс, представляющий банковский счёт"""

    def __init__(self, name):
        """Конструктор класса"""
        self.name = name
        self.balance : float = 0.0  # Баланс на счету
        self.history: list[str] = []

    def __str__(self):
        return self.name

    def deposit(self, amount: float):
        """Вносим депозит"""
        self.balance  += amount
        self.history.append(f'Пополнено {amount}')
        print(f'Ложим депозит {amount} в банк. Текущий баланс {self.balance}')


    def withdraw(self, amount: float):
        """Снимаем с баланса"""
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f'Снято {amount}')
            print(f'Снимаем сумму: {amount}. Текущий баланс {self.balance}')
        else:
            print("Недостаточно средств.")


    def get_balance(self) -> float:
        """Запрос баланса"""
        return self.balance

    def get_history(self):
        return self.history

    def transfer_to(self, other_account, amount: float):
        if self.get_balance() >= amount:
            self.withdraw(amount)
            self.history.append(f'Переведено {amount} -> {other_account}')

            other_account.history.append(f'Перевод {amount} от {self}')
            other_account.deposit(amount)


class SavingsAccount(BankAccount):
    def __init__(self,name,  interest_rate):
        super().__init__(name)
        self.interest_rate = interest_rate

    def apply_interest(self, ):
        """Начисляем проценты"""
        self.balance += (self.balance / 100) *  self.interest_rate
        self.history.append(f'Начисленно:{ self.interest_rate}%')
        print(f'Начислены проценты: { self.interest_rate}%. Новый баланс: {self.balance}')


ac1 = BankAccount('Вася')
ac2 = BankAccount('Петя')

ac1.deposit(1000)

ac1.transfer_to(ac2, 300)

print(ac1.get_balance())
print(ac2.get_balance())

print(ac1.get_history())
print(ac2.get_history())



