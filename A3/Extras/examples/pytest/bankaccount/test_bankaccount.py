from bankaccount import BankAccount


def test_insufficient_funds_on_withdraw():
    # Test case 1: Check if it's possible to withdraw 10 with insufficient funds
    assert BankAccount("test1").withdraw(10) == False
    # Test case 2: Check if it's possible to withdraw 100 with insufficient funds
    assert BankAccount("test2").withdraw(100) == False
    # Test case 3: Check if it's possible to withdraw 1000 with insufficient funds
    assert BankAccount("test3").withdraw(1000) == False


def test_sufficient_funds_on_withdraw():
    # Test case 1: Check if it's possible to withdraw 10 with sufficient funds
    assert BankAccount("test1").balance(10).withdraw(10) == True
    # Test case 2: Check if it's possible to withdraw 100 with sufficient funds
    assert BankAccount("test2").balance(100).withdraw(100) == True
    # Test case 3: Check if it's possible to withdraw 1000 with sufficient funds
    assert BankAccount("test3").balance(1000).withdraw(1000) == True

def test_negative_deposit():
    # Test case 1: Check if it's possible to deposit a negative 10 into the account
    assert BankAccount("test1").deposit(-10) == False
    # Test case 2: Check if it's possible to deposit a negative 100 into the account
    assert BankAccount("test2").deposit(-100) == False
    # Test case 3: Check if it's possible to deposit a negative 1000 into the account
    assert BankAccount("test3").deposit(-1000) == False


def test_positive_deposit():
    # Test case 1: Check if it's possible to deposit a positive 10 into the account
    assert BankAccount("test1").deposit(10) == True
    # Test case 2: Check if it's possible to deposit a positive 100 into the account
    assert BankAccount("test2").deposit(100) == True
    # Test case 3: Check if it's possible to deposit a positive 1000 into the account
    assert BankAccount("test3").deposit(1000) == True
