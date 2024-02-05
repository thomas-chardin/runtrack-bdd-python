import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="laplateforme")
cursor = connexion.cursor()
 
cursor.execute("SELECT nom, capacite FROM salle")

print(cursor.fetchall())

cursor.close()
connexion.close()
