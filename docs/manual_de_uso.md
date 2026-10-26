# Manual de Uso — TechBairro

## 1. Apresentação

O TechBairro é um sistema desenvolvido em Python para cadastrar e gerenciar clientes. Com ele, é possível adicionar novos clientes, consultar os cadastros existentes, editar informações e excluir registros por meio de uma interface gráfica simples.

Este manual mostra como abrir o sistema e utilizar suas principais funções.

## 2. Como iniciar o sistema

Para abrir o TechBairro, siga os passos abaixo:

1. Verifique se o Python está instalado no computador.

2. Abra a pasta do projeto TechBairro.

3. Abra um terminal dentro dessa pasta.

4. Digite o comando abaixo e pressione Enter:

   bash
   python techbairro.py


   Se o comando não funcionar no Windows, tente:

   bash
   py techbairro.py
   

5. Aguarde até que a janela do sistema seja aberta.

Se o programa não iniciar, confira se o Python está instalado corretamente, se o Tkinter está disponível e se o comando foi executado na pasta certa.

## 3. Conhecendo a tela principal

Na tela principal, você encontrará os campos usados para preencher os dados dos clientes:

Nome:nome completo ou nome informado pelo cliente.
Telefone: número de telefone, utilizando somente números.
E-mail: endereço de e-mail do cliente.
Endereço: endereço informado no cadastro.

A tela também possui os botões Salvar, Cancelar e Consultar, além de mensagens que orientam o usuário durante a utilização do sistema.

Há também um contador que mostra a quantidade de clientes cadastrados.

## 4. Como cadastrar um cliente

Para adicionar um novo cliente ao sistema:

1. Preencha o campo Nome.
2. Digite o telefone usando somente números.
3. Informe o e-mail em um formato válido, como `cliente@exemplo.com`.
4. Preencha o campo Endereço.
5. Clique em Salvar.
6. Confira a mensagem exibida para saber se o cadastro foi realizado.

Todos os campos são obrigatórios. Se algum deles estiver vazio ou apresentar informações inválidas, o sistema mostrará um aviso indicando o que precisa ser corrigido.

## 5. Como consultar clientes

Para visualizar os clientes já cadastrados:

1. Clique no botão Consultar, na tela principal.
2. Aguarde a abertura da janela Consulta de Clientes.
3. Confira a lista de registros disponíveis.
4. Selecione o cliente desejado caso queira editar ou excluir seu cadastro.

Se ainda não houver clientes cadastrados, o sistema informará que não existem registros disponíveis.

## 6. Como editar um cadastro

Se precisar corrigir ou atualizar os dados de um cliente, siga estas etapas:

1. Abra a janela de consulta.
2. Selecione o cadastro que deseja alterar.
3. Clique em Editar selecionado ou dê dois cliques sobre o registro.
4. Altere as informações necessárias na tela principal.
5. Clique em Salvar edição.
6. Confira a mensagem exibida para verificar se a atualização foi concluída.

Se o cadastro não existir mais, o sistema poderá informar que o cliente não foi encontrado.

## 7. Como excluir um cadastro

Para remover um cliente do sistema:

1. Abra a janela Consulta de Clientes
2. Selecione o cliente que deseja excluir.
3. Clique em Excluir selecionado.
4. Leia a mensagem de confirmação.
5. Confirme a exclusão somente se tiver certeza de que deseja remover o registro.

A exclusão remove o cadastro do banco de dados e não pode ser desfeita diretamente pelo programa. Por isso, confira se selecionou o cliente correto antes de confirmar.

Se nenhum cliente estiver selecionado, o sistema exibirá um aviso solicitando a seleção de um registro.

## 8. Como utilizar o botão Cancelar

O botão *Cancelar serve para interromper uma edição que ainda não foi salva.

Se você começou a alterar os dados de um cliente, mas decidiu não continuar, utilize essa opção para cancelar a edição sem gravar as alterações realizadas.

O sistema exibirá a mensagem informando que a edição foi cancelada e que nada foi alterado.

## 9. Entendendo as mensagens do sistema

Durante o uso do TechBairro, algumas mensagens podem aparecer para informar o resultado de uma operação ou indicar
