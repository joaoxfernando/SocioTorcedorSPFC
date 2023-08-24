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

## Instruções
1. Rode diretamente o arquivo main.py via terminal/prompt de comando. Abra o diretorio aonde salvou o arquivo e rode o comando abaixo

```bash
pyhon script.py
```
2. Caso possua o jupyter notebook instalado, você pode rodar abrindo diretamente o arquivo **num_socios.ipynb** e rodando as células 
3. Para gerar algumas análises e também o gráfico, rode arquivo **consultas.py** ou **consultas.ipynb** da mesma forma que a instrução anterior.
4. Para cadastrar algum evento/notícia, rode o arquivo **eventos.ipynb** ou **eventos.py**


## Observações
Recomendo rodar o arquivo eventos.py apenas quando quiser cadastrar algum evento/notícia. Caso queira apenas visualizar, rode o arquivo eventos.ipynb, pois rodando pelo terminal a visualização dos dados não fica bem formatada, ao contrário do jupyter notebook. 
O mesmo serve para o arquivo consultas, mas lá não será cadastrado nenhuma informação personalizada, então a sugestão de rodar o arquivo com extensão ipynb pelo jupyter notebook é para visualização das tabelas. Se rodar o arquivo .py, será gerado apenas um arquivo .png na pasta images cujo o nome será a data-atual no formato **ANO-MÊS-DIA.png**