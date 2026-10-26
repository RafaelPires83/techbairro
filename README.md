# TechBairro — Cadastro de Clientes

O TechBairro é um sistema de cadastro de clientes desenvolvido em Python, com interface gráfica feita em Tkinter e banco de dados SQLite. A versão atual é a **v3.2**.

## O que o sistema faz

Com o TechBairro, é possível cadastrar novos clientes, consultar os registros, editar informações e excluir cadastros. Cada cliente possui nome, telefone, e-mail e endereço.

Os dados ficam armazenados no arquivo `techbairro.db`, permitindo que as informações continuem salvas mesmo depois que o programa é fechado. Na tela principal, também é possível ver o total de clientes cadastrados.

Antes de salvar um cadastro, o sistema verifica se os dados foram preenchidos corretamente. Nenhum campo pode ficar vazio, o telefone deve conter apenas números e o e-mail precisa ter um formato válido, com texto antes do `@` e um ponto depois dele.

## Como executar o programa

Para rodar o projeto, é necessário ter o Python 3 instalado. O Tkinter já acompanha a instalação padrão do Python na maioria dos sistemas.

Com o terminal aberto na pasta do projeto, execute o comando:

```bash
python techbairro.py
```

Ao iniciar, o terminal exibe a mensagem "Banco em uso", seguida do caminho do banco de dados. Em seguida, a janela de cadastro é aberta.

Para consultar os registros existentes, basta clicar no botão **Consultar**. Na lista de clientes, é possível selecionar um cadastro e editar ou excluir suas informações.

## Estrutura do projeto

```text
TechBairro/
├── techbairro.py      # Programa principal, telas e eventos
├── Dados.py           # Classes Cliente e GerenciadorClientes
├── techbairro.db      # Banco de dados local
├── CHANGELOG.md       # Histórico de alterações
├── README.md          # Documentação principal
├── scripts/           # Scripts de apoio
└── docs/              # Modelagem, testes e verificações
```

O arquivo `Dados.py` deve permanecer na mesma pasta que `techbairro.py`, pois o programa importa as classes definidas nele.

O banco `techbairro.db` é criado e utilizado localmente e não deve ser incluído no versionamento.

## Scripts de apoio

A pasta `scripts/` reúne alguns utilitários que trabalham com o mesmo banco de dados localizado na pasta principal do projeto.

* **`importar_planilha_antiga.py`** — importa os clientes de uma planilha antiga para o banco de dados. Deve ser executado apenas uma vez para evitar cadastros duplicados.
* **`verificar_banco.py`** — verifica o banco de dados e exibe a mensagem "Banco verificado", junto com o caminho do arquivo e a quantidade de clientes cadastrados.
* **`travar_banco.py`** — permite simular uma situação em que o banco está ocupado, ajudando a testar o comportamento do sistema. Para liberar o banco, basta pressionar Enter.

## Controle de versões

O histórico das alterações e melhorias do projeto está disponível no arquivo `CHANGELOG.md`.

O TechBairro utiliza o versionamento semântico, seguindo o formato `MAJOR.MINOR.PATCH`, que identifica mudanças principais, novas funcionalidades e correções.

## Cuidados com os dados

O arquivo `techbairro.db` pode conter informações reais de clientes. Por isso, ele não deve ser enviado ao Git nem compartilhado fora da equipe. Essa medida ajuda a proteger os dados armazenados no sistema.
