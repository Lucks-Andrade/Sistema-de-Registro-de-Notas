from database import *
from tkinter import *
from tkinter import messagebox


def cadastrar_aluno():
    matricula = entry_matricula.get()
    nome = entry_nome.get()
    data_nascimento = entry_data.get()
    nota = entry_nota.get()

    if not matricula or not nome or not data_nascimento or not nota:
        messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")
        return

    try:
        nota_float = float(nota)
        if nota_float < 0 or nota_float > 10:
            messagebox.showwarning("Atenção", "A nota deve ser entre 0 e 10!")
            return
    except ValueError:
        messagebox.showwarning("Atenção", "A nota deve ser um número!")
        return

    inserir_aluno(matricula, nome, data_nascimento, nota_float)
    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
    limpar_campos()

def atualizar_aluno_interface():
    matricula = entry_matricula.get()
    nome = entry_nome.get()
    data_nascimento = entry_data.get()
    nota = entry_nota.get()

    if not matricula or not nome or not data_nascimento or not nota:
        messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")
        return

    try:
        nota_float = float(nota)
        if nota_float < 0 or nota_float > 10:
            messagebox.showwarning("Atenção", "A nota deve ser entre 0 e 10!")
            return
    except ValueError:
        messagebox.showwarning("Atenção", "A nota deve ser um número!")
        return

    atualizar_aluno(matricula, nome, data_nascimento, nota_float)
    messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
    limpar_campos()

def deletar_aluno_interface():
    matricula = entry_matricula.get()

    if not matricula:
        messagebox.showwarning("Atenção", "A matrícula deve ser preenchida!")
        return

    deletar_aluno(matricula)
    messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
    limpar_campos()

def buscar_aluno_interface():
    matricula = entry_matricula.get()

    if not matricula:
        messagebox.showwarning("Atenção", "A matrícula deve ser preenchida!")
        return

    aluno = buscar_matricula(matricula)

    if aluno:
        texto_resultado.delete(1.0, END)
        texto_resultado.insert(END, f"Matrícula: {aluno[0]}\n")
        texto_resultado.insert(END, f"Nome: {aluno[1]}\n")
        texto_resultado.insert(END, f"Data de Nascimento: {aluno[2]}\n")
        texto_resultado.insert(END, f"Nota: {aluno[3]}\n")
    else:
        messagebox.showinfo("Resultado", "Aluno não encontrado!")
        texto_resultado.delete(1.0, END)

def listar_alunos_interface():
    alunos = listar_alunos()

    if alunos:
        texto_resultado.delete(1.0, END)
        for aluno in alunos:
            texto_resultado.insert(END, f"Matrícula: {aluno[0]}\n")
            texto_resultado.insert(END, f"Nome: {aluno[1]}\n")
            texto_resultado.insert(END, f"Data de Nascimento: {aluno[2]}\n")
            texto_resultado.insert(END, f"Nota: {aluno[3]}\n")
            texto_resultado.insert(END, "-------------------------\n")
    else:
        messagebox.showinfo("Resultado", "Nenhum aluno cadastrado!")
        texto_resultado.delete(1.0, END)

def limpar_campos():
    entry_matricula.delete(0, END)
    entry_nome.delete(0, END)
    entry_data.delete(0, END)
    entry_nota.delete(0, END)
    texto_resultado.delete(1.0, END)

# CRIA A JANELA
janela = Tk()
janela.configure(bg="#e8f0fe")
janela.title("Sistema de Registro de Notas")
janela.geometry("700x550")
janela.resizable(False, False)

# TÍTULO
titulo = Label(
    janela,
    text="Sistema de Registro de Notas",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=10)

# FRAME DOS CAMPOS
frame_campos = Frame(janela)
frame_campos.pack(pady=10)

# MATRÍCULA
label_matricula = Label(frame_campos, text="Matrícula:")
label_matricula.grid(row=0, column=0, padx=5, pady=5)

entry_matricula = Entry(frame_campos, width=30)
entry_matricula.grid(row=0, column=1, padx=5, pady=5)

# NOME
label_nome = Label(frame_campos, text="Nome:")
label_nome.grid(row=1, column=0, padx=5, pady=5)

entry_nome = Entry(frame_campos, width=30)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

# DATA
label_data = Label(frame_campos, text="Data de Nascimento:")
label_data.grid(row=2, column=0, padx=5, pady=5)

entry_data = Entry(frame_campos, width=30)
entry_data.grid(row=2, column=1, padx=5, pady=5)

# NOTA
label_nota = Label(frame_campos, text="Nota:")
label_nota.grid(row=3, column=0, padx=5, pady=5)

entry_nota = Entry(frame_campos, width=30)
entry_nota.grid(row=3, column=1, padx=5, pady=5)

# FRAME DOS BOTÕES
frame_botoes = Frame(janela)
frame_botoes.pack(pady=15)

# BOTÕES
botao_cadastrar = Button(
    frame_botoes,
    text="Cadastrar",
    width=15,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    command=cadastrar_aluno
)
botao_cadastrar.grid(row=0, column=0, padx=5, pady=5)

botao_buscar = Button(
    frame_botoes,
    text="Buscar",
    width=15,
    command=buscar_aluno_interface
)
botao_buscar.grid(row=0, column=1, padx=5, pady=5)

botao_atualizar = Button(
    frame_botoes,
    text="Atualizar",
    width=15,
    command=atualizar_aluno_interface
)
botao_atualizar.grid(row=0, column=2, padx=5, pady=5)

botao_deletar = Button(
    frame_botoes,
    text="Deletar",
    width=15,
    command=deletar_aluno_interface
)
botao_deletar.grid(row=0, column=3, padx=5, pady=5)

botao_listar = Button(
    frame_botoes,
    text="Listar Alunos",
    width=15,
    command=listar_alunos_interface
)
botao_listar.grid(row=1, column=1, padx=5, pady=5)

botao_limpar = Button(
    frame_botoes,
    text="Limpar",
    width=15,
    command=limpar_campos
)
botao_limpar.grid(row=1, column=2, padx=5, pady=5)

# ÁREA DE RESULTADOS
texto_resultado = Text(
    janela,
    width=80,
    height=12,
    font=("Consolas", 10)
)

texto_resultado.pack(pady=20)

# LOOP PRINCIPAL
janela.mainloop()