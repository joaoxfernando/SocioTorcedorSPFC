from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
import pandas as pd

# Definindo a URL e configurações do Selenium

url = 'https://sociotorcedor.com.br/'
options = options = webdriver.FirefoxOptions()
options.add_argument('--headless')
xpath = '/html/body/app-root/div/fengstlayout-header/header/section/div/span[2]'
driver = webdriver.Firefox(options=options)

driver.get(url)
time.sleep(10)

# pegando os dados para alimentar a nossa base de dados
data = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d').date()
data = data.strftime('%Y-%m-%d')
hoje = data

# pegando a quantidade de sócios na pagina inicial  e adicionando os dados da data e qtde de sócios em um array
qtde_st = driver.find_elements(By.XPATH, xpath)[0].text
dados = [data,qtde_st.replace('.','')]

driver.quit() # fechando o browser

# carregando a base de dados
df = pd.read_excel('socios.xlsx')

# criando um segundo dataframe com os dados da data atual
df2 = pd.DataFrame({'Data':[dados[0]],'Quantidade Sócios': [dados[1]]})
df2['Quantidade Sócios'] = df2['Quantidade Sócios'].astype(int)
# unindo os dois dataframes se a data atual for diferente da ultima data do dataframe
ult_data = df['Data'].iloc[-1]
ult_data = ult_data.strftime('%Y-%m-%d')

if ult_data != hoje:

    df = pd.concat([df,df2])
    df['Data'] = pd.to_datetime(df['Data'])

    # salvando o novo dataframe com os dados atualizados.

    df.to_excel('socios.xlsx',index=False)
else:
    print('Você já atualizou a base de dados hoje! Tente novamente amanha.')

# Fazendo os cálculos de variação absoluta e relativa da quantidade de STs
df_var = df
df_var['Crescimento #'] = df['Quantidade Sócios'] - df['Quantidade Sócios'].shift(1)
df_var['Crescimento %'] = df['Quantidade Sócios']/df['Quantidade Sócios'].shift(1) - 1
df_var.fillna(0,inplace=True)
variacao_rel = df_var['Quantidade Sócios'].iloc[-1] / df_var['Quantidade Sócios'].iloc[0] -1
variacao_abs = df_var['Quantidade Sócios'].iloc[-1] - df_var['Quantidade Sócios'].iloc[0]

# pegando a primeira e a última data do DataFrame
prim_data = df_var['Data'].iloc[0]
ult_data = df_var['Data'].iloc[-1]

dias = abs((ult_data - prim_data).days) +1 # calculando a quantidade de dias desde que começou a análise # type: ignore
dias_alt = df_var['Data'].count() # calculando a quantidade de vezes que o script foi rodado

prim_data = prim_data.strftime('%d/%m/%y')
ult_data = ult_data.strftime('%d/%m/%y')

# checando se a variação foi positiva ou negativa
if variacao_abs > 0:
    msg_1 = 'O número de sócios torcedores cresceu '
else:
    msg_1 = 'O número de sócios torcedores caiu em '
msg_2 = 'desde o começo da análise'


print(f'{msg_1}{variacao_rel:.2%} ({variacao_abs} torcedores) {msg_2}.')
print(f'A análise começou no dia {prim_data} e a última atualização foi no dia {ult_data}, totalizando {dias} dias de análise.')

# inclua # no começo da linha abaixo caso não queira salvar o arquivo com a variação dia a dia, caso queira salvar, basta retirar o # do ínicio da linha.
df_var.to_excel('Variacao.xlsx',index=False)