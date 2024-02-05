import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="LaPlateforme")
cursor = connexion.cursor()

calcul_superficie_query = "SELECT SUM(superficie) FROM etage"
cursor.execute(calcul_superficie_query)
print(f"La superficie de la plateforme est de : {cursor.fetchone()[0]} m²")
cursor.close()
connexion.close()
