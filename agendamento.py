from tkinter.filedialog import askopenfilename
from docx import Document
from docx.shared import Inches
import pandas as pd

diretorio_tabela = askopenfilename()

nome_do_arquivo = input("Nome do arquivo: ")
data_missa = input("Data da missa: ")
hora_missa = input("Hora da missa: ")

df = pd.read_excel(diretorio_tabela, usecols="C,D", skiprows=7)
df = df["Nome"] + "" + df["Sobrenome"]

df = df.dropna()

df_list = df.values.tolist()

document = Document()
document.add_heading('Santa Missa ' + data_missa + " às " + hora_missa, 0)

tam = len(df_list)

for x in range(tam):
    document.add_paragraph(df_list[x], style ='List Bullet')

document.save(nome_do_arquivo)