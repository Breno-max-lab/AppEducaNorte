"""
Módulo Fundamental — EducaNorte
6º ao 9º ano · Contextualizado para a Amazônia
"""

# ── PORTUGUÊS ──────────────────────────────────────────────
LICOES_PORTUGUES = {
    1: {"titulo": "Tipos de texto", "texto": "Existem vários tipos de texto: narrativo (conta uma história), descritivo (descreve algo), argumentativo (defende uma ideia) e informativo (informa sobre fatos). Cada tipo tem características próprias.",
        "perguntas": [
            {"enunciado": "Um texto que conta uma história com personagens é:", "opcoes": ["Descritivo","Narrativo","Argumentativo","Informativo"], "resposta": "Narrativo", "dica": "Pense em contos e lendas."},
            {"enunciado": "Uma notícia de jornal é um exemplo de texto:", "opcoes": ["Narrativo","Poético","Informativo","Lírico"], "resposta": "Informativo", "dica": "Notícias informam sobre fatos reais."},
            {"enunciado": "Um texto que defende um ponto de vista com argumentos é:", "opcoes": ["Descritivo","Narrativo","Argumentativo","Dramático"], "resposta": "Argumentativo", "dica": "Argumentar é defender uma ideia com razões."},
            {"enunciado": "Qual recurso linguístico é mais usado em textos descritivos?", "opcoes": ["Verbos de ação","Adjetivos","Conjunções","Verbos no futuro"], "resposta": "Adjetivos", "dica": "Adjetivos caracterizam e descrevem."},
        ]},
    2: {"titulo": "Classes de palavras", "texto": "As palavras classificam-se em: substantivos (nomeiam seres), adjetivos (caracterizam), verbos (ação ou estado), advérbios (modificam verbos/adjetivos) e pronomes (substituem substantivos).",
        "perguntas": [
            {"enunciado": "Em 'O boto nada rapidamente', 'rapidamente' é:", "opcoes": ["Substantivo","Adjetivo","Advérbio","Verbo"], "resposta": "Advérbio", "dica": "Modifica o verbo — indica como."},
            {"enunciado": "Na frase 'A floresta é exuberante', 'exuberante' é:", "opcoes": ["Substantivo","Adjetivo","Advérbio","Verbo"], "resposta": "Adjetivo", "dica": "Caracteriza o substantivo 'floresta'."},
            {"enunciado": "Qual é o substantivo coletivo para grupo de peixes?", "opcoes": ["Cardume","Bando","Alcateia","Manada"], "resposta": "Cardume", "dica": "Cardume = grupo de peixes."},
            {"enunciado": "Em 'Ele pescou muito', 'Ele' é um:", "opcoes": ["Substantivo","Adjetivo","Pronome","Advérbio"], "resposta": "Pronome", "dica": "Pronomes substituem substantivos."},
        ]},
    3: {"titulo": "Sujeito e predicado", "texto": "Toda oração tem sujeito (quem pratica/sofre a ação) e predicado (o que se diz do sujeito). O sujeito pode ser simples, composto ou inexistente (verbos impessoais).",
        "perguntas": [
            {"enunciado": "Em 'O pescador lançou a rede', o sujeito é:", "opcoes": ["lançou a rede","O pescador","a rede","no rio"], "resposta": "O pescador", "dica": "Sujeito é quem pratica a ação."},
            {"enunciado": "Em 'Choveu muito na Amazônia', o sujeito é:", "opcoes": ["Choveu","muito","na Amazônia","Inexistente"], "resposta": "Inexistente", "dica": "Verbos de fenômeno natural não têm sujeito."},
            {"enunciado": "Em 'O rio está cheio', o predicado é:", "opcoes": ["O rio","está cheio","cheio","está"], "resposta": "está cheio", "dica": "Predicado é tudo que se diz do sujeito."},
            {"enunciado": "Qual oração tem sujeito composto?", "opcoes": ["O boto nada","João e Maria pescaram","Chove na floresta","O peixe fugiu"], "resposta": "João e Maria pescaram", "dica": "Sujeito composto tem mais de um núcleo."},
        ]},
    4: {"titulo": "Interpretação de texto", "texto": "A Amazônia abriga cerca de 10% das espécies do planeta. A floresta regula o clima, armazena carbono e é lar de povos tradicionais. O desmatamento ameaça esse ecossistema vital.",
        "perguntas": [
            {"enunciado": "Qual porcentagem das espécies do planeta a Amazônia abriga?", "opcoes": ["1%","5%","10%","20%"], "resposta": "10%", "dica": "Resposta está na primeira frase."},
            {"enunciado": "Qual função da floresta NÃO é citada no texto?", "opcoes": ["Regular o clima","Armazenar carbono","Produzir medicamentos","Ser lar de povos"], "resposta": "Produzir medicamentos", "dica": "Releia as funções listadas."},
            {"enunciado": "Qual é a ameaça mencionada?", "opcoes": ["Queimadas","Caça","Desmatamento","Poluição"], "resposta": "Desmatamento", "dica": "A última frase cita a ameaça."},
            {"enunciado": "Qual é o tom predominante do texto?", "opcoes": ["Humorístico","Informativo e preocupante","Poético","Publicitário"], "resposta": "Informativo e preocupante", "dica": "Observe os dados e a temática."},
        ]},
    5: {"titulo": "Redação dissertativa", "texto": "Um texto dissertativo-argumentativo tem: introdução (apresenta tema e tese), desenvolvimento (argumenta com exemplos) e conclusão (retoma a tese e propõe solução). É o formato exigido no ENEM.",
        "perguntas": [
            {"enunciado": "Qual parte apresenta a tese?", "opcoes": ["Desenvolvimento","Conclusão","Introdução","Transição"], "resposta": "Introdução", "dica": "A tese é apresentada no início."},
            {"enunciado": "O desenvolvimento deve ter:", "opcoes": ["Apenas a tese","Argumentos e exemplos","A proposta","Repetição da introdução"], "resposta": "Argumentos e exemplos", "dica": "Desenvolver é argumentar com evidências."},
            {"enunciado": "A conclusão deve conter:", "opcoes": ["Novos argumentos","Resumo + proposta de solução","Apenas a tese","Uma pergunta"], "resposta": "Resumo + proposta de solução", "dica": "A conclusão fecha e propõe."},
            {"enunciado": "O que NÃO deve aparecer em redação formal?", "opcoes": ["Dados estatísticos","Gírias e abreviações","Citações","Argumentos"], "resposta": "Gírias e abreviações", "dica": "Redação formal exige linguagem culta."},
        ]},
}

