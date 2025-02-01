from fpdf import FPDF

class PDFGenerator:
    def __init__(self, file_name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.file_name = file_name

    def add_text(self, text, size=12):
        self.pdf.set_font("Arial", size)
        self.pdf.multi_cell(0, 10, txt=text, border=0, align='L')

    def save_pdf(self):
        self.pdf.output(self.file_name)

if __name__ == "__main__":
    pdf_file = "documento.pdf"

    generator = PDFGenerator(pdf_file)

    while True:
        text = input("Digite o texto para adicionar ao PDF (ou deixe em branco para parar): ")
        if not text:
            break
        generator.add_text(text)

    generator.save_pdf()
    print(f"PDF '{pdf_file}' gerado com sucesso!")