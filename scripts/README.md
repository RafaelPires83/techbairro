# TechBairro

A TechBairro é um sistema de cadastro e gerenciamento de clientes desenvolvido em Python. O sistema permite cadastrar, consultar, editar e excluir clientes, auxiliando na organização das informações de uma associação de moradores.

**Versão atual:** 3.3.2 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar os clientes cadastrados.
- Editar os dados de um cliente existente.
- Excluir clientes mediante confirmação.
- Validar campos obrigatórios, telefone e formato básico do e-mail.
- Armazenar os cadastros em um banco de dados SQLite.
- Exibir mensagens de confirmação, aviso e erro para orientar o usuário.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows, Linux ou macOS compatível com Python e Tkinter. O sistema operacional testado deve ser informado após a realização do teste. |
| Python | Python 3 (versão testada: preencher após verificar a versão utilizada nos testes). |
| Tkinter | Necessário para executar a interface gráfica. Sua disponibilidade deve ser verificada na instalação do Python. |
| Bibliotecas externas | Nenhuma no momento. O projeto utiliza módulos da biblioteca padrão do Python, como `tkinter`, `sqlite3` e `os`. |
| Internet | Necessária para clonar ou baixar o projeto. Não é necessária para as funções básicas após o download. |

## Instalação

1. Baixe o projeto pelo GitHub, acessando [TechBairro](https://github.com/RafaelPires83/techbairro) e selecionando Code → Download ZIP, ou clone o repositório pelo terminal:

   bash
   git clone https://github.com/RafaelPires83/techbairro.git
   

2. Extraia o arquivo ZIP, se tiver escolhido o download, e abra a pasta do projeto no VS Code ou no terminal. Se clonou o repositório, entre na pasta:

   bash
   cd techbairro
   

3. Execute o programa na pasta que contém o arquivo `techbairro.py`:

   bash
   python techbairro.py
   

   No Windows, se necessário, utilize:

   bash
   py techbairro.py
   
   Se a execução ocorrer corretamente, a janela da TechBairro será aberta e o terminal exibirá o caminho do banco de dados em uso.

## Configuração do banco de dados

A TechBairro utiliza o SQLite para armazenar as informações dos clientes. O arquivo techbairro.db fica no mesmo diretório do arquivo Python principal, `techbairro.py`, e é criado pelo sistema quando necessário, durante a inicialização do banco de dados.

Para saber qual banco está sendo utilizado, observe a mensagem Banco em uso: ... exibida no terminal ao iniciar o programa.

O banco de dados não deve ser incluído no repositório público porque pode conter dados pessoais dos clientes. O arquivo deve ser mantido fora do controle de versão por meio do .gitignore.

Para fazer uma cópia de segurança, feche o programa e copie o arquivo techbairro.db para uma pasta segura, com acesso restrito. Se o arquivo ainda não tiver sido criado, execute o programa primeiro. Faça cópias de segurança periódicas e não publique bancos que contenham dados reais.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

- techbairro.py — arquivo principal, responsável pela interface gráfica e pelas operações de cadastro e gerenciamento.
- README.md — documentação principal, com informações sobre o projeto, requisitos e instalação.
- requirements.txt — registra informações sobre as dependências do projeto; atualmente, não há bibliotecas externas necessárias.
- CHANGELOG.md — histórico das alterações realizadas em cada versão do sistema.
- docs/ — pasta destinada à documentação complementar.
- docs/manual_de_uso.md — manual com instruções para utilizar as funcionalidades da aplicação.
- .gitignore — define os arquivos e diretórios que não devem ser enviados ao repositório, como o banco de dados local.

## Autor

Rafael Pires+

Curso Técnico em Desenvolvimento de Sistemas — Senac-DF.
