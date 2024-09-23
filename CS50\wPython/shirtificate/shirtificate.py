from fpdf import FPDF

class PDF():
    def __init__(self, name):
        #pdf object
        self.pdf = FPDF()
        self.pdf.add_page()

        #header
        self.pdf.set_font("Times", "", 45)
        self.pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

        #shirt image
        self.pdf.image("shirtificate.png", w=self.pdf.epw)

        #shirt text
        self.pdf.set_font("Times", "", 25)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.cell(0, -230, f"{name} took CS50", align="C")

        #save
        self.pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    shirtificate = PDF(name)

if __name__ == "__main__":
    main()
