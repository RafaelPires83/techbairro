# ============================================================
# TRAVAR BANCO (Aula 16)
# ============================================================
#
# Simula outro programa usando o banco ao mesmo tempo
# e segurando uma trava exclusiva nele.
#
# Enquanto este script estiver esperando o Enter,
# nenhum outro programa consegue ler nem gravar no techbairro.db
# (quem tentar espera 5 segundos e recebe o erro "database is locked").
import sqlite3
import os
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
# isolation_level=None: nós mesmos controlamos a transação
conexao = sqlite3.connect(CAMINHO_BANCO, isolation_level=None)
# BEGIN EXCLUSIVE: pega a trava exclusiva do banco
conexao.execute("BEGIN EXCLUSIVE")
input("Banco TRAVADO. Teste a TechBairro agora e aperte Enter aqui paraliberar...")
# Desfaz a transação (não alteramos nada) e libera a trava
conexao.execute("ROLLBACK")
conexao.close()
print("Banco liberado.")