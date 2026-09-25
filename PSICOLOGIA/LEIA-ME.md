# Protocolo de Investigação: factores psicossociais e comportamento agressivo (ESM, Nampula)

**Autora.** Eunice Carlos Marcelino (BI 030105324374B, n.º de estudante 20220108005), Curso de
Psicologia, FCS, UniLúrio. **Orientador:** Mestre Armando Salvador Cumbe.

**Tema.** Factores psicossociais relacionados ao comportamento agressivo em adolescentes dos 10 aos
19 anos: caso da Escola Secundária de Muatala, cidade de Nampula, segundo semestre de 2026.

**Entregável.** `03_TCC/PROTOCOLO_AGRESSIVIDADE_MUATALA.docx`, com o PDF ao lado (71 páginas,
cerca de 22.700 palavras, 108 referências, 5 quadros, 1 tabela, 1 figura, 5 apêndices). **Versão 3,
de 23 de Setembro de 2026**, com enquadramento clínico. As versões 1 e 2 (e o código-fonte da v2) estão
em `03_TCC/_versoes_anteriores/`. O registo passo a passo da revisão está em `REVISAO_V3_PROGRESSO.md`.

---

## 1. O que ainda falta preencher ou confirmar

Os nomes, o BI e o número de estudante já estão em todo o documento. Falta apenas:

| Onde | O que preencher ou confirmar |
|---|---|
| Declaração do orientador | BI do orientador, data e assinatura (o modelo da FCS pede o BI) |
| Apêndice B, contactos | Telefone e correio electrónico da investigadora |
| Apêndice E, pedido à escola | Referência do parecer do comité de bioética (depois da aprovação) |
| Secções VI a VIII do questionário | **Confirmar os testes** (a estudante disse que ainda vai indicar os testes): a bateria proposta é SDQ, DERS-SF, Rosenberg e CRIES-8 |
| Tabela 1 | Número de alunos elegíveis (pedir à direcção da escola) |
| Questionário, classe | Confirmar se a escola já tem 7.ª classe (a opção foi acrescentada) |

O índice já vem preenchido com as páginas. Se editar o `.docx` no Word e as páginas mudarem, basta
clicar no índice e escolher Actualizar campo, Actualizar índice inteiro.

## 1-A. O que mudou na versão 3 (pedido de 23/09/2026: "foge da área clínica" e "rever as referências")

**Enquadramento clínico, mantendo o título registado pela coordenação.**
- Introdução e problema: a agressividade tratada como manifestação clínica transdiagnóstica
  ("o que está por detrás"), com a motivação dos episódios de 2025 na escola.
- Objectivos (5): novo objectivo sobre os factores psicológicos individuais; objectivo analítico com
  mediação exploratória. Hipóteses operacionais: reactiva ligada à desregulação emocional e ao trauma,
  proactiva ao baixo comportamento pró-social; mediação pela regulação emocional.
- Revisão da literatura: novas secções 6.3 (psicopatologia: DSM-5-TR, traços de insensibilidade
  emocional, irritabilidade, comorbilidade), 6.4 (frustração-agressão, processamento da informação
  social, Modelo Geral da Agressão, biopsicossocial), 6.5 (regulação emocional, atribuição hostil,
  trauma, auto-estima, empatia), 6.10 (avaliação psicológica) e 6.11 (implicações clínicas e
  intervenção, incluindo ensaios africanos e os recursos de saúde mental em Moçambique).
- Figura 1 nova: contextos (distais), factores psicológicos (proximais), comportamento agressivo.
- Metodologia: bateria psicológica (SDQ completo, DERS-SF, Rosenberg, CRIES-8), questionário com 9
  secções e cerca de 45 minutos; regressão por blocos; modelos separados para agressão reactiva e
  proactiva; mediação com bootstrap; poder da mediação calculado (0,99 para a=b=0,26; efeito mínimo
  0,19); ética de rastreio (não é diagnóstico), filtro na secção de trauma, encaminhamento para SAAJ.

