# Desafio Intuitive Care

## Visão Geral
Este repositório contém diferentes módulos para extração, transformação, teste de dados e visualização utilizando Vue.js. Cada módulo é independente e deve ser executado separadamente.

## Estrutura do Projeto

```
IntuitiveCare/
├── .venv/                   # Ambiente virtual Python
├── anexos/                  # Arquivos complementares
├── database/                # Banco de dados
├── pdfs/                    # Relatórios e documentos PDF
├── questão 1/
│   ├── 01_web_scraping.py   # Script para web scraping
├── questão 2/
│   ├── 02_Tranformação_de_Dados.py  # Transformação de dados
├── questão 3/
│   ├── 03_teste_banco_de_dados.ipynb  # Testes com banco de dados
├── questão 4/
│   ├── vue-operadoras/       # Aplicativo Vue.js para visualização de dados
├── node_modules/            # Dependências do Node.js
├── public/                  # Arquivos públicos do Vue.js
├── src/                     # Código-fonte do Vue.js
├── app.py                   # Script principal do backend
├── babel.config.js          # Configuração do Babel
├── jsconfig.json            # Configuração do JavaScript
├── package.json             # Dependências do projeto Vue.js
├── package-lock.json        # Versões exatas das dependências
├── README.md                # Documentação do projeto
├── Relatorio_cadop.csv      # Dados analisados
├── vue.config.js            # Configuração do Vue.js
```

## Configuração e Execução
Cada módulo pode ser executado separadamente conforme descrito abaixo:

### Questão 1 - Web Scraping
```bash
python questao\ 1/01_web_scraping.py
```

### Questão 2 - Transformação de Dados
```bash
python questao\ 2/02_Tranformacao_de_Dados.py
```

### Questão 3 - Testes com Banco de Dados
Abrir o arquivo Jupyter Notebook e rodar os códigos:
```bash
jupyter notebook questao\ 3/03_teste_banco_de_dados.ipynb
```

### Questão 4 - Aplicativo Vue.js
Instalar dependências e rodar o servidor Vue.js:
para executar o frontend:
```bash
cd questao\ 4/vue-operadoras
npm install
npm run serve
```
para executar o backend:
```bash
cd questao\ 4/vue-operadoras
python app.py
```

## Dependências
- Python 3.8+
- Node.js 16+
- Vue.js 3
- Pandas, Requests (para Python)
- Jupyter Notebook (para execução dos testes)



