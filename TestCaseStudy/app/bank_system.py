import random


class Account:

    def __init__(self, amount, owner):
        self._amount = amount
        self._owner = owner
        self._number = random.randint(1, 10000)

    def transfer(self, amount):
        self._amount += amount

    def __repr__(self):
        return f"{self._number}2"

    def get_balance(self):
        return self._amount

    def number(self):
        return self._number

    def get_owner(self):
        return self._owner


class Card:

    def __init__(self, account: Account, pin):
        self._account = account
        self._pin = pin

    def __repr__(self):
        return self._account.get_owner()

    def get_account(self):
        return self._account

    def check_pin(self, pin) -> bool:
        if self._pin == pin:
            return True
        else:
            return False


class CashMachine:

    def __init__(self, money_amount):
        self._money_amount = money_amount
        self._card = None
        self._pin_attempts = 0

    def insert_card(self, card: Card):
        self._card = card

    def withdraw(self, amount):
        if amount >= self._money_amount:
            self._card.get_account().transfer(amount)

    def enter_pin(self, pin):
        check_pin = self._card.check_pin(pin)
        if check_pin:
            return f"You can withdraw money from {self._card.get_account()}"
        if not check_pin:
            self._pin_attempts += 1
            return f"Pin is incorrect, {3 - self._pin_attempts} attempts left"
        if self._pin_attempts == 3:
            del self._card
            return f"Card will be destroyed"

    def retrieve_card(self):
        self._card = None