# Agendamento Automático

Utilitário para extração do nome completo das planilhas geradas pelo Sympla

## Motivação

No contexto da pandemia, fez-se necessário a realização de agendamentos para participação em diversos eventos, inclusive religiosos. Nesse sentido, a Paróquia de São Pedro começou a realizar os agendamentos para as Missas dominicais, utilizando a plataforma Sympla para tal. Visto que o Sympla exportava um arquivo com diversos dados desnecessários para o contexto, criei esse pequeno utilitário para extrair apenas o nome completo das pessoas que fizeram a inscrição. Fazer esse trabalho manualmente custava um certo tempo, visto que era necessário 

## Funcionamento

Inicialmente, o utilitário apresenta a opção de seleção de um ou mais arquivos para leitura. Depois disso, utiliza-se REGEX para pegar, a partir do nome do arquivo, a data e o horário da Missa. Depois disso, concatena-se o nome com o sobrenome dos participantes (a tabela do Sympla - resultado da exportação dos participantes - coloca o nome e sobrenome em duas colunas) e, por fim, coloca-os num arquivo .docx em formato de lista. 
