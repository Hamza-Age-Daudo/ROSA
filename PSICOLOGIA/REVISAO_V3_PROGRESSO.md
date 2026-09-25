# Revisão v3 do Protocolo (Muatala): registo de progresso

Ficheiro vivo, actualizado a cada passo para não se perder o fio. Data de início: 23/09/2026.

## Pedido
- Rever o protocolo com base nos ficheiros da pasta `OOX` (2 áudios de WhatsApp de 23/09/2026).
- Dados da estudante: **Eunice Carlos Marcelino**, BI **030105324374B**, n.º de estudante **20220108005**.
- Orientador: **Mestre Armando Salvador Cumbe**.
- Comentários recebidos (texto):
  - "Foge muito da área clínica; parece mais um protocolo de psicologia escolar ou educacional."
  - "Deves explorar mais os aspectos psicológicos."
  - Orientador: falta **rever as referências** e **falar mais sobre aspectos psicológicos**.

## Estado
- [x] Ler LEIA-ME.md (v2, 19/09/2026, 57 referências, 14 secções, 86 testes)
- [x] Transcrever os 2 áudios da pasta OOX (faster-whisper medium, CPU)
- [x] Mapear o conteúdo actual dos módulos `_protocolo_*.py`, do validador e dos testes
- [x] Cópia de segurança da v2 (`03_TCC/_versoes_anteriores/`: docx, pdf e `fontes_v2/`)
- [x] Plano de alterações (clínico/psicológico + referências + nomes)
- [~] Workflow de pesquisa lançado (run wf_87b3ae20-485): 4 auditores das 57 referências + 7 temas com contra-verificação
- [x] Identificação preenchida: capa, folha de rosto (orientador, sem co-orientador), declaração do orientador no modelo FCS (BI e n.º da estudante; BI do orientador fica em branco para ele preencher), Quadro 5, Apêndices B e E; feminino (a autora, investigadora, licenciada, a requerente)
- [~] Implementar
  - [x] Figura 1 nova (`_figura_esquema.py`): contextos distais, factores psicológicos proximais, comportamento agressivo; setas tracejadas para associação directa
  - [x] `_protocolo_amostra.py`: PREDITORES_LINEAR 15 para 20; novo `poder_mediacao()` (teste de significância conjunta) e `efeito_minimo_mediacao()`; n efectivo 283: poder 0,99 para a=b=0,26; efeito mínimo detectável a=b=0,19; f² mínimo 0,028 (inalterado)
  - [x] Apêndice A: SDQ completo (25), DERS-SF (18), Rosenberg (10), filtro + CRIES-8 (8), em secções VI a VIII; agressividade passa a secção IX; 6 testes novos (87 passam)
  - [x] Texto reescrito: introdução (enquadramento clínico), problema (motivação 2025, pergunta), objectivos (5), hipóteses (3 operacionais), justificativa (motivação clínica), revisão (6.1 a 6.13 com 6.3 perspectiva clínica, 6.4 modelos, 6.5 mecanismos, 6.10 avaliação psicológica, 6.11 implicações clínicas), metodologia (bateria, análise por blocos, mediação, ética, 5 limitações), resultados esperados (6), resumo 299 palavras, abstract 285, 27 siglas
  - [x] Referências: 57 para 103 (11 corrigidas, 7 retiradas, 53 novas verificadas); todas citadas
  - [x] Orçamento: impressão 15 para 20 MZN (questionário mais longo); total 111.210 MZN
- [x] Regenerar docx/pdf (66 páginas), validar (sem erros), testes (96 passam)
- [x] Revisão adversarial (workflow wf_abb95856-ebf, 4 revisores): 150 achados (3 críticos, 25 altos, 66 médios, 56 baixos); todos concordam que a v3 já responde à crítica de 'fugir da área clínica'
- [x] Aplicar correcções da revisão e regenerar: todas as críticas e altas e a maioria das médias e baixas; validador sem erros; 99 testes; 25 verificações automáticas no texto final passam
- [x] Verificação final (workflow wf_216c9e10-a8b, 2 revisores, 49 achados, sem problemas maiores nos números): correcções aplicadas; validador sem erros; 99 testes; 71 páginas; 108 referências; resumo 295 palavras
- [x] Relatório final ao utilizador
- [ ] Relatório final

## Notas

### Transcrição dos áudios (OOX, 23/09/2026)

**Áudio 1 (1 min 57 s), a estudante:**
- O tema que ela escolheu era **"Implicações psicológicas do comportamento agressivo em adolescentes"**;
  ao submeter a proposta, a **coordenação corrigiu** para "Factores psicossociais relacionados...".
