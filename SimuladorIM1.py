import pandas as pd
import streamlit as st
import base64

# Configuração do layout
st.set_page_config(layout="wide")


# ------------------ LINK DE ORIGEM DO ÍCONE DE DOWLOAD ----------------#


st.markdown(
    """
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap">
    <style>
    .material-symbols-outlined {
      font-variation-settings:
      'FILL' 0,
      'wght' 400,
      'GRAD' 0,
      'opsz' 24;
      font-size: 32px;
      color: #333333;
      vertical-align: middle; /* Centraliza verticalmente */
    }
    </style>
        """,
    unsafe_allow_html=True
)

# ---------------------------- // ESTILOS PARA O CABEÇALHO E IMPUTS // ---------------------------------------------------- #

# Injetando CSS para estilizar o background principal, inputs, expanders e tabelas
st.markdown(
"""
    <style>
    /* Alteração do background principal com gradiente e imagem */
    .stApp {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)),
                    url('https://i.postimg.cc/021cV8dz/Vibra-Wallpaper2.png');
        background-size: cover; /* Ajusta a imagem para cobrir todo o fundo */
        background-attachment: fixed; /* A imagem fica fixa no fundo ao rolar a página */
    }

    /* Estilo para o contêiner externo dos inputs com desfoque e opacidade */
    .stTextInput, .stNumberInput {
        background-color: rgba(255, 255, 255, 0.2); /* Fundo branco com opacidade */
        border-radius: 20px;
        padding: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Sombra suave */
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Estilo para a área de entrada de texto interno */
    .stTextInput > div > input, .stNumberInput > div > input {
        background-color: rgba(255, 255, 255, 0);
        color: #333333;
        border: none;
        padding: 5px 10px;
        font-weight: bold;
    }

    /* Estilo para o texto do placeholder */
    .stTextInput > div > input::placeholder, .stNumberInput > div > input::placeholder {
        color: #333333; /* Cor do texto de dica */
        opacity: 0.7; /* Ajuste da opacidade do placeholder */
    }

    /* Estilo para o label (título) dos inputs */
    label {
        color: #333333 !important; /* Força a cor do texto dos labels */
        font-size: 16px; /* Ajusta o tamanho do texto do label */
    }


/* Estilo para o contêiner do slider com desfoque e opacidade */
    .stSlider > div {
        background-color: rgba(255, 255, 255, 0.2); /* Fundo branco com opacidade */
        border-radius: 20px; /* Bordas arredondadas */
        padding: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Sombra suave */
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Estilo para o preenchimento do slider */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #f28d35, #f2c879); /* Gradiente de preenchimento */
        border-radius: 20px; /* Bordas arredondadas */
    }

    /* Estilo para o botão circular do slider */
    .stSlider > div > div > div > div > div {
        background-color: #ffffff !important; /* Cor do indicador */
        border-radius: 50%; /* Botão circular */
        width: 20px;
        height: 20px;
    }

    

    /* Estilo para o label do slider */
    .stSlider label {
        color: #333333 !important; /* Cor do texto do label */
        font-size: 16px;
        font-weight: bold;
    }

    /* Estilo para os textos das marcas do slider */
    .stSlider span {
        color: #333333 !important;
        opacity: 0.7;
    }




    /* Estilização do título */
    .stMarkdown h1 {
        color: #1f2d3d;
        font-weight: bold;
        text-align: center;
    }



   </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------- // TÍTULO DA PÁGINA // ---------------------------------- #
st.markdown(
    """
<style>
    /* Importando a fonte Quicksand */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;600&display=swap');

    /* Aplicando a fonte ao título */
    .custom-title {
        font-family: 'Roboto', sans-serif;
        color: #000000;
        font-size: 35px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 0.1px; /* Ajusta o espaço entre o título e a linha */
    }

    /* Linha abaixo do título */
    .custom-title-line {
        width: 35%;
        margin: 0 auto 20px auto; /* Centraliza a linha e adiciona espaçamento abaixo dela */
        border: 0.3px solid rgba(242, 131, 107, 0.5);
    }
</style>

<div style="text-align: center;">
    <h1 class="custom-title">Simulador de Financiamento Imobiliário</h1>
    <hr class="custom-title-line">
</div>


    """,
    unsafe_allow_html=True
)



# ------------------------------------------------------------------------------------------------------------------ #



# Carrega a base de dados da planilha de dados financeiros e do INCC
caminho_planilha = 'Matriz.xlsx'
dados = pd.read_excel(caminho_planilha)
dados = dados[dados["RENDA"] >= 2900]  # Filtra valores de renda a partir de 2900


incc_data = pd.read_csv('incc_data.csv')  # Lê o arquivo CSV atualizado com o valor de INCC acumulado   
itbi_registro_df = pd.read_excel('ITBI_Registro.xlsx', sheet_name='Tabela Cartório')  # Base de ITBI e Registro

# Convertendo a coluna 'Unnamed: 1' para float, ignorando erros
itbi_registro_df['Unnamed: 1'] = pd.to_numeric(itbi_registro_df['Unnamed: 1'], errors='coerce')


# Agrupando os campos em colunas para um layout mais compacto
_, col1, col2, col3, _ = st.columns([0.3, 0.2, 0.2, 0.2, 0.3])

with col1:
    # Entrada para valor do imóvel
    valor_imovel = st.number_input("Insira o valor do imóvel:", min_value=0.0, step=1000.0, format="%.0f")

with col2:
    # Entrada para percentual do sinal
    percentual_sinal = st.number_input("Percentual do sinal (%)", min_value=0, max_value=100, step=1)
    percentual_sinal_decimal = percentual_sinal / 100  # Converte para decimal para uso nos cálculos


with col3:
    # Filtro para a coluna 'Comprometimento' usando uma régua
    comprometimento_limite = st.slider("Defina o percentual de comprometimento", min_value=0.01, max_value=100.0, value=(15.0, 22.0), step=0.1, format="%d%%")


# Função para obter o último valor de "Acumulado 12 meses" no arquivo de INCC
def obter_incc_acumulado():
    ultimo_acumulado = incc_data["Acumulado 12 meses"].iloc[-1]
    incc_acumulado = float(ultimo_acumulado.replace("%", "").replace(",", ".")) / 100
    return incc_acumulado

# Função para calcular o ITBI e Registro com base no valor do imóvel
def calcular_itbi_registro(valor_imovel):
    faixa = itbi_registro_df[itbi_registro_df['Unnamed: 1'] <= valor_imovel]['Total.1'].max()
    if pd.isna(faixa):
        st.warning("Faixa não encontrada para o valor do imóvel.")
        return 0, 0
    itbi = valor_imovel * 0.02  # Aplica 2% sobre o valor total do imóvel como ITBI
    registro = valor_imovel * 0.01  # Aplica 1% sobre o valor total do imóvel como Registro
    return itbi, registro

# ---------------------------------- // FORMATAÇÃO DE DADOS DAS TABELAS // ----------------------------------------------------------#

# ------------------------->> Função para formatação de valores monetários e percentuais <<------------------------------------------#

def formatar_valores(df):

    # Defina as colunas que devem receber o formato de moeda (com "R$")
    colunas_moeda = [
        "Financiamento",
        "Renda", 
        "Subsidio", 
        "FGTS*", 
        "Finan. + Subs + FGTS",
        "Máximo Financiamento (80%)", 
        "Recursos Próprios**", 
        "Sinal***",
        "Pró-Soluto", 
        "Parcela Obra (24x)",

        "Valor de Sinal (INCC)",
        "Pró-Soluto (INCC)", 
        "Valor Parcela 24m (INCC)", 
        
        "Valor Sem Documentação",
        "Recursos Próprios (SD)", 
        "Valor Sinal (SD)", 
        "Pró-Soluto (SD)",
        "Valor Parcela 24m (SD)", 
        "Valor Original do Imóvel",
        
        "Valor Original do Imóvel (INCC)", 
        "Valor Sem Documentação (INCC)",
        
        "Recursos Próprios (SD INCC)", 
        "Valor Sinal (SD INCC)",
        "Pró-Soluto (SD INCC)", 
        "Valor Parcela 24m (SD INCC)"
    ]

   
    # Defina as colunas que devem receber o formato de porcentagem (com "%")
    colunas_percentual = [
        "Taxa %", 
        "% Pró-Soluto", 
        "% Pró-Soluto (INCC)", 
        "Comprometimento (%)", 
        "Comprometimento (INCC) (%)", 
        "% Pró-Soluto (SD)", 
        "% Pró-Soluto (SD INCC)", 
        "Comprometimento (SD) (%)", 
        "Comprometimento (SD INCC) (%)"
    ]

    # Aplique a formatação nas colunas de moeda
    for coluna in colunas_moeda:
        if coluna in df.columns:
            df[coluna] = df[coluna].map(lambda x: f"R$ {x:,.0f}".replace(",", "."))

    # Aplique a formatação nas colunas de percentual
    for coluna in colunas_percentual:
        if coluna in df.columns:
            df[coluna] = df[coluna].map(lambda x: f"{x:.2f}%")

   
    
    return df

# ------------------------------------------------------------------------------------------------------------------ #


# Função de cálculo para todas as rendas, considerando a projeção de INCC
def calcular():
    # Obtém o INCC acumulado dos últimos 12 meses
    incc_acumulado = obter_incc_acumulado()
    valor_imovel_incc = valor_imovel * (1 + incc_acumulado)
    taxa_incc_percentual = incc_acumulado * 100

    # Cálculo do ITBI e Registro para os valores originais e com INCC
    itbi, registro = calcular_itbi_registro(valor_imovel)
    itbi_incc, registro_incc = calcular_itbi_registro(valor_imovel_incc)

    resultados, resultados_incc, resultados_sem_documentacao, resultados_sem_documentacao_incc = [], [], [], []

    # Usar uma renda de referência para o cálculo fixo de `recursos_proprios` e `valor_sinal`
    renda_referencia = dados['RENDA'].iloc[0]
    capacidade_maxima_referencia = dados.loc[dados['RENDA'] == renda_referencia, 'FINANCIAMENTO NOVO 360 MESES'].values[0]
    subsidio_atual_referencia = dados.loc[dados['RENDA'] == renda_referencia, 'SUBSIDIO ATUAL'].values[0]

    # Calcula `recursos_proprios` e `valor_sinal` usando a renda de referência
    total_financiamento_referencia = capacidade_maxima_referencia + (renda_referencia * 3) + subsidio_atual_referencia
    recursos_proprios = valor_imovel - total_financiamento_referencia
    valor_sinal = percentual_sinal_decimal * valor_imovel  # Calculado uma vez fora do loop


    # Loop para calcular os valores com base nas rendas disponíveis
    for renda_escolhida in dados['RENDA'].unique():
        taxa_juros = dados.loc[dados['RENDA'] == renda_escolhida, 'TAXA DE JUROS'].values[0]
        capacidade_maxima = dados.loc[dados['RENDA'] == renda_escolhida, 'FINANCIAMENTO NOVO 360 MESES'].values[0]
        subsidio_atual = dados.loc[dados['RENDA'] == renda_escolhida, 'SUBSIDIO ATUAL'].values[0]
        
        # Calcula os valores variáveis específicos para cada `renda_escolhida`
        fgts = renda_escolhida * 3
        total_financiamento = capacidade_maxima + fgts + subsidio_atual
        max_finan_80 = valor_imovel * 0.8
        recursos_proprios = valor_imovel - total_financiamento
        if recursos_proprios < 0:
            recursos_proprios = 0

        valor_sinal = percentual_sinal_decimal * valor_imovel
        if valor_sinal >= recursos_proprios:
            valor_sinal = recursos_proprios

        pro_soluto = recursos_proprios - valor_sinal   
        valor_parcela_24m = pro_soluto / 24
        comprometimento = valor_parcela_24m / renda_escolhida
        percentual_pro_soluto = (pro_soluto / valor_imovel) * 100

        
    
        resultados.append({
            "Renda": renda_escolhida,
            "Taxa %": taxa_juros * 100,
            "Finan. + Subs + FGTS": round(total_financiamento,0),
            "Financiamento": round(capacidade_maxima,0),
            "Subsidio": round(subsidio_atual, 0),
            "FGTS*": round(fgts, 0),
            "Recursos Próprios**": round(recursos_proprios, 0),
            "Sinal***": round(valor_sinal, 0),
            "Pró-Soluto": round(pro_soluto, 0),
            "% Pró-Soluto": percentual_pro_soluto,
            "Parcela Obra (24x)": round(valor_parcela_24m, 0),
            "Comprometimento (%)": comprometimento * 100
        })

        max_finan_80_incc = valor_imovel_incc * 0.8
        recursos_proprios_incc = valor_imovel_incc - total_financiamento
        if recursos_proprios_incc < 0:
            recursos_proprios_incc = 0

        valor_sinal_incc = percentual_sinal_decimal * valor_imovel_incc
        if valor_sinal_incc >= recursos_proprios_incc:
            valor_sinal_incc = recursos_proprios_incc

        pro_soluto_incc = recursos_proprios_incc - valor_sinal_incc
        valor_parcela_24m_incc = pro_soluto_incc / 24
        comprometimento_incc = valor_parcela_24m_incc / renda_escolhida

        resultados_incc.append({
            "Renda": renda_escolhida,
            "Taxa %": taxa_juros * 100,
            "Finan. + Subs + FGTS": total_financiamento,
            "Financiamento": capacidade_maxima,
            "Subsidio": subsidio_atual,
            "FGTS*": fgts,
            "Recursos Próprios**": recursos_proprios_incc,
            "Sinal***": valor_sinal_incc,
            "Pró-Soluto": pro_soluto_incc,
            "% Pró-Soluto": comprometimento_incc * 100,
            "Parcela Obra (24x)": valor_parcela_24m_incc,
            "Comprometimento (%)": comprometimento_incc * 100
        })

        valor_sem_documentacao = valor_imovel - (itbi + registro)
        recursos_proprios_sd = valor_sem_documentacao - total_financiamento
        if recursos_proprios_sd < 0:
            recursos_proprios_sd = 0

        valor_sinal_sd = percentual_sinal_decimal * valor_sem_documentacao
        if valor_sinal_sd >= recursos_proprios_sd:
            valor_sinal_sd = recursos_proprios_sd

        pro_soluto_sd = recursos_proprios_sd - valor_sinal_sd
        valor_parcela_24m_sd = pro_soluto_sd / 24
        comprometimento_sd = valor_parcela_24m_sd / renda_escolhida

        resultados_sem_documentacao.append({
            "Renda": renda_escolhida,
            "Taxa %": taxa_juros * 100,
            "Finan. + Subs + FGTS": total_financiamento,
            "Financiamento": capacidade_maxima,
            "Subsidio": subsidio_atual,
            "FGTS*": fgts,                    
            "Recursos Próprios**": recursos_proprios_sd,
            "Sinal***": valor_sinal_sd,
            "Pró-Soluto": pro_soluto_sd,
            "% Pró-Soluto": comprometimento_sd * 100,
            "Parcela Obra (24x)": valor_parcela_24m_sd,
            "Comprometimento (%)": comprometimento_sd * 100
        })

        valor_sem_documentacao_incc = valor_imovel_incc - (itbi_incc + registro_incc)
        recursos_proprios_sdi = valor_sem_documentacao_incc - total_financiamento
        if recursos_proprios_sdi < 0:
           recursos_proprios_sdi = 0

        valor_sinal_sdi = percentual_sinal_decimal * valor_sem_documentacao_incc
        if valor_sinal_sdi >= recursos_proprios_sdi:
            valor_sinal_sdi = recursos_proprios_sdi

        pro_soluto_sdi = recursos_proprios_sdi - valor_sinal_sdi
        valor_parcela_24m_sdi = pro_soluto_sdi / 24
        comprometimento_sdi = valor_parcela_24m_sdi / renda_escolhida

        resultados_sem_documentacao_incc.append({
            "Renda": renda_escolhida,
            "Taxa %": taxa_juros * 100,
            "Finan. + Subs + FGTS": total_financiamento,
            "Financiamento": capacidade_maxima,
            "Subsidio": subsidio_atual,
            "FGTS*": fgts,
            "Recursos Próprios**": recursos_proprios_sdi,
            "Sinal***": valor_sinal_sdi,
            "Pró-Soluto": pro_soluto_sdi,
            "% Pró-Soluto": comprometimento_sdi * 100,
            "Parcela Obra (24x)": valor_parcela_24m_sdi,
            "Comprometimento (%)": comprometimento_sdi * 100
        })


    # Código de cálculo (omitido para foco na correção do erro)

    # Conversão dos resultados em DataFrames e remoção de formatação para aplicar o filtro
    df_resultados = pd.DataFrame(resultados)
    df_resultados_incc = pd.DataFrame(resultados_incc)
    df_resultados_sd = pd.DataFrame(resultados_sem_documentacao)
    df_resultados_sd_incc = pd.DataFrame(resultados_sem_documentacao_incc)

   
# ---------------------------- SLIDE DE COMPROMETIMENTO!! ------------------------------------- # 
   

    # -------------------------------- VALOR ATUAL ------------------------------------------ #    

    # Converte a coluna 'Comprometimento (%)' para string, remove o símbolo de % e converte para float
    if "Comprometimento (%)" in df_resultados.columns:
        df_resultados["Comprometimento (%)"] = pd.to_numeric(
            df_resultados["Comprometimento (%)"].astype(str).str.replace("%", ""), errors='coerce'
        )

    # Definição com base no valor selecionado no slide de "Comprometimento"
        df_resultados = df_resultados[
            (df_resultados["Comprometimento (%)"] >= comprometimento_limite[0]) &  # Mínimo do intervalo
            (df_resultados["Comprometimento (%)"] <= comprometimento_limite[1])    # Máximo do intervalo
            
        ]

    # -------------------------------- INCC ------------------------------------------ #

    if "Comprometimento (%)" in df_resultados_incc.columns:
        df_resultados_incc["Comprometimento (%)"] = pd.to_numeric(
            df_resultados_incc["Comprometimento (%)"].astype(str).str.replace("%", ""), errors='coerce'
        )

        df_resultados_incc = df_resultados_incc[
            (df_resultados_incc["Comprometimento (%)"] >= comprometimento_limite[0]) &  # Mínimo do intervalo
            (df_resultados_incc["Comprometimento (%)"] <= comprometimento_limite[1])    # Máximo do intervalo
        ]

    # -------------------------------- SEM DOCUMENTAÇÃO ------------------------------------------ #

    if "Comprometimento (%)" in df_resultados_sd.columns:
        df_resultados_sd["Comprometimento (%)"] = pd.to_numeric(
            df_resultados["Comprometimento (%)"].astype(str).str.replace("%", ""), errors='coerce'
        )

        df_resultados_sd = df_resultados_sd[
            (df_resultados_sd["Comprometimento (%)"] >= comprometimento_limite[0]) &  # Mínimo do intervalo
            (df_resultados_sd["Comprometimento (%)"] <= comprometimento_limite[1])    # Máximo do intervalo
        ]

    # -------------------------------- SEM DOCUMENTAÇÃO C/ INCC ------------------------------------ #

    if "Comprometimento (%)" in df_resultados_sd_incc.columns:
        df_resultados_sd_incc["Comprometimento (%)"] = pd.to_numeric(
            df_resultados_sd_incc["Comprometimento (%)"].astype(str).str.replace("%", ""), errors='coerce'
        )

        df_resultados_sd_incc = df_resultados_sd_incc[
            (df_resultados_sd_incc["Comprometimento (%)"] >= comprometimento_limite[0]) &  # Mínimo do intervalo
            (df_resultados_sd_incc["Comprometimento (%)"] <= comprometimento_limite[1])    # Máximo do intervalo
        ]

# -----------------------------------------------------------------------------------------------------------------------#

    # Formatação dos valores após o filtro, se necessário
    df_resultados = formatar_valores(df_resultados)
    df_resultados_incc = formatar_valores(df_resultados_incc)
    df_resultados_sd = formatar_valores(df_resultados_sd)
    df_resultados_sd_incc = formatar_valores(df_resultados_sd_incc)
 

    # // ------------------- TABELAS ------------------------ // #

    # Exibição das tabelas com `st.expander` e valor no título, com ITBI e Registro ao lado

    st.markdown(
    """
    <style>
    /* Estilo personalizado para o expander */
    div[data-testid="stExpander"] {
        border: 2px solid rgba(51, 51, 51, 0.1) !important; /* Borda escura com opacidade */
        background-color: rgba(249, 249, 249, 0.1) !important; /* Fundo com opacidade ajustada */
        color: #333333 !important; /* Cor do texto */
        font-size: 21px; /* Define o tamanho do texto */
        border-radius: 10px; /* Arredondamento das bordas */
        padding: 2px;
    }

    /* Estilo para o texto dentro do expander */
    div[data-testid="stExpander"] > div > div {
        color: #333333 !important; /* Texto escuro para visibilidade */
        font-weight: bold !important; /* Deixa o texto em negrito */
        font-size: 21px; /* Define o tamanho do texto */
    }

   
    </style>
    """,
    unsafe_allow_html=True
)    
    
    st.markdown(f"""
    <p style="color: black; font-size: 16px;">
    <b>*FGTS</b> = 3 Salários
    <br>
    <b>**Recursos Próprios</b> = Sinal + Pró-soluto
    <br>
    <b>***Sinal</b> = Entrada + parcelas 30, 60 e 90 dias
    </p>
    """, 
    unsafe_allow_html=True)
    
# ---------------------------------- // TABELA DE VALOR ATUAL // ---------------------------------- #
          
    # Gerando o Excel para download
    excel_buffer = pd.ExcelWriter('tabela_valor_atual.xlsx', engine='xlsxwriter')
    df_resultados.to_excel(excel_buffer, index=False, sheet_name='Sheet1')
    excel_buffer.save()
    excel_data = open('tabela_valor_atual.xlsx', 'rb').read()
    b64_excel = base64.b64encode(excel_data).decode()

    col1, col2 = st.columns([0.01, 0.9])


    # Ícone para download
    col1.markdown(
  f"""
    <div style="display: flex; align-items: center; gap: 2px;">
        <!-- Ícone de download à esquerda -->
        <a href="data:file/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_excel}" download="tabela_valor_atual.xlsx" style="text-decoration: none;">
            <span class="material-symbols-outlined" style="font-size: 30px; margin-top: 6.9px; color: #D8B08C;">download</span>
        </a>    

    </div>
    """,
    unsafe_allow_html=True
)
   

        # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["Comprometimento (%)"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 30%
            if numeric_value > 30:
                # Estilizar células da 13ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(13) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)


            # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["% Pró-Soluto"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 14%
            if numeric_value > 14:
                # Estilizar células da 11ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(11) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)



    with col2.expander(f"Valor Atual: R$ {valor_imovel:,.0f}".replace(",", ".")):
        st.table(df_resultados)
    
    # ---------------------------------- // TABELA INCC // ---------------------------------- #
      
    # Gerando o Excel para download
    excel_buffer = pd.ExcelWriter('valor_atual_incc.xlsx', engine='xlsxwriter')
    df_resultados_incc.to_excel(excel_buffer, index=False, sheet_name='Sheet1')
    excel_buffer.save()
    excel_data = open('valor_atual_incc.xlsx', 'rb').read()
    b64_excel = base64.b64encode(excel_data).decode()

    col1, col2 = st.columns([0.01, 0.9])

    # Ícone para download
    col1.markdown(
  f"""
    <div style="display: flex; align-items: center; gap: 2px;">
        <!-- Ícone de download à esquerda -->
        <a href="data:file/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_excel}" download="valor_atual_incc.xlsx" style="text-decoration: none;">
            <span class="material-symbols-outlined" style="font-size: 30px; margin-top: 6.9px; color: #D8B08C;">download</span>
        </a>

    </div>
    """,
    unsafe_allow_html=True
)

        # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["Comprometimento (%)"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 30%
            if numeric_value > 30:
                # Estilizar células da 13ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(13) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados_incc)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)


            # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["% Pró-Soluto"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 14%
            if numeric_value > 14:
                # Estilizar células da 11ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(11) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados_incc)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)



  
    with col2.expander(f"Valor Atual C/INCC: R$ {valor_imovel_incc:,.0f}".replace(",", ".")):
      st.markdown(f"""
        
        **Nota:** INCC-DI Acumulado 12 meses: {taxa_incc_percentual:.2f}%
        """)
      
      st.table(df_resultados_incc)


# ---------------------------------- // TABELA S/ DOCUMENTAÇÃO // ---------------------------------- #
        
  # Gerando o Excel para download
    excel_buffer = pd.ExcelWriter('valor_atual_sem_documentacao.xlsx', engine='xlsxwriter')
    df_resultados_incc.to_excel(excel_buffer, index=False, sheet_name='Sheet1')
    excel_buffer.save()
    excel_data = open('valor_atual_sem_documentacao.xlsx', 'rb').read()
    b64_excel = base64.b64encode(excel_data).decode()

    col1, col2 = st.columns([0.01, 0.9])

    # Ícone para download
    col1.markdown(
  f"""
    <div style="display: flex; align-items: center; gap: 2px;">
        <!-- Ícone de download à esquerda -->
        <a href="data:file/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_excel}" download="valor_atual_sem_documentacao.xlsx" style="text-decoration: none;">
            <span class="material-symbols-outlined" style="font-size: 30px; margin-top: 6.9px; color: #D8B08C;">download</span>
        </a>

    </div>
    """,
    unsafe_allow_html=True
)
    

            # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["Comprometimento (%)"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 30%
            if numeric_value > 30:
                # Estilizar células da 13ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(13) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados_sd)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)


            # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["% Pró-Soluto"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 14%
            if numeric_value > 14:
                # Estilizar células da 11ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(11) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados_sd)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)



    with col2.expander(f"Valor S/Documentação: R$ {abs(valor_sem_documentacao):,.0f}".replace(",", ".")):
        st.markdown(f"""
        **Detalhes de Taxas:**
        
        - **ITBI**: R$ {itbi:,.0f}
        - **Registro**: R$ {registro:,.0f}
    """.replace(",", "."), unsafe_allow_html=True)
        st.table(df_resultados_sd)


# ---------------------------------- // TABELA S/ DOCUMENTAÇÃO C/INCC // ---------------------------------- #    

 # Gerando o Excel para download
    excel_buffer = pd.ExcelWriter('valor_atual_sem_documentacao_incc.xlsx', engine='xlsxwriter')
    df_resultados_incc.to_excel(excel_buffer, index=False, sheet_name='Sheet1')
    excel_buffer.save()
    excel_data = open('valor_atual_sem_documentacao_incc.xlsx', 'rb').read()
    b64_excel = base64.b64encode(excel_data).decode()

    col1, col2 = st.columns([0.01, 0.9])

    # Ícone para download
    col1.markdown(
  f"""
    <div style="display: flex; align-items: center; gap: 2px;">
        <!-- Ícone de download à esquerda -->
        <a href="data:file/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_excel}" download="valor_atual_sem_documentacao_incc.xlsx" style="text-decoration: none;">
            <span class="material-symbols-outlined" style="font-size: 30px; margin-top: 6.9px; color: #D8B08C;">download</span>
        </a>

    </div>
    """,
    unsafe_allow_html=True
)


            # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["Comprometimento (%)"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 30%
            if numeric_value > 30:
                # Estilizar células da 13ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(13) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados_sd_incc)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)


            # Função para processar a coluna e criar o CSS dinâmico
    def generate_dynamic_css(df):
        css_styles = ""
        for i, value in enumerate(df["% Pró-Soluto"]):  # Altere o nome da coluna, se necessário
            # Remover o símbolo '%' e converter para número
            numeric_value = float(value.replace("%", "").replace(",", ".")) if isinstance(value, str) else value
            
            # Verifica se o valor é maior que 14%
            if numeric_value > 14:
                # Estilizar células da 11ª coluna (ajustar índice CSS para a posição real)
                css_styles += f"""
                table tbody tr:nth-child({i + 1}) td:nth-child(11) {{
                    background-color: transparent !important; /* Fundo laranja com opacidade */
                    color: rgba(255, 87, 51, 0.7) !important; /* Texto translúcido */
                    font-weight: bold !important; /* Texto em negrito */
                }}      

                """
        return css_styles

    # Gera o CSS dinâmico
    dynamic_css = generate_dynamic_css(df_resultados_sd_incc)

    # Injetando o CSS dinâmico no Streamlit
    st.markdown(f"""
        <style>
        {dynamic_css}
        </style>
    """, unsafe_allow_html=True)




    with col2.expander(f"Valor S/Documentação C/INCC: R$ {abs(valor_sem_documentacao_incc):,.0f}".replace(",", ".")):
        st.markdown(f"""
        **Detalhes de Taxas:**
        
        - **ITBI**: R$ {itbi_incc:,.0f}
        - **Registro**: R$ {registro_incc:,.0f}
        """.replace(",", "."), unsafe_allow_html=True)
        
        st.table(df_resultados_sd_incc)



# ---------------------------------- ESTILO DO BOTÃO [CALCULAR] E DOS EXPANDERS ---------------------------------- #  

# Centralizando o botão "Calcular" e ajustando os estilos dos expanders
st.markdown(
    """
    <style>
    /* Botão "Calcular" com efeito vidro fosco e estilo personalizado */
    .stButton > button {
        display: block;
        margin: 0 auto; /* Centraliza o botão */
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        color: #ffffff
        background: rgba(0, 0, 0, 0.9); /* Fundo transparente com efeito vidro */
        border: 1px solid rgba(242, 169, 126, 0.4); /* Borda suave */
        border-radius: 8px; /* Bordas arredondadas */
        backdrop-filter: blur(8px); /* Efeito de desfoque para vidro fosco */
        -webkit-backdrop-filter: blur(8px);
        transition: background 0.3s ease, color 0.3s ease, border 0.3s ease, box-shadow 0.3s ease;
        outline: none; /* Remove contorno padrão */
        box-shadow: none; /* Remove qualquer sombra extra */
    }

    /* Estilo do botão ao focar, clicar, ou passar o mouse */
    
    .stButton > button:hover, .stButton > button:focus, .stButton > button:active {
    background: rgba(255, 213, 171, 0.3); /* Fundo levemente mais claro no hover */
    color: #A63F03 !important; /* Cor do texto no hover, foco e clique */
    border: 1px solid rgba(242, 169, 126, 0.4); /* Borda consistente */
    box-shadow: none !important; /* Remove sombra vermelha */
    outline: none !important; /* Remove contorno */
}

/* Remover o foco persistente ao perder o foco */
.stButton > button:focus:not(:focus-visible) {
    outline: none;
    border: 1px solid rgba(242, 169, 126, 0.4); /* Borda consistente */
    }


 
#------------------------- // FORMATAÇÃO DAS TABELAS // ---------------------------------------- #

<style>
/* Estilo para as tabelas dentro dos expanders */
.st-expander .stDataFrame, .st-expander .stTable, .stDataFrame, .stTable {
    background-color: rgba(255, 255, 255, 0.2) !important; /* Fundo mais claro para a tabela */
    color: #333333 !important; /* Cor do texto das células */
    border-radius: 5px; /* Bordas arredondadas para as tabelas */
    border: 1px solid rgba(200, 200, 200, 0.5); /* Borda suave para a tabela */
}

/* Estilo para o cabeçalho das tabelas */
.stDataFrame thead tr th, .stTable thead tr th {
    color: #333333 !important; /* Cor do texto do título das colunas */
    font-weight: bold !important; /* Negrito para o título das colunas */
    background-color: rgba(240, 240, 240, 0.9) !important; /* Fundo leve para o cabeçalho */
    border-bottom: 1px solid rgba(200, 200, 200, 0.5); /* Linha de divisão no cabeçalho */
    text-align: center !important; /* Centraliza o texto do título das colunas */
    vertical-align: middle !important; /* Centraliza o texto verticalmente */
}

/* Estilo para as células de dados na tabela */
.stDataFrame tbody tr td, .stTable tbody tr td {
    color: #333333 !important; /* Cor do texto nas células de dados */
    border: 1px solid rgba(200, 200, 200, 0.5); /* Linha de grade das células */
    text-align: center !important; /* Centraliza o conteúdo das células */
    vertical-align: middle !important; /* Centraliza verticalmente o conteúdo */
}
</style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------// BOTÃO DE CÁLCULO // -------------------------------------------# 


if st.button("Calcular"):
    calcular()


# -------------------------------------------- // RODAPÉ DA APLICAÇÃO // ----------------------------------------#

# CSS para o rodapé

st.markdown(
    """
    <style>
    /* Rodapé fixo na parte inferior da página */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(242, 169, 126, 0.9); /* Fundo do rodapé com opacidade */
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer img {
        width: 150px; /* Largura da imagem, ajuste conforme necessário */
        vertical-align: middle; /* Alinha a imagem ao centro verticalmente */
        margin-right: 10px; /* Espaço à direita da imagem */
    }
    </style>
    
    <!-- HTML para o conteúdo do rodapé -->
    <div class="footer">
        <a href="https://tinyurl.com/344hha6j" target="_blank">
        <img src="https://i.postimg.cc/wxV0VdPQ/IM-LOGO-ALL-BLACK.png" alt="Inteligência de Mercado"> <!-- Substitua pela URL da sua imagem -->
        </div>
    """,
    unsafe_allow_html=True
)