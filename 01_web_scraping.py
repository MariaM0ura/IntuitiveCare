import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL da página
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PASTA_DOWNLOAD = "pdfs"
ARQUIVO_ZIP = "anexos_rol_ans.zip"

# Criar pasta para os PDFs
os.makedirs(PASTA_DOWNLOAD, exist_ok=True)

# Acessar a página
print("[*] Acessando página...")
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar os links dos Anexos I e II
print("[*] Buscando links dos anexos...")
links_pdf = []
for link in soup.find_all('a', href=True):
    href = link['href']
    texto = link.text.lower()
    if "anexo i" in texto or "anexo ii" in texto:
        if href.endswith(".pdf"):
            links_pdf.append(href if href.startswith("http") else f"https://www.gov.br{href}")

# Baixar os PDFs
print(f"[*] Baixando {len(links_pdf)} arquivos PDF...")
for url in links_pdf:
    nome_arquivo = url.split("/")[-1]
    caminho_arquivo = os.path.join(PASTA_DOWNLOAD, nome_arquivo)
    with open(caminho_arquivo, 'wb') as f:
        f.write(requests.get(url).content)
    print(f"  - Baixado: {nome_arquivo}")

# Compactar arquivos em .zip
print("[*] Compactando arquivos em ZIP...")
with ZipFile(ARQUIVO_ZIP, 'w') as zipf:
    for nome in os.listdir(PASTA_DOWNLOAD):
        zipf.write(os.path.join(PASTA_DOWNLOAD, nome), arcname=nome)

print(f"✅ Arquivo ZIP criado: {ARQUIVO_ZIP}")