**Referências (de 57 para 108).** Todas as 57 anteriores foram reauditadas no Crossref, PubMed e nas
páginas oficiais: 11 corrigidas (autores errados em Vigneri, Xu, Tarafa, Zietz, Miedema e Tian;
autoria do VACS; King 2026 como publicação antecipada; ano e formato das fichas da OMS), 7 retiradas
por não sustentarem o texto (Sweidan, revista de ortodontia; Palermo; Abio; Obeid; Olejarnik;
Tordjman; relatório OMS 2020) e várias frases reescritas (Ugwu 2024 é da África do Sul e não da
Nigéria; o bullying em Han 2019 não difere por sexo; o BPAQ-SF é de Bryant e Smith 2001). Entraram
53 fontes novas de psicologia clínica e de Moçambique, todas com DOI ou URL confirmados e com os
números conferidos nos resumos (por exemplo, Amu et al. 2020: sofrimento psicossocial em 21,2% dos
adolescentes escolarizados moçambicanos, associado às lutas físicas).


**Revisão adversarial (4 revisores independentes: examinador clínico, metodólogo, verificador de
citações, revisor de norma e língua).** Os quatro concluíram que a v3 já responde à crítica de fugir da
área clínica. Corrigiu-se tudo o que era crítico ou alto, entre outros:
- A perturbação de oposição e desafio não tem agressão física nos critérios do DSM-5-TR (texto corrigido,
  com a CID-11).
- **Os itens do BPAQ-SF no Apêndice A estavam errados desde a v2** (5 dos 12 eram da versão longa, com
  um item invertido). Passaram a ser os 12 itens de Bryant e Smith (2001). Na aplicação usa-se a versão
  portuguesa de Pechorro et al.
- Amostra: justificação do efeito de desenho (1 + (m - 1) × correlação intraclasse) e coluna de
  sensibilidade com efeito de desenho de 2,0 na Tabela 1 (577 alunos no cenário de 1.600); pelo menos 2
  turmas por classe, pesos amostrais e correcção para poucos conglomerados.
- Análise: o modelo logístico passa a usar a participação em lutas físicas (36,4%, 154 eventos, até 15
  parâmetros; Firth se necessário) em vez do percentil 75. Os modelos reactiva/proactiva controlam a
  outra forma e usam o teste de Wald. A mediação usa a agressão comportamental (física + verbal) e
  significância conjunta com Monte Carlo. Imputação múltipla; testes bivariados ajustados ao desenho.
- Quadro 2 com as variáveis compostas (índice de exposição à violência, n.º de experiências adversas) e
  os itens que antes não entravam em nenhuma variável.
- CRIES-8: quem responde Não ao filtro fica com 0 (não omisso); categorias fechadas no filtro.
- SDQ: bandas só dos 11 aos 17 anos. Validações portuguesas descritas com os seus limites (rapazes,
  contexto forense; RPQ também numa amostra escolar mista, Pechorro 2018).
- Ética: talão de auto-referenciação numa urna separada, Linha Fala Criança (116), Lei n.º 7/2008,
  aceitação escrita do serviço de referência e risco emocional no TCLE.
- O Ministério da Educação chama-se agora Ministério da Educação e Cultura (MEC), confirmado em mec.gov.mz.
- Várias frases que as fontes não sustentavam foram corrigidas (Scott, Henneberger, Ameli, Gershoff,
  Nguyen retirada, Taber, Polit, Goodman 2001, Cortina, Schmitt, Igreja).
- Itens do questionário simplificados ("quando me sinto mal" em vez de "perturbado"; "raiva" em vez
  de "temperamento").

