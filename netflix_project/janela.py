from tkinter import *
from tkinter import ttk
from create import inserir_usuarios, inserir_filmes

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        janela.mainloop()
    

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.geometry('700x500')
        self.janela.configure(background='#C44536')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    
    def frames(self):
        self.frame_0 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.35)

        self.frame_2 = Frame(self.janela, bg='#000', highlightthickness=0.03, highlightbackground='white')
        self.frame_2.place(relx=0.03, rely=0.60, relwidth=0.94, relheight=0.35)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text='Buscar', bg='red')
        self.btBuscar.place(relx=0.15, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btLimpar = Button(self.frame_0, text='Limpar', bg='red')
        self.btLimpar.place(relx=0.28, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btCreate = Button(self.frame_0, text='Create', bg='red', command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btRead = Button(self.frame_0, text='Read', bg='red')
        self.btRead.place(relx=0.55, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btUpdate = Button(self.frame_0, text='Update', bg='red')
        self.btUpdate.place(relx=0.65, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btDelete = Button(self.frame_0, text='Delete', bg='red')
        self.btDelete.place(relx=0.75, rely=0.25, relwidth=0.10, relheight=0.50)

    
    def labels(self):
        self.lbIDUsuario = Label(self.frame_0, text='ID', background='red')
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.10, relheight=0.3)

        self.lbNome = Label(self.frame_1, text='Nome', background="red")
        self.lbNome.place(relx=0.005, rely=0.05, relwidth=0.10, relheight=0.15)
        
        self.lbEmail = Label(self.frame_1, text='Email', background="red")
        self.lbEmail.place(relx=0.005, rely=0.25, relwidth=0.10, relheight=0.15)

        self.lbPlano = Label(self.frame_1, text='Plano', background="red")
        self.lbPlano.place(relx=0.005, rely=0.45, relwidth=0.10, relheight=0.15)

        self.lbTipo = Label(self.frame_1, text='Tipo', background="red")
        self.lbTipo.place(relx=0.335, rely=0.45, relwidth=0.08, relheight=0.15)

        self.lbIdade = Label(self.frame_1, text='Idade', background="red")
        self.lbIdade.place(relx=0.632, rely=0.45, relwidth=0.08, relheight=0.15)


    def inputs(self):
        self.inpIDUsuario = Entry(self.frame_0)
        self.inpIDUsuario.place(relx=0.005, rely=0.25, relwidth=0.1, relheight=0.4)

        self.inpNome = Entry(self.frame_1)
        self.inpNome.place(relx=0.12, rely=0.05, relwidth=0.8, relheight=0.15)

        self.inpEmail = Entry(self.frame_1)
        self.inpEmail.place(relx=0.12, rely=0.25, relwidth=0.8, relheight=0.15)

        self.inpPlano = Entry(self.frame_1)
        self.inpPlano.place(relx=0.12, rely=0.45, relwidth=0.2, relheight=0.15)

        self.inpTipo = Entry(self.frame_1)
        self.inpTipo.place(relx=0.425, rely=0.45, relwidth=0.2, relheight=0.15)

        self.inpIdade = Entry(self.frame_1)
        self.inpIdade.place(relx=0.72, rely=0.45, relwidth=0.2, relheight=0.15)


    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1',
                                                                      'col2',
                                                                      'col3',
                                                                      'col4',
                                                                      'col5',
                                                                      'col6'))
       

        self.listaCli.heading('#0', text='ID')
        self.listaCli.heading('#1', text='Nome')
        self.listaCli.heading('#2', text='Email')
        self.listaCli.heading('#3', text='Plano')
        self.listaCli.heading('#4', text='Tipo')
        self.listaCli.heading('#5', text='Idade')

        self.listaCli.column('#0', width=10)
        self.listaCli.column('#1', width=220)
        self.listaCli.column('#2', width=220)
        self.listaCli.column('#3', width=50)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)

        self.listaCli.place(relx=0.025, rely=0.080, relwidth=0.95, relheight=0.85)


    def insert_user(self):
        inserir_usuarios(self.inpNome.get(),
                        self.inpEmail.get(),
                        self.inpPlano.get(),
                        self.inpTipo.get(),
                        self.inpIdade.get())