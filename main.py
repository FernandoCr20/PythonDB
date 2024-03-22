import sqlite3
from modelo import Pessoa, Marca, Veiculo

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Pessoa(
    cpf INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    oculos BOOLEAN NOT NULL
);''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Marca(
    id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    sigla CHARACTER(2) NOT NULL,
    PRIMARY KEY(id)
);''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Veiculo(
    placa CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario INTEGER NOT NULL,
    marca INTEGER NOT NULL,
    PRIMARY KEY(placa),
    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
    FOREIGN KEY(marca) REFERENCES Marca(id)
    
);''')

# cursor.execute(''' ALTER TABLE Veiculo ADD motor REAL; ''')

# pessoa = Pessoa(12345678900, 'Fernando', '29-12-2002', False)

# comando = ''' INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES (?,?,?,?); '''
# cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.usa_oculos))

# pessoas = [Pessoa(98765432100, 'Pedro', '15-03-2000', True), Pessoa(78945613200, 'Ana', '01-01-2001', False)]
# comando = ''' INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES(?,?,?,?); '''

# cursor.executemany(comando, [(i.cpf, i.nome, i.nascimento, i.usa_oculos) for i in pessoas])

# ---------------------------------------------------------------------------------------------------------------------------

# comando = ''' INSERT INTO Marca(nome, sigla) VALUES (:nome, :sigla); '''
# marcaA = Marca("Marca A", "MA")

# cursor.execute(comando, vars(marcaA))
# marcaA.id = cursor.lastrowid

# marcaB = Marca("Marca B", "MB")
# cursor.execute(comando, vars(marcaB))
# marcaB.id = cursor.lastrowid

comando = ''' INSERT INTO Veiculo(placa, ano, cor, motor, proprietario, marca) VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca); '''
veiculo1 = Veiculo("AABB001", "2001", "Prata", 1.0, 12345678900, 1)
veiculo2 = Veiculo("BABB001", "2002", "Preto", 1.5, 78945613200, 2)
cursor.execute(comando, vars(veiculo1))
cursor.execute(comando, vars(veiculo2))

banco.commit()
cursor.close()