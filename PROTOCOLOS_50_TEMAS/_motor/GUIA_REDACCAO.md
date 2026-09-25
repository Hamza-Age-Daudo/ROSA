# Guia de redacção dos 50 protocolos (FCS/UniLúrio, Licenciatura em Farmácia)

Este guia é obrigatório para quem redige ou revê um protocolo desta pasta. Junta
a norma oficial da Faculdade de Ciências de Saúde (FCS) da Universidade Lúrio
(documentos 00, 01, 09 e 12 de `GABY/PROMPTS_TCC_UNILURIO`), o padrão de
documentos do utilizador e as lições tiradas dos protocolos já feitos
(Muanchura, Rosa). Cada protocolo tem de ficar ao nível de um documento pronto a
submeter à Comissão Científica e ao comité de bioética.

## 1. Como se produz um protocolo

| Passo | Comando (a partir de `PROTOCOLOS_50_TEMAS/`) |
|---|---|
| Ler o tema | `_motor/temas.json` (número, categoria, título proposto, descrição) |
| Ver a forma dos campos | `_conteudo/_modelo_tema.py` (só forma; não reaproveitar texto) |
| Pesquisar literatura | `python _motor/refs.py buscar "termos em inglês" --n 20 --desde 2016` e WebSearch para documentos da OMS, MISAU, INE, ANARME |
| Ler o resumo de um artigo antes de citar números | `python _motor/refs.py resumo <PMID ou DOI>` (ou WebFetch do texto integral) |
| Gerar a referência Vancouver | `python _motor/refs.py doi <DOI>` ou `pmid <PMID>` (artigos); `python _motor/refs.py web --autor ... --titulo ... --local ... --editora ... --ano ... --url ...` (documentos oficiais) |
| Escrever o módulo | `_conteudo/tema_NN.py` (NN com dois dígitos) |
| Compor e validar | `python _motor/motor.py _conteudo/tema_NN.py` até `PROBLEMAS: nenhum` |
| Verificar todas as fontes | `python _motor/refs.py verificar _conteudo/tema_NN.py` até `erros: 0` |

O `.docx` sai em `NN_CATEGORIA/PROTOCOLO_TNN_SLUG.docx`. Não editar ficheiros em
`_motor/` (são partilhados por 50 processos em paralelo); se encontrar um
defeito do motor, contorná-lo no módulo e relatá-lo na resposta final. Não
tocar em módulos de outros temas.

## 2. Contexto fixo (igual em todos os protocolos)

- Curso: Licenciatura em Farmácia, FCS, Universidade Lúrio, Nampula. Protocolo
  datado de 2026 (capa: Nampula, 2026). Execução em 2027.
- Cronograma: `inicio (2026, 10)`, `n_meses 12` (Outubro de 2026 a Setembro de
  2027). A recolha só começa depois da aprovação ética (nunca antes de
  Fevereiro de 2027). Fases: revisão e protocolo; submissão ao comité e
  autorizações; preparação, validação e pré-teste do instrumento (ou
  aquisição de reagentes e validação do método); recolha; processamento e
  análise; redacção; revisão e entrega; defesa.
- Estudos documentais retrospectivos: período de dados de 1 de Janeiro a 31 de
  Dezembro de 2026 (ou 2025 a 2026 quando o volume de casos o exigir), com
  consulta dos arquivos em 2027.
- Comité de ética: Comité Institucional de Bioética para a Saúde da
  Universidade Lúrio (CIBS-UniLúrio) e, quando aplicável, Comité Nacional de
  Bioética para a Saúde (CNBS). Autorizações: Direcção Provincial de Saúde de
  Nampula, Serviço Distrital de Saúde, Mulher e Acção Social (SDSMAS) da Cidade
  de Nampula, direcção de cada unidade sanitária, e a autoridade reguladora
  quando o estudo envolver farmácias ou medicamentos no mercado (confirmar a
  designação actual e citá-la). Contactos telefónicos: `[preencher]`.
- Análise estatística: IBM SPSS Statistics (versão 26 ou superior) ou
  equivalente de acesso livre (JASP ou R). Nível de significância de 5%
  (p<0,05) e intervalos de confiança a 95% (IC95%).
- `AUTOR = "[Nome do(a) estudante]"` e `ORIENTADOR = "[Nome e grau académico
  do(a) orientador(a)]"`: não mudar.
- O título proposto no documento de temas é ponto de partida: delimitar com
  local, população e período (até cerca de 25 palavras, sem siglas).
- Não inventar nomes de unidades sanitárias, números de camas, número de
  farmácias licenciadas, volume de doentes, nomes de chefes. Quando o desenho
  depende desse número, apresentar a regra (censo se N for pequeno, amostragem
  se for grande) e uma tabela de cenários, e marcar `[confirmar junto de ...]`.
  Usar `[preencher]` e `[confirmar]` só para o que é genuinamente
  desconhecido (no máximo cerca de 10 marcadores por protocolo).

