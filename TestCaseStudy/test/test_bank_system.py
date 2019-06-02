import unittest
from TestCaseStudy.app.bank_system import Account

'''
Są dwie klasy: Account i Card.
Metoda Account.get_owner powinna zwracać Imię  i nazwisko właściciela.
Metoda Account.get_balance powinna zwracać aktualny stan konta. 
Metoda Account.get_number powinna zwracać numer konta. Numer konta powinien być nadawny przez system.
Metoda Account.transfer powinna zmieniać stan konta o podaną kwotę
Odwołanie się do Card.owner powinno zwracać imie i nazwisko właściciela konta.
Metoda Card.check_pin powinna sprawdzić czy pin jest poprawny.
Metoda Card.get_account powinna zwrócić konto do którego karta jest „podpięta”
'''


# tworzę klase testową Account

class TestAcccount(unittest.TestCase):

    # Metoda Account.get_owner powinna zwracać Imię  i nazwisko właściciela.

    def test_whenAccountOnerCalled_thenOwnerIsReturned(self):
        # Given
        owner = "Bartlomiej Karaban"
        account = Account(amount=100, owner=owner)

        # When
        owner_recieved = account.get_owner()

        # Then

        self.assertEqual(owner, owner_recieved)