# ── MATEMÁTICA ─────────────────────────────────────────────
LICOES_MATEMATICA = {
    1: {"titulo": "Frações e decimais", "texto": "Uma fração representa partes de um todo. O numerador indica quantas partes temos e o denominador em quantas partes o todo foi dividido. Decimais são formas alternativas: 1/2 = 0,5; 1/4 = 0,25; 3/4 = 0,75.",
        "perguntas": [
            {"enunciado": "Quanto é 3/4 em decimal?", "opcoes": ["0,34","0,75","0,43","0,3"], "resposta": "0,75", "dica": "Divida 3 por 4."},
            {"enunciado": "Uma canoa tem 8 lugares e 6 estão ocupados. A fração dos vazios é:", "opcoes": ["6/8","2/6","2/8","1/4"], "resposta": "2/8", "dica": "Vazios = 8-6 = 2. Total = 8."},
            {"enunciado": "1/3 + 1/3 = ?", "opcoes": ["1/6","2/6","2/3","1/9"], "resposta": "2/3", "dica": "Denominadores iguais: some os numeradores."},
            {"enunciado": "0,5 + 0,25 = ?", "opcoes": ["0,7","0,75","0,25","1,25"], "resposta": "0,75", "dica": "Some as partes decimais."},
        ]},
    2: {"titulo": "Porcentagem", "texto": "Porcentagem significa 'por cem'. Para calcular a porcentagem de um número: multiplique por ela e divida por 100. Exemplo: 20% de 50 = (20 × 50) / 100 = 10.",
        "perguntas": [
            {"enunciado": "Quanto é 10% de 200?", "opcoes": ["10","20","2","100"], "resposta": "20", "dica": "10% = 1/10. Divida por 10."},
            {"enunciado": "Uma pesca de 50 peixes teve 30% de piranhas. Quantas?", "opcoes": ["10","15","20","30"], "resposta": "15", "dica": "30% de 50 = 0,30 × 50."},
            {"enunciado": "25% de 40 alunos são meninas. Quantas?", "opcoes": ["8","10","15","25"], "resposta": "10", "dica": "25% = 1/4. Divida por 4."},
            {"enunciado": "50% de 80 = ?", "opcoes": ["8","30","40","50"], "resposta": "40", "dica": "50% = metade. Divida por 2."},
        ]},
    3: {"titulo": "Equações do 1º grau", "texto": "Uma equação do 1º grau tem a forma ax + b = c. Para resolver, isole o x: leve os termos sem x para o outro lado, invertendo a operação (+ vira −, × vira ÷).",
        "perguntas": [
            {"enunciado": "Resolva: x + 5 = 12", "opcoes": ["x=5","x=7","x=17","x=6"], "resposta": "x=7", "dica": "x = 12 − 5."},
            {"enunciado": "Resolva: 2x = 18", "opcoes": ["x=9","x=16","x=36","x=8"], "resposta": "x=9", "dica": "Divida os dois lados por 2."},
            {"enunciado": "Resolva: 3x − 6 = 9", "opcoes": ["x=1","x=5","x=3","x=4"], "resposta": "x=5", "dica": "3x = 15, logo x = 5."},
            {"enunciado": "Um barco faz x km/h e em 3h percorre 60 km. Quanto é x?", "opcoes": ["15","20","18","25"], "resposta": "20", "dica": "3x = 60, logo x = 20."},
        ]},
    4: {"titulo": "Geometria — Áreas", "texto": "Área mede a superfície de uma figura. Retângulo: A = base × altura. Triângulo: A = (base × altura) / 2. Círculo: A = π × r² (use π ≈ 3,14).",
        "perguntas": [
            {"enunciado": "Uma roça mede 8 m × 12 m. Qual é a área?", "opcoes": ["40 m²","80 m²","96 m²","20 m²"], "resposta": "96 m²", "dica": "A = 8 × 12."},
            {"enunciado": "Perímetro de um quadrado com lado 5 m:", "opcoes": ["10 m","15 m","20 m","25 m"], "resposta": "20 m", "dica": "4 lados iguais: 4 × 5."},
            {"enunciado": "Triângulo com base 10 m e altura 6 m. Área?", "opcoes": ["60 m²","30 m²","16 m²","20 m²"], "resposta": "30 m²", "dica": "(10 × 6) / 2 = 30."},
            {"enunciado": "Lago circular com raio 7 m. Área? (π ≈ 3)", "opcoes": ["21 m²","147 m²","44 m²","49 m²"], "resposta": "147 m²", "dica": "3 × 7² = 3 × 49 = 147."},
        ]},
    5: {"titulo": "Estatística básica", "texto": "Média = soma ÷ quantidade. Moda = valor que mais aparece. Mediana = valor central quando os dados estão em ordem crescente. Esses conceitos ajudam a analisar dados do dia a dia.",
        "perguntas": [
            {"enunciado": "Peixes pescados em 5 dias: 4, 6, 8, 6, 11. Qual é a média?", "opcoes": ["6","7","8","35"], "resposta": "7", "dica": "Soma (35) ÷ 5 = 7."},
            {"enunciado": "Nos mesmos dados, qual é a moda?", "opcoes": ["4","6","8","11"], "resposta": "6", "dica": "Moda = valor que mais aparece."},
            {"enunciado": "Dados em ordem: 4, 6, 6, 8, 11. Qual é a mediana?", "opcoes": ["4","6","8","11"], "resposta": "6", "dica": "Mediana = 3º elemento de 5."},
            {"enunciado": "Para que serve a estatística no dia a dia?", "opcoes": ["Apenas em provas","Analisar e interpretar dados reais","Calcular frações","Resolver equações"], "resposta": "Analisar e interpretar dados reais", "dica": "Estatística interpreta números da realidade."},
        ]},
}

