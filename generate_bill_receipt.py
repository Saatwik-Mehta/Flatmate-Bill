import os
import webbrowser

from fpdf import FPDF

pdf = FPDF(orientation="P", unit="pt", format="A4")


class PdfGenerator:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def create_receipt(self, flatmate_1, flatmate_2, bill):
        pdf.add_page(orientation="p")

        pdf.image("files\house.png", w=50, h=50)

        pdf.set_font(family="Arial", style="B", size=30)
        pdf.cell(w=0, h=70, align="C", txt="Flat Mate Bill", ln=1)

        pdf.set_font(family="Arial", size=15)

        pdf.cell(w=100, h=25, txt=f"{flatmate_1.name}", ln=0)
        pdf.cell(
            w=150, h=25, txt=f"{flatmate_1.pays(bill, flatmate_2)}", ln=1, align="R"
        )

        pdf.cell(w=100, h=30, txt=f"{flatmate_2.name}", ln=0)
        pdf.cell(
            w=150, h=30, txt=f"{flatmate_2.pays(bill, flatmate_1)}", ln=1, align="R"
        )

        # As we are storing the bill in `monthly_bill` directory, we need to switch to it for any further operations.
        os.chdir("monthly_bill")
        pdf.output(self.file_name)
        webbrowser.open(self.file_name)