- O que ela quer mesmo saber: **o que está por detrás** do comportamento agressivo, ou seja, as
  **causas psicológicas**; o que leva os alunos a ter este comportamento.
- Motivação: em **2025** registaram-se **muitos casos de agressividade na Escola Secundária de Muatala**.
- Deve **explorar a componente clínica**, porque o curso dela é **Psicologia Clínica**; o texto actual
  "está mais para educacional".
- "Quanto aos **testes**, eu ainda vou te dizer" (instrumentos psicológicos: ela confirma depois).

**Áudio 2 (36 s):**
- Há indicação de que a entrega do protocolo é **esta semana** (informação ainda por confirmar).
- Vai imprimir a versão feita e deixar para correcção; só ajusta nome do estudante, orientador, etc.
- Pede que o trabalho seja feito com calma, sem pressão.

### Leitura inicial (implicações)
1. O título registado mantém-se (foi imposto pela coordenação), mas o **enquadramento passa a ser de
   psicologia clínica**: mecanismos psicológicos (regulação emocional, impulsividade, raiva/hostilidade,
   processamento de informação social, trauma), psicopatologia associada (sintomas externalizantes e
   internalizantes, perturbações disruptivas DSM-5-TR/CID-11), avaliação psicológica e implicações
   para a intervenção clínica.
2. **Instrumentos**: propor bateria clínica com validação portuguesa/africana, mas assinalar que a
   escolha final dos testes fica para a estudante confirmar.
3. **Referências**: verificar todas (existência, metadados, norma da FCS) e reforçar com literatura
   de psicologia clínica (teorias clássicas e evidência recente, incluindo Moçambique/África).
4. **Preencher**: nome, BI, n.º de estudante e orientador em todos os campos em branco.

### Diagnóstico da v2 (porque parece "psicologia escolar")
- O enquadramento é de saúde pública/escola: modelo ecológico da OMS, INSPIRE, "programa escolar de
  prevenção", ligação à escola, absentismo; a secção 5.2 fala em "psicologia escolar e comunitária".
- O nível individual/psicológico ocupa uma linha (6.7) e uma subescala de 5 itens (SDQ emocional).
- Faltam: psicopatologia (DSM-5-TR/CID-11), mecanismos psicológicos (regulação emocional,
  impulsividade, atribuição hostil, trauma, auto-estima, traços de insensibilidade emocional), modelo
  integrador (Modelo Geral da Agressão, biopsicossocial), avaliação clínica e implicações clínicas.
- Referências: muitas de epidemiologia/saúde pública; algumas fracas ou fora da área (ex.: sweidan2024
  numa revista de ortodontia; obeid2019 sobre dependência da Internet); 3 de 2026 por reconfirmar
  (king2026, vigneri2026 sem número de artigo, miedema2026); formato das páginas web ("[consultado a ...]")
  difere do modelo da norma ("[citado ano mês dia]").

### Modelo da FCS para a identificação (visto no protocolo da Muanchura)
A declaração do orientador identifica a estudante: "... protocolo de investigação da estudante X,
portadora do B.I. n.º ... e n.º de estudante ..., com o tema: ..., se encontra estrutural e
metodologicamente capaz de ser apresentado em provas públicas." O BI e o n.º de estudante entram aí.

### Plano v3
1. Pesquisa (workflow paralelo): (a) verificar as 57 referências no Crossref/PubMed; (b) encontrar e
   verificar literatura de psicologia clínica por tema; (c) confirmar instrumentos com validação
   portuguesa/africana; (d) confirmar o nome oficial do curso na UniLúrio.
2. Reescrever com foco clínico mantendo o título registado: introdução, problema, objectivos (+ factores
   psicológicos individuais), hipóteses (reactiva vs proactiva), justificativa (motivação de 2025,
   relevância clínica), revisão (novas secções clínicas), metodologia (bateria psicológica, análise de
   mediação exploratória, bandas clínicas do SDQ), ética, resultados esperados, figura 1, apêndices.
3. Identificação: Eunice Carlos Marcelino (BI 030105324374B, n.º 20220108005); orientador Mestre
   Armando Salvador Cumbe; concordância no feminino ("a autora", "investigadora", "licenciada").
4. Regenerar, validar, testes, revisão adversarial (examinador clínico, metodólogo, referências, norma).

