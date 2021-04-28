import MySQLdb

#Coloque suas credenciais para a conexão com o banco de dados
Connection = MySQLdb.connect(host="localhost", user="root", passwd="", database="uriexamples")

mycursor = Connection.cursor()
mycursor.execute("select * from usuarios")

result = mycursor.fetchall()
for i in result:
    print(i)