**Verificação final (2 revisores, 24/09/2026).** Confirmou os números da Tabela 1 e do poder. Levou a
mais correcções: a mediação passou a exploratória, e as hipóteses confirmatórias são a 1.ª e a 3.ª, com
correcção de Holm. O número de experiências adversas e o índice de exposição entram em modelos
próprios, para evitar colinearidade. A supervisão parental ficou separada da ligação parental. O modelo
logístico tem variáveis pré-especificadas (12 a 15 parâmetros) e o teste de Archer e Lemeshow. O BPAQ
foi usado em amostras africanas (Butovskaya 2019, Tanzânia), o que corrige uma afirmação que era falsa.
O RPQ só é invariante entre sexos sem o item 21. A aplicação assistida faz-se em espaço separado. O TCLE
passou a pai/mãe/responsável legal, e o assentimento inclui o contacto do CIBS. Foram acrescentadas a
perturbação de desregulação disruptiva do humor e a limitação de não se medir a atribuição hostil.

**Nota para o orientador:** "relacionados ao" é regência brasileira (em português europeu,
"relacionados com"). Mantive-a só no título registado; no texto corrido passou a "relacionados com".

**Ficou por fazer (decisão da estudante e do orientador):** confirmar os testes; eventualmente
acrescentar o Inventário de Traços Calosos e Não Emocionais (ICU), se se quiser medir de facto os traços
de insensibilidade emocional (a subescala pró-social do SDQ não os mede); itálico nos estrangeirismos
(bullying, odds ratio), que o construtor ainda não faz; desdobrar a rubrica de impressão do orçamento.

## 2. O que mudou na versão 2 (inspirado no protocolo da Muanchura e nas normas da FCS)

Comparei o protocolo com o da Muanchura (`03_TCC/MUANCHURA`) e com as normas da pasta
`PROMPTS_TCC_UNILURIO` (documentos 00, 01, 02 e 12). O da Muanchura trouxe quatro boas práticas que
faltavam aqui; as normas e a auditoria transversal dos protocolos apontaram as restantes.

**Trazido do protocolo da Muanchura**
- Índice automático do Word, com páginas, até ao 3.º nível, e numeração romana nos pré-textuais
  (iii, iv...) e árabe a partir da Introdução.
- Substituição numérica da fórmula da amostra à vista do júri (n₀ = 1,96² × 0,537 × ... = 382,06),
  agora com expoentes e índices reais do Word.