### Desenho detalhado da v3 (decidido enquanto a pesquisa corre)
**Objectivos específicos (5):** 1) perfil sociodemográfico e escolar; 2) nível e perfil do comportamento
agressivo (BPAQ-SF, RPQ) e proporção com problemas de comportamento de relevância clínica (SDQ);
3) **NOVO** factores psicológicos individuais (regulação emocional, impulsividade/hiperactividade,
auto-estima, sintomas emocionais, stress pós-traumático, comportamento pró-social); 4) factores
familiares, escolares, de pares e comunitários (fundidos); 5) associação independente + mediação
exploratória da desregulação emocional entre exposição à violência e agressividade.

**Hipóteses operacionais novas:** reactiva ligada a desregulação/sintomas emocionais/trauma; proactiva a
baixo comportamento pró-social (indicador de emoções pró-sociais limitadas); mediação parcial pela
desregulação emocional (mediação estatística, não causal).

**Revisão da literatura (nova ordem):** 6.1 adolescência; 6.2 conceito e funções da agressão; 6.3 NOVA
perspectiva clínica (DSM-5-TR/CID-11, irritabilidade, emoções pró-sociais limitadas, comorbilidade,
Moffitt); 6.4 modelos teóricos (aprendizagem social, frustração-agressão, processamento da informação
social, Modelo Geral da Agressão como integrador); 6.5 NOVA mecanismos psicológicos individuais;
6.6 magnitude; 6.7 família; 6.8 escola e pares; 6.9 comunidade; 6.10 avaliação psicológica;
6.11 implicações clínicas e intervenção; 6.12 estado da arte; 6.13 esquema conceptual (Figura 1 nova:
contextos distais, factores psicológicos proximais, comportamento agressivo).

**Bateria (a confirmar pela estudante, ela disse que ainda vai dizer os testes):** SDQ completo de
auto-avaliação (25), DERS-SF (18), Escala de Auto-Estima de Rosenberg (10), CRIES-8 (8), mais BPAQ-SF
(12) e RPQ (23); APGAR, ACE-IQ e GSHS mantêm-se. Tempo previsto ~45 min (um tempo lectivo).

### Auditoria das referências da v2 (resultados parciais, 15/57)
Nota: a máquina tem 4 CPUs, o workflow só corre 2 agentes de cada vez; os 7 temas de pesquisa foram
relançados como agentes independentes em paralelo (ficheiros `tema_t1.json` a `tema_t7.json` no scratchpad).
- **vigneri2026**: autores errados (são Vigneri, Fadare, Devries, Iversen, Brück; Cluver e Meinck não são autores); falta o n.º de artigo 3044; o estudo mede exposição passada a violência política, não "memória".
- **xu2024**: autores errados (Xu X, Wu Y, Xu Y, Ding M, Zhou S, Long S). Achados: 118 estudos; atribuição hostil e agressão rho 0,303; mais forte na agressão reactiva.
- **tarafa2022**: 4.º autor é Tarecha D; estudo comunitário (819), não escolar; não fala de disfunção familiar; é sobre vitimização.
- **sweidan2024**: autores 4 e 5 errados; revista de ortodontia, fora da área; não diz o que o texto lhe atribui. **Substituir** (proposta: Amu et al. 2020, sofrimento psicossocial em adolescentes escolarizados em Moçambique, GSHS, Child Adolesc Psychiatry Ment Health).
- **oms_saude_mental**: ano 2025 (não 2026); "metade antes dos 14 anos" não está na ficha (vem de Kessler 2005, e a meta-análise de Solmi 2022 dá 34,6% antes dos 14); a ficha diz 1 em 7 dos 10-19 anos com perturbação mental e perturbação do comportamento em 3,3% (10-14) e 1,8% (15-19).
- **tordjman2022**: metadados certos, mas não sustenta as frases onde é citado (reactiva/proactiva, consequências). Retirar dessas posições.
- OK: inspire2016, matsinhe2024, bandura1961, nguyen2020, ameli2017, gershoff2016, elgar2018, henneberger2016, tian2019.

### Auditoria (30/57)
- **vacs2019**: autoria errada (Together for Girls só aloja o ficheiro). Autoria oficial: INS, MISAU, MGCAS, INE e CDC; título "Mozambique Violence Against Children and Youth Survey (VACS 2019): final report", Maputo, 2022. Todos os números do protocolo confirmados no PDF.
- **king2026**: Epub ahead of print (12 Jun 2026), sem volume/páginas. Os 2,7% são dos adolescentes **com perturbação** que procuraram cuidados (não do total). Ansiedade 17,8%, depressão 8,6%, raparigas OR 1,60, idade OR 1,28. O artigo aponta os cuidados primários (não a escola) como local de integração: corrigir 5.3.
- **oms_adolescente**, **oms_violencia_jovem**: formato "[Internet] ... [citado 2026 Set 23]"; a ficha de violência juvenil refere 15-29 anos para homicídios (acrescentar ao texto); 6.1 chama "inicial/tardia" a grupos que a OMS não nomeia assim.
- OK: krug2002, buss1992, raine2006, han2019, aboagye2021a, aboagye2021b, amene2024, sema2025, igreja2024, scott2018, oms_status2020 (relevância baixa).

