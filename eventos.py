import pandas as pd

df = pd.read_excel('eventos.xlsx')

fatos_novos = {}
data = []
evento = []
tipo = []

data.append(fatos_novos['Data']) if len(fatos_novos) != 0 else None

data.append(input("Digite a data no formato: dd/mm/aaaa "))
evento.append(input('Digite o nome do evento: '))
tipo.append(input("Digite a tipo do evento (noticia/campeonato disputado/etc)"))

fatos_novos.update(dict(Data=data))
fatos_novos.update(dict(Evento=evento))
fatos_novos.update(dict(Tipo=tipo))

fn = pd.DataFrame(fatos_novos)
df = pd.concat([df,fn])
df['Data'] = df['Data'].astype('datetime64[ns]')
df.to_excel('eventos.xlsx', index=False)

df_var = pd.read_excel('Variacao.xlsx')

novo_df = pd.merge(df_var, df, how='left', on='Data')
novo_df[['Evento', 'Tipo']] = novo_df[['Evento', 'Tipo']].fillna('')
