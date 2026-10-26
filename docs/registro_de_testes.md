Teste	Resultado 
CT01 — Cadastrar cliente	
ok
CT02 — Nome e endereço vazios	
ok
CT03 — Telefone com espaços	
Falhou
CT04 — E-mail sem ponto	
ok
CT05 — Editar cliente	
ok
CT06 — Excluir cliente	
ok

-+-+-++--+-+-+-+-++-+-+--+-++-+-+-+-+-+-+-+-+-+-+

CT01 — Cadastrar cliente: OK.

CT02 — Nome e endereço vazios: OK.

CT03 — Telefone com espaços: Falhou inicialmente. Após a correção da validação, o teste foi executado novamente e passou.

CT04 — E-mail sem ponto: OK.

CT05 — Editar cliente: OK.

CT06 — Excluir cliente: OK.

Resultado: Os seis testes automáticos passaram. Foram verificadas situações como cadastro válido, campos obrigatórios vazios, telefone com letras e e-mails inválidos.

Problemas encontrados e correções

Durante os testes, o CT03 mostrou que o sistema não aceitava números de telefone com espaços. Para corrigir isso, a validação em validacao.py foi ajustada para remover os espaços antes de verificar se o telefone contém apenas números.

Também foi atualizada, no arquivo teste_validacao.py, a mensagem esperada para o teste de telefone com letras.

Após as alterações, os seis testes automáticos passaram e o CT03 foi executado novamente na interface, com resultado positivo.

Commit da correção: [Corrige validação de telefone com espaços e registra testes da versão 3.3.2].