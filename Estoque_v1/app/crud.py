from Estoque_v1.app.db import conectar

#Adicionar pisos
def create(dados):
    conexao = conectar()
    cursor = conexao.cursor()
    
    #Inserindo no banco de dados todos os valores em ordem na tabela do SQL
    comando = 'INSERT INTO pisos (name, type, color, quantity_box, meters_box, entry_date, value_box) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(comando, dados)
    conexao.commit()

    cursor.close()
    conexao.close()

#listar pisos

def read():
    conexao = conectar()
    cursor = conexao.cursor()
    
    comando = 'SELECT * FROM pisos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexao.close()

#Atualziar

def update_name(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET name = %s WHERE idpisos = %s'

    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()

def update_type(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET type = %s WHERE idpisos = %s'

    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()

def update_color(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET color = %s WHERE idpisos = %s'

    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()

def update_box(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET quantity_box = %s WHERE idpisos = %s'
    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()
    
def update_meters(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    conexao = conectar()
    cursor = conexao.cursor()
    comando = 'UPDATE pisos SET meters_box = %s WHERE idpisos = %s'
    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()
def update_entry(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET entry_date = %s WHERE idpisos = %s'
    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()

def update_depar(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET depar_date = %s WHERE idpisos = %s'
    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()

def update_value(escolha):
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'UPDATE pisos SET value_box = %s WHERE idpisos = %s'
    cursor.execute(comando, escolha)
    conexao.commit()

    cursor.close()
    conexao.close()


#Deletar
def delete(deletar):
    conexao = conectar()
    cursor = conexao.cursor()
    #Exclui o dado do banco de dados
    comando = 'DELETE FROM pisos WHERE idpisos = %s'

    cursor.execute(comando, deletar)
    conexao.commit()

    cursor.close()
    conexao.close()



