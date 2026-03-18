import polars as pl

arquivo_info = 'Music Info.csv'
arquivo_user = 'User Listening History.csv'

try:

 df_musica = pl.read_csv(arquivo_info)
 df_execucao = pl.read_csv(arquivo_user)

 #print(df_info.glimpse())
 #print(df_user.glimpse())
 df_execucao_agrupado = df_execucao.group_by('track_id').agg(pl.col('playcount').sum().alias("plays"))
 print(df_execucao_agrupado.head())


 df_merge = df_musica.join(df_execucao_agrupado, left_on='track_id', right_on='track_id', how='left')
 
 
 
 #print(df_merge.head())
 #print(df_merge.glimpse())






except Exception as e :
    print( "erro")