### Auditoria concluída para 45/57 (o 4.º lote e os 7 temas falharam por limite de utilização da API, às 09:40 foi reposto)
Correcções a aplicar:
- **krug2002**: define violência, não agressão; a definição de agressão passa para Anderson e Bushman 2002; retirar "toda a violência é agressão" (a OMS inclui violência autodirigida); definição da OMS completa ("real ou em ameaça", "deficiência de desenvolvimento").
- **buss1992**: o BPAQ-SF de 12 itens é de **Bryant e Smith 2001** (J Res Pers 35(2):138-67), não de Buss e Perry.
- **han2019**: o bullying (34,4%) não difere por sexo; só lutas, lesões e ataque físico são mais frequentes nos rapazes; retirar "idade mais avançada" (6.7).
- **annor2024**: não estuda violência; ausência parental = pai/mãe biológico ausente 6+ meses antes dos 18 (30,5% mulheres, 25,1% homens, 5 países incl. Moçambique), associada a pior saúde mental e consumo de substâncias.
- **palermo2019**: estuda factores de risco PARA a vitimização; substituir por Ford et al. 2010 (polivitimização e perturbação psiquiátrica e delinquência).
- **zietz2020**: autores errados (Moracco, Shanahan, Martin; Moodley não é autor); homens adultos, ACE retrospectivas.
- **miedema2026**: 20 autores (Miedema, Matthews, Annor, Villaveces, Mndzebele, Adler, et al.); Moçambique n=424, perpetração 21,0%.
- **zhu2016**: provavelmente transversal (1401, 11-14 anos), desfecho "comportamentos problemáticos" e não agressão isolada.
- **li2024**: estudo testou mediação (RI-CLPM), não moderação; pares desviantes e agressão reforçam-se mutuamente; 4078 alunos, ~10 anos.
- **ugwu2024**: é **África do Sul** (Noroeste), não Nigéria; 769 alunos das Grades 11-12; moderação por traços de personalidade.
- **tian2021**: autores errados (Tian S, Zhang T, Chen X, Pan CW).
- **abio2020**: fraca (dados 2006, agressão não fica no modelo) e autores mal formatados: substituir/retirar.
- **obeid2019**: não sustenta auto-estima e ira; usar Donnellan et al. 2005 para a auto-estima.
- **olejarnik2023**: adultos do Reddit; substituir por Prescott et al. 2018 (PNAS, meta-análise, beta 0,08 a 0,11).
- **sukhodolsky2016**: OK; não diz que a proactiva responde a contingências (reformular).
- OK: blum2019, brown2024, ma2018 (25,0% bebem, 12-15 anos).

### Verificação directa (script Crossref + PubMed, sem agentes, para poupar o limite)
- Lote 1: 49 DOI novos, todos existem e os metadados batem (`scratchpad/lote1.json`, com resumos).
- Lote 2: as 12 referências da v2 por auditar estão correctas (pechorro2016, pechorro2015, tuvblad2016,
  goodman1997, smilkstein1978 PMID, strobe2007, charan2013, faul2009, peduzzi1996, helsinquia2024; URLs
  ACE-IQ, GSHS, mhGAP 2.0, Guilford/Hayes, VACS PDF, CID-11, sdqinfo com HTTP 200). tuvblad2016 estava mal
  usada para o limiar do alfa: passa a taber2018.
- Achados-chave confirmados nos resumos: Amu 2020 (Moçambique, GSHS 2015, 1.918 alunos, sofrimento
  psicossocial 21,2%, lutas aOR 1,38, agredido aOR 1,80, bullying aOR 1,45, amigos próximos aOR 0,50);
  Polanczyk 2015 (13,4% qualquer perturbação; disruptivas 5,7%; ansiedade 6,5%; PHDA 3,4%); Fairchild 2019
  (perturbação do comportamento ~3%, duas vezes mais nos rapazes); Cortina 2012 (14,3% na África
  subsariana); Solmi 2022; Dodge 2015 (1.299 crianças, 12 grupos, 9 países); Verhoef 2019 (111 estudos,
  29.272; NÃO mais forte na reactiva); Xu 2024 (rho 0,303, mais forte na reactiva); Vachon 2014 (empatia
  r=-0,11, adultos); Donnellan 2005; McLaughlin 2011 (N=1.065, desregulação prediz agressão); Heleniak
  2016 (mediação maus-tratos, regulação emocional, psicopatologia); Fowler 2009 (114 estudos); Prescott
  2018 (beta 0,08-0,11); Goodman 2001 (alfa médio 0,73); Kaufman 2016; **Moreira 2022 (DERS-SF em 612
  adolescentes portugueses; total sem a subescala de consciência)**; Perrin 2005 (CRIES-8 corte 17);
  Murray 2015 (TF-CBT Zâmbia, d=2,39); Nkuba 2018 (ICC-T Tanzânia); Hecker 2014 (castigo físico e
  externalização, Tanzânia); dos Santos 2016 (psicólogos 56 para 109, psiquiatras 9 para 10, 2010-2014).
- Sem resumo disponível (citar só pelo conteúdo que o título garante, sem números): sukhodolsky2004,
  roberton2012, moffitt1993, crick1994, bryant2001, card2006 (não usar).

### Revisão adversarial da v3 (achados principais a corrigir)
Críticos: (1) a perturbação de oposição e desafio NÃO inclui agressão física nos critérios do DSM-5-TR
(erro na introdução e em 6.3); (2) 5 dos 12 itens do BPAQ-SF no Apêndice A são da versão longa (herdado
da v2): os itens certos (Bryant e Smith 2001) são os originais 5, 21, 27 (física), 6, 14, 18 (verbal),
3, 22, 25 (ira), 8, 12, 16 (hostilidade), sem itens invertidos.
Altos: efeito de desenho 1,5 sem justificação (acrescentar sensibilidade com 2,0); número de turmas e
correcção para poucos conglomerados; CRIES-8 com filtro (quem diz Não fica com 0, não omisso); modelo
logístico com poucos parâmetros (classe ordinal; desfecho binário passa a lutas físicas, 36,4%);
reactiva e proactiva controlando a outra, com teste de Wald; variáveis compostas em falta no Quadro 2
(índice de exposição à violência, n.º de experiências adversas); contradição 7.8 "simplificar" vs
"versões validadas sem alterações"; cronograma apertado (plano de contingência); SDQ pró-social não
mede traços de insensibilidade; SDQ de auto-avaliação é dos 11 aos 17 anos; validações portuguesas do
BPAQ-SF e RPQ são de rapazes em contexto forense; "impulsividade" sem medida própria (usar
hiperactividade e desatenção); CRIES-8 não mede hipervigilância; ética: talão de auto-referenciação,
Linha Fala Criança 116, Lei 7/2008; MINEDH mudou de nome em 2025 (a confirmar); Han 2019 na introdução;
definição de agressão (Anderson e Bushman, não a OMS); Nguyen 2020 não diz o que o texto afirma.
Médios/baixos: fidelidade a Scott, Henneberger, Ameli, Gershoff, Taber, Polit, Goodman 2001, Cortina,
Schmitt, Igreja; pesos amostrais; imputação múltipla; testes bivariados ajustados ao desenho; mediação
ajustada ao desenho (significância conjunta + Monte Carlo); tempo de preenchimento; itens do
questionário mais simples ("perturbado", "remoer", "temperamento", "ondas de sentimentos"); TCLE com
risco emocional; categorias fechadas no filtro de trauma; numerais; enumerações repetidas.

### Correcções aplicadas após a revisão (23/09/2026)
Ver secção 1-A do LEIA-ME.md. Novas fontes verificadas: firth1993, card2006 (resumo: a agressão reactiva
relaciona-se mais com a maioria dos índices de ajustamento, diferença pequena, alta intercorrelação),
pechorro2018 (RPQ em 782 jovens portugueses de escolas, invariância entre sexos sem o item 21), gratz2004,
oms_cid11. Retirada nguyen2020. Código: `_protocolo_amostra.py` com DEFF_SENSIBILIDADE=2,0 e
PREVALENCIA_LUTAS=0,364 (OR mínimo 2,11; 154 eventos; 15 parâmetros; PREDITORES_LINEAR=35); testes
actualizados em conformidade; legendas das tabelas a 10 pt (house_docx.py).
Não feito: itálico dos estrangeirismos; desdobrar a impressão no orçamento; ICU (decisão da estudante).
