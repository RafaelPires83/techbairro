import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente
VERSAO = "3.3.2"

# ============================================================
# JANELA PRINCIPAL
# ============================================================
janela = tk.Tk()
janela.title(f"TechBairro v{VERSAO}")
janela.geometry("480x460")
janela.resizable(False, False)

# ============================================================
# OBJETO GERENCIADOR
# ============================================================
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
print(f"Banco em uso: {CAMINHO_BANCO}")
gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()
id_em_edicao = None

# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================
cabecalho = tk.Frame(janela, bg="#2c3e50")
cabecalho.pack(side="top", fill="x")
tk.Label(
    cabecalho, text="Cadastro de Cliente", fg="white", bg="#2c3e50",
    font=("Arial", 14, "bold"), pady=12
).pack()

# ============================================================
# FORMULÁRIO
# ============================================================
form = tk.Frame(janela)
form.pack(pady=20)
campos = ["Nome", "Telefone", "E-mail", "Endereço"]
entradas = {}
for i, campo in enumerate(campos):
    tk.Label(form, text=f"{campo}:").grid(
        row=i, column=0, sticky="e", padx=5, pady=6
    )
    entrada = tk.Entry(form, width=30)
    entrada.grid(row=i, column=1, padx=5, pady=6)
    entradas[campo] = entrada

# ============================================================
# STATUS E CONTADOR
# ============================================================
status = tk.Label(
    janela, text="Nenhum cliente cadastrado ainda", fg="gray",
    wraplength=440, justify="left"
)
status.pack(pady=(0, 5))
contador = tk.Label(janela, text=f"Clientes cadastrados: {gerenciador.total()}")
contador.pack()

# ============================================================
# LIMPAR CAMPOS
# ============================================================
def limpar_campos():
    global id_em_edicao
    for entrada in entradas.values():
        entrada.delete(0, tk.END)
    id_em_edicao = None
    # NOVO NA AULA 20: volta ao texto normal fora do modo de edição
    botao_salvar.config(text="Salvar")

# ============================================================
# SALVAR
# ============================================================
def salvar():
    global id_em_edicao
    valores = {campo: entradas[campo].get().strip() for campo in campos}
    cliente = Cliente(
        valores["Nome"], valores["Telefone"],
        valores["E-mail"], valores["Endereço"]
    )

    # MUDOU NA AULA 21: as regras saíram daqui e foram
    # para o ValidadorCliente (validacao.py).
    # A tela só pergunta e mostra a resposta.
    erro = validador.validar(cliente)
    if erro is not None:
        status.config(
            text=erro,
            fg="red"
        )
        return

    try:
        # CADASTRO
        if id_em_edicao is None:
            gerenciador.adicionar(cliente)
            status.config(text=f"Cliente '{cliente.nome}' salvo com sucesso!", fg="green")
        # ATUALIZAÇÃO
        else:
            # MUDOU NA AULA 20: guardamos a resposta do atualizar()
            # True = uma linha foi alterada; False = o id não existe mais.
            alterou = gerenciador.atualizar(id_em_edicao, cliente)
            # NOVO NA AULA 20: o cliente pode ter sido excluído enquanto o formulário estava aberto
            if not alterou:
                status.config(
                    text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                    fg="red"
                )
                limpar_campos()
                return
            status.config(text=f"Cliente '{cliente.nome}' atualizado com sucesso!", fg="green")
    except sqlite3.Error as erro:
        status.config(text=f"Erro ao salvar no banco: {erro}", fg="red")
        return

    contador.config(text=f"Clientes cadastrados: {gerenciador.total()}")
    limpar_campos()

# ============================================================
# CANCELAR
# ============================================================
def cancelar():
    # NOVO NA AULA 20: antes de limpar, descobre se estava editando
    estava_editando = id_em_edicao is not None
    limpar_campos()
    # MUDOU NA AULA 20: mensagem diferente para quem cancela uma edição
    if estava_editando:
        status.config(text="Edição cancelada. Nada foi alterado.", fg="gray")
    else:
        status.config(text="Formulário limpo", fg="gray")