# ── CIÊNCIAS ────────────────────────────────────────────────
LICOES_CIENCIAS = {
    1: {"titulo": "Ecossistemas amazônicos", "texto": "Um ecossistema é formado por seres vivos e o ambiente físico onde vivem. Na Amazônia existem: floresta de terra firme, várzea (alagada sazonalmente) e igapó (alagado permanentemente). Cada um tem espécies adaptadas.",
        "perguntas": [
            {"enunciado": "O que forma um ecossistema?", "opcoes": ["Apenas animais","Apenas plantas","Seres vivos + ambiente físico","Apenas o solo"], "resposta": "Seres vivos + ambiente físico", "dica": "Eco = ambiente + seres vivos."},
            {"enunciado": "A floresta permanentemente alagada chama-se:", "opcoes": ["Várzea","Igapó","Terra firme","Cerrado"], "resposta": "Igapó", "dica": "Igapó = sempre inundado."},
            {"enunciado": "A várzea amazônica alaga:", "opcoes": ["Permanentemente","Sazonalmente","Nunca","Só à noite"], "resposta": "Sazonalmente", "dica": "Várzea alaga quando o rio sobe."},
            {"enunciado": "Qual NÃO é componente do ambiente físico?", "opcoes": ["Temperatura","Umidade","Fotossíntese","Solo"], "resposta": "Fotossíntese", "dica": "Fotossíntese é processo dos seres vivos."},
        ]},
    2: {"titulo": "Cadeia alimentar", "texto": "A cadeia alimentar mostra quem come quem: produtores (plantas) → consumidores primários (herbívoros) → consumidores secundários (carnívoros) → decompositores (fungos e bactérias, que devolvem nutrientes ao solo).",
        "perguntas": [
            {"enunciado": "Quem inicia toda cadeia alimentar?", "opcoes": ["Carnívoros","Produtores (plantas)","Decompositores","Consumidores secundários"], "resposta": "Produtores (plantas)", "dica": "Plantas produzem energia pela fotossíntese."},
            {"enunciado": "Um peixe que come algas é chamado de:", "opcoes": ["Produtor","Consumidor primário","Consumidor secundário","Decompositor"], "resposta": "Consumidor primário", "dica": "Come diretamente o produtor."},
            {"enunciado": "Fungos e bactérias que decompõem matéria são:", "opcoes": ["Produtores","Consumidores primários","Decompositores","Predadores"], "resposta": "Decompositores", "dica": "Devolvem nutrientes ao solo."},
            {"enunciado": "Sem decompositores o que aconteceria?", "opcoes": ["Nada muda","A matéria orgânica se acumularia no ambiente","Carnívoros morreriam primeiro","Mais plantas cresceriam"], "resposta": "A matéria orgânica se acumularia no ambiente", "dica": "Decompositores reciclam a matéria orgânica."},
        ]},
    3: {"titulo": "Sistemas do corpo humano", "texto": "O corpo humano tem sistemas: digestório (processa alimentos), respiratório (troca de gases), circulatório (transporta sangue), nervoso (controla funções) e excretor (elimina resíduos). Todos trabalham juntos.",
        "perguntas": [
            {"enunciado": "Qual sistema realiza a troca de O₂ e CO₂?", "opcoes": ["Digestório","Circulatório","Respiratório","Excretor"], "resposta": "Respiratório", "dica": "Respiramos O₂ e exalamos CO₂."},
            {"enunciado": "O coração faz parte de qual sistema?", "opcoes": ["Digestório","Nervoso","Respiratório","Circulatório"], "resposta": "Circulatório", "dica": "O coração bombeia o sangue."},
            {"enunciado": "A digestão química dos alimentos ocorre no:", "opcoes": ["Boca apenas","Estômago e intestino","Pulmões","Rins"], "resposta": "Estômago e intestino", "dica": "Digestão química começa no estômago."},
            {"enunciado": "Os rins fazem parte do sistema:", "opcoes": ["Digestório","Respiratório","Excretor","Nervoso"], "resposta": "Excretor", "dica": "Os rins filtram o sangue e produzem urina."},
        ]},
    4: {"titulo": "Matéria e energia", "texto": "Matéria é tudo que tem massa e ocupa espaço. Energia é a capacidade de realizar trabalho. Lei da Conservação de Energia: a energia não se cria nem se destrói, apenas se transforma.",
        "perguntas": [
            {"enunciado": "O que define a matéria?", "opcoes": ["Ter cor e cheiro","Ter massa e ocupar espaço","Ser visível","Ser sólida"], "resposta": "Ter massa e ocupar espaço", "dica": "Até o ar invisível é matéria."},
            {"enunciado": "Água passando por uma turbina transforma energia:", "opcoes": ["Química em elétrica","Cinética em elétrica","Solar em cinética","Térmica em luminosa"], "resposta": "Cinética em elétrica", "dica": "Água em movimento (cinética) gera eletricidade."},
            {"enunciado": "A Lei da Conservação de Energia diz que energia:", "opcoes": ["Se cria na natureza","Se destrói no calor","Só se transforma, nunca se cria ou destrói","É ilimitada"], "resposta": "Só se transforma, nunca se cria ou destrói", "dica": "Lei fundamental da física."},
            {"enunciado": "A água a 0 °C está no estado:", "opcoes": ["Gasoso","Líquido","Sólido","Plasma"], "resposta": "Sólido", "dica": "0 °C é o ponto de solidificação da água."},
        ]},
    5: {"titulo": "Saúde e doenças tropicais", "texto": "Na Amazônia, doenças como malária, dengue e leishmaniose são comuns. A malária é transmitida pelo mosquito Anopheles; a dengue, pelo Aedes aegypti. Prevenção: repelente, mosquiteiro, eliminação de água parada.",
        "perguntas": [
            {"enunciado": "Qual mosquito transmite a dengue?", "opcoes": ["Anopheles","Aedes aegypti","Culex","Pernilongo-comum"], "resposta": "Aedes aegypti", "dica": "O Aedes também transmite zika e chikungunya."},
            {"enunciado": "Melhor forma de prevenir malária:", "opcoes": ["Tomar antibióticos","Usar mosquiteiro e repelente","Beber muito líquido","Comer frutas"], "resposta": "Usar mosquiteiro e repelente", "dica": "Prevenção é a melhor defesa."},
            {"enunciado": "O que é um vetor de doença?", "opcoes": ["O vírus","O organismo que transmite a doença","O medicamento","O sintoma"], "resposta": "O organismo que transmite a doença", "dica": "Mosquito = vetor da dengue."},
            {"enunciado": "Por que água parada é perigosa?", "opcoes": ["Fica suja","É criadouro do Aedes aegypti","Não serve para beber","Atrai cobras"], "resposta": "É criadouro do Aedes aegypti", "dica": "O Aedes se reproduz em água parada."},
        ]},
}

