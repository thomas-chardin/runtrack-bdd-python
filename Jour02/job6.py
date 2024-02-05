import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="LaPlateforme")
cursor = connexion.cursor()

calcul_superficie_query = "SELECT SUM(capacite) FROM salle"
cursor.execute(calcul_superficie_query)
print(f"La capacité de toute les salles est de : {cursor.fetchone()[0]}")
cursor.close()
connexion.close()