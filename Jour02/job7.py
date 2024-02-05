import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="LaPlateforme")
cursor = connexion.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS employe (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom VARCHAR(255) NOT NULL, prenom VARCHAR(255) NOT NULL, salaire DECIMAL NOT NULL, id_service INT NOT NULL)")

# cursor.execute('INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ("Nom1", "Prenom1", 1000.00, 1), ("Nom2", "Prenom2", 2000.00, 1), ("Nom3", "Prenom3", 3000.00, 2), ("Nom4", "Prenom4", 4000.00, 2), ("Nom5", "Prenom5", 5000.00, 3)')

# cursor.execute("CREATE TABLE IF NOT EXISTS service (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom VARCHAR(255) NOT NULL)")
# cursor.execute("INSERT INTO service (nom) VALUES ('Service1'), ('Service2'), ('Service3')")

cursor.execute("SELECT * FROM employe WHERE salaire > 3000.00")
print(cursor.fetchall())

cursor.execute("SELECT * FROM employe, service WHERE employe.id_service = service.id")
print(cursor.fetchall())
class Salarie():
    def __init__(self):
        self.nom = None
        self.prenom = None
        self.salaire = None
        self.id_service = None
        self.service = None

    def add_salaries(self, nom, prenom, salaire, id_service):
        cursor.execute(f'INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ("{nom}", "{prenom}", {salaire}, {id_service})')
        connexion.commit()
    def get_higher_salaire(self):        
        cursor.execute("SELECT * FROM employe ORDER BY  salaire DESC LIMIT 1")
        print(cursor.fetchall())
    def get_down_salaire(self):
        cursor.execute("SELECT * FROM employe ORDER BY salaire LIMIT 1")
        print(cursor.fetchall())
    def get_employee_by_index(self, index):
        cursor.execute(f"SELECT * FROM employe WHERE id = {index}")
        print(cursor.fetchall())
    def get_employee_by_name(self, name):
        cursor.execute(f"SELECT * FROM employe WHERE nom = '{name}'")
    
n = Salarie()
n.get_down_salaire()
n.get_higher_salaire()
n.get_employee_by_index(1)
n.get_employee_by_name('Nom1')