# ============================================================
# CONSULTA DE CLIENTES
# ============================================================
def abrir_consulta():
    consulta = tk.Toplevel(janela)
    consulta.title("Consulta de Clientes")
    consulta.geometry("500x380")
    consulta.resizable(False, False)

    # NOVO NA AULA 20: guarda os clientes que estão aparecendo na Listbox, na mesma ordem das linhas.
    clientes_na_tela = []

    # LISTBOX
    lista = tk.Listbox(consulta, width=65, height=12)
    lista.pack(padx=10, pady=10)

    # BARRA DE ROLAGEM
    scrollbar = tk.Scrollbar(consulta)
    scrollbar.pack(side="right", fill="y", pady=10)
    lista.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista.yview)

    # ATUALIZAR LISTA
    def atualizar_lista():
        lista.delete(0, tk.END)
        # NOVO NA AULA 20: esvazia também a lista da tela
        clientes_na_tela.clear()
        try:
            clientes_cadastrados = gerenciador.listar()
        except sqlite3.Error as erro:
            lista.insert(tk.END, f"Erro ao ler o banco: {erro}")
            return

        if not clientes_cadastrados:
            lista.insert(tk.END, "Nenhum cliente cadastrado")
            return

        for cliente in clientes_cadastrados:
            lista.insert(tk.END, cliente.resumo())
            # NOVO NA AULA 20: guarda o cliente na mesma posição da linha
            clientes_na_tela.append(cliente)

    # CLIENTE SELECIONADO
    # NOVO NA AULA 20: devolve o cliente da linha selecionada, ou None se nenhuma linha válida estiver selecionada.
    # Editar e Excluir usam esta função, e não gerenciador.listar()[indice].
    def cliente_selecionado(acao):
        selecionado = lista.curselection()
        # Protege também as linhas de aviso, que não são clientes.
        if not selecionado or selecionado[0] >= len(clientes_na_tela):
            messagebox.showwarning("Atenção", f"Selecione um cliente antes de {acao}.")
            return None
        return clientes_na_tela[selecionado[0]]

    # EDITAR CLIENTE
    def editar_cliente():
        # MUDOU NA AULA 20: pega o cliente que está na tela
        cliente = cliente_selecionado("editar")
        if cliente is None:
            return

        entradas["Nome"].delete(0, tk.END)
        entradas["Nome"].insert(0, cliente.nome)
        entradas["Telefone"].delete(0, tk.END)
        entradas["Telefone"].insert(0, cliente.telefone)
        entradas["E-mail"].delete(0, tk.END)
        entradas["E-mail"].insert(0, cliente.email)
        entradas["Endereço"].delete(0, tk.END)
        entradas["Endereço"].insert(0, cliente.endereco)

        global id_em_edicao
        id_em_edicao = cliente.id
        status.config(text=f"Editando cliente: {cliente.nome}", fg="blue")
        # NOVO NA AULA 20: deixa o modo de edição visível no botão
        botao_salvar.config(text="Salvar edição")
        consulta.destroy()

    # EXCLUIR CLIENTE
    def excluir_cliente():
        # MUDOU NA AULA 20: pega o cliente que está na tela
        cliente = cliente_selecionado("excluir")
        if cliente is None:
            return

        # CONFIRMAÇÃO
        confirmado = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cadastro de {cliente.nome}?\n\n"
            f"Essa ação não pode ser desfeita."
        )
        if not confirmado:
            return

        # Remove pelo id do cliente
        try:
            # MUDOU NA AULA 20: guardamos a resposta do remover()
            removeu = gerenciador.remover(cliente.id)
        except sqlite3.Error as erro:
            messagebox.showerror(
                "Erro no banco", f"Não foi possível excluir o cliente.\n{erro}"
            )
            return

        # NOVO NA AULA 20: o cliente já tinha sido excluído
        if not removeu:
            messagebox.showwarning(
                "Cliente não encontrado",
                f"{cliente.nome} já não está mais no banco.\n"
                f"A lista será atualizada."
            )
            atualizar_lista()
            return

        atualizar_lista()
        contador.config(text=f"Clientes cadastrados: {gerenciador.total()}")
        status.config(text=f"Cliente '{cliente.nome}' excluído com sucesso!", fg="green")

    # BOTÕES DA CONSULTA
    botoes_consulta = tk.Frame(consulta)
    botoes_consulta.pack(pady=10)
    tk.Button(
        botoes_consulta, text="Editar selecionado", width=18, command=editar_cliente
    ).grid(row=0, column=0, padx=5)
    tk.Button(
        botoes_consulta, text="Excluir selecionado", width=18, command=excluir_cliente
    ).grid(row=0, column=1, padx=5)

    # NOVO NA AULA 20: duplo clique numa linha também abre a edição.
    lista.bind("<Double-Button-1>", lambda evento: editar_cliente())
    atualizar_lista()

# ============================================================
# BOTÕES DA JANELA PRINCIPAL
# ============================================================
botoes = tk.Frame(janela)
botoes.pack(pady=10)

# Botão Salvar
# MUDOU NA AULA 20: botão guardado para mudar o texto durante a edição.
botao_salvar = tk.Button(
    botoes, text="Salvar", width=13, command=salvar
)
botao_salvar.grid(row=0, column=0, padx=5)

# Botão Cancelar
tk.Button(
    botoes, text="Cancelar", width=12, command=cancelar
).grid(row=0, column=1, padx=5)

# Botão Consultar
tk.Button(
    botoes, text="Consultar", width=12, command=abrir_consulta
).grid(row=0, column=2, padx=5)

# ============================================================
# VERSÃO
# ============================================================
tk.Label(janela, text=f"{VERSAO}", fg="gray").place(
    relx=0.97, rely=0.97, anchor="se"
)

# ============================================================
# INICIALIZAÇÃO
# ============================================================
janela.mainloop()
