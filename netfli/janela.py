from tkinter import *
from tkinter import ttk
from create import inserir_usuarios, inserir_filmes
from read import listar_usuarios, procurar_usuario
from update import up_usuario, up_filme
from delete import dt_filme, dt_usuario
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


janela = Tk()
usuarios = []
idades = []

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        self.select_list()
        self.grafico()
        janela.mainloop()
    

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.geometry('700x1000')
        self.janela.configure(background='#C44536')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=800)

    
    def frames(self):
        self.frame_0 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.08)

        self.frame_1 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_1.place(relx=0.03, rely=0.13, relwidth=0.94, relheight=0.15)

        self.frame_2 = Frame(self.janela, bg='#000', highlightthickness=0.05, highlightbackground='white')
        self.frame_2.place(relx=0.03, rely=0.3, relwidth=0.94, relheight=0.25)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text='Buscar', bg='red', command=self.select_user)
        self.btBuscar.place(relx=0.15, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btLimpar = Button(self.frame_0, text='Limpar', bg='red', command=self.clear)
        self.btLimpar.place(relx=0.28, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btCreate = Button(self.frame_0, text='Create', bg='red', command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btRead = Button(self.frame_0, text='Read', bg='red', command=self.ler_usuario)
        self.btRead.place(relx=0.55, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btUpdate = Button(self.frame_0, text='Update', bg='red', command=self.update_user)
        self.btUpdate.place(relx=0.65, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btDelete = Button(self.frame_0, text='Delete', bg='red', command=self.delete_user)
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
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col0',
                                                                      'col1',
                                                                      'col2',
                                                                      'col3',
                                                                      'col4',
                                                                      'col5',
                                                                      'col6'))
       

        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Email')
        self.listaCli.heading('#4', text='Plano')
        self.listaCli.heading('#5', text='Tipo')
        self.listaCli.heading('#6', text='Idade')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=10)
        self.listaCli.column('#2', width=220)
        self.listaCli.column('#3', width=220)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)
        self.listaCli.column('#6', width=50)

        self.listaCli.place(relx=0.025, rely=0.080, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.98, rely=0.10, relwidth=0.02, relheight=0.85)

    def select_list(self):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in listar_usuarios():
            self.listaCli.insert(parent='', index=0,values=i)
            usuarios.append(i[1])
            idades.append(i[5])


    def insert_user(self):
        inserir_usuarios(self.inpNome.get(),
                        self.inpEmail.get(),
                        self.inpPlano.get(),
                        self.inpTipo.get(),
                        self.inpIdade.get())
        self.limpar_tela()
        self.select_list()
        self.grafico()

    def delete_user(self):
        dt_usuario(self.inpIDUsuario.get())
        self.limpar_tela()
        self.select_list()

    def limpar_tela(self):
        self.inpIDUsuario.delete(0, END)
        self.inpTipo.delete(0, END)
        self.inpNome.delete(0, END)
        self.inpIdade.delete(0, END)
        self.inpEmail.delete(0, END)
        self.inpPlano.delete(0, END)
        self.listaCli.delete(*self.listaCli.get_children())

    def clear(self):
        self.listaCli.delete(*self.listaCli.get_children())

    def ler_usuario(self):
        self.clear()
        usuarios = listar_usuarios()
        for usuario in usuarios:
            self.listaCli.insert("", "end", values=usuario)

    def update_user(self):
        if self.inpNome.get():
            self.inpIDUsuario.update()
            self.inpNome.update()
            self.inpTipo.update()
            self.inpEmail.update()
            self.inpIdade.update()
            self.inpPlano.update()
            up_usuario(self.inpIDUsuario.get(),
                       self.inpNome.get(), self.inpEmail.get(),
                       self.inpPlano.get(), self.inpTipo.get(),
                       self.inpIdade.get())
            self.limpar_tela()
            self.select_list()

    def select_user(self):
        self.clear()
        usuario = procurar_usuario(self.inpIDUsuario.get())
        self.listaCli.insert(parent='', index=0, values=usuario[0])
        self.inpNome.insert(0, usuario[0][1])
        self.inpEmail.insert(0, usuario[0][2])
        self.inpPlano.insert(0, usuario[0][3])
        self.inpTipo.insert(0, usuario[0][4])
        self.inpIdade.insert(0, usuario[0][5])

    def grafico(self):

        figura = plt.Figure(figsize=(6,3), dpi=60)
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, self.janela)
        canva.get_tk_widget().place(relx=0.05, rely=0.60)

        x = usuarios
        y = idades

        ax.bar(x, y)

        ax.set_ylabel('idades')
        ax.set_title('Netflix')

        plt.show()