Objetivo Atual:
    consertar a cagada de prganizations e fazer bonitinho agr

    sistema de criar novas organizacoes e listar seus usuarios para o admin ou apenas a organizacao em que cada orgadmin pertence.



Admin:
Possui acesso total a todas as funcionalidades do The Hive.
Pode criar, editar e excluir casos, tarefas, observáveis e indicadores.
Gerencia usuários, configurações do sistema e integrações.
É responsável por ajustar configurações de segurança, políticas de dados e autenticação.

OrgAdmin:
Administra um determinado tenant ou organização dentro do The Hive.
Tem controle completo sobre todos os casos e recursos da organização específica.
Pode criar, editar e deletar usuários e configurações dessa organização, mas sem acesso às configurações globais do sistema.

Analyst:
Papel mais comum para membros de um SOC que analisam incidentes e realizam investigações.
Pode visualizar, criar, editar e resolver casos, tarefas e observáveis.
Normalmente não possui permissões para gerenciar configurações ou usuários.

Read-Only:
Tem acesso apenas para visualização.
Pode ver casos, tarefas, relatórios e observáveis, mas não pode editar ou modificar dados.
Ideal para auditores e gestores que precisam acompanhar o progresso sem interferir.
    


Como vai funcionar:
Admins -> criam organizacoes -> cada organizacao tera seu admin e seus funcionarios com diferentes perfis que teram permissoes variadas.