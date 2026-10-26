# ============================================================
# VALIDAÇÃO (Aula 21)
# ============================================================
#
# Responsabilidade: as regras de negócio do cadastro (RF01 a RF03).
# Este arquivo não sabe nada de janela nem de banco.

# Classe responsável por conferir se um cliente pode ser gravado
class ValidadorCliente:
    # Confere todas as regras do cliente.
    #
    # Retorna a mensagem do primeiro problema encontrado,
    # ou None se o cliente estiver válido.
    def validar(self, cliente):
        # RF01: lista com os campos vazios, com o nome que aparece na tela
        vazios = []
        if cliente.nome == "":
            vazios.append("Nome")
        if cliente.telefone == "":
            vazios.append("Telefone")
        if cliente.email == "":
            vazios.append("E-mail")
        if cliente.endereco == "":
            vazios.append("Endereço")

        # Se houver algum campo vazio
        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        # RF02: o telefone precisa ter somente números
            # RF02: o telefone pode conter números e espaços
        telefone = cliente.telefone.replace(" ", "")

        if not telefone.isdigit():
            return "Telefone inválido: use somente números e espaços."

        # RF03: o e-mail precisa estar no formato nome@dominio.com
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido: use o formato nome@dominio.com"

        # Nenhum problema encontrado
        return None

    # MUDOU NA AULA 21: era uma função solta no techbairro.py,
    # agora é um método do ValidadorCliente
    def email_parece_valido(self, email):
        if "@" not in email:
            return False
        usuario, _, dominio = email.partition("@")
        if usuario == "":
            return False
        if "." not in dominio:
            return False
        return True