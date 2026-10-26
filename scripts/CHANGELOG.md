# CHANGELOG — TechBairro
## v3.3.2 (Aula 27)

### Adicionado
- Manual de uso em `docs/manual_de_uso.md`.
- Arquivo `docs/requirements.txt`.
- Atualização das instruções de execução em `docs/COMO_EXECUTAR.txt`.
- Registro dos testes funcionais em `docs/registro_de_testes.md`.
- Checklist da entrega final em `docs/entrega_final.md`.

### Manutenção
- Atualização do gerador de pacotes para produzir a versão 3.3.2.
- Ajustes na documentação e nos arquivos de teste.

## v3.3.0 (Aula 20)

### Adicionado
- Lista em memória (clientes_na_tela) alinhada às linhas exibidas na Consulta.
- Função cliente_selecionado(acao) para validar a seleção e impedir ações sobre linhas de aviso.
- Aviso quando o cliente selecionado já não existe no banco durante uma tentativa de exclusão.
- Indicação visual do modo de edição: o botão muda para Salvar edição.
- Duplo clique em uma linha da Consulta para carregar o cliente no formulário.
- Mensagem específica quando uma edição é cancelada.

### Corrigido
- Edição e exclusão passam a usar o cliente associado à linha que o usuário realmente selecionou, evitando erros quando a lista fica desatualizada.
- A atualização verifica o retorno de atualizar() e não informa sucesso se o registro não existir mais.
- A exclusão verifica o retorno de remover() e atualiza a lista quando o cliente já tiver sido excluído.
- A seleção de linhas informativas, como Nenhum cliente cadastrado, não é tratada como seleção de cliente.
- O botão de salvar volta ao texto Salvar quando o formulário sai do modo de edição.
## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.