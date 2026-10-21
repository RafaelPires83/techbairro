# ============================================================
# GERAR PACOTE DA VERSÃO (Aula 18)
# ============================================================

import os
import zipfile

PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)

# Mesma versão usada no atividade25.py
VERSAO = "3.2.1"

# Pastas que NÃO entram no pacote
PASTAS_FORA = ["dist", "__pycache__"]

# Tipos de arquivo que NÃO entram no pacote
EXTENSOES_FORA = [".db", ".pyc"]

PASTA_DIST = os.path.join(PASTA_DO_PROJETO, "dist")
os.makedirs(PASTA_DIST, exist_ok=True)

NOME_PACOTE = f"TechBairro-{VERSAO}"
CAMINHO_PACOTE = os.path.join(PASTA_DIST, NOME_PACOTE + ".zip")

print(f"Gerando {NOME_PACOTE}.zip")
print()

incluidos = 0
deixados_de_fora = 0

with zipfile.ZipFile(CAMINHO_PACOTE, "w", zipfile.ZIP_DEFLATED) as pacote:

    for pasta_atual, subpastas, arquivos in os.walk(PASTA_DO_PROJETO):

        for nome in arquivos:

            caminho = os.path.join(pasta_atual, nome)
            relativo = os.path.relpath(caminho, PASTA_DO_PROJETO)

            dentro_de_pasta_fora = False

            for parte in relativo.split(os.sep):
                if parte in PASTAS_FORA:
                    dentro_de_pasta_fora = True

            extensao = os.path.splitext(nome)[1]

            if dentro_de_pasta_fora or extensao in EXTENSOES_FORA:

                print(f" fora {relativo}")
                deixados_de_fora += 1

            else:

                pacote.write(
                    caminho,
                    os.path.join(NOME_PACOTE, relativo)
                )

                print(f" incluído {relativo}")
                incluidos += 1

print()
print(f"Arquivos incluídos: {incluidos}")
print(f"Arquivos deixados de fora: {deixados_de_fora}")
print(f"Pacote salvo em: {CAMINHO_PACOTE}")
