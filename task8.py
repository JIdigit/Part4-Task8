import moneyftm

cash = moneyftm.MoneyFmt(12345.1231212)
print(cash.dollar)
print(cash.update(11413.1232))
print(cash.repr())
print(cash.str())