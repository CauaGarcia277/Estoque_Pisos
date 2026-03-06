import mysql.connector
import os

#Conexão banco de dados
def conectar():
    return mysql.connector.connect(
        host= "localhost",
        user= "root",
        password= "Ca272525#",
        database= "geren_estoque"
    )

