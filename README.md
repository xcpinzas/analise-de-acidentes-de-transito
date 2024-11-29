# Analise-de-acidentes-de-transito

 Através dos dados disponibilizados pela Polícia Rodoviária Federal no período entre 2021 e 2024, foi realizada uma análise exploratória desses dados a fim de identificar possíveis insights. 
 
 Em um primeiro momento foi feita uma limpeza e preparação desses dados e depois foi realizada uma análise. Os principais gráficos e resultados são disponibilizados usando o framework Streamlit. 
## Estrutura do Repositório

Este repositório contém os seguintes diretórios e arquivos:

- **dashboard/**: 
  - `app.py`: Script principal que utiliza Streamlit para visualizar os dados.
  
- **notebook/**: 
  - `*.ipynb`: Jupyter Notebook que descreve as etapas para visualizar os dados.

- **requirements/**: 
  - `requirements.txt`: Arquivo com a lista de pacotes necessários para executar o projeto.

## Instalação

Para usar este projeto, primeiro certifique-se de ter instalado python 3.12.7

Depois disso, você deve:
1. Criar o ambiente virtual 
    ```
    python -m venv venv
    ```
2. Activar o ambiente virtual criado:

   Linux:
    ```
    source ./venv/bin/activate
    ```
 
   Windows:
   ```
   venv\bin\activate
   ```
2. Instalar os requisitos do modelo de projeto executando
    ```
    pip install -r requirements/requirement.txt
    ```
3. Executar o projeto:

    ```
    cd dashborad
    ```
    ```
    streamlit run app.py
    ```

