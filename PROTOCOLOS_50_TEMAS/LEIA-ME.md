# 50 protocolos de TCC, Licenciatura em Farmácia (FCS, UniLúrio, Nampula)

Ficheiro de continuação. Diz o que está feito, como se produz cada protocolo e o
que falta fazer. Actualizado a 20 de Setembro de 2026, 09h30.

## 1. O que é

Um protocolo de investigação completo, em Word, para cada um dos 50 temas de
`../Temas_TCC_Farmacia_UniLurio.docx`, ao nível do protocolo de referência
`../MUANCHURA/03_TCC/PROTOCOLO MUANCHURA_ORIGINAL.docx` e segundo a norma da
Faculdade de Ciências de Saúde. A norma de redacção está em
`_motor/GUIA_REDACCAO.md` e é obrigatória para quem escreve ou revê.

Cada protocolo tem 13 secções mais pré-textuais e apêndices, corpo de 7.500 a
10.000 palavras, 35 a 55 referências reais (pelo menos 80% de 2016 a 2026),
resumo de 250 a 300 palavras, cronograma de Outubro de 2026 a Setembro de 2027
e orçamento em meticais.

## 2. Como se produz

| Passo | Comando (a partir desta pasta) |
|---|---|
| Ver o tema | `_motor/temas.json` (número, categoria, título, descrição) |
| Forma dos campos | `_conteudo/_modelo_tema.py` (só a forma, não reaproveitar texto) |
| Pesquisar | `python -X utf8 _motor/refs.py buscar "termos em inglês" --n 20 --desde 2016` |
| Ler antes de citar | `python -X utf8 _motor/refs.py resumo <PMID ou DOI>` |
| Gerar referência | `refs.py doi <DOI>`, `refs.py pmid <PMID>`, `refs.py web --autor ... --url ...` |
| Escrever | `_conteudo/tema_NN.py` |
| Compor e validar | `python -X utf8 _motor/motor.py _conteudo/tema_NN.py` até `PROBLEMAS: nenhum` |
| Verificar fontes | `python -X utf8 _motor/refs.py verificar _conteudo/tema_NN.py` até `erros: 0` |
| Auditoria global | `python -X utf8 _motor/auditar_todos.py [--sem-fontes] [NN ...]` |
| Acabamento no Word | `python -X utf8 _motor/word.py actualizar --todos` (só no fim) |

O `.docx` sai em `NN_CATEGORIA/PROTOCOLO_TNN_SLUG.docx`. Não editar ficheiros de
`_motor/`, que são partilhados por todos os temas. Um defeito do motor
contorna-se no módulo do tema e regista-se na secção 6 deste ficheiro.

Cada tema passa por dois agentes: um redactor, que pesquisa, escreve e valida, e
um revisor adversarial, que confirma as afirmações contra as fontes, refaz a
aritmética da amostra, verifica a coerência e corrige directamente o módulo.
Correm em paralelo, cerca de dez de cada vez.

## 3. Estado a 24 de Setembro de 2026

Nota: as linhas 01 a 10 e a secção "Em curso" abaixo ficaram por confirmar
desde 20 de Setembro (outras sessões trabalharam noutros temas, como 23, 26 e
48, sem actualizar este ficheiro); antes de assumir o estado de qualquer tema
que não seja o 33, correr `python -X utf8 _motor/auditar_todos.py --sem-fontes`
para confirmar.

Fechados (redigidos, validados e revistos), confirmados nesta data: 9 de 50 (linhas
abaixo) mais o tema 33.

| Tema | Título curto | Corpo | Refs | Motor | Fontes |
|---|---|---|---|---|---|
| 01 | Adesão à terapêutica anti-retroviral, HCN | 9.735 | 54 | sem problemas | erros 0 |
| 02 | Técnica e conservação da insulina, HCN | 9.483 | 52 | sem problemas | erros 0 |
| 04 | Problemas relacionados com medicamentos, Medicina, HCN | 9.299 | 49 | sem problemas | erros 0 |
| 05 | Adesão e interrupção do tratamento da tuberculose | 9.799 | 49 | sem problemas | erros 0 |
| 06 | Indicadores de prescrição da OMS, centros de saúde | 9.919 | 55 | sem problemas | erros 0 |
| 07 | Antibióticos em menores de cinco anos, AWaRe | 9.916 | 51 | sem problemas | erros 0 |
| 08 | Automedicação em estudantes da UniLúrio | 9.997 | 55 | sem problemas | erros 0 |
| 09 | Profilaxia antibiótica em cesarianas, HCN | 9.304 | 54 | sem problemas | erros 0 |
| 10 | Conformidade no diagnóstico e tratamento da malária | 9.995 | 42 | sem problemas | erros 0 |
| 33 | Plantas medicinais e interacção com anti-hipertensores, doentes internados, Medicina I/II, HCN | 9.993 | 41 | sem problemas | erros 0 |

Em curso (estado a 20 de Setembro, por confirmar):

- Tema 03 (controlo da pressão arterial e adesão anti-hipertensora): redigido e
  validado, revisão adversarial a decorrer, com ordem de cortar o corpo de
  10.255 para menos de 10.000 palavras.
- Temas 11 a 19: redacção a decorrer (farmacovigilância e gestão farmacêutica).
  Módulos já gravados com trabalho parcial: 11, 12, 13, 15 e 16.

Por confirmar o estado real (módulos existem em `_conteudo/`, não auditados
nesta sessão): 23, 26, 48. Por começar: os restantes temas 20 a 50 além
destes.

### Tema 33: mudança de âmbito por indicação do orientador (24 de Setembro)

