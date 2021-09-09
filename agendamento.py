from tkinter.filedialog import askopenfilename
from docx import Document
import pandas as pd
import ntpath
import re

diretorio_tabela = askopenfilename()
nome_tabela = ntpath.basename(diretorio_tabela)

print(nome_tabela)

nome_do_arquivo = input("Nome do arquivo: ")
data_missa = input("Data da missa: ")
hora_missa = input("Hora da missa: ")

df = pd.read_excel(diretorio_tabela, usecols="C,D", skiprows=7)
df = df["Nome"] + "" + df["Sobrenome"]

df = df.dropna()

df_list = df.values.tolist()

document = Document()
document.add_heading('Santa Missa ' + data_missa + " às " + hora_missa, 0)

for x in df_list:
    document.add_paragraph(x, style ='List Bullet')

document.save(nome_do_arquivo + '.docx')

#([0-9]{7})\w