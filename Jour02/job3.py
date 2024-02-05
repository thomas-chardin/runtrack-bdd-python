import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="LaPlateforme")
cursor = connexion.cursor()
# info_etage = "INSERT INTO etage (nom, numero, superficie) VALUES  ('RDC', 0, 500), ('R+1', 1, 100)"
# info_salle = "INSERT INTO salle (nom, id_etage, capacite) VALUES ('Lounge,', 1, 100), ('Studio Son', 1, 5), ('Broadcasting',2,50), ('Bocal Peda',2,4),('Coworking',2,80), ('Studio Video',2,5)"
cursor.execute("SELECT * FROM etage")
for table in cursor.fetchall():
    print(f"etage :{table}")
cursor.execute("SELECT * FROM salle")
for table in cursor.fetchall():
    print(f"salle :{table}")
cursor.execute("SELECT * FROM salle")

cursor.close()
connexion.close()

