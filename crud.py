import sqlite3
from tkinter import *
from tkinter import messagebox



class Funcs():
    def limpa_cliente(self):
        self.codigo_entry.delete(0, END)
        self.tele_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.valor_entry.delete(0,END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientess.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        #Cria tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                cpf VARCHAR(11),
                telefone INTEGER(20),
                cidade CHAR(40),
                valor DECIMAL(10,2)
            );
        
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cpf = self.cpf_entry.get()
        self.fone = self.tele_entry.get()
        self.cidade = self.city_entry.get()
        self.valor = self.valor_entry.get()
    
    def OnDoubleClick(self, event):
        self.limpa_cliente()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.cpf_entry.insert(END, col3)
            self.tele_entry.insert(END, col4)
            self.city_entry.insert(END, col5)
            self.valor_entry.insert(END, col6)

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, cpf, telefone, cidade, valor)
            VALUES (?, ?, ?, ?, ?)""", (self.nome,self.cpf, self.fone, self.cidade, self.valor))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, cpf = ?, telefone = ?, cidade = ?, valor = ?
            WHERE cod = ? """,
                            (self.nome, self.cpf, self.fone, self.cidade, self.valor, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    
    def deleta_cliente(self):
        resposta = messagebox.askquestion("Excluir Cliente", "Tem certeza que deseja excluir este cliente?")
        if resposta == "yes":
            self.variaveis()
            self.conecta_bd()
            self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
            self.conn.commit()
            self.limpa_cliente()
            self.select_lista()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        else:
            messagebox.showinfo("Cancelado", "Operação cancelada.")


    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, cpf, telefone, cidade, valor FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    
    def busca_cliente(self):
        self.janela2()
