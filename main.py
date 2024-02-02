from fpdf import FPDF
pdf = FPDF(orientation="P", unit="pt", format="A4")

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
    def __init__(self,name, days_of_stay) -> None:
        self.name = name
        self.days_of_stay = days_of_stay

    def pays(self, bill, flatmate_2):
        total_amount = bill.amount * (self.days_of_stay/(self.days_of_stay+flatmate_2.days_of_stay))
        return round(total_amount, 2)

class PdfGenerator:

    def __init__(self, file_name) -> None:
        self.file_name=file_name

    def create_receipt(self, flatmate_1, flatmate_2, bill):
        pdf.add_page(orientation='p')
        
        pdf.image("files\house.png", w=50, h=50)

        pdf.set_font(family="Arial", style="B", size=30)
        pdf.cell(w=0, h=70, align="C", txt="Flat Mate Bill", ln=1)

        pdf.set_font(family="Arial", size=15)
        
        pdf.cell(w=50, h=25, txt=f"{flatmate_1.name}", ln=0)
        pdf.cell(w=50, h=25, txt=f"{flatmate_1.pays(bill, flatmate_2)}", ln=1)
        
        pdf.cell(w=50, h=30, txt=f"{flatmate_2.name}", ln=0)
        pdf.cell(w=50, h=30, txt=f"{flatmate_2.pays(bill, flatmate_1)}", ln=1)
        
        pdf.output(self.file_name)
        


if __name__ == "__main__":
    monthly_bill = Bill(500, "December 2023")
    flatmate_1 = FlatMate("Rahul", 20)
    flatmate_2 = FlatMate("Vaidya", 23)

    pdf_generator = PdfGenerator("Decemember23_receipt.pdf")
    pdf_generator.create_receipt(flatmate_1, flatmate_2, monthly_bill)

