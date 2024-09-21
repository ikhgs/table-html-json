from requests_html import HTMLSession

# Créer une session HTML
s = HTMLSession()

# URL de la table à scraper
url = 'https://www.skysports.com/league-1-table'

# Faire une requête GET
r = s.get(url)

# Trouver la table dans le contenu HTML
table = r.html.find('table')[0]

# Extraire les données des cellules <td> pour chaque ligne <tr> (sauf la première ligne des en-têtes)
tabledata = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')[1:]]

# Extraire les en-têtes des colonnes à partir de la première ligne <th>
tableheader = [c.text for row in table.find('tr')[0:1] for c in row.find('th')[:-1]]

# Créer une liste de dictionnaires, où chaque dictionnaire associe un en-tête à une valeur
res = [dict(zip(tableheader, t)) for t in tabledata]

# Afficher le résultat
print(res)
