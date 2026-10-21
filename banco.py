# ============================================================
# BANCO (Aula 21)
# ============================================================
#
# Responsabilidade: toda a comunicação com o banco SQLite.
# Este arquivo não sabe nada de janela.

# Importa o módulo do SQLite (já vem com o Python)
import sqlite3

# O banco devolve linhas; o GerenciadorClientes transforma cada linha
# num objeto Cliente, por isso precisa conhecer a classe
from cliente import Cliente

class GerenciadorClientes:
    def __init__(self, caminho_banco="techbairro.db"):
        self.caminho_banco = caminho_banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):
        conexao = self.conectar()
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT,
                endereco TEXT
            )
        """)
        conexao.commit()
        conexao.close()

    # CREATE
    def adicionar(self, cliente):
        conexao = self.conectar()
        cursor = conexao.execute(
            "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
            (cliente.nome, cliente.telefone, cliente.email, cliente.endereco)
        )
        conexao.commit()
        cliente.id = cursor.lastrowid
        conexao.close()

    # READ
    def listar(self):
        conexao = self.conectar()
        linhas = conexao.execute(
            "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY nome"
        ).fetchall()
        conexao.close()
        return [
            Cliente(nome, telefone, email, endereco, id)
            for (id, nome, telefone, email, endereco) in linhas
        ]

    # UPDATE
    def atualizar(self, id_cliente, novo_cliente):
        conexao = self.conectar()
        cursor = conexao.execute(
            "UPDATE clientes SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id = ?",
            (novo_cliente.nome, novo_cliente.telefone, novo_cliente.email,
             novo_cliente.endereco, id_cliente)
        )
        conexao.commit()
        conexao.close()
        return cursor.rowcount == 1

    # DELETE
    def remover(self, id_cliente):
        conexao = self.conectar()
        cursor = conexao.execute(
            "DELETE FROM clientes WHERE id = ?", (id_cliente,)
        )
        conexao.commit()
        conexao.close()
        return cursor.rowcount == 1

    # TOTAL
    def total(self):
        conexao = self.conectar()
        quantidade = conexao.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
        conexao.close()
        return quantidade
