import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="LaPlateforme")
cursor = connexion.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS etage (id INT PRIMARY  KEY NOT NULL AUTO_INCREMENT,nom VARCHAR(255) NOT NULL,numero INT NOT NULL, superficie INT NOT NULL)")
# cursor.execute("CREATE TABLE IF NOT EXISTS salle (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(255),id_etage INT, capacite INT)")
cursor.execute("SELECT * FROM salle")
print(cursor.fetchall())
cursor.execute("SELECT * FROM salle")
print(cursor.fetchall())

cursor.close()
connexion.close()