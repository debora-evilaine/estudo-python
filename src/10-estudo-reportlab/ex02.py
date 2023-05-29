from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_pdf():
    doc = SimpleDocTemplate("meu_documento.pdf")

    # Obter os estilos de amostra
    styles = getSampleStyleSheet()

    # Definir o título com fonte de 16pt
    title_style = styles['Title']
    title_style.fontSize = 16
    title = Paragraph("<b>Meu Título</b>", title_style)

    # Definir o estilo dos parágrafos com fonte de 12pt
    paragraph_style = styles['Normal']
    paragraph_style.fontSize = 12
    
    p1_style = styles['Heading1']
    p1_style.fontSize = 15
    p1_style.fontName = 'Times-Roman'
    
    p2_style = styles['Heading2']
    p2_style.fontSize = 25
    p2_style.fontName = 'Helvetica'
    

    # Definir o primeiro parágrafo
    paragraph1 = Paragraph("Este é o primeiro parágrafo.", paragraph_style)

    # Definir o espaço entre o título e o primeiro parágrafo
    space1 = Spacer(1, 20)

    # Definir o segundo parágrafo
    paragraph2 = Paragraph("Este é o segundo parágrafo.", paragraph_style)

    # Definir o espaço entre os parágrafos
    space2 = Spacer(1, 15)
    
    paragraph3 = Paragraph("Este parágrafo foi adicionado no excerício 01, com espaçamento de 25pts e fonte 15pts.",p1_style)

    space3 = Spacer(1, 25)
    
    paragraph4 = Paragraph("Este parágrafo também foi adicionado no exercício 01, com espaçamento de 15 pts e fonte 25pts.",p2_style)

    space4= Spacer(1, 15)


    # Criar a lista de elementos a serem adicionados ao documento
    elements = [title, space1, paragraph1, space2, paragraph2, space3, paragraph3, space4, paragraph4]

    # Adicionar os elementos ao documento
    doc.build(elements)

    print("PDF criado com sucesso!")

# Chamada da função para criar o PDF