# ── HISTÓRIA ────────────────────────────────────────────────
LICOES_HISTORIA = {
    1: {"titulo": "Povos originários da Amazônia", "texto": "Antes dos europeus, a Amazônia tinha centenas de povos indígenas com culturas, línguas e tradições próprias. Desenvolveram técnicas de agricultura, navegação e medicina adaptadas à floresta. Hoje, mais de 300 etnias vivem no Brasil.",
        "perguntas": [
            {"enunciado": "Quantas etnias indígenas vivem no Brasil?", "opcoes": ["Menos de 50","Cerca de 100","Mais de 300","Exatamente 500"], "resposta": "Mais de 300", "dica": "O texto informa esse número."},
            {"enunciado": "O que os povos originários desenvolveram?", "opcoes": ["Apenas caça","Agricultura, navegação e medicina","Só rituais","Cidades de pedra"], "resposta": "Agricultura, navegação e medicina", "dica": "Releia o segundo parágrafo."},
            {"enunciado": "O que diferenciava os povos indígenas entre si?", "opcoes": ["Nada","Línguas, culturas e tradições","Apenas localização","Tamanho das aldeias"], "resposta": "Línguas, culturas e tradições", "dica": "Cada povo tinha sua identidade única."},
            {"enunciado": "As línguas indígenas eram:", "opcoes": ["Todas iguais","Cada povo tinha a sua","Derivadas do português","Uma só língua geral"], "resposta": "Cada povo tinha a sua", "dica": "O texto cita línguas e culturas próprias."},
        ]},
    2: {"titulo": "Colonização da Amazônia", "texto": "A colonização europeia da Amazônia começou no século XVII. Portugueses e espanhóis disputavam o território. O Tratado de Madri (1750) definiu as fronteiras atuais. A colonização causou a morte de milhões de indígenas por doenças e escravidão.",
        "perguntas": [
            {"enunciado": "Em que século começou a colonização europeia da Amazônia?", "opcoes": ["XV","XVI","XVII","XVIII"], "resposta": "XVII", "dica": "O texto menciona o século."},
            {"enunciado": "O Tratado de Madri (1750) serviu para:", "opcoes": ["Libertar escravos","Definir fronteiras","Proibir borracha","Criar missões"], "resposta": "Definir fronteiras", "dica": "O texto explica para que serviu."},
            {"enunciado": "Principal causa da morte de indígenas na colonização:", "opcoes": ["Fome","Doenças e escravidão","Guerras tribais","Migração voluntária"], "resposta": "Doenças e escravidão", "dica": "A última frase do texto responde."},
            {"enunciado": "Quais países disputavam a Amazônia?", "opcoes": ["França e Holanda","Portugal e Espanha","Inglaterra e Portugal","Espanha e França"], "resposta": "Portugal e Espanha", "dica": "O texto cita os dois países."},
        ]},
    3: {"titulo": "Ciclo da Borracha", "texto": "Entre 1850 e 1912, a Amazônia viveu o Ciclo da Borracha. Manaus enriqueceu e construiu o Teatro Amazonas (1896). O ciclo entrou em declínio quando a Malásia passou a produzir borracha mais barata com sementes contrabandeadas do Brasil.",
        "perguntas": [
            {"enunciado": "Em que período ocorreu o Ciclo da Borracha?", "opcoes": ["1750-1850","1850-1912","1912-1950","1500-1600"], "resposta": "1850-1912", "dica": "O texto indica as datas."},
            {"enunciado": "Qual obra foi construída com a riqueza da borracha?", "opcoes": ["Museu do Índio","Teatro Amazonas","Catedral de Manaus","Palácio Rio Negro"], "resposta": "Teatro Amazonas", "dica": "O texto cita essa obra."},
            {"enunciado": "Por que o Ciclo da Borracha entrou em declínio?", "opcoes": ["A borracha acabou","A Malásia produziu borracha mais barata","O Brasil proibiu exportação","Greve dos seringueiros"], "resposta": "A Malásia produziu borracha mais barata", "dica": "O texto explica a causa."},
            {"enunciado": "De onde vieram as sementes que a Malásia plantou?", "opcoes": ["África","Índia","Brasil (contrabandeadas)","China"], "resposta": "Brasil (contrabandeadas)", "dica": "O texto menciona o contrabando."},
        ]},
    4: {"titulo": "Brasil República", "texto": "A República Brasileira foi proclamada em 15 de novembro de 1889 pelo Marechal Deodoro da Fonseca. A Primeira República (1889-1930) foi marcada pelo coronelismo e pela política do 'café com leite' entre SP e MG.",
        "perguntas": [
            {"enunciado": "Quando foi proclamada a República Brasileira?", "opcoes": ["7 de setembro de 1822","15 de novembro de 1889","1 de janeiro de 1900","13 de maio de 1888"], "resposta": "15 de novembro de 1889", "dica": "Data histórica citada no texto."},
            {"enunciado": "O que foi a política do 'café com leite'?", "opcoes": ["Aliança de cafeicultores","Alternância de poder entre SP e MG","Bebida popular","Tratado comercial"], "resposta": "Alternância de poder entre SP e MG", "dica": "O texto explica essa política."},
            {"enunciado": "Quem proclamou a República?", "opcoes": ["Dom Pedro II","Getúlio Vargas","Marechal Deodoro da Fonseca","Rui Barbosa"], "resposta": "Marechal Deodoro da Fonseca", "dica": "Primeira frase do texto."},
            {"enunciado": "O coronelismo era:", "opcoes": ["Um partido político","Poder político local de grandes proprietários","Uma guerra civil","Um tipo de governo federal"], "resposta": "Poder político local de grandes proprietários", "dica": "O 'coronel' dominava a política local."},
        ]},
    5: {"titulo": "Brasil contemporâneo", "texto": "O Brasil viveu ditadura militar de 1964 a 1985. A redemocratização culminou com a Constituição de 1988, chamada 'Constituição Cidadã'. Em 1989 ocorreram as primeiras eleições presidenciais diretas em 29 anos.",
        "perguntas": [
            {"enunciado": "Por quanto tempo durou a ditadura militar?", "opcoes": ["10 anos","21 anos","30 anos","5 anos"], "resposta": "21 anos", "dica": "De 1964 a 1985 = 21 anos."},
            {"enunciado": "Por que a Constituição de 1988 é chamada 'Cidadã'?", "opcoes": ["Escrita por cidadãos","Ampliou os direitos dos cidadãos","Aprovada por referendo","Proibiu o voto de analfabetos"], "resposta": "Ampliou os direitos dos cidadãos", "dica": "'Cidadã' = garantiu direitos fundamentais."},
            {"enunciado": "Qual é a forma de governo do Brasil?", "opcoes": ["Monarquia","República parlamentarista","República federativa presidencialista","Oligarquia"], "resposta": "República federativa presidencialista", "dica": "A última frase do texto responde."},
            {"enunciado": "Em que ano foram as primeiras eleições diretas após a ditadura?", "opcoes": ["1985","1988","1989","1990"], "resposta": "1989", "dica": "O texto cita 1989."},
        ]},
}

