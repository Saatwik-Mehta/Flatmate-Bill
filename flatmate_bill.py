class Bill:
    """
    Bill generated for the monthly period
    """

    def __init__(self, amount, month) -> None:
        self.amount = amount
        self.month = month


class FlatMate:
    """
    This class will generate the amount that each flatmate will pay.
    """

    def __init__(self, name, days_of_stay) -> None:
        self.name = name
        self.days_of_stay = days_of_stay

    def pays(self, bill, flatmate_2):
        total_amount = bill.amount * (
            self.days_of_stay / (self.days_of_stay + flatmate_2.days_of_stay)
        )
        return round(total_amount, 2)
