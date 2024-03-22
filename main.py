from flatmate_bill import Bill, FlatMate
from generate_bill_receipt import PdfGenerator


if __name__ == "__main__":
    amount_to_pay = int(input("Enter the bill amount: ₹ "))
    bill_period = input("Enter the bill period: ")
    monthly_bill = Bill(amount_to_pay, bill_period)
    flatmate1_name = input("Enter the name of first flatmate: ")
    flatmate1_days_of_stay = int(input("Enter days of stay of first flatmate: "))
    flatmate2_name = input("Enter the name of second flatmate: ")
    flatmate2_days_of_stay = int(input("Enter days of stay of second flatmate: "))
    flatmate_1 = FlatMate(flatmate1_name, flatmate1_days_of_stay)
    flatmate_2 = FlatMate(flatmate2_name, flatmate2_days_of_stay)

    pdf_generator = PdfGenerator(f"{bill_period.replace(' ', '_')}.pdf")
    pdf_generator.create_receipt(flatmate_1, flatmate_2, monthly_bill)
