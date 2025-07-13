from typing import Dict, List, Optional, Any

class BankAccount():
    accounts: dict[str, 'BankAccount'] = {}

    def __init__(self,name: str, pin: int) -> None:
        self.name = name
        self.__pin = pin
        self.balance: float = 0

        BankAccount.accounts[self.name] = self

    def deposit(self, amount: float) -> None:
        """Метод пополнения баланса"""
        self.balance += amount
        print(f'✅Пополнение на сумму {amount} \n {self.get_balance()}\n')

    def withdraw(self, amount: float) -> None:
        """Метод снятие денег"""
        if self.balance >= amount:
            self.balance -= amount
            print(f'Снятие средств в размере {amount} \n {self.get_balance()}')
        else:
            print(f'❌Недостаточно средств❌\n {self.get_balance()} Попытка снять сумму {amount}\n')


    def transfer(self, recipient: str, summ: float) -> None:
        count_pin = 0
        while count_pin < 3:
            input_pin = int(input('Введите пин код'))
            if self.__pin == input_pin:

                if self.balance >= summ:
                    acc_recipient = BankAccount.accounts.get(recipient)
                    if acc_recipient:
                        self.balance -= summ
                        acc_recipient.deposit(summ)
                        print(f"💸 Перевод {summ}₽ от {self.name} к {acc_recipient.name}")
                        break
                    else:
                        print(f"❌ Получатель {recipient} не найден")
                        break
                else:
                    print("❌ Недостаточно средств")
                    break

            else:
                count_pin += 1
                print(f"Пин-код неверный. Осталось попыток: {3-count_pin}")
        else:
            print('❌Счет заблокирован❌')

    def get_balance(self):
        return f'💰 Баланс {self.name}: {self.balance}₽'

    def __str__(self):
        return f'🏦 Счёт {self.name}: {self.balance}₽'


igor = BankAccount('Игорь', 1234)
igor.deposit(200)
igor.withdraw(150)
print(igor)

vasya = BankAccount('Вася', 2222)
vasya.deposit(500)
vasya.transfer('Игорь', 288)

