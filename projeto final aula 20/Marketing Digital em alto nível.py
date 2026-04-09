#Marketing Digital - sistema

import sqlite3 # banco de dados
import tkinter as tk # lib de interface gráfica
from tkinter import messagebox, ttk # caixa de msg / tkinter


def conectar():
    return sqlite3.connect('Clientes.db')

# CREATE READ UPDATE DELETE

# banco de dados
def criar_tabela():
    conn = conectar()
    c = conn.cursor() # digitar sql num arquivo python
    c.execute('''
               CREATE TABLE IF NOT EXISTS usuarios(
             
            
              nome TEXT NOT NULL,
              email TEXT NOT NULL,
              telefone INTEGER NOT NULL,
              interesse TEXT NOT NULL,
              status TEXT NOT NULL
             
              )''')
    conn.commit()
    conn.close()          


# CREATE CRUD

def inserir_usuario():
    
   
    nome  =  entry_nome.get().strip()
    email =  entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    interesse  =  entry_interesse.get().strip()
    status = entry_status.get().strip()
   
    if nome and email and telefone and interesse and status:
    #    try:
            conn  =  conectar()
            c = conn.cursor()
            c.execute('INSERT INTO usuarios (nome, email, telefone, interesse, status) VALUES (?,?,?,?,?)', (nome,email,telefone,interesse,status))
            conn.commit()
            conn.close()
            messagebox.showinfo('Dados','DADOS INSERIDOS COM SUCESSO!')
            mostra_usuario()
            entry_nome.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
            entry_interesse.delete(0, tk.END)
            entry_status.delete(0, tk.END)
            if status == '1':
                 tipo = 'Andamento'
            elif status == '2':
                 tipo = 'Convertido'
            elif status == '3':
                 tipo = 'Perdido'
            
    #    except sqlite3.IntegrityError:
    #         messagebox.showerror('Erro', 'O DADO JA EXISTE')

    else:
        messagebox.showwarning('Dado', 'INSIRA TODOS OS DADOS')


def mostra_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn  =  conectar()
    c = conn.cursor()        
    c.execute('SELECT * FROM usuarios')
    usuarios =  c.fetchall()
    for usuario in usuarios:
        tree.insert('', 'end', values=usuario)
    conn.close()    


# ATUALIZAR
def editar():
    selecao = tree.selection()
    user_telefone  =  tree.item(selecao)['values'][0]
    if selecao:
       
        novo_nome  =  entry_nome.get()
        novo_email =  entry_email.get()
        novo_interesse = entry_interesse.get()
        novo_status = entry_status.get()

        if  novo_nome and novo_email:
            try:
                    conn  =  conectar()
                    c = conn.cursor()
                    c.execute('UPDATE usuarios SET nome = ?,  email = ? WHERE id = ?', (novo_nome, novo_email,user_telefone,novo_interesse,novo_status))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Dados','DADOS INSERIDOS COM SUCESSO!')
                    mostra_usuario()
                    entry_nome.delete(0, tk.END)
                    entry_email.delete(0, tk.END)
                    entry_telefone.delete(0, tk.END)
                    entry_interesse.delete(0, tk.END)
                    entry_status.delete(0, tk.END)
            except:
                    messagebox.showerror('Erro', 'OCORREU UM ERRO AO INSERIR OS DADOS, VERIFIQUE')
        else:
            messagebox.showwarning('Dado', 'INSIRA TODOS OS DADOS')





# DELETAR

def deletar_usuario():
    selecao = tree.selection()
    if selecao:
        user_telefone  =  tree.item(selecao)['values'][0]
        conn  =  conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE telefone = ?', (user_telefone,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Dados', 'DADOS DELETADOS COM SUCESSO!')
        mostra_usuario()
    else:
        messagebox.showerror('Dados', 'ERRO AO DELEETAR OS DADOS!')    
     
   


