"""
  Ensemble des vues realises sur notre base de donnees 
  supermarkets.
"""

import pandas as pd


def groupby_maker(group_var:str, column_study:str, dataset):
  """ Realiser un group by par une colonne sur une colonne en y appliquant des fonctions d'aggreaga """
  
  #realisation du group by
  dataset =  dataset.groupby([group_var])[column_study].sum().reset_index()
  
  #recuperation des index
  index =  dataset[group_var].to_list()

  #recuperation des values rattaches aux index
  value =  dataset[column_study].to_list()

  #retourne un dictionnaire former des liste d'index et de values.
  return dict(zip(index, value))


def sales_per_month(dataset):
  """Realiser une evaluation du total des ventes par mois  """

  #casting de la variable Date en datetimeObject
  dataset['Date'] =  pd.to_datetime(dataset['Date'])
  
  #recuperation des mois de chaques dates dans une liste month
  month =  []
  for i in range(dataset.shape[0]):
    month.append(dataset['Date'][i].month)

  #creation de la colonne month de notre dataset
  dataset['month'] =  month

  #realisations de l'aggreagation sur les mois 
  Total_sales_per_month = dataset.groupby(['month'])['Total'].sum().reset_index()

  #maping de l'ordre des mois avec leurs noms
  Total_sales_per_month['month'] = ['01 - janvier','02 - Fevrier','03 - Mars']


  #meme methode realiser dans la fonction plus haut -- dictionnaire a partir de deux listes
  index =  Total_sales_per_month['month'].to_list()
  value =  Total_sales_per_month['Total'].to_list()
  return dict(zip(index, value))


def sales_per_hour(dataset):
  """ Realisation des ventes totales par heure et evaluation des heures de ventes optimal en moyenne """
  
  #casting en datetimeObject
  dataset['Date'] =  pd.to_datetime(dataset['Date'])

  #creation de la colonne heure
  dataset['Hour'] =  pd.to_datetime(dataset['Time']).dt.hour

  #grouping des ventes par heure
  Total_sales_per_hour =  dataset.groupby(['Hour'])['Total'].mean().reset_index().sort_values('Hour', ascending = True)

  #meme methode
  index =  Total_sales_per_hour['Hour'].to_list()
  value =  Total_sales_per_hour['Total'].to_list()

  return dict(zip(index, value))



def sales_per_hour_per_product_line(dataset):
  """ donnees pour les ventes moyenne par heure par categories de produit  """

  indexs =  dataset['Product line'].unique()

  values =  []
  for index in indexs:
    data =  dataset[dataset['Product line'] == index ]

    values.append(sales_per_hour(data))
  indexs =  [ii.replace(' ','_') for ii in indexs]

  return dict(zip(indexs, values))




#member vs no-member
def member_vs_no_member(dataset):

  """ Realise les etudes sur les clients membres et les visiteurs  l'objectif etant d'observer les habitude de conso rattaches a nos differents groupe de consommateur"""

  #total ventes des menbres par categories de produits -- quelles sont les produits les plus consomes par nos clients
  df_member_Total_sales =  dataset[dataset['Customer type'] == "Member"].groupby(['Product line'])['Total'].sum().reset_index().sort_values('Product line', ascending = True)
  
  #total ventes des visiteurs par categories de produits -- quelles sont les prodruits les sollicites par les visiteurs en moyenne.
  df_no_member_Total_sales =  dataset[dataset['Customer type'] != "Member"].groupby(['Product line'])['Total'].sum().reset_index().sort_values('Product line', ascending = True)


  #meme operation 
  dico_member =  dict(zip(df_member_Total_sales['Product line'].to_list(), df_member_Total_sales['Total'].to_list()))
  dico_no_member =  dict(zip(df_no_member_Total_sales['Product line'].to_list(), df_no_member_Total_sales['Total'].to_list()))


  return {'member': dico_member, 'no_member': dico_no_member}
  