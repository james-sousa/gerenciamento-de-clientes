from tkinter import *
from tkinter import ttk

from crud import Funcs

from relatorios import Relatorios

root = Tk()






class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.botoes_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        #criando o loop
        root.mainloop()


    def tela(self):
        
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.wm_maxsize(1280, 1080)
        self.root.wm_minsize(720, 480)

    def frames_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2 = Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)

        
    
    def mostra_tooltip(self, texto):
        self.tooltip = Label(self.root, text=texto, background="yellow", font=("verdana", 8, "bold"))
        self.tooltip.place(x=self.root.winfo_pointerx() - self.root.winfo_rootx() + 10, 
                       y=self.root.winfo_pointery() - self.root.winfo_rooty() + 10)

    def esconde_tooltip(self):
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()









    
    def botoes_frame1(self):
        # Criando o Frame para os botões dentro de frame1
        self.botoes_frame1 = Frame(self.frame1, bg='#dfe3ee')
        self.botoes_frame1.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)  # Ajustando o posicionamento

        # Criando os botões dentro de 'self.botoes_frame1' e usando 'place'
        self.bt_limpar = Button(self.botoes_frame1, text='Limpar', bg='#107db2', fg='white', font=("verdana", 10, "bold"), command = self.limpa_cliente)
        self.bt_limpar.place(relx=0.14, rely=0.08, relwidth=0.15, relheight=0.22)  # Ajustando a posição

        self.bt_buscar = Button(self.botoes_frame1, text='Buscar', bg='#107db2', fg='white', font=("verdana", 10, "bold"), command=self.busca_cliente)
        self.bt_buscar.place(relx=0.26, rely=0.08, relwidth=0.15, relheight=0.22)  # Ajustando a posição
        self.bt_buscar.bind("<Enter>", lambda e: self.mostra_tooltip("Pesquisar por cliente"))
        self.bt_buscar.bind("<Leave>", lambda e: self.esconde_tooltip())

        self.bt_novo = Button(self.botoes_frame1, text='Novo', bg='#107db2', fg='white', font=("verdana", 10, "bold"),command= self.add_cliente)
        self.bt_novo.place(relx=0.50, rely=0.08, relwidth=0.15, relheight=0.22)  # Ajustando a posição

        self.bt_alterar = Button(self.botoes_frame1, text='Alterar', bg='#107db2', fg='white', font=("verdana", 10, "bold"), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.62, rely=0.08, relwidth=0.15, relheight=0.22)  # Ajustando a posição

        self.bt_apagar = Button(self.botoes_frame1, text='Apagar', bg='#107db2', fg='white', font=("verdana", 10, "bold"), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.74, rely=0.08, relwidth=0.15, relheight=0.22)  # Ajustando a posição

        #criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame1, text='Código', bg='white', font=("verdana", 10, "bold"))
        self.lb_codigo.place(relx=0.04 ,rely =0.05)
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.02, rely=0.15, relheight=0.08, relwidth=0.10)
        self.lb_nome = Label(self.frame1, text="Nome", bg= 'white', font=("verdana", 10, "bold"))
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.4)
        self.lb_cpf = Label(self.frame1, text="CPF", bg= 'white', font=("verdana", 10, "bold"))
        self.lb_cpf.place(relx=0.5, rely=0.35)
        self.cpf_entry = Entry(self.frame1)
        self.cpf_entry.place(relx=0.5, rely=0.45, relwidth=0.4)
        self.lb_tele = Label(self.frame1, text="Telefone", bg= 'white', font=("verdana", 10, "bold"))
        self.lb_tele.place(relx=0.05, rely=0.6)
        self.tele_entry = Entry(self.frame1)
        self.tele_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        self.lb_city = Label(self.frame1, text="Cidade", bg= 'white', font=("verdana", 10, "bold"))
        self.lb_city.place(relx=0.5, rely=0.6)
        self.city_entry = Entry(self.frame1)
        self.city_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
        self.lb_valor = Label(self.frame1, text='Valor', bg='white', font=("verdana", 10, "bold"))
        self.lb_valor.place(relx=0.05 ,rely =0.8)
        self.valor_entry = Entry(self.frame1)
        self.valor_entry.place(relx=0.05, rely=0.89, relwidth=0.10)

        self.valor_entry.place()
    
    
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3,
                                        column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaCli.heading("#0", text="")                               
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Cpf")
        self.listaCli.heading("#4", text="Telefone")
        self.listaCli.heading("#5", text="Cidade")
        self.listaCli.heading("#6", text="Valor")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.column("#5", width=125)
        self.listaCli.column("#6", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu=filemenu)
        menubar.add_cascade(label="Relatorios", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpa cliente", command= self.limpa_cliente)

        filemenu2.add_command(label="Ficha do cliente", command=self.geraRelatCliente)
    
    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title("Buscar Cliente")
        self.root2.geometry("800x400")
        
        
        
        Label(self.root2, text="CPF:").place(relx=0.5, rely=0.15)
        self.cpf_entry = Entry(self.root2)
        self.cpf_entry.place(relx=0.60, rely=0.05, relwidth=0.3)
        
        Button(self.root2, text="Buscar", command=self.preenche_janela2).place(relx=0.85, rely=0.05, relwidth=0.1)
        
        self.listaCli2 = ttk.Treeview(self.root2, height=5, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaCli2.heading("#0", text="")
        self.listaCli2.heading("#1", text="Código")
        self.listaCli2.heading("#2", text="Nome")
        self.listaCli2.heading("#3", text="CPF")
        self.listaCli2.heading("#4", text="Telefone")
        self.listaCli2.heading("#5", text="Cidade")
        self.listaCli2.heading("#6", text="Valor")
        
        self.listaCli2.column("#0", width=1)
        self.listaCli2.column("#1", width=50)
        self.listaCli2.column("#2", width=150)
        self.listaCli2.column("#3", width=100)
        self.listaCli2.column("#4", width=100)
        self.listaCli2.column("#5", width=100)
        self.listaCli2.column("#6", width=50)
        
        self.listaCli2.place(relx=0.02, rely=0.2, relwidth=0.95, relheight=0.7)
        
        self.scroolLista2 = Scrollbar(self.root2, orient='vertical')
        self.listaCli2.configure(yscroll=self.scroolLista2.set)
        self.scroolLista2.place(relx=0.96, rely=0.2, relwidth=0.03, relheight=0.7)
    
    def preenche_janela2(self):
        self.listaCli2.delete(*self.listaCli2.get_children())
        self.conecta_bd()
        
        cpf = self.cpf_entry.get() + "%"
        print("Buscando CPF:", cpf) 
        
        self.cursor.execute("""
            SELECT cod, nome_cliente, cpf, telefone, cidade, valor FROM clientes
            WHERE cpf LIKE ?
            ORDER BY nome_cliente ASC
        """, (cpf,))
        
        clientes = self.cursor.fetchall()
        print("Clientes encontrados:", clientes)
        for cliente in clientes:
            self.listaCli2.insert("", END, values=cliente)
        
        self.desconecta_bd()



Application()