import dearpygui.dearpygui as dpg
import mysql.connector


def insert_table():
    cnx = mysql.connector.connect(user = '###',
                                  password = '###',
                                  database = '###')
    
    aluno = dpg.get_value('aluno_nome')
    sobrenome = dpg.get_value('aluno_sobrenome')
    nota = dpg.get_value('aluno_nota')

    cursor = cnx.cursor()
    cursor.execute("INSERT INTO registro (aluno, sobrenome, nota )" 
                   f"VALUES ('{aluno}', '{sobrenome}', {nota});")
    
    cnx.commit()
    cursor.close()
    cnx.close()
    dpg.set_value('mostra_feedback', 'inserção bem sucedida!')

#insert_table()

def select_table():
    cnx = mysql.connector.connect(user='###',
                                  password='###',
                                  database='###')

    aluno = dpg.get_value('verifica_nome')
    sobrenome = dpg.get_value('verifica_sobrenome')

    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM registro WHERE aluno = '{aluno}' AND sobrenome = '{sobrenome}';")
    
    result = cursor.fetchall()
    for i in result:
        dpg.set_value('mostra_select_table', f'{i}')

    cursor.close()
    cnx.close()

#select_table()

def delete_table():
    cnx = mysql.connector.connect(user='###',
                                password='###',
                                database='###')

    nome = dpg.get_value('deleta_nome')
    sobrenome = dpg.get_value('deleta_sobrenome')

    cursor = cnx.cursor()
    cursor.execute("DELETE FROM registro "
                   f"WHERE aluno = '{nome}' AND sobrenome = '{sobrenome}';")
    
    cnx.commit()
    cursor.close()
    cnx.close()
    dpg.set_value('deleta_feedback', 'exclusão foi um sucesso!')

#delete_table()