## 3. Estrutura (13 secções da FCS) e o que cada uma tem de ter

O motor numera secções, subsecções, quadros, tabelas e figuras; não escrever
números à mão. Remissões: `[[quadro:chave]]`, `[[tabela:chave]]`,
`[[figura:esquema]]`. Todo o quadro, tabela e figura tem de ser remetido no
texto.

Pré-textuais (o motor compõe): capa, folha de rosto, declaração do orientador,
resumo, abstract, lista de abreviaturas, índice.

- **RESUMO**: parágrafo único de 250 a 300 palavras (o validador conta), sem
  citações e sem siglas (escrever tudo por extenso: "vírus da
  imunodeficiência humana", "Organização Mundial da Saúde"). Conteúdo:
  problema, objectivo, desenho, local e período, população e amostra,
  instrumento, análise, resultados esperados e utilidade. Palavras-chave: 3 a 5,
  por ordem alfabética. ABSTRACT: tradução fiel, keywords por ordem alfabética.
- **1. Introdução e contextualização** (5 a 7 parágrafos, 600 a 900
  palavras): funil do global para a África subsariana, para Moçambique e para
  Nampula, com dados citados; termina na lacuna e no objectivo do estudo.
- **2. Problema e delimitação** (3 a 4 parágrafos): o problema concreto no
  local, a sua consequência, o que falta saber. `PERGUNTA` numa frase
  interrogativa. `DELIMITACAO`: local, população, período, objecto e o que
  fica de fora.
- **3. Objectivos**: um geral e 3 a 5 específicos, verbos no infinitivo,
  mensuráveis, pela ordem lógica (caracterizar, determinar, identificar,
  analisar a associação...). Cada objectivo específico tem de ter variável no
  quadro de variáveis, análise na secção de análise e resultado esperado.
- **4. Hipóteses**: H0 e H1 para cada componente analítica (associação,
  comparação), coerentes com os testes previstos. Para componentes só
  descritivas, `QUESTOES`.
- **5. Justificativa**: parágrafo de abertura e as quatro relevâncias
  (científica, académica, social, política), 1 a 2 parágrafos cada, com dados
  e citações (como no protocolo do Muanchura).
- **6. Revisão da literatura**: 5 a 7 subtemas, 2 a 4 parágrafos densos cada.
  Incluir: conceitos e definições (com a definição operacional que será
  usada), magnitude e consequências, determinantes, o enquadramento normativo
  moçambicano (normas do MISAU, lista nacional de medicamentos essenciais,
  legislação farmacêutica, programas nacionais), e os métodos ou instrumentos
  de medida e as suas propriedades (validação, fiabilidade, critérios).
- **7. Estado da arte e esquema conceptual**: quadro `estado_arte` com 10 a 15
  estudos empíricos reais dos últimos 10 anos (autor e ano com citação, local,
  desenho e n, principais resultados com os números da fonte), incluindo os
  estudos moçambicanos e africanos que existam; depois 1 a 2 parágrafos de
  leitura crítica (padrão recorrente, divergências, lacuna que o estudo
  preenche). Esquema: 1 parágrafo que o explica e o dicionário `ESQUEMA`
  (blocos de variáveis independentes, desfecho, confundidores).
- **8. Metodologia** (a secção mais escrutinada; 2.500 a 4.000 palavras), com
  subsecções cujos títulos contenham estas palavras: tipo e desenho; local e
  período; população (ou material de estudo) e unidade de análise; amostra e
  cálculo do tamanho; critérios de inclusão e exclusão; variáveis (quadro
  `variaveis` com a coluna "Objectivo"); instrumentos (ou métodos, ensaios)
  e fontes; procedimentos de recolha e controlo de qualidade; processamento e
  análise; limitações (quadro `limitacoes` com limitação, consequência,
  mitigação); considerações éticas.
- **9. Resultados esperados**: um por objectivo específico, pela mesma ordem,
  sem inventar números (pode indicar a direcção esperada com apoio na
  literatura citada) e a utilidade prática de cada um.
- **10. Divulgação**: defesa pública, relatório às instituições envolvidas,
  artigo em revista com revisão por pares, jornadas científicas; devolução à
  comunidade quando aplicável.
- **11. Cronograma**: `CRONOGRAMA` (o motor desenha o quadro).
- **12. Orçamento**: `ORCAMENTO` com rubricas realistas em meticais (o motor
  calcula subtotais, 10% de imprevistos e total; não somar à mão). Parágrafo
  com a fonte de financiamento (próprio ou a solicitar) e a justificação das
  rubricas maiores. Ordem de grandeza: 25.000 a 150.000 MT consoante o
  desenho; estudos laboratoriais incluem reagentes, padrões de referência,
  meios de cultura e consumíveis.
- **13. Referências**: o motor gera a lista pela ordem de citação.
- **Apêndices** (mínimo dois): o instrumento completo (todas as perguntas,
  com escalas e codificação, ou a ficha de registo laboratorial com todos os
  campos e critérios de aceitação), a folha de informação ao participante e o
  termo de consentimento (com impressão digital e testemunha para quem não
  sabe ler), ou o pedido de dispensa de consentimento (estudos documentais),
  e o pedido de autorização institucional.

## 4. Rigor metodológico exigido (lições das auditorias anteriores)

1. **Tamanho da amostra completo**: fórmula (`FORMULA`), cada valor com a sua
   justificação e fonte (p de um estudo citado ou 0,5 na falta de dados), a
   substituição numérica, o resultado, a correcção para população finita
   quando N é conhecido ou uma tabela de cenários de N, o efeito de desenho
   (1,5 a 2) em amostragem por conglomerados, e a margem para não resposta.
   Indicar o número de conglomerados e de unidades por conglomerado.
2. **Poder para os objectivos analíticos**, não só para o descritivo: para
   comparações de dois grupos, fórmula de duas proporções (α 5%, poder 80%);
   para regressão logística, pelo menos 10 eventos por variável. Quando o
   poder for limitado, declará-lo.
3. **Unidade de análise explícita** (doente, receita, episódio, amostra,
   farmácia, visita) e o que se faz com registos múltiplos da mesma pessoa.
4. **Classificações que dependem de julgamento** (adequação, erros,
   problemas relacionados com medicamentos, legibilidade, identificação de
   plantas): dois avaliadores independentes, concordância pelo kappa de Cohen
   e consenso ou terceiro avaliador.
5. **Estudos documentais**: verificação prévia da fonte em cerca de 30
   registos antes da recolha, com regra de decisão escrita (por exemplo,
   variável com menos de 60% de preenchimento sai dos objectivos); dupla
   extracção de 10% dos registos; ficha sem identificadores; dispensa de
   consentimento justificada.
6. **Instrumentos**: adaptados de instrumentos validados e citados (nunca
   inventar itens de escalas validadas; quando não se reproduz o item exacto,
   dizer que é adaptado); validade de conteúdo por painel de peritos (índice
   de validade de conteúdo de pelo menos 0,80), tradução e retroversão para
   Emakhuwa quando aplicável, pré-teste em cerca de 10% da amostra fora da
   amostra final, fiabilidade (KR-20 para itens dicotómicos, alfa de
   Cronbach para escalas, ambos de pelo menos 0,70). Pontos de corte (por
   exemplo, Bloom: bom de 80% ou mais, moderado de 60% a 79%, fraco abaixo de
   60%) iguais no texto e no quadro de variáveis.
7. **Estudos laboratoriais**: monografias e capítulos gerais da farmacopeia
   de referência (Farmacopeia Internacional da OMS, Farmacopeia Britânica,
   Europeia ou dos Estados Unidos) citados; critérios de aceitação em quadro;
   número de marcas, lotes, unidades e réplicas justificado; calibração,
   substância de referência, ensaio em branco e adequação do sistema;
   estatística (média, desvio-padrão, coeficiente de variação, proporção de
   conformidade com IC95%, ANOVA ou Kruskal-Wallis); biossegurança, equipamento
   de protecção e eliminação de resíduos; aquisição das amostras como cliente
   comum, com registo de lote e validade; na ética, autorização institucional
   e confidencialidade das marcas nos relatórios públicos quando adequado.
8. **Microbiologia**: métodos da farmacopeia ou normas do CLSI ou EUCAST
   (versão em vigor, citada), estirpes de controlo ATCC, meios com controlo de
   qualidade, nível de biossegurança 2.
9. **Cliente simulado, comportamentos sensíveis, inquéritos a estudantes**:
   justificação ética específica (dispensa de consentimento prévio,
   devolução agregada e não punitiva, anonimato, recolha em urna selada,
   participação sem efeito nas avaliações académicas, encaminhamento para
   apoio quando surgir necessidade).
10. **Ética em todos**: Declaração de Helsínquia na revisão de 2024 (citar o
    artigo do JAMA, 2025), CIBS-UniLúrio, autorizações, confidencialidade,
    riscos e benefícios, e uma via de referenciação quando o estudo detectar
    um problema de saúde no participante (como no protocolo do Muanchura).
11. **Normas de relato**: STROBE (observacionais), ChecKAP (inquéritos CAP),
    RECORD (dados de rotina), COREQ ou SRQR (componente qualitativa),
    orientações específicas para cliente simulado ou estudos
    etnofarmacológicos quando existirem. Citar a que se aplicar.
12. **Coerência total**: título, objectivos, hipóteses, variáveis, análise,
    resultados esperados, cronograma e orçamento dizem o mesmo (as mesmas
    datas, o mesmo n, os mesmos pontos de corte).

## 5. Referências (nunca inventar)

- Mínimo 30 citadas; alvo 35 a 55. Pelo menos 80% de 2016 a 2026. Anteriores a
  2016 só se forem seminais (manual original de um instrumento, norma de
  referência) e registadas em `SEMINAIS` com o motivo.
- Artigos: SEMPRE gerados por `refs.py doi` ou `refs.py pmid`. Documentos
  oficiais: `refs.py web` com o URL real verificado (HTTP 200). Nunca
  escrever autores, revista, volume ou páginas de memória.
- Cada número, percentagem ou afirmação específica atribuída a uma fonte tem
  de estar no resumo ou no texto dessa fonte, lido com `refs.py resumo` ou
  WebFetch. Se não confirmar, não escrever o número.
- Procurar activamente a evidência de Moçambique e de Nampula
  (`refs.py buscar "<tema> Mozambique"`, `"<tema> Nampula"`), da África
  subsariana e global. Se não houver estudos locais, dizê-lo: é a lacuna.
- `python _motor/refs.py verificar` tem de terminar com `erros: 0`. Avisos de
  sítios que bloqueiam robôs (HTTP 403) são aceitáveis se o endereço for o
  oficial e tiver sido confirmado por WebFetch ou WebSearch.

## 6. Escrita

- Português europeu anterior ao Acordo Ortográfico de 1990: objectivo,
  actividade, factores, acção, direcção, protecção, infecção, selecção,
  respectivo, óptimo, facto, anti-retroviral, anti-séptico, extracto. Meses
  com maiúscula (Janeiro). Vocabulário de Portugal e Moçambique: equipa,
  registo, utente, formação, telemóvel, frigorífico, cancro, crónico.
- Zero travessões e traços (— – −), zero setas, zero "≈", zero reticências
  tipográficas, zero emojis, aspas «» e não “ ”. Intervalos com hífen simples
  (60-79%).
- Decimais com vírgula e milhares com ponto (37,1%; 1.250 doentes; p<0,05).
- Sem negrito dentro de parágrafos. Itálico (`*...*`) para nomes científicos
  (*Staphylococcus aureus*, *Moringa oleifera*) e termos latinos (*in vitro*).
  Índices e expoentes com `<sub>` e `<sup>` (n<sub>0</sub>, CO<sub>2</sub>).
- Prosa corrida e argumentada. Nada de sequências de rótulos ("Tendência: ...
  Dispersão: ..."). Listas só para critérios, objectivos e itens que são de
  facto enumeráveis.
- Proibido: "vale ressaltar", "é importante notar", "em suma", "mergulhar",
  "de suma importância", "cabe destacar", "papel crucial", "no cenário
  actual", "ademais", meta-comentários ("este texto apresenta...") e qualquer
  marca de texto gerado.
- Registo impessoal e voz activa ("o estudo avalia", "serão recolhidos").
- Siglas: forma extensa na primeira ocorrência seguida da sigla entre
  parênteses; na lista só as que o texto usa; sem siglas no título nem no
  resumo.

## 7. Extensão, eficiência e acabamento

- Corpo (secções 1 a 12): 7.500 a 10.000 palavras. O validador rejeita menos
  de 6.500 e mais de 12.000. Orientação por secção: introdução 700 a 900;
  problema e delimitação 500 a 700; justificativa 500 a 700; revisão 2.000 a
  2.600; estado da arte 700 a 1.000; metodologia 3.000 a 4.000 (a amostra não
  precisa de mais de 700); resultados esperados, divulgação, cronograma e
  orçamento 500 a 800 no conjunto. Resumo: 250 a 300 palavras, contadas.
  Com apêndices, o documento fica entre 30 e 45 páginas.
- Referências: 35 a 50 bem escolhidas valem mais do que 60. Não gastar tempo
  a acumular fontes redundantes.
- Gravar o módulo cedo e por partes (FONTES e secções 1 a 7 primeiro, depois
  8 a 12 e apêndices). Se já existir um `tema_NN.py` de uma sessão
  interrompida, **continuar a partir dele**: ler o que está feito, completar
  o que falta e só reescrever o que estiver errado ou fora destes limites.
- Entregar apenas com `PROBLEMAS: nenhum` no motor e `erros: 0` na
  verificação de fontes, e depois de ler e resolver os avisos.
- Reler o texto inteiro uma vez do princípio ao fim antes de terminar, à
  procura de repetições, contradições de números e frases vazias.