O tema 33 tinha sido redigido, revisto e fechado com o âmbito original do
catálogo (uso de plantas medicinais em três grupos de doentes crónicos
ambulatórios: hipertensos, diabéticos e em TARV, nas unidades sanitárias da
Cidade de Nampula). O orientador do estudante deu feedback que obrigou a
reformular o protocolo de raiz:

1. Uma só doença (hipertensão arterial), não três grupos.
2. Local: internamento nos Departamentos de Medicina I e II do Hospital
   Central de Nampula (HCN), não ambulatório de quatro unidades da cidade.
3. Reforço da componente de interacções entre os anti-hipertensores e as
   plantas (objectivo específico 4, com subsecção própria na revisão da
   literatura), mantendo a base em literatura e bases de dados.

Isto mudou a população, o desenho amostral (de amostragem sistemática por
quota entre grupos para amostragem consecutiva e exaustiva de uma população
de internamento pequena, com correcção para população finita agora aplicada a
sério), o objectivo e a hipótese 5 (de "grupo de doença" para "gravidade da
apresentação clínica que motivou o internamento") e cerca de um quarto das
referências (saíram fontes específicas de diabetes/TARV, incluindo o
Liverpool HIV Drug Interactions Checker; entraram fontes farmacocinéticas por
classe de anti-hipertensor e dados hospitalares moçambicanos, dois deles com o
HCN como local de estudo). O ficheiro `_conteudo/tema_33.py` antigo foi
sobrescrito (não há cópia à parte); o `.docx` antigo com o título anterior
(`PROTOCOLO_T33_Plantas_Medicinais_Concomitantes_Doentes_Cronicos_Nampula.docx`)
ficou na pasta `07_Farmacognosia_Plantas_Medicinais/`, órfão do âmbito antigo,
por remover quando confirmado que já não é preciso.

Se o mesmo tipo de feedback (uma doença em vez de vários grupos, local
hospitalar específico em vez de "unidades sanitárias da cidade") vier a
aplicar-se a outros temas do lote, vale a pena rever previamente com o
orientador, antes de fechar, para poupar uma reformulação a jusante.

## 4. Retomar depois de uma paragem

1. Ver que módulos existem: `ls _conteudo/tema_*.py`.
2. Correr `python -X utf8 _motor/auditar_todos.py --sem-fontes` para saber quais
   compõem e quantas palavras e referências têm. O resumo fica em
   `_motor/auditoria.json`.
3. Para cada tema incompleto, ler o módulo e continuar a partir dele, sem
   recomeçar. Os módulos parciais são sintacticamente válidos.
4. Só depois de todos os temas fechados: `python -X utf8 _motor/word.py
   actualizar --todos`, que actualiza o índice e conta as páginas de cada
   documento. Uma nova composição pelo motor apaga o índice actualizado, por
   isso este passo é sempre o último.

Nota sobre a infra-estrutura: durante esta produção a API caiu muitas vezes
(ligação perdida, ligação recusada, timeouts). Os agentes morrem, mas o que está
gravado em disco não se perde e eles retomam do ponto onde estavam. Daí a regra
de gravar cada avanço de imediato, fazer um pedido de rede de cada vez e não
lançar subagentes.

## 5. O que fica pendente em todos os protocolos

Cada protocolo tem entre 4 e 9 marcadores `[preencher]` e `[confirmar]`, que são
dados que só as instituições podem dar e que não devem ser inventados:

- número de unidades sanitárias elegíveis e volume de consultas ou de doentes,
  a confirmar junto do Serviço Distrital de Saúde, Mulher e Acção Social e das
  direcções das unidades;
- existência e edição em vigor de protocolos e normas locais em 2026;
- taxa de submissão ao Comité Institucional de Bioética para a Saúde da
  Universidade Lúrio;
- contactos telefónicos do estudante, do orientador e do comité de bioética;
- nome do estudante e nome e grau do orientador, que estão como
  `[Nome do(a) estudante]` e `[Nome e grau académico do(a) orientador(a)]`.

## 6. Defeitos conhecidos do motor (não corrigidos, contornados nos módulos)

1. O validador extrai `IC95` de `IC95%` e assinala-o como sigla não listada,
   embora a lista contenha a forma correcta. Falso positivo comum a todos os
   temas.
2. O controlo da ordem das citações ignora as citações dentro de quadros, o que
   gera avisos de «fora de ordem» quando uma referência aparece primeiro num
   quadro.
3. `_ano_ref` lê o último número de quatro dígitos da referência, pelo que toma
   por ano o número do artigo em revistas que o usam (por exemplo `18(3):1965`).
   Contorna-se registando a fonte em `SEMINAIS` com o motivo.
4. O teste do separador decimal apanha códigos como `C3.1` ou `V9.1`, isentando
   apenas contextos com «versão», «secção», «item», «pontos» e «Apêndice».
5. `refs.py` avisa de divergência de primeiro autor em obras de autoria
   colectiva (GBD, NCD-RisC) e quando normaliza apóstrofos tipográficos. São
   falsos positivos das próprias linhas que a ferramenta gera.

## 7. Erros que a revisão adversarial tem apanhado

Registo do que já foi corrigido, para orientar quem revir os temas seguintes:

- números atribuídos a fontes que não os contêm, ou lidos do resumo quando a
  análise ajustada inverte o sentido;
- denominadores trocados (percentagens de um subgrupo apresentadas como do
  total);
- normas de relato citadas com a referência errada;
- fórmulas de amostra com arredondamentos inconsistentes entre o texto e a
  tabela de cenários, e poder calculado sobre a amostra bruta em vez dos casos
  analisáveis;
- regras de classificação circulares, que tornavam impossível detectar o que se
  queria medir;
- itens de listas de verificação impossíveis de observar no momento previsto;
- variáveis no quadro sem objectivo correspondente, e objectivos sem variável;
- incoerências entre resumo e metodologia no n, nas datas e no número de
  entrevistas.
