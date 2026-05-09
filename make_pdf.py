from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'DIY EEG Circuit Guide (TL074 + Single 9V Battery)', new_x="LMARGIN", new_y="NEXT", align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_pdf():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # 1. Schematic Page
    if os.path.exists('EEG_Schematic.png'):
        pdf.add_page(orientation='L')
        pdf.set_font('helvetica', 'B', 16)
        pdf.cell(0, 10, 'Formal Circuit Schematic', new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.image('EEG_Schematic.png', x=10, y=30, w=270)

    # 2. Realistic Layout Page
    if os.path.exists('EEG_Fritzing_Layout.png'):
        pdf.add_page(orientation='L')
        pdf.set_font('helvetica', 'B', 16)
        pdf.cell(0, 10, 'Fritzing-Style Breadboard Layout', new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.image('EEG_Fritzing_Layout.png', x=10, y=30, w=270)

    # 3. Documentation Pages
    files = ['DESIGN.md', 'ASSEMBLY.md', 'TESTING.md']
    for filename in files:
        if not os.path.exists(filename):
            continue

        pdf.add_page(orientation='P')
        pdf.set_font('helvetica', 'B', 16)
        pdf.cell(0, 10, filename.replace('.md', ''), new_x="LMARGIN", new_y="NEXT", align='L')
        pdf.ln(5)

        pdf.set_font('helvetica', '', 11)
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            content = content.replace('#', '').replace('**', '').replace('*', '').replace('$', '')
            content = content.replace('≈', '~').replace('Ω', ' Ohm').replace('µ', 'u')
            content = content.replace('⚠', 'WARNING:')
            content = content.encode('latin-1', 'ignore').decode('latin-1')
            pdf.multi_cell(0, 10, content)

    pdf.output('EEG_Circuit_Guide.pdf')

if __name__ == "__main__":
    create_pdf()