- Número Vancouver de cada estudo no Quadro 1 (estado da arte), por exemplo "Han et al., 2019 (7)".
- Declaração do orientador no texto-modelo da FCS ("em condições de ser apresentado e defendido em
  provas públicas").

**Exigido pelas normas da FCS e antes em falta**
- Resumo e abstract em parágrafo único de 250 a 300 palavras (297), sem rótulos em série
  ("Introdução:", "Objectivo:"), sem siglas e com 5 palavras-chave por ordem alfabética (eram 6).
- Referências com a primeira linha sem avanço e as restantes a 0,75 cm, espaço simples; retirada a
  nota de meta-comentário que precedia a lista.
- Cabeçalho e rodapé a 1,5 cm.
- Forma extensa na primeira ocorrência de cada sigla (ACE-IQ, APGAR, BPAQ, BPAQ-SF, GSHS, INSPIRE,
  RPQ, SDQ, STROBE, VACS e aOR não a tinham).
- Subsecções 5.1 a 5.4 passaram a título de 2.º nível, como 2.1, 3.1 e 7.1.

**Metodologia reforçada (a falha que a auditoria encontrou nos quatro protocolos, incluindo o da
Muanchura: o cálculo só dimensionava o objectivo descritivo)**
- Novo parágrafo de poder para o objectivo analítico: com 424 questionários válidos e efeito de
  desenho de 1,5, o tamanho efectivo é de cerca de 283; a regressão linear detecta efeitos pequenos
  (f² de Cohen 0,028, cerca de 2,7% de variância); a logística só detecta OR a partir de 2,27 para
  uma exposição em 30% dos alunos. Daí a regressão linear passar a análise principal e a logística
  a complementar, com no máximo 10 parâmetros (106 eventos, regra de 10 eventos por parâmetro).
  Duas referências novas, confirmadas no Crossref: Faul et al., 2009 (G*Power) e Peduzzi et al., 1996.
- O p = 53,7% passou a ter correspondência medida: acrescentou-se a pergunta 28 do GSHS ("foi
  agredido fisicamente"), que com a 27 ("lutas físicas") forma exactamente o indicador de
  violência interpessoal de Aboagye et al.; nova variável no Quadro 2.
- Análise ajustada ao desenho por turmas (SPSS Complex Samples ou erros-padrão agrupados por
  turma); o código da turma passou a ser registado na pergunta 1. Regra para itens omissos.
- Justificação do percentil 75 como critério relativo, só para a análise complementar.

**Coerência corrigida**
- Ética: com questionário anónimo não é possível encaminhar quem relatou violência nas respostas.
  O encaminhamento passou a ser feito a pedido do aluno ou por sofrimento observado na sessão, e a
  folha de contactos é entregue a todos (7.11, Apêndice B e TCLE alinhados).
- Cronograma: a aprovação ética estava em Julho-Setembro de 2026, o que já não é possível. Agora:
  submissão em Setembro-Outubro, pré-teste e recolha só depois da aprovação (há um teste que o
  garante).
- 7.7: o castigo físico na escola estava descrito na Secção IV do questionário, mas a pergunta está
  na Secção III.

## 3. Decisões que continuam do lado do estudante e do orientador

- **Calendário.** Recolha em Outubro-Novembro de 2026 depende de parecer ético rápido e tem de
  terminar antes das provas finais. Se o parecer atrasar, a alternativa honesta é passar a recolha
  para 2027, como fez a Muanchura (o título dela diz 2027), e mudar o título em conformidade.
- **Título com 26 palavras.** A norma da FCS pede no máximo 15 na capa. Não o alterei por ser o
  tema registado; uma versão com 14 palavras seria "Factores psicossociais e comportamento
  agressivo em adolescentes da Escola Secundária de Muatala, Nampula, 2026".
- **Número de alunos elegíveis**, para fixar a linha da Tabela 1.

## 4. Decisões metodológicas que o júri vai perguntar

- **Desenho:** transversal analítico, quantitativo, reportado segundo STROBE. Não permite inferir
  causalidade, e o protocolo di-lo explicitamente na secção 7.1 e na Figura 1.
- **Amostragem:** probabilística estratificada por classe, com selecção aleatória de turmas.
- **Cálculo amostral:** proporção única com p = 53,7% (indicador GSHS de violência interpessoal,
  Aboagye et al., 2021), Z = 1,96, d = 0,05, efeito de desenho 1,5 e 10% para não resposta: 383,
  depois 575, depois corrigido para a população finita. Poder verificado para o objectivo
  analítico (secção 2 acima).
- **Desfecho:** forma reduzida do Questionário de Agressividade de Buss e Perry (12 itens) e
  Questionário de Agressão Reactiva e Proactiva (23 itens), ambos com versão portuguesa validada.
- **Factores psicológicos:** SDQ completo (bandas de rastreio), DERS-SF (total sem os itens de
  consciência, como na validação portuguesa), Rosenberg e CRIES-8 (corte 17).
- **Factores do contexto:** APGAR familiar, itens do ACE-IQ e itens do GSHS.
- **Análise:** regressão linear múltipla por blocos (principal), logística binária (complementar),
  modelos separados para reactiva e proactiva e mediação exploratória com bootstrap, ajustadas ao
  desenho amostral, p < 0,05.
- **Ética:** consentimento do encarregado mais assentimento do adolescente, recusa do adolescente
  prevalece, questionário anónimo, pessoa com primeiros socorros psicológicos em cada sessão.

## 5. Base científica

As 108 referências são reais e foram verificadas a 23 de Setembro de 2026: artigos no Crossref e
no PubMed (com leitura do resumo quando se citam números), documentos da OMS, o relatório VACS e o
livro de Hayes por resposta HTTP 200, e 1 referência sem DOI (Smilkstein 1978, PMID 660126). A numeração Vancouver é
gerada por programa pela ordem de aparecimento, pelo que não pode haver saltos.

## 6. Ficheiros da pasta

```
03_TCC/PROTOCOLO_AGRESSIVIDADE_MUATALA.docx   documento final (versão 3)
03_TCC/PROTOCOLO_AGRESSIVIDADE_MUATALA.pdf    versão PDF para enviar
03_TCC/_versoes_anteriores/                   versões 1 (16/09) e 2 (19/09), fontes_v2/
03_TCC/MUANCHURA/                             protocolo de referência (não mexer)
figuras/esquema_conceptual.png                Figura 1, contextos, factores psicológicos, desfecho
OOX/                                          áudios de WhatsApp da estudante (23/09/2026)
REVISAO_V3_PROGRESSO.md                       registo da revisão v3 (transcrição, auditoria, decisões)
pytest.ini                                    exclui as cópias de segurança da recolha de testes
construir_protocolo.py                        gera o .docx e chama o Word para o índice e o PDF
actualizar_word.py                            actualiza índice e páginas no Word e exporta o PDF
validar_protocolo.py                          valida o documento contra as regras da casa
house_docx.py                                 construtor de estilo da casa (cópia local, alargada)
test_protocolo.py, test_house_docx.py         99 testes, incluindo do próprio validador
_figura_esquema.py                            gera a figura
_protocolo_amostra.py                         tamanho da amostra, poder da regressão e da mediação
_protocolo_referencias.py                     as 108 fontes e o numerador Vancouver
_protocolo_texto.py                           pré-textuais e secções 1 e 2
_protocolo_revisao.py                         secções 3 a 6
_protocolo_metodologia.py                     secções 7 a 12
_protocolo_apendices.py                       apêndices A a E (perguntas numeradas automaticamente)
```

O `house_docx.py` passou a viver nesta pasta: o original está em
`E:\HAMZA\DOCUMENTOZ_5_9_2026\TRABALHOS_ACADEMIA\_FERRAMENTAS\` e o caminho `../_FERRAMENTAS`
deixou de existir quando o projecto mudou de pasta. A cópia local não altera o original.

## 7. Como regenerar depois de editar o texto

Editar o módulo `_protocolo_*.py` correspondente e correr, dentro desta pasta:

```bash
python _figura_esquema.py        # só se a figura mudar
python construir_protocolo.py    # gera o .docx, actualiza o índice no Word e exporta o PDF
python validar_protocolo.py      # tem de terminar com "Sem erros"
python -m pytest -q
```

Sem Word disponível: `python construir_protocolo.py --sem-word` e actualizar o índice à mão.
Se editar directamente o `.docx` no Word, as alterações perdem-se na próxima execução do
construtor; depois de preencher os nomes no Word, passe a trabalhar só no `.docx`.

## 8. O que o validador verifica

Página A4, margens 3/3/2,5/2,5 cm, cabeçalho e rodapé a 1,5 cm; Times New Roman 12 a preto
(incluindo a formatação herdada dos estilos); espaçamento; ausência de travessões, setas, expoentes
Unicode e outros símbolos proibidos; grafia anterior ao Acordo de 1990; clichés de geração
automática; as 14 secções obrigatórias; resumo e abstract conformes à norma (parágrafo único, 250 a
300 palavras, sem rótulos, siglas nem citações, 3 a 5 palavras-chave alfabéticas); índice automático
já actualizado; numeração Vancouver íntegra; referências com avanço de 0,75 cm; cada sigla listada
usada no corpo e definida na primeira ocorrência; correspondência entre objectivos e resultados
esperados; número de página no canto inferior direito, ausente na capa.

## 9. Próximos passos sugeridos

1. Levar a versão 3 ao orientador, com as secções 1 e 3 deste ficheiro (testes, calendário e título).
2. Pedir à direcção da escola o número de alunos por classe, turma e turno.
3. Pedir autorização formal aos autores das escalas (Pechorro et al.; SDQ em sdqinfo.org; DERS-SF).
4. Submeter ao Comité Institucional de Bioética para a Saúde da UniLúrio.
5. Quando o protocolo for aprovado: slides de defesa e guião de perguntas do oponente, no formato
   já usado nas pastas MUANCHURA e MANU.
