import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="LaPlateforme")
cursor = connexion.cursor()

cursor.execute("SELECT * FROM etudiant")

for table in cursor.fetchall():
    print(table)

cursor.close()
connexion.close()