# ── GEOGRAFIA ───────────────────────────────────────────────
LICOES_GEOGRAFIA = {
    1: {"titulo": "Regiões do Brasil", "texto": "O Brasil tem 5 regiões: Norte (maior em área), Nordeste, Centro-Oeste (cerrado e agronegócio), Sudeste (mais industrializada) e Sul (menor região). Cada uma tem características geográficas, climáticas e culturais próprias.",
        "perguntas": [
            {"enunciado": "Qual é a maior região do Brasil em área?", "opcoes": ["Sudeste","Nordeste","Norte","Centro-Oeste"], "resposta": "Norte", "dica": "A Amazônia está na região Norte."},
            {"enunciado": "Qual é a região mais industrializada?", "opcoes": ["Norte","Nordeste","Sul","Sudeste"], "resposta": "Sudeste", "dica": "SP e RJ ficam no Sudeste."},
            {"enunciado": "O bioma predominante no Centro-Oeste é:", "opcoes": ["Amazônia","Caatinga","Cerrado","Mata Atlântica"], "resposta": "Cerrado", "dica": "Centro-Oeste = cerrado e agronegócio."},
            {"enunciado": "Qual é a menor região do Brasil?", "opcoes": ["Norte","Nordeste","Sul","Sudeste"], "resposta": "Sul", "dica": "O texto informa qual é a menor."},
        ]},
    2: {"titulo": "Hidrografia amazônica", "texto": "O Rio Amazonas é o maior do mundo em volume de água e o segundo em extensão. A Amazônia tem clima equatorial: quente e úmido. A 'friagem' ocorre quando massas de ar frio do sul chegam e reduzem a temperatura abruptamente.",
        "perguntas": [
            {"enunciado": "O Rio Amazonas é o maior em:", "opcoes": ["Extensão","Volume de água","Profundidade","Número de afluentes"], "resposta": "Volume de água", "dica": "O Nilo é maior em extensão."},
            {"enunciado": "Como é o clima amazônico?", "opcoes": ["Semiárido","Temperado","Equatorial","Subtropical"], "resposta": "Equatorial", "dica": "Próximo à Linha do Equador."},
            {"enunciado": "O que é a 'friagem' na Amazônia?", "opcoes": ["Período seco","Chegada de ar frio do sul","Inversão do rio","Chuva intensa"], "resposta": "Chegada de ar frio do sul", "dica": "O texto define claramente."},
            {"enunciado": "Qual grande afluente do Amazonas nasce na Colômbia?", "opcoes": ["Rio Tapajós","Rio Negro","Rio Madeira","Rio Xingu"], "resposta": "Rio Negro", "dica": "O Rio Negro vem do noroeste."},
        ]},
    3: {"titulo": "Coordenadas geográficas", "texto": "Latitude mede a distância à Linha do Equador (0° a 90° N/S). Longitude mede a distância ao Meridiano de Greenwich (0° a 180° L/O). Juntas, localizam qualquer ponto na Terra.",
        "perguntas": [
            {"enunciado": "O que mede a latitude?", "opcoes": ["Distância ao Meridiano","Distância ao Equador","Altitude","Temperatura"], "resposta": "Distância ao Equador", "dica": "Equador → latitude."},
            {"enunciado": "Qual é a latitude na Linha do Equador?", "opcoes": ["90°","45°","0°","180°"], "resposta": "0°", "dica": "O Equador é a referência zero."},
            {"enunciado": "O Brasil está em qual hemisfério?", "opcoes": ["Apenas Norte","Apenas Sul","Norte e Sul","Apenas Leste"], "resposta": "Norte e Sul", "dica": "O Equador passa pelo norte do Brasil."},
            {"enunciado": "O que é o Meridiano de Greenwich?", "opcoes": ["Linha horizontal de referência","Linha vertical de referência da longitude","Trópico de Capricórnio","Linha do Equador"], "resposta": "Linha vertical de referência da longitude", "dica": "Greenwich = referência zero da longitude."},
        ]},
    4: {"titulo": "Urbanização brasileira", "texto": "Urbanização é o crescimento das cidades. No Brasil acelerou a partir de 1950 com a industrialização. O êxodo rural é a migração do campo para a cidade. Hoje, cerca de 87% dos brasileiros vivem em áreas urbanas.",
        "perguntas": [
            {"enunciado": "O que é êxodo rural?", "opcoes": ["Migração da cidade para o campo","Migração do campo para a cidade","Crescimento rural","Criação de fazendas"], "resposta": "Migração do campo para a cidade", "dica": "Êxodo = saída. Saída do campo."},
            {"enunciado": "Que % dos brasileiros vive em cidades?", "opcoes": ["50%","70%","87%","95%"], "resposta": "87%", "dica": "O texto informa o dado atual."},
            {"enunciado": "Quando a urbanização acelerou no Brasil?", "opcoes": ["1850","1920","1950","1980"], "resposta": "1950", "dica": "Ligada à industrialização."},
            {"enunciado": "Qual problema a urbanização acelerada causa?", "opcoes": ["Mais empregos rurais","Periferias sem infraestrutura","Mais florestas","Menos poluição"], "resposta": "Periferias sem infraestrutura", "dica": "Crescimento rápido sem planejamento gera periferias precárias."},
        ]},
    5: {"titulo": "Problemas ambientais globais", "texto": "O aquecimento global é causado pelo aumento do efeito estufa (emissão de CO₂ e outros gases). Consequências: derretimento de geleiras, elevação do nível do mar e eventos climáticos extremos. O desmatamento amazônico agrava o problema, pois a floresta absorve CO₂.",
        "perguntas": [
            {"enunciado": "O que causa o aquecimento global?", "opcoes": ["Diminuição do efeito estufa","Mais chuvas","Aumento do efeito estufa por CO₂","Erupções vulcânicas apenas"], "resposta": "Aumento do efeito estufa por CO₂", "dica": "CO₂ intensifica o efeito estufa."},
            {"enunciado": "Por que o desmatamento agrava o aquecimento?", "opcoes": ["Libera água","Sem floresta há mais CO₂ na atmosfera","Aquece o solo","Elimina animais"], "resposta": "Sem floresta há mais CO₂ na atmosfera", "dica": "A floresta absorve CO₂."},
            {"enunciado": "Uma consequência do aquecimento global:", "opcoes": ["Só mais chuvas","Derretimento das geleiras","Menos furacões","Resfriamento dos oceanos"], "resposta": "Derretimento das geleiras", "dica": "O texto lista as consequências."},
            {"enunciado": "O efeito estufa natural é:", "opcoes": ["Um problema ambiental","Essencial para manter a Terra aquecida","Resultado do desmatamento","Um tipo de poluição"], "resposta": "Essencial para manter a Terra aquecida", "dica": "O problema é o excesso, não o efeito estufa em si."},
        ]},
}

# ── ÍNDICE GERAL ────────────────────────────────────────────
MODULOS_FUNDAMENTAL = {
    "portugues":  {"titulo": "Português",  "icone": "📝", "cor": "#00C9A7", "licoes": LICOES_PORTUGUES},
    "matematica": {"titulo": "Matemática", "icone": "➗", "cor": "#F4A261", "licoes": LICOES_MATEMATICA},
    "ciencias":   {"titulo": "Ciências",   "icone": "🔬", "cor": "#4ADE80", "licoes": LICOES_CIENCIAS},
    "historia":   {"titulo": "História",   "icone": "📜", "cor": "#F87171", "licoes": LICOES_HISTORIA},
    "geografia":  {"titulo": "Geografia",  "icone": "🌍", "cor": "#9B72CF", "licoes": LICOES_GEOGRAFIA},
}
