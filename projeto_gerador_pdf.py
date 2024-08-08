from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variáveis

cliente = input("Informe o nome do cliente\n")
consulta = input("Informe o tipo da consulta\n")
valor = float(input("Informe o valor da consulta\n"))
valor_msg = str(f"{valor:.2f}")
valor_extenso = num2words(valor, lang="pt-br").capitalize()
valor_extenso_msg = f"{valor_extenso} reais"
data = date.today()
dia = str(data.day).zfill(2)  # Adiciona zero à esquerda se necessário
mes = str(data.month).zfill(2)  # Adiciona zero à esquerda se necessário
ano = data.year

# 2 - Layout do Recibo

# Configurando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("dados/rec.jpg", x=0, y=0)

# Posicionando valores na tela
pdf.text(162, 45, valor_msg.replace(".", ","))
pdf.text(72, 86, cliente)
pdf.text(72, 112, valor_extenso_msg)
pdf.text(72, 137, consulta)
pdf.set_text_color(255, 255, 255)  # Muda a cor do texto
pdf.text(28.5, 193, str(dia))
pdf.text(48.5, 193, str(mes))
pdf.text(68.5, 193, str(ano))

# Gerando o PDF
nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}"
pdf.output(f"{nome_arquivo}.pdf")
print("Recibo gerado com sucesso!")
