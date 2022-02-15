# Extração de nomes automática do Sympla 💻 

Utilitário para extração do nome completo das planilhas geradas pelo Sympla

## Motivação ⛪

No contexto da pandemia, fez-se necessário a realização de agendamentos para participação em diversos eventos, inclusive religiosos. Nesse sentido, a Paróquia de São Pedro começou a realizar os agendamentos para as Missas dominicais, utilizando a plataforma Sympla para tal. Visto que o Sympla exportava um arquivo com diversos dados desnecessários para o contexto, criei esse pequeno utilitário para extrair apenas o nome completo das pessoas que fizeram a inscrição. Fazer esse trabalho manualmente custava um certo tempo, sendo a otimização do tempo para realização desse processo a principal motivação para a criação desse simples programa.

## Funcionamento 

Inicialmente, o utilitário apresenta a opção de seleção de um ou mais arquivos para leitura. Depois disso, utiliza-se REGEX para pegar, a partir do nome do arquivo, a data e o horário da Missa. Depois disso, concatena-se o nome com o sobrenome dos participantes (a tabela do Sympla - resultado da exportação dos participantes - coloca o nome e sobrenome em duas colunas) e, por fim, coloca-os num arquivo .docx em formato de lista. O programa foi pensado especificamente para o cenário explicado acima, sendo assim, ele funciona corretamente apenas nesse contexto.

## Problemas conhecidos ⚠️

O maior problema diz respeito a extração da data e horário do nome do arquivo. Inicialmente, pensei que seguia um padrão pré-definido, mas na realidade o nome do arquivo muda de acordo com o título inserido no nome do evento no próprio Sympla. Como eu geralmente fazia o cadastro do evento na plataforma, sempre seguia o mesmo padrão, mas caso o título fosse colocado de uma maneira diferente, o funcionamento do utilitário ficaria comprometido. Para resolver esse problema, basta extrair as informações de data e hora da própria planilha. Utilizar REGEX também foi proposital, visto que eu desejava estudar mais sobre o assunto e ver a sua utilização na prática, mas claramente não foi a opção mais adequada.   
