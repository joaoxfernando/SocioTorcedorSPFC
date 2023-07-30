# Webscrap e Análise da quantidade de Sócios Torcedores do São Paulo FC.

## Como funciona

- O script irá entrar no site do Sócio Torcedor (www.sociotorcedor.com.br) e pegar a quantidade atual de sócios torcedores disponíveis na página e armazenar em um dataframe.
- Esses dados serão salvos em um arquivo de Excel chamado 'sócios.xlsx' (você pode alterar o nome caso deseje)
- Em seguida será criado outro dataframe com as análises de variação absoluta e relativa do número de sócios em comparação ao dia anterior.
- O script está configurado para rodar apenas 1x por dia, para não armazenar datas duplicadas, optei por rodar o script diariamente por volta das 12h.
- Caso deseja salvar a planilha com a variação absoluta e relativa, retirar o caractere # no ínicio da última linha

**DE**
```python
#df_var.to_excel('Variacao.xlsx',index=False)
```

**PARA**
```python
df_var.to_excel('Variacao.xlsx',index=False)
```