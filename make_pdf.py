from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'DIY EEG Guide (TL074 + 9V)', new_x="LMARGIN", new_y="NEXT", align='C')

def create_pdf():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    for f in ['EEG_Schematic.png', 'EEG_Fritzing_Layout.png']:
        if os.path.exists(f):
            pdf.add_page(orientation='L')
            pdf.image(f, x=10, y=30, w=270)
    for filename in ['DESIGN.md', 'ASSEMBLY.md', 'TESTING.md', 'CONNECTIONS.md']:
        if not os.path.exists(filename): continue
        pdf.add_page()
        pdf.set_font('helvetica', 'B', 16)
        pdf.cell(0, 10, filename.replace('.md', ''), new_x="LMARGIN", new_y="NEXT", align='L')
        pdf.ln(5)
        pdf.set_font('helvetica', '', 11)
        with open(filename, 'r') as f:
            pdf.multi_cell(0, 10, f.read().replace('#', '').replace('*', ''))
    pdf.output('EEG_Circuit_Guide.pdf')

if __name__ == "__main__": create_pdf()
