from ex4.account import Account
def test_cash_out():
    bankaccount = Account('23', 'Paul', 400)
    bankaccount.cash_out(200)
    assert bankaccount.sum == 200
