from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

def create_pdf():
    # Criação do arquivo PDF
    c = canvas.Canvas("hello_world.pdf", pagesize=letter)

    # Configurações de fonte
    c.setFont("Helvetica", 12)

    # Desenho da string "Hello World"
    c.drawString(1 * inch, 10 * inch, "Hello World")

    # Desenho de retângulos e elipse
    c.setFillColor(colors.red)
    c.rect(2 * inch, 8 * inch, 2 * inch, 1 * inch, fill=True, stroke=False)
    
    c.setFillColor(colors.green)
    c.rect(5 * inch, 8 * inch, 2 * inch, 1 * inch, fill=True, stroke=False)
    
    c.setFillColor(colors.blue)
    c.ellipse(3 * inch, 5 * inch, 7 * inch, 2 * inch, fill=True, stroke=False)

    # Salvando o arquivo PDF
    c.save()
    print("PDF criado com sucesso!")

# Chamada da função para criar o PDF
create_pdf()
