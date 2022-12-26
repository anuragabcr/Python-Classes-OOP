import webbrowser

from fpdf import FPDF
class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, days, name):
        self.name = name
        self.days = days

    def pay(self, bill, mate):
        return bill.amount * (self.days / (self.days + mate.days))


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pay1 = str(round(flatmate1.pay(bill, flatmate2), 2))
        pay2 = str(round(flatmate2.pay(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("bill.png", h=40, w=30)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=15, style='B')
        pdf.cell(w=100, h=40, txt='Period: ', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=pay1, border=0, ln=1)

        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=pay2, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


bill = Bill(120, "March 2020")
john = Flatmate(20, "john")
marry = Flatmate(25, "Marry")
print(john.pay(bill, marry))
print(marry.pay(bill, john))

report = PdfReport("report.pdf")
report.generate(john, marry, bill)