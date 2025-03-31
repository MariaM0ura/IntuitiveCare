# Obejtivo : Extrair os dados do Anexo 1 e salvar em um arquivo CSV
#   Substituir as abreviações das colunas OD e AMB por seus nomes completos

import pdfplumber
import pandas as pd
import zipfile
import os

# Nome do arquivo PDF (ajuste conforme necessário)
PDF_ANEXO_I = "pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"  
CSV_SAIDA = "Rol_de_Procedimentos.csv"
ZIP_SAIDA = "Teste_Maria.zip"  # Substitua pelo seu nome

# Criar uma lista para armazenar os dados extraídos
dados = []

# Abrir o PDF e extrair tabelas de todas as páginas
print("[*] Extraindo tabelas do PDF...")
with pdfplumber.open(PDF_ANEXO_I) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                dados.append(linha)

# Criar um DataFrame e remover linhas vazias
df = pd.DataFrame(dados).dropna().reset_index(drop=True)

# Definir cabeçalho
df.columns = df.iloc[0]  # Define a primeira linha como cabeçalho
df = df[1:].reset_index(drop=True)  # Remove a primeira linha duplicada

# Substituir abreviações conforme legenda do rodapé
substituicoes = {"OD": "Consulta Odontológica", "AMB": "Atendimento Ambulatorial"}
df.replace(substituicoes, inplace=True)

# Salvar os dados estruturados em um CSV
df.to_csv(CSV_SAIDA, index=False, encoding='utf-8')

# Compactar o CSV em ZIP
print("[*] Compactando CSV em ZIP...")
with zipfile.ZipFile(ZIP_SAIDA, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(CSV_SAIDA)

print(f"✅ Arquivo ZIP criado: {ZIP_SAIDA}")
