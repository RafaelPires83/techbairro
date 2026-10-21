# ============================================================
# CLIENTE (Aula 21)
# ============================================================
#
# Responsabilidade: representar os dados de um cliente.
#
# NOVO NA AULA 21: a classe Cliente saiu do techbairro.py
# e veio para este arquivo, sem nenhuma mudança por dentro.
# Este arquivo não sabe nada de janela nem de banco.

class Cliente:
    def __init__(self, nome, telefone, email, endereco, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"

    def iniciais(self):
        partes = self.nome.split()
        return "".join(parte[0].upper() for parte in partes if parte)