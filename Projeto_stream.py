# app resultado de ações
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import timedelta, datetime #lib utilizada para utilizar o paramentro step

from pandas.io.pytables import performance_doc

#comando para executar o streamlit: "streamlit run Projeto_stream.py"
#comando para parar de rodar: "ctrl + c"
#OBS: EXECUTAR NO TERMINAL

#criar cabeçalho da pagina no streamlit
st.write("""
# Painel de Preço de Ações
O gráfico abaixo representa a evolução do preço de ações no período selecionado ao lado
""")

data_atual = datetime.now()
data_futura = data_atual + timedelta(days=1)
data_futura_formatada = data_futura.strftime("%Y-%m-%d")

#criando um decorator
@st.cache_data
def carregar_dados(empresa):
    texto_acoes = ' '.join(empresa)
    dados_acao = yf.Tickers(texto_acoes) #ticker é um registrador de cotações, ou seja, ele busca as cotações da empresa especificada
    precos_acao = dados_acao.history(period='1d', start='2000-01-01', end=data_futura_formatada) #history exibe o histórico de ações da empresa
    precos_acao = precos_acao["Close"] #Pegamos somente os dados de fechamento(close) da ação e retorna em formato de dataframe
    return precos_acao

@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv('IBOV.csv', sep =";")
    tickers = list(base_tickers['Código'])
    tickers = [item + '.SA' for item in tickers] #list comprehension
    return tickers

acoes = carregar_tickers_acoes() #colocamos '.SA' pois queremos no estado de SP
dados  = carregar_dados(acoes)

#preparar a visualisação dos dados


st.sidebar.header("Filtros") # 'st.sidebar' cria barra lateral, o metodo 'header' cria um titulo

#filtro de ações
lista_acoes = st.sidebar.multiselect('Escolha as ações que deseja visualizar', dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: 'Close'})

#filtro de datas #################

#criamos variaveis que contém a menor e maior data dentro de acordo com a coluna da nossa tabela dados.
#o medotod 'to_pydatetime()' converte o formato da data para datetime, que é lido pelo streamlit
data_inicial= dados.index.min().to_pydatetime()
data_final= dados.index.max().to_pydatetime()

#cirando um icone de intervalo de datas
intervalo_datas = st.sidebar.slider("Selecione o periodo", min_value=data_inicial,
                                    max_value=data_final,
                                    value=(data_inicial, data_final),#caso vc coloque só um parametro dentro de 'value' ele exibe no formato de uma data só(sem intervalo)
                                    step=timedelta(days=1)) #'step' define de quanto em quanto tempo varia o slidebar

#usamos o metodo 'loc' para filtrar as linhas da tabela e incluimos o intervalo que queremos filtrar dentro(no caso, o intervalo que o usuario colocar no slidebar)
dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]

#plotando grafico na pagina
grafico = st.line_chart(dados) #o gráfico é plotado de maneira "inteligente" pelo streamlit

texto_performance_ativos = "" #para o '\n' funcionar, deve haver dois espaços antes dele



if len(lista_acoes) == 0: #se a lista de ações(multiselect) for vazia, exibe todas as ações na performance
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={'Close': acao_unica})

#criando uma carterira, onde cada açao nela custa 1k
carteira = [1000 for acao in lista_acoes]
total_inicial_carteira = sum(carteira)

for i, acao in enumerate(lista_acoes):
    performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1 #performance = valor final/valor inicial - 1. O metodo 'iloc' permite localizar uma célula de acordo com a posição dele em uma lista
    performance_ativo = float(performance_ativo) #transformando o formato para numérico para o streamlit interpretar
    carteira[i] = carteira[i] * (1 + performance_ativo)

    #adicionando cor ao texto da performance
    if performance_ativo > 0:
        #sintaxe p/ mudar cor: ':cor[texto]'
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :green[{performance_ativo:.1%}]"
    elif performance_ativo < 0:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :red[{performance_ativo:.1%}]"
    else:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: {performance_ativo:.1%}"

total_final_carteira = sum(carteira)
performance_carteira = total_final_carteira / total_inicial_carteira - 1

#adicionando cor ao texto da performance
if performance_carteira > 0:
        #sintaxe p/ mudar cor: ':cor[texto]'
    texto_performance_carteira = f"Performance da carteira com todos ativos: :green[{performance_carteira:.1%}]"
elif performance_carteira < 0:
    texto_performance_carteira = f"Performance da carteira com todos ativos: :red[{performance_carteira:.1%}]"
else:
    texto_performance_carteira = f"Performance da carteira com todos ativos: [{performance_carteira:.1%}]"



st.write(f"""
### Performance dos ativos
Veja abaixo o quanto cada ativo obteve de crescimento no período especificado:

{texto_performance_ativos}

{texto_performance_carteira}
""")

st.caption("##### Nota: o percentual da carteira só é calculado caso todas as ações especificadas possuam dados históricos no período selecionado(diferente de NaN)")

st.caption("Desenvolvido por Vitor Alves.")