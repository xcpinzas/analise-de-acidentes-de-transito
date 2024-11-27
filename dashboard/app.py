# Imports necessários
from streamlit_option_menu import option_menu
from PIL import Image


import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


############################################################################################################
########################################## ESTILO DA PÁGINA ################################################
############################################################################################################
# Configurações globais
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Configuração da página
st.set_page_config(
    page_title="Análise Exploratória - Acidentes de Trânsito",
    layout="wide"
)

# Estilo personalizado
PAGE_STYLE = '''
<style>
    p {
        text-align: justify;
    }
    .css-1vq4p4l {
        padding: 1.5rem 1rem 1.5rem;
    }
</style>
'''
st.markdown(PAGE_STYLE, unsafe_allow_html=True)

############################################################################################################
############################################## MENU ########################################################
############################################################################################################

# Logo e menu lateral
logo = Image.open('logo2.jpeg')
st.sidebar.image(logo, use_container_width=True)

with st.sidebar:
    selected_option = option_menu(
        "Análise Exploratória Acidentes De Trânsito",
        ["Sobre o App", "Filtros"],
        icons=['house', 'funnel'],
        menu_icon="app-indicator",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#F0F2F6"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "margin": "0px", "--hover-color": "#ff8585"},
            "nav-link-selected": {"background-color": "#DC0000"},
        }
    )
############################################################################################################
##################################### IMPORTANDO DATASET ###################################################
############################################################################################################
# Carregamento do dataset
DATA_PATH = '../csv/dados_2021_a_2024.csv'
PLANILHA_PRINCIPAL = 'Acidentes de Trânsito 2021-2024'

uploaded_data = st.sidebar.file_uploader("Upload Dataset", type=["csv", "xls"], key='new_data')
dataset_name = st.sidebar.text_input("Nome da planilha", value=PLANILHA_PRINCIPAL)

@st.cache_data(max_entries=50)
def load_data(file_path):
    return pd.read_csv(file_path)

data = load_data(uploaded_data if uploaded_data else DATA_PATH)
############################################################################################################
######################################## INÍCIO DAS PÁGINAS ################################################
############################################################################################################


############################################################################################################
######################################### PÁGINA 1 - SOBRE #################################################
############################################################################################################
    
## Page 1 - APRESENTAÇÃO
# Exibição de informações com base na seleção do menu
if selected_option == "Sobre o App":
    st.markdown("""
        <style> .font { font-size:35px; font-family: 'Cooper Black'; color: #DC0000;} </style>
    """, unsafe_allow_html=True)
    st.markdown("## <span style='color:#DC0000'>Sobre o Aplicativo</span>", unsafe_allow_html=True)
    st.write("""
        Dashboard desenvolvido pelos residentes Xander Cortez Pinzas e Lucas Gabriel dos Santos do Hub de IA do Senai - Londrina.
    """)
############################################################################################################
######################################### PÁGINA 2 - FILTROS ###############################################
############################################################################################################

# Page 2 - FILTROS

elif selected_option == "Filtros":
    st.markdown("""
        <style> .font { font-size:35px; font-family: 'Cooper Black'; color: #DC0000;} </style>
    """, unsafe_allow_html=True)
    st.markdown("## <span style='color:#DC0000'>Seleção de Características</span>", unsafe_allow_html=True)

    # Exibição do DataFrame agrupado por ano
    st.subheader("Busca por Ano")
    acidentes_por_ano = data.groupby('Ano').size().reset_index(name='Números de Acidentes')
    st.dataframe(acidentes_por_ano, use_container_width=True)
    
    st.subheader("Frequência de Acidentes por Estado")    
    estados = sorted(data['uf'].unique())
    uf = st.selectbox('Selecione um Estado:', estados)
    df_agrupado = data.groupby(['uf', 'Ano']).sum().reset_index()
    df_filtrado = df_agrupado[df_agrupado['uf'] == uf]
    campos_desejados = ['Ano','dia_semana', 'municipio']
    st.dataframe(df_filtrado[campos_desejados], use_container_width=True)
    
###########################################################################################################
############################################# FUNÇÕES DE PLOT ##############################################
############################################################################################################
    # Gráfico de acidentes por estado
    st.subheader("Gráfico de Acidentes por Estado")
    freq_por_estado = data['uf'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=freq_por_estado.index,
        y=freq_por_estado.values,
        hue=freq_por_estado.index,
        palette="coolwarm",
        dodge=False,
        legend=False
    )
    plt.title("Números de Acidentes por Estado", fontsize=16)
    plt.xlabel("Estado", fontsize=12)
    plt.ylabel("Número de Acidentes", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Gráfico das 10 causas principais de acidentes
    st.subheader("Maiores Causas de Acidentes")
    top_causas = data['causa_acidente'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=top_causas.values,
        y=top_causas.index,
        hue=top_causas.index,
        palette="coolwarm",
        dodge=False,
        legend=False
    )
    plt.title("Top 10 Causas Mais Comuns de Acidentes", fontsize=16)
    plt.xlabel("Número de Acidentes", fontsize=12)
    plt.ylabel("Causa", fontsize=12)
    plt.tight_layout()
    st.pyplot(plt)

    # Gráfico de acidentes por hora do dia
    st.subheader("Períodos e Horários de Acidentes")
    data['data_completa'] = pd.to_datetime(data['data_inversa'] + ' ' + data['horario'])
    data['horas'] = data['data_completa'].dt.hour
    acidentes_por_hora = data['horas'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=acidentes_por_hora.index, y=acidentes_por_hora.values, marker="o", color="blue")
    plt.title("Acidentes por Hora do Dia", fontsize=16)
    plt.xlabel("Hora do Dia", fontsize=12)
    plt.ylabel("Número de Acidentes", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

    # Gráfico de acidentes por dia da semana
    st.subheader("Acidentes por Dia da Semana")
    acidentes_por_dia = data['dia_semana'].value_counts().reindex(
    ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo' ])
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=acidentes_por_dia.index, y=acidentes_por_dia.values, marker="o", color="blue")
    plt.title("Acidentes por Dia da Semana", fontsize=16)
    plt.xlabel("Dia da Semana", fontsize=12)
    plt.ylabel("Número de Acidentes", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)


    # Gráfico de condições climáticas
    st.subheader("Condições Climáticas e Número de Acidentes")
    cond_clim_freq = data['condicao_metereologica'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=cond_clim_freq.values,
        y=cond_clim_freq.index,
        hue=cond_clim_freq.index,
        palette="coolwarm",
        dodge=False,
        legend=False
    )
    plt.title("Distribuição de Acidentes por Condições Climáticas", fontsize=16)
    plt.xlabel("Número de Acidentes", fontsize=12)
    plt.ylabel("Condições Climáticas", fontsize=12)
    plt.tight_layout()
    st.pyplot(plt)