# interface grafica
janela = tk.Tk()
janela.geometry('800x550')
janela.title(' MARKETING ')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background = 'yellow', font = ('arial', 10))
style.configure('TEntry', font = ('Segoe UI', 10))
style.configure('TButton', font = ('Segoe UI', 10), padding = 6)
style.configure('Treeview.Hending', font = ('Segoe UI', 10, 'bold'))
style.configure('Treeview',font = ('Segoe UI', 10, 'bold'))


# frames  -  sessão
main_frame =  ttk.Frame(janela, padding=16)
main_frame.pack(fill=tk.BOTH, expand=True)


# widgets -  elementos  

titulo = ttk.Label(main_frame, text='Sistema de Marketing', font=('Segoe UI', 10, 'bold'))
titulo.grid(row=0, columnspan=3,pady=(0,15), sticky='w')
###############################

# widgets -  elementos  



input_frame =  ttk.LabelFrame(main_frame, text='DADOS DO USUARIO', padding=10)
input_frame.grid(row=1,column= 0, columnspan = 2, sticky='ew', pady=(0,15))

# textos para direcionar
# NOME
ttk.Label(input_frame, text='NOME').grid(row=0, column=0, padx=(0,10), pady=5, sticky='e')

entry_nome = ttk.Entry(input_frame, width=30)
entry_nome.grid(row=0, column=1, padx=(0,20), pady=5, sticky='w')


# textos para direcionar
# E-MAIL
ttk.Label(input_frame, text='E-MAIL').grid(row=1, column=0, padx=(0,10), pady=5, sticky='e')

entry_email = ttk.Entry(input_frame, width=30)
entry_email.grid(row=1, column=1, padx=(0,20), pady=5, sticky='w')

# textos para direcionar
# Telefone
ttk.Label(input_frame, text='TELEFONE').grid(row=2, column=0, padx=(0,10), pady=5, sticky='e')

entry_telefone = ttk.Entry(input_frame, width=30)
entry_telefone.grid(row=2, column=1, padx=(0,20), pady=5, sticky='w')

# textos para direcionar
# Interesse / Andamento
# textos para direcionar
#Interesse
ttk.Label(input_frame, text='INTERESSE').grid(row=3, column=0, padx=(0,10), pady=5, sticky='e')

entry_interesse = ttk.Entry(input_frame, width=30)
entry_interesse.grid(row=3, column=1, padx=(0,20), pady=5, sticky='w')

#opções
ttk.Label(input_frame, text='STATUS').grid(row=4, column=0, padx=(0,10), pady=5, sticky='e')

opcoes = ['andamento','convertido','perdido']
entry_status = ttk.Combobox(input_frame, width=30,values=opcoes,state='readonly')
entry_status.grid(row=4, column=1, padx=(0,20), pady=5, sticky='w')

# botões
btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=2, column=0, columnspan=3, pady=(0,15), sticky='ew')


btn_salvar = ttk.Button(btn_frame, text='SALVAR', command=inserir_usuario)
btn_salvar.pack(side = tk.LEFT, padx=5 )

btn_atualizar = ttk.Button(btn_frame, text='ATUALIZAR', command=editar)
btn_atualizar.pack(side = tk.LEFT, padx=5 )

btn_deletar = ttk.Button(btn_frame, text='DELETAR', command= deletar_usuario)
btn_deletar.pack(side = tk.LEFT, padx=5 )

# btn_limpar = ttk.Button(btn_frame, text='LIMPAR')
# btn_limpar.pack(side = tk.LEFT, padx=5 )

# Treeview - vizualizar os dados

tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=3, column=0, columnspan=2, sticky='nsew')

main_frame.columnconfigure(0, weight = 1)
main_frame.rowconfigure(3,weight = 1)

# criação da TreeView
columns = ('NOME', 'E-MAIL','TELEFONE', 'INTERESSE','STATUS' )
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=12)
tree.pack(fill=tk.BOTH, expand=True)

for col in columns:
    tree.heading(col, text= col)
    tree.column(col, width=150, anchor='center')

# scrolbar -  barra rolagem

scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

criar_tabela()
mostra_usuario()

janela.mainloop()
