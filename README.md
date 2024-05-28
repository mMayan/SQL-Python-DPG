# Protótipo de CRUD em um Banco de Dados

## Requisitos do programa
Crie um protótipo (independente da linguagem de programação) de um CRUD com acesso ao banco de dados para inserir, deletar e pesquisar dados em uma tabela específica.

O protótipo deve ter uma tela para interação com o usuário, não será aceito a interação pelo terminal da IDE

## Como configurar a conexão com o banco de dados
você precisa previamente criar um usuário e um banco de dados, para isso abra o console do MYSQL e digite:

`CREATE USER 'novo_usuario'@'localhost' IDENTIFIED BY 'senha';`

após isso digite:

 `GRANT ALL PRIVILEGES ON *.* TO 'novo_usuario'@'localhost' WITH GRANT OPTION;` 

 e por último digite: 
 
 `FLUSH PRIVILEGES;`

 após criar o usuário você precisa criar um novo banco de dados, para isso digite:

`CREATE DATABASE escolha_nome`

 agora que você criou o usuário e o banco de dados precisa criar uma nova tabela com as colunas e atribuições, para isso digite os seguintes comandos:

 `CREATE TABLE registro(id INT AUTO_INCREMENT PRIMARY KEY, aluno varchar(50), sobrenome(50), nota FLOAT);`


 a configuração do ambiente do MYSQL está completa, agora precisamos modificar no código `SQL_connection.py` algumas coisas.

repare que nas funções `insert_table()`, `select_table()` e `delete_table()` possui esses 3 argumentos:
* `user='###'`
* `password='###'`
* `database='###'`

esses são os argumentos que você precisa modificar em cada função com os dados que você usou durante a criação e edição do banco de dados. 

exemplo de como você deve botar seus dados na linha de código:

`cnx = mysql.connector.connect(user='teste', password='teste123', database='sua_database')`

depois que você tiver alterado o valor desses argumentos seu código estará pronto para rodar e fazer alterações no banco de dados!

### Bibliotecas usadas no código
* [mysql](https://dev.mysql.com/doc/connector-python/en/)
* [dearpygui](https://dearpygui.readthedocs.io/en/latest/tutorials/first-steps.html)