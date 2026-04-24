"""
Módulo Médio/Adulto — EducaNorte
1º ao 3º ano do Ensino Médio + Preparação ENEM
7 disciplinas × 5 níveis = 35 lições, 140 perguntas
"""

# ── REDAÇÃO ENEM ────────────────────────────────────────────
LICOES_REDACAO = {
    1: {"titulo": "As 5 competências do ENEM", "texto": "A redação do ENEM avalia 5 competências: 1) Domínio da norma culta da língua; 2) Compreensão do tema proposto; 3) Seleção e organização dos argumentos; 4) Coesão e coerência textual; 5) Proposta de intervenção que respeite os direitos humanos. Cada competência vale até 200 pontos (total: 1000 pontos).",
        "perguntas": [
            {"enunciado": "Quantas competências a redação do ENEM avalia?", "opcoes": ["3","4","5","6"], "resposta": "5", "dica": "O texto lista as 5 competências."},
            {"enunciado": "Qual é a pontuação máxima da redação do ENEM?", "opcoes": ["500","800","1000","200"], "resposta": "1000", "dica": "5 competências × 200 pontos = 1000."},
            {"enunciado": "A competência 5 exige que a proposta de intervenção respeite:", "opcoes": ["O governo","Os direitos humanos","A BNCC","As leis ambientais"], "resposta": "Os direitos humanos", "dica": "A última competência trata da intervenção social."},
            {"enunciado": "Qual competência avalia a coesão e coerência?", "opcoes": ["Competência 1","Competência 2","Competência 3","Competência 4"], "resposta": "Competência 4", "dica": "O texto lista as competências em ordem."},
        ]},
    2: {"titulo": "Estrutura da redação dissertativa", "texto": "A redação dissertativa-argumentativa tem três partes obrigatórias: Introdução (apresenta o tema e a tese — ideia central do texto); Desenvolvimento (dois ou mais parágrafos com argumentos, dados e exemplos que sustentam a tese); Conclusão (retoma a tese e apresenta a proposta de intervenção detalhada).",
        "perguntas": [
            {"enunciado": "Qual parte da redação apresenta a tese?", "opcoes": ["Desenvolvimento","Conclusão","Introdução","Parágrafo de transição"], "resposta": "Introdução", "dica": "A tese é apresentada no início do texto."},
            {"enunciado": "O desenvolvimento deve conter:", "opcoes": ["Apenas a tese","Argumentos, dados e exemplos","A proposta de intervenção","Repetição da introdução"], "resposta": "Argumentos, dados e exemplos", "dica": "Desenvolver é argumentar com evidências."},
            {"enunciado": "A conclusão deve conter:", "opcoes": ["Novos argumentos","Resumo e proposta de intervenção detalhada","Apenas a tese","Uma pergunta ao leitor"], "resposta": "Resumo e proposta de intervenção detalhada", "dica": "A conclusão fecha o texto e propõe solução."},
            {"enunciado": "Quantos parágrafos de desenvolvimento são recomendados?", "opcoes": ["Apenas 1","Dois ou mais","Exatamente 3","Quantos quiser"], "resposta": "Dois ou mais", "dica": "O texto diz 'dois ou mais parágrafos'."},
        ]},
    3: {"titulo": "Proposta de intervenção", "texto": "A proposta de intervenção deve conter 5 elementos: Ação (o que fazer), Agente (quem vai fazer), Meio/Modo (como fazer), Finalidade (por que fazer) e Efeito esperado (o que vai melhorar). Deve ser detalhada, viável e respeitar os direitos humanos. Propostas vagas não pontuam na competência 5.",
        "perguntas": [
            {"enunciado": "Quantos elementos deve ter uma proposta de intervenção completa?", "opcoes": ["3","4","5","6"], "resposta": "5", "dica": "Ação, agente, meio, finalidade e efeito."},
            {"enunciado": "O 'agente' na proposta de intervenção é:", "opcoes": ["O que será feito","Quem vai executar a ação","Como será feito","O resultado esperado"], "resposta": "Quem vai executar a ação", "dica": "Agente = responsável pela ação."},
            {"enunciado": "Uma proposta de intervenção deve ser:", "opcoes": ["Apenas criativa","Viável e respeitar os direitos humanos","Baseada apenas em leis existentes","Sempre de responsabilidade do governo"], "resposta": "Viável e respeitar os direitos humanos", "dica": "A última frase do texto responde."},
            {"enunciado": "O que torna uma proposta de intervenção ineficaz?", "opcoes": ["Ter agente definido","Ser vaga e genérica","Ter finalidade clara","Respeitar direitos humanos"], "resposta": "Ser vaga e genérica", "dica": "O texto alerta sobre propostas vagas."},
        ]},
    4: {"titulo": "Repertório e argumentação", "texto": "Um bom argumento é sustentado por repertório sociocultural: dados estatísticos, citações de especialistas, referências históricas, filosóficas ou literárias. O repertório deve ser legitimado (correto e verificável) e relacionado ao tema. Frases vagas como 'todo mundo sabe' não constituem argumento válido.",
        "perguntas": [
            {"enunciado": "O que é repertório sociocultural?", "opcoes": ["Palavras difíceis","Dados e referências que sustentam o argumento","Introdução do texto","O número de linhas"], "resposta": "Dados e referências que sustentam o argumento", "dica": "Repertório = conjunto de conhecimentos usados como argumento."},
            {"enunciado": "Qual exemplo de repertório é mais valorizado?", "opcoes": ["'Todo mundo sabe que...'","Dado estatístico verificável","Opinião pessoal","Experiência familiar"], "resposta": "Dado estatístico verificável", "dica": "O repertório deve ser legitimado, ou seja, verificável."},
            {"enunciado": "O repertório deve ser:", "opcoes": ["Extenso e complicado","Correto, verificável e relacionado ao tema","Retirado apenas de livros clássicos","Sempre de filósofos gregos"], "resposta": "Correto, verificável e relacionado ao tema", "dica": "O texto define 'legitimado'."},
            {"enunciado": "Frases vagas como 'todo mundo sabe' são:", "opcoes": ["Muito aceitas no ENEM","Argumentos filosóficos","Não constituem argumento válido","Equivalentes a dados estatísticos"], "resposta": "Não constituem argumento válido", "dica": "A última frase do texto confirma isso."},
        ]},
    5: {"titulo": "Coesão, coerência e conectivos", "texto": "Coesão é a articulação das partes do texto por meio de conectivos. Coerência é a unidade de sentido — o texto não pode se contradizer. Conectivos adversativos (porém, entretanto, contudo) indicam oposição. Aditivos (além disso, ademais) somam ideias. Conclusivos (portanto, logo, assim) concluem. Explicativos (pois, porque) explicam.",
        "perguntas": [
            {"enunciado": "O que é coesão textual?", "opcoes": ["Ausência de erros gramaticais","Articulação entre as partes do texto com conectivos","Unidade de sentido","Originalidade das ideias"], "resposta": "Articulação entre as partes do texto com conectivos", "dica": "Coesão = ligação entre as partes do texto."},
            {"enunciado": "Qual conectivo é adversativo (indica oposição)?", "opcoes": ["Ademais","Portanto","Entretanto","Além disso"], "resposta": "Entretanto", "dica": "Adversativos indicam contraste ou oposição."},
            {"enunciado": "O conectivo 'portanto' é:", "opcoes": ["Adversativo","Aditivo","Conclusivo","Explicativo"], "resposta": "Conclusivo", "dica": "Portanto, logo, assim = conclusão."},
            {"enunciado": "Um texto com informações contraditórias falta:", "opcoes": ["Coesão","Coerência","Argumentos","Conectivos"], "resposta": "Coerência", "dica": "Coerência = unidade de sentido, sem contradições."},
        ]},
}

# ── MATEMÁTICA ─────────────────────────────────────────────
LICOES_MATEMATICA = {
    1: {"titulo": "Funções do 1º e 2º grau", "texto": "Função do 1º grau: f(x) = ax + b (gráfico é uma reta). Função do 2º grau: f(x) = ax² + bx + c (gráfico é uma parábola). O vértice tem x = -b/2a. A discriminante Δ = b² − 4ac: se Δ > 0, duas raízes reais; Δ = 0, uma raiz real; Δ < 0, sem raízes reais.",
        "perguntas": [
            {"enunciado": "O gráfico de uma função do 1º grau é:", "opcoes": ["Parábola","Reta","Hipérbole","Elipse"], "resposta": "Reta", "dica": "f(x) = ax + b sempre gera uma reta."},
            {"enunciado": "Para f(x) = x² − 5x + 6, qual é o valor de Δ?", "opcoes": ["1","4","√6","11"], "resposta": "1", "dica": "Δ = b² − 4ac = 25 − 24 = 1."},
            {"enunciado": "Se Δ < 0, a equação do 2º grau tem:", "opcoes": ["Duas raízes reais","Uma raiz real","Nenhuma raiz real","Raízes negativas"], "resposta": "Nenhuma raiz real", "dica": "Δ negativo → sem raízes reais."},
            {"enunciado": "O vértice de f(x) = x² − 4x + 3 tem x = ?", "opcoes": ["1","2","3","4"], "resposta": "2", "dica": "x = −b/2a = 4/2 = 2."},
        ]},
    2: {"titulo": "Trigonometria", "texto": "No triângulo retângulo: seno = cateto oposto/hipotenusa; cosseno = cateto adjacente/hipotenusa; tangente = cateto oposto/cateto adjacente. Valores especiais: sen 30° = 0,5; cos 60° = 0,5; tan 45° = 1; sen 90° = 1.",
        "perguntas": [
            {"enunciado": "Seno é a razão entre:", "opcoes": ["Cateto adjacente e hipotenusa","Cateto oposto e hipotenusa","Cateto oposto e adjacente","Hipotenusa e cateto oposto"], "resposta": "Cateto oposto e hipotenusa", "dica": "SOH: Seno = Oposto / Hipotenusa."},
            {"enunciado": "Qual é o valor de sen 30°?", "opcoes": ["√2/2","√3/2","0,5","1"], "resposta": "0,5", "dica": "sen 30° = 1/2 = 0,5."},
            {"enunciado": "Cateto oposto = 3, hipotenusa = 5. Qual é o seno?", "opcoes": ["0,4","0,5","0,6","0,75"], "resposta": "0,6", "dica": "seno = 3/5 = 0,6."},
            {"enunciado": "tan 45° = ?", "opcoes": ["0","0,5","1","√3"], "resposta": "1", "dica": "Em 45° os catetos são iguais, tan = 1."},
        ]},
    3: {"titulo": "Probabilidade e combinatória", "texto": "Probabilidade = casos favoráveis ÷ casos totais. Fatorial: n! = n×(n−1)×...×1. Arranjo (ordem importa): Aₙₖ = n!/(n−k)!. Combinação (ordem não importa): Cₙₖ = n!/[k!(n−k)!]. Exemplo: C(5,2) = 120/12 = 10.",
        "perguntas": [
            {"enunciado": "Probabilidade de tirar cara ao jogar uma moeda:", "opcoes": ["1/4","1/3","1/2","2/3"], "resposta": "1/2", "dica": "1 caso favorável ÷ 2 possíveis."},
            {"enunciado": "De quantas formas escolher 2 de 5 alunos (sem importar a ordem)?", "opcoes": ["10","20","5","15"], "resposta": "10", "dica": "C(5,2) = 5!/(2!×3!) = 10."},
            {"enunciado": "Num baralho de 52 cartas, qual a prob. de sortear um ás?", "opcoes": ["1/52","1/13","1/4","4/13"], "resposta": "1/13", "dica": "4 ases em 52 cartas = 4/52 = 1/13."},
            {"enunciado": "4! (quatro fatorial) = ?", "opcoes": ["8","12","16","24"], "resposta": "24", "dica": "4×3×2×1 = 24."},
        ]},
    4: {"titulo": "Progressões e logaritmos", "texto": "PA: cada termo = anterior + razão (r). Fórmula: aₙ = a₁ + (n−1)r. PG: cada termo = anterior × razão (q). Logaritmo: log_b(x) = y significa b^y = x. log₁₀(1000) = 3 pois 10³ = 1000. Usado em juros compostos, escala Richter e decibéis.",
        "perguntas": [
            {"enunciado": "PA com a₁ = 2 e r = 3. Qual é o 5º termo?", "opcoes": ["14","15","17","20"], "resposta": "14", "dica": "a₅ = 2 + (5−1)×3 = 2 + 12 = 14."},
            {"enunciado": "PG com a₁ = 2 e q = 3. Qual é o 4º termo?", "opcoes": ["18","54","27","81"], "resposta": "54", "dica": "a₄ = 2×3³ = 2×27 = 54."},
            {"enunciado": "log₁₀(100) = ?", "opcoes": ["1","2","10","100"], "resposta": "2", "dica": "10² = 100, logo log = 2."},
            {"enunciado": "Juros compostos crescem como qual progressão?", "opcoes": ["PA","PG","Estatística","Geometria plana"], "resposta": "PG", "dica": "Juros compostos multiplicam por uma razão fixa."},
        ]},
    5: {"titulo": "Geometria analítica", "texto": "Distância entre P₁(x₁,y₁) e P₂(x₂,y₂): d = √[(x₂−x₁)² + (y₂−y₁)²]. Ponto médio: M = ((x₁+x₂)/2, (y₁+y₂)/2). Equação da reta: y = ax + b (a = coeficiente angular; b = coeficiente linear). Retas paralelas têm mesmo coeficiente angular.",
        "perguntas": [
            {"enunciado": "Distância entre (0,0) e (3,4):", "opcoes": ["5","7","12","√7"], "resposta": "5", "dica": "√(3²+4²) = √25 = 5."},
            {"enunciado": "Ponto médio entre (2,4) e (6,8):", "opcoes": ["(4,6)","(8,12)","(4,4)","(3,5)"], "resposta": "(4,6)", "dica": "M = ((2+6)/2, (4+8)/2) = (4,6)."},
            {"enunciado": "Na equação y = 2x + 3, o coeficiente angular é:", "opcoes": ["3","2","5","0"], "resposta": "2", "dica": "Coeficiente angular = a na forma y = ax + b."},
            {"enunciado": "Retas paralelas têm:", "opcoes": ["Mesmo coeficiente linear","Mesmo coeficiente angular","Coeficientes opostos","Coeficientes nulos"], "resposta": "Mesmo coeficiente angular", "dica": "Paralelas têm a mesma inclinação."},
        ]},
}

# ── FÍSICA ─────────────────────────────────────────────────
LICOES_FISICA = {
    1: {"titulo": "Cinemática — MU e MRUV", "texto": "Movimento Uniforme (MU): velocidade constante, aceleração nula. Fórmula: s = s₀ + v·t. Movimento Uniformemente Variado (MRUV): aceleração constante ≠ 0. Fórmulas: v = v₀ + a·t e s = s₀ + v₀·t + a·t²/2. Equação de Torricelli: v² = v₀² + 2·a·Δs.",
        "perguntas": [
            {"enunciado": "No MU (Movimento Uniforme) a aceleração é:", "opcoes": ["Positiva","Negativa","Zero","Variável"], "resposta": "Zero", "dica": "MU = velocidade constante = aceleração nula."},
            {"enunciado": "Um barco percorre 120 km em 3 h. Qual é sua velocidade?", "opcoes": ["30 km/h","40 km/h","360 km/h","60 km/h"], "resposta": "40 km/h", "dica": "v = Δs/Δt = 120/3 = 40 km/h."},
            {"enunciado": "No MRUV com v₀ = 0, a = 2 m/s² e t = 5 s, qual é a velocidade final?", "opcoes": ["5 m/s","7 m/s","10 m/s","2,5 m/s"], "resposta": "10 m/s", "dica": "v = v₀ + a·t = 0 + 2×5 = 10 m/s."},
            {"enunciado": "A equação de Torricelli é útil quando:", "opcoes": ["O tempo é conhecido","O tempo não é conhecido","A aceleração é zero","A velocidade é constante"], "resposta": "O tempo não é conhecido", "dica": "Torricelli relaciona v, v₀, a e Δs sem o tempo."},
        ]},
    2: {"titulo": "Leis de Newton", "texto": "1ª Lei (Inércia): um corpo em repouso ou MU permanece assim se a força resultante for nula. 2ª Lei: F = m·a (força resultante = massa × aceleração). 3ª Lei (Ação-Reação): toda ação tem reação igual, oposta e aplicada em corpos diferentes.",
        "perguntas": [
            {"enunciado": "A 2ª Lei de Newton relaciona:", "opcoes": ["Velocidade e distância","Força, massa e aceleração","Energia e tempo","Pressão e volume"], "resposta": "Força, massa e aceleração", "dica": "F = m·a."},
            {"enunciado": "Força de 10 N aplicada a massa de 2 kg gera aceleração de:", "opcoes": ["20 m/s²","5 m/s²","12 m/s²","8 m/s²"], "resposta": "5 m/s²", "dica": "a = F/m = 10/2 = 5 m/s²."},
            {"enunciado": "A 1ª Lei de Newton é chamada de lei da:", "opcoes": ["Ação e reação","Inércia","Aceleração","Gravitação"], "resposta": "Inércia", "dica": "Inércia = tendência de manter o estado de movimento."},
            {"enunciado": "Ao remar uma canoa, a água empurra o remo e a canoa avança. Isso é a:", "opcoes": ["1ª Lei","2ª Lei","3ª Lei","Lei da Gravidade"], "resposta": "3ª Lei", "dica": "Ação (remo na água) → Reação (água empurra a canoa)."},
        ]},
    3: {"titulo": "Termologia e calor", "texto": "Temperatura mede a agitação das moléculas. Calor (Q) é energia transferida entre corpos de diferentes temperaturas. Q = m·c·ΔT (m = massa em g, c = calor específico, ΔT = variação de temperatura). Conversão: °F = (9/5)·°C + 32; K = °C + 273.",
        "perguntas": [
            {"enunciado": "Calor é:", "opcoes": ["O mesmo que temperatura","Energia transferida entre corpos","Medido em graus","A temperatura de um objeto"], "resposta": "Energia transferida entre corpos", "dica": "Calor flui do mais quente para o mais frio."},
            {"enunciado": "Para aquecer 2000 g de água (c = 1 cal/g·°C) de 20 °C a 70 °C:", "opcoes": ["50 cal","100 cal","100.000 cal","1.000 cal"], "resposta": "100.000 cal", "dica": "Q = 2000 × 1 × 50 = 100.000 cal."},
            {"enunciado": "37 °C em Fahrenheit é:", "opcoes": ["96,6 °F","98,6 °F","100 °F","102 °F"], "resposta": "98,6 °F", "dica": "°F = (9/5)×37 + 32 = 66,6 + 32 = 98,6."},
            {"enunciado": "0 °C em Kelvin é:", "opcoes": ["0 K","100 K","173 K","273 K"], "resposta": "273 K", "dica": "K = °C + 273 = 0 + 273 = 273 K."},
        ]},
    4: {"titulo": "Ondas e óptica", "texto": "Ondas transportam energia sem transportar matéria. Comprimento de onda (λ), frequência (f) e velocidade (v) relacionam-se por: v = f·λ. Frequência medida em Hertz (Hz). A luz visível é onda eletromagnética (não precisa de meio). Som é onda mecânica (precisa de meio).",
        "perguntas": [
            {"enunciado": "Ondas transportam:", "opcoes": ["Matéria e energia","Apenas matéria","Apenas energia","Nem matéria nem energia"], "resposta": "Apenas energia", "dica": "A onda se propaga; a matéria oscila no lugar."},
            {"enunciado": "A relação entre v, f e λ é:", "opcoes": ["v = f + λ","v = f/λ","v = f·λ","v = λ/f"], "resposta": "v = f·λ", "dica": "Fórmula fundamental das ondas."},
            {"enunciado": "A unidade de frequência é:", "opcoes": ["Metro","Segundo","Hertz (Hz)","Joule"], "resposta": "Hertz (Hz)", "dica": "Hz = oscilações por segundo."},
            {"enunciado": "Qual onda NÃO precisa de meio material para se propagar?", "opcoes": ["Som","Onda em corda","Luz","Onda no mar"], "resposta": "Luz", "dica": "Luz é eletromagnética — propaga-se no vácuo."},
        ]},
    5: {"titulo": "Eletricidade — Lei de Ohm e circuitos", "texto": "Lei de Ohm: V = R·I (tensão = resistência × corrente). Potência: P = V·I = R·I². Circuitos em série: Rt = R₁ + R₂ + ... Circuitos em paralelo: 1/Rt = 1/R₁ + 1/R₂ + ... Energia elétrica: E = P·t (medida em kWh na conta de luz).",
        "perguntas": [
            {"enunciado": "A Lei de Ohm é:", "opcoes": ["F = m·a","V = R·I","E = mc²","P = W/t"], "resposta": "V = R·I", "dica": "Tensão = Resistência × Corrente."},
            {"enunciado": "Com V = 220 V e R = 44 Ω, a corrente é:", "opcoes": ["2 A","5 A","10 A","0,2 A"], "resposta": "5 A", "dica": "I = V/R = 220/44 = 5 A."},
            {"enunciado": "Potência de um chuveiro de 220 V e 10 A:", "opcoes": ["22 W","2.200 W","220 W","22 kW"], "resposta": "2.200 W", "dica": "P = V·I = 220 × 10 = 2.200 W."},
            {"enunciado": "Em circuito em série com R₁ = 4 Ω e R₂ = 6 Ω, a resistência total é:", "opcoes": ["2,4 Ω","10 Ω","24 Ω","1 Ω"], "resposta": "10 Ω", "dica": "Série: Rt = R₁ + R₂ = 4 + 6 = 10 Ω."},
        ]},
}

# ── QUÍMICA ─────────────────────────────────────────────────
LICOES_QUIMICA = {
    1: {"titulo": "Tabela periódica e ligações", "texto": "A Tabela Periódica organiza os elementos por número atômico crescente. Períodos (linhas) = nível de energia. Grupos/famílias (colunas) = propriedades semelhantes. Metais alcalinos (grupo 1), halogênios (grupo 17), gases nobres (grupo 18). Ligação iônica: metal + não-metal. Ligação covalente: não-metal + não-metal.",
        "perguntas": [
            {"enunciado": "O que elementos da mesma família têm em comum?", "opcoes": ["Mesmo número atômico","Propriedades químicas semelhantes","Mesma massa atômica","Mesmo estado físico"], "resposta": "Propriedades químicas semelhantes", "dica": "Família = coluna = propriedades parecidas."},
            {"enunciado": "Os gases nobres estão no grupo:", "opcoes": ["1","2","17","18"], "resposta": "18", "dica": "Grupo 18 = gases nobres (He, Ne, Ar...)."},
            {"enunciado": "A ligação entre Na e Cl é:", "opcoes": ["Covalente","Iônica","Metálica","Dipolo"], "resposta": "Iônica", "dica": "Metal (Na) + não-metal (Cl) = iônica."},
            {"enunciado": "A água (H₂O) tem ligação:", "opcoes": ["Iônica","Metálica","Covalente","Intermolecular"], "resposta": "Covalente", "dica": "H e O são não-metais → compartilham elétrons."},
        ]},
    2: {"titulo": "Reações químicas e balanceamento", "texto": "Reações transformam reagentes em produtos. A Lei de Lavoisier afirma que a massa dos reagentes = massa dos produtos ('nada se cria, nada se perde'). Tipos: Síntese (A+B→AB), Decomposição (AB→A+B), Simples troca (A+BC→AC+B), Dupla troca (AB+CD→AD+CB).",
        "perguntas": [
            {"enunciado": "A Lei de Lavoisier afirma que:", "opcoes": ["A energia se conserva","Massa dos reagentes = massa dos produtos","Só metais reagem","Toda reação libera calor"], "resposta": "Massa dos reagentes = massa dos produtos", "dica": "'Nada se cria, nada se perde, tudo se transforma.'"},
            {"enunciado": "H₂ + O₂ → H₂O é uma reação de:", "opcoes": ["Decomposição","Síntese","Simples troca","Dupla troca"], "resposta": "Síntese", "dica": "Dois simples formam um composto = síntese."},
            {"enunciado": "2H₂O → 2H₂ + O₂ é uma reação de:", "opcoes": ["Síntese","Decomposição","Simples troca","Dupla troca"], "resposta": "Decomposição", "dica": "Um composto se divide em mais simples = decomposição."},
            {"enunciado": "Balancear uma equação significa:", "opcoes": ["Escrever nomes dos produtos","Igualar o número de átomos de cada elemento","Calcular a velocidade","Identificar reagentes"], "resposta": "Igualar o número de átomos de cada elemento", "dica": "Balancear respeita a Lei de Lavoisier."},
        ]},
    3: {"titulo": "pH, ácidos e bases", "texto": "pH mede a acidez: pH < 7 = ácido; pH = 7 = neutro; pH > 7 = básico/alcalino. Escala vai de 0 (mais ácido) a 14 (mais básico). Ácidos liberam H⁺ em água; bases liberam OH⁻. Indicadores como fenolftaleína (incolor em ácido, rosa em base) e papel tornassol detectam o pH.",
        "perguntas": [
            {"enunciado": "Uma solução com pH = 3 é:", "opcoes": ["Neutra","Básica","Ácida","Salina"], "resposta": "Ácida", "dica": "pH < 7 = ácido."},
            {"enunciado": "O que os ácidos liberam em solução aquosa?", "opcoes": ["OH⁻","H⁺","Na⁺","Cl⁻"], "resposta": "H⁺", "dica": "Ácido de Arrhenius libera H⁺."},
            {"enunciado": "Suco de limão tem pH ≈ 2. Isso indica:", "opcoes": ["Neutro","Muito ácido","Levemente básico","Fortemente básico"], "resposta": "Muito ácido", "dica": "Quanto menor o pH (abaixo de 7), mais ácido."},
            {"enunciado": "A fenolftaleína fica rosa/vermelho em soluções:", "opcoes": ["Ácidas","Neutras","Básicas","Salinas"], "resposta": "Básicas", "dica": "Fenolftaleína: incolor em ácido, rosa em base."},
        ]},
    4: {"titulo": "Estequiometria", "texto": "Estequiometria estuda as proporções entre reagentes e produtos. 1 mol de qualquer substância contém 6,02×10²³ partículas (Número de Avogadro) e ocupa 22,4 L (nas CNTP). Massa molar (g/mol) = soma das massas atômicas. Exemplo: H₂O tem massa molar = 2×1 + 16 = 18 g/mol.",
        "perguntas": [
            {"enunciado": "Quantas partículas tem 1 mol de qualquer substância?", "opcoes": ["10²³","6,02×10²³","22,4×10²³","3,01×10²³"], "resposta": "6,02×10²³", "dica": "Número de Avogadro = 6,02×10²³."},
            {"enunciado": "Qual é a massa molar da água (H₂O)?", "opcoes": ["10 g/mol","16 g/mol","18 g/mol","20 g/mol"], "resposta": "18 g/mol", "dica": "2×H(1) + O(16) = 2 + 16 = 18 g/mol."},
            {"enunciado": "Nas CNTP, 1 mol de gás ocupa:", "opcoes": ["1 L","10 L","22,4 L","100 L"], "resposta": "22,4 L", "dica": "Volume molar nas CNTP = 22,4 L/mol."},
            {"enunciado": "Estequiometria estuda:", "opcoes": ["Velocidade das reações","Proporções entre reagentes e produtos","Temperatura das reações","Cor dos compostos"], "resposta": "Proporções entre reagentes e produtos", "dica": "Do grego: stoicheion = elemento; metron = medida."},
        ]},
    5: {"titulo": "Química ambiental", "texto": "Principais problemas ambientais de origem química: efeito estufa (CO₂, CH₄), destruição da camada de ozônio (CFCs), chuva ácida (SO₂ e NOₓ) e poluição da água por metais pesados (mercúrio, chumbo). Na Amazônia, o garimpo ilegal libera mercúrio nos rios, contaminando peixes e comunidades ribeirinhas.",
        "perguntas": [
            {"enunciado": "Principal gás responsável pelo efeito estufa:", "opcoes": ["O₂","CO","CO₂","N₂"], "resposta": "CO₂", "dica": "Gás carbônico = principal gás estufa."},
            {"enunciado": "O que destrói a camada de ozônio?", "opcoes": ["CO₂","SO₂","CFCs","NOₓ"], "resposta": "CFCs", "dica": "Clorofluorcarbonetos (aerossóis e refrigeradores antigos)."},
            {"enunciado": "A chuva ácida é causada por:", "opcoes": ["CO₂ e O₂","SO₂ e NOₓ","CFCs e CO","H₂O e N₂"], "resposta": "SO₂ e NOₓ", "dica": "Reagem com a água formando ácidos sulfúrico e nítrico."},
            {"enunciado": "O garimpo ilegal na Amazônia contamina os rios com:", "opcoes": ["Cloro","Mercúrio","Flúor","Chumbo apenas"], "resposta": "Mercúrio", "dica": "O mercúrio é usado para separar o ouro do minério."},
        ]},
}

# ── BIOLOGIA ────────────────────────────────────────────────
LICOES_BIOLOGIA = {
    1: {"titulo": "Célula — estrutura e função", "texto": "A célula é a unidade básica da vida. Célula procarionte: sem núcleo definido, sem organelas membranosas (bactérias). Célula eucarionte: com núcleo e organelas. Organelas importantes: mitocôndria (respiração celular/energia), cloroplasto (fotossíntese), ribossomo (síntese de proteínas).",
        "perguntas": [
            {"enunciado": "Células sem núcleo definido são chamadas de:", "opcoes": ["Eucariontes","Procariontes","Vegetais","Animais"], "resposta": "Procariontes", "dica": "Bactérias são procariontes."},
            {"enunciado": "Qual organela realiza a respiração celular?", "opcoes": ["Ribossomo","Cloroplasto","Mitocôndria","Núcleo"], "resposta": "Mitocôndria", "dica": "Mitocôndria = 'usina de energia' da célula."},
            {"enunciado": "A fotossíntese ocorre em qual organela?", "opcoes": ["Mitocôndria","Ribossomo","Cloroplasto","Vacúolo"], "resposta": "Cloroplasto", "dica": "Cloroplasto contém clorofila."},
            {"enunciado": "Os ribossomos são responsáveis pela:", "opcoes": ["Produção de energia","Fotossíntese","Síntese de proteínas","Divisão celular"], "resposta": "Síntese de proteínas", "dica": "Ribossomo = fábrica de proteínas da célula."},
        ]},
    2: {"titulo": "Genética — Leis de Mendel", "texto": "Mendel descobriu as leis da hereditariedade. 1ª Lei (Segregação): os alelos de um par se separam na formação dos gametas. 2ª Lei (Segregação independente): pares de alelos diferentes se combinam independentemente. Alelo dominante (D) se manifesta sobre o recessivo (r) no heterozigoto (Dd).",
        "perguntas": [
            {"enunciado": "Na genética, alelos são:", "opcoes": ["Cromossomos","Formas alternativas do mesmo gene","Proteínas","Tipos de célula"], "resposta": "Formas alternativas do mesmo gene", "dica": "Cada versão do gene é um alelo."},
            {"enunciado": "Um indivíduo com genótipo Dd é:", "opcoes": ["Homozigoto dominante","Homozigoto recessivo","Heterozigoto","Portador invisível"], "resposta": "Heterozigoto", "dica": "Dois alelos diferentes = heterozigoto."},
            {"enunciado": "No cruzamento Dd × Dd, quantos filhos serão recessivos (dd)?", "opcoes": ["0%","25%","50%","75%"], "resposta": "25%", "dica": "Quadrado de Punnett: DD, Dd, Dd, dd → dd = 1/4."},
            {"enunciado": "A 1ª Lei de Mendel estabelece:", "opcoes": ["Herança independente de pares","Segregação dos alelos na formação dos gametas","Mutação genética","Codominância"], "resposta": "Segregação dos alelos na formação dos gametas", "dica": "1ª Lei = Lei da Segregação."},
        ]},
    3: {"titulo": "Evolução e ecologia", "texto": "Darwin propôs a Seleção Natural: organismos com características favoráveis sobrevivem e se reproduzem mais. Relações ecológicas: Mutualismo (+,+), Comensalismo (+,0), Predatismo (+,−), Parasitismo (+,−), Amensalismo (0,−). O símbolo indica o efeito sobre cada espécie envolvida.",
        "perguntas": [
            {"enunciado": "O que é seleção natural?", "opcoes": ["Criação de espécies","Sobrevivência e reprodução de organismos com características favoráveis","Mutação aleatória","Extinção coletiva"], "resposta": "Sobrevivência e reprodução de organismos com características favoráveis", "dica": "Os mais adaptados deixam mais descendentes."},
            {"enunciado": "Flores e abelhas têm relação de:", "opcoes": ["Predatismo","Parasitismo","Mutualismo","Comensalismo"], "resposta": "Mutualismo", "dica": "Ambos se beneficiam: (+,+)."},
            {"enunciado": "No parasitismo os efeitos são:", "opcoes": ["(+,+)","(+,−)","(0,−)","(+,0)"], "resposta": "(+,−)", "dica": "Parasita se beneficia; hospedeiro é prejudicado."},
            {"enunciado": "Rêmoras alimentam-se de restos de tubarões sem prejudicá-los. Isso é:", "opcoes": ["Mutualismo","Predatismo","Comensalismo","Parasitismo"], "resposta": "Comensalismo", "dica": "Um se beneficia; o outro é indiferente (+,0)."},
        ]},
    4: {"titulo": "Biotecnologia e DNA", "texto": "O DNA é formado por bases: Adenina (A), Timina (T), Guanina (G) e Citosina (C). A−T e G−C se pareiam. A biotecnologia usa o DNA para criar organismos transgênicos (genes de outras espécies inseridos), vacinas recombinantes e terapia gênica (correção de genes defeituosos).",
        "perguntas": [
            {"enunciado": "Quais bases nitrogenadas se pareiam no DNA?", "opcoes": ["A−G e T−C","A−T e G−C","A−C e G−T","A−A e T−T"], "resposta": "A−T e G−C", "dica": "Adenina com Timina; Guanina com Citosina."},
            {"enunciado": "Organismos transgênicos são:", "opcoes": ["Organismos extintos","Organismos com genes de outras espécies inseridos","Organismos clonados","Organismos sem DNA"], "resposta": "Organismos com genes de outras espécies inseridos", "dica": "Trans = além; gênico = relativo ao gene."},
            {"enunciado": "O DNA está localizado no:", "opcoes": ["Citoplasma","Núcleo celular","Ribossomo","Mitocôndria"], "resposta": "Núcleo celular", "dica": "O núcleo é o centro de controle da célula."},
            {"enunciado": "A terapia gênica serve para:", "opcoes": ["Criar animais","Corrigir genes defeituosos","Acelerar a evolução","Clonar humanos"], "resposta": "Corrigir genes defeituosos", "dica": "Terapia gênica substitui ou corrige genes."},
        ]},
    5: {"titulo": "Fisiologia — Fotossíntese e respiração", "texto": "Fotossíntese (cloroplasto): 6CO₂ + 6H₂O + luz → C₆H₁₂O₆ + 6O₂. Respiração celular (mitocôndria): C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP (energia). Fermentação: ocorre sem oxigênio, produz menos energia. Usada em pão, cerveja e iogurte.",
        "perguntas": [
            {"enunciado": "Qual gás é liberado pela fotossíntese?", "opcoes": ["CO₂","H₂O","N₂","O₂"], "resposta": "O₂", "dica": "Fotossíntese: CO₂ + H₂O → glicose + O₂."},
            {"enunciado": "A respiração celular ocorre na:", "opcoes": ["Cloroplasto","Ribossomo","Mitocôndria","Vacúolo"], "resposta": "Mitocôndria", "dica": "Mitocôndria = 'usina de energia'."},
            {"enunciado": "A fermentação ocorre:", "opcoes": ["Com muito oxigênio","Sem oxigênio","Apenas em plantas","Apenas em fungos"], "resposta": "Sem oxigênio", "dica": "Fermentação = respiração anaeróbica."},
            {"enunciado": "Qual produto a fermentação alcoólica gera?", "opcoes": ["Glicose e O₂","Etanol e CO₂","Ácido láctico e H₂","Água e ATP"], "resposta": "Etanol e CO₂", "dica": "Usada em pães e bebidas alcoólicas."},
        ]},
}

# ── FILOSOFIA / SOCIOLOGIA ──────────────────────────────────
LICOES_FILOSOFIA = {
    1: {"titulo": "Sócrates, Platão e Aristóteles", "texto": "Sócrates usava a maiêutica (diálogo para buscar a verdade). Platão criou a Teoria das Ideias: o mundo real é sombra do mundo ideal (Alegoria da Caverna). Aristóteles, discípulo de Platão, valorizou a observação empírica e classificou os seres vivos — fundou a lógica formal.",
        "perguntas": [
            {"enunciado": "O método socrático de buscar a verdade pelo diálogo é:", "opcoes": ["Empirismo","Maiêutica","Racionalismo","Dedução"], "resposta": "Maiêutica", "dica": "Maiêutica = 'partejar' ideias pelo questionamento."},
            {"enunciado": "A Alegoria da Caverna foi criada por:", "opcoes": ["Sócrates","Aristóteles","Platão","Tales"], "resposta": "Platão", "dica": "Platão escreveu A República, onde está a Alegoria."},
            {"enunciado": "Aristóteles se diferenciou de Platão por valorizar:", "opcoes": ["O mundo das ideias","A observação empírica do mundo real","A matemática pura","As leis divinas"], "resposta": "A observação empírica do mundo real", "dica": "Aristóteles fundou a ciência empírica."},
            {"enunciado": "'Só sei que nada sei' é atribuída a:", "opcoes": ["Platão","Aristóteles","Sócrates","Descartes"], "resposta": "Sócrates", "dica": "Expressa a humildade intelectual socrática."},
        ]},
    2: {"titulo": "Filosofia política — contrato social", "texto": "Hobbes: sem o Estado, o homem vive em guerra ('o homem é o lobo do homem'). Locke: direitos naturais (vida, liberdade e propriedade) são anteriores ao Estado. Rousseau: Contrato Social — os indivíduos cedem parte da liberdade em troca de proteção. Montesquieu: separação dos três poderes (Executivo, Legislativo e Judiciário).",
        "perguntas": [
            {"enunciado": "Quem propôs a separação dos três poderes?", "opcoes": ["Rousseau","Hobbes","Locke","Montesquieu"], "resposta": "Montesquieu", "dica": "Executivo, Legislativo e Judiciário."},
            {"enunciado": "Para Hobbes, sem o Estado o homem viveria em:", "opcoes": ["Harmonia natural","Estado de guerra","Democracia","Cooperação plena"], "resposta": "Estado de guerra", "dica": "'O homem é o lobo do homem.'"},
            {"enunciado": "O Contrato Social de Rousseau implica:", "opcoes": ["Poder absoluto do rei","Indivíduos cedem parte da liberdade por proteção social","A natureza é perfeita sem Estado","A propriedade é sagrada"], "resposta": "Indivíduos cedem parte da liberdade por proteção social", "dica": "Contrato = acordo entre indivíduo e sociedade."},
            {"enunciado": "Locke defendia como direitos naturais:", "opcoes": ["Fama, poder e riqueza","Vida, liberdade e propriedade","Trabalho, saúde e educação","Obediência, ordem e progresso"], "resposta": "Vida, liberdade e propriedade", "dica": "Influenciou a Independência dos EUA."},
        ]},
    3: {"titulo": "Ética — Kant, utilitarismo e virtude", "texto": "Kant: imperativo categórico — 'Aja apenas segundo a máxima que possa ser lei universal.' A ação correta independe das consequências (deontologia). Utilitarismo (Mill/Bentham): o certo é o que produz o maior bem para o maior número. Aristóteles: virtude é o equilíbrio (justo-meio) entre extremos.",
        "perguntas": [
            {"enunciado": "O imperativo categórico de Kant pede para agir:", "opcoes": ["Buscando o prazer","Segundo normas que possam ser universais","Seguindo a maioria","Obedecendo ao Estado"], "resposta": "Segundo normas que possam ser universais", "dica": "Kant: a ação deve ser universalizável."},
            {"enunciado": "O utilitarismo considera correto o que:", "opcoes": ["Segue leis divinas","Agrada ao governante","Gera maior bem para o maior número","É imposto pela tradição"], "resposta": "Gera maior bem para o maior número", "dica": "Utilitarismo = máxima utilidade coletiva."},
            {"enunciado": "Para Kant, a ética depende das:", "opcoes": ["Consequências das ações","Intenções e a ação em si","Emoções do agente","Leis do país"], "resposta": "Intenções e a ação em si", "dica": "Kant é deontológico — foco no dever, não no resultado."},
            {"enunciado": "Quem propôs que a virtude é o justo-meio entre extremos?", "opcoes": ["Platão","Kant","Aristóteles","Mill"], "resposta": "Aristóteles", "dica": "Coragem = meio entre covardia e temeridade."},
        ]},
    4: {"titulo": "Sociologia — Durkheim, Marx e Weber", "texto": "Durkheim: sociedade é maior que a soma dos indivíduos; estudou o suicídio como fato social. Marx: história é luta de classes; capitalismo explora o proletariado (mais-valia). Weber: a ação social tem sentido para o agente; estudou a relação entre protestantismo e capitalismo.",
        "perguntas": [
            {"enunciado": "Quem estudou o suicídio como fato social?", "opcoes": ["Marx","Weber","Durkheim","Comte"], "resposta": "Durkheim", "dica": "Durkheim fundou a sociologia como ciência."},
            {"enunciado": "Para Marx, a história é movida por:", "opcoes": ["Grandes indivíduos","Luta de classes","A vontade divina","Progresso tecnológico"], "resposta": "Luta de classes", "dica": "'A história é a história da luta de classes.' — Marx."},
            {"enunciado": "O que é mais-valia para Marx?", "opcoes": ["Salário extra","Valor produzido além do que o trabalhador recebe","Imposto cobrado","Lucro comercial justo"], "resposta": "Valor produzido além do que o trabalhador recebe", "dica": "Mais-valia = exploração do trabalhador."},
            {"enunciado": "Weber estudou a relação entre protestantismo e:", "opcoes": ["Democracia","Capitalismo","Socialismo","Feudalismo"], "resposta": "Capitalismo", "dica": "'A Ética Protestante e o Espírito do Capitalismo.'"},
        ]},
    5: {"titulo": "Direitos humanos e cidadania", "texto": "A Declaração Universal dos Direitos Humanos (1948, ONU) reconhece direitos inalienáveis a todos os seres humanos. A Constituição Brasileira de 1988 garante: educação, saúde, moradia, trabalho e liberdade. Cidadania é o conjunto de direitos civis, políticos e sociais exercidos pelo indivíduo na sociedade.",
        "perguntas": [
            {"enunciado": "Em que ano foi criada a Declaração Universal dos Direitos Humanos?", "opcoes": ["1945","1948","1950","1960"], "resposta": "1948", "dica": "Logo após a 2ª Guerra Mundial, em 1948."},
            {"enunciado": "Qual órgão criou a Declaração Universal dos Direitos Humanos?", "opcoes": ["OEA","OTAN","ONU","UNESCO"], "resposta": "ONU", "dica": "Organização das Nações Unidas."},
            {"enunciado": "A Constituição Brasileira de 1988 é chamada de:", "opcoes": ["Constituição do Império","Constituição Cidadã","Constituição Militar","Constituição Provisória"], "resposta": "Constituição Cidadã", "dica": "Ampliou direitos — por isso 'Cidadã'."},
            {"enunciado": "Cidadania plena envolve direitos:", "opcoes": ["Apenas políticos","Apenas civis","Civis, políticos e sociais","Apenas econômicos"], "resposta": "Civis, políticos e sociais", "dica": "Cidadania = conjunto de direitos civis, políticos e sociais."},
        ]},
}

# ── SIMULADO ENEM ───────────────────────────────────────────
LICOES_ENEM = {
    1: {"titulo": "Linguagens e Códigos", "texto": "O ENEM avalia linguagem verbal e não-verbal, intertextualidade, ironia, metáfora, paródia e textos multimodais. A intertextualidade ocorre quando um texto faz referência a outro. Metáfora = comparação implícita. Paródia = imitação crítica ou humorística. Eufemismo = suavização de algo negativo.",
        "perguntas": [
            {"enunciado": "O que é intertextualidade?", "opcoes": ["Erro gramatical","Quando um texto referencia outro texto","Tipo de linguagem não-verbal","Técnica de redação"], "resposta": "Quando um texto referencia outro texto", "dica": "Inter = entre textos."},
            {"enunciado": "Paródia é:", "opcoes": ["Cópia fiel de um texto","Imitação com intenção crítica ou humorística","Tradução literal","Resumo de outro texto"], "resposta": "Imitação com intenção crítica ou humorística", "dica": "Paródia transforma o original com humor ou crítica."},
            {"enunciado": "Textos multimodais combinam:", "opcoes": ["Apenas texto escrito","Linguagem verbal e não-verbal","Apenas imagens","Texto e música somente"], "resposta": "Linguagem verbal e não-verbal", "dica": "Multi = múltiplos modos de comunicação."},
            {"enunciado": "Qual figura de linguagem usa comparação implícita (sem 'como')?", "opcoes": ["Ironia","Metáfora","Antítese","Eufemismo"], "resposta": "Metáfora", "dica": "Metáfora = comparação direta, sem usar 'como' ou 'parece'."},
        ]},
    2: {"titulo": "Ciências Humanas — Conceitos chave", "texto": "O ENEM aborda: globalização (integração econômica, cultural e política mundial), sustentabilidade (atender necessidades atuais sem comprometer o futuro), desigualdade social, tecnologia e democracia. O Brasil é o 5º maior país do mundo em área e tem a maior biodiversidade do planeta.",
        "perguntas": [
            {"enunciado": "O que é globalização?", "opcoes": ["Isolamento econômico","Integração econômica, cultural e política mundial","Comércio nacional","Unificação das línguas"], "resposta": "Integração econômica, cultural e política mundial", "dica": "Global = mundial; globalização = integração."},
            {"enunciado": "Sustentabilidade significa:", "opcoes": ["Preservar só o ambiente","Usar recursos sem preocupação","Atender necessidades presentes sem comprometer o futuro","Proibir desenvolvimento"], "resposta": "Atender necessidades presentes sem comprometer o futuro", "dica": "Desenvolvimento sustentável = equilíbrio."},
            {"enunciado": "O Brasil ocupa qual posição entre os maiores países em área?", "opcoes": ["3º","4º","5º","6º"], "resposta": "5º", "dica": "O texto informa a posição."},
            {"enunciado": "Qual é o maior bioma brasileiro em área?", "opcoes": ["Cerrado","Caatinga","Amazônia","Mata Atlântica"], "resposta": "Amazônia", "dica": "A Amazônia ocupa cerca de 50% do território brasileiro."},
        ]},
    3: {"titulo": "Ciências da Natureza — Conceitos chave", "texto": "O ENEM exige: energia (cinética = mv²/2; potencial gravitacional = mgh), ondas (v = f·λ), estados da matéria, célula (procarionte × eucarionte), ecologia (cadeias alimentares, biomas) e saúde (doenças, prevenção). Mudanças de estado: fusão (sólido→líquido), vaporização (líquido→gasoso), sublimação (sólido→gasoso).",
        "perguntas": [
            {"enunciado": "Qual é a maior biodiversidade entre os biomas brasileiros?", "opcoes": ["Cerrado","Caatinga","Amazônia","Mata Atlântica"], "resposta": "Amazônia", "dica": "A Amazônia abriga ~10% das espécies do planeta."},
            {"enunciado": "Células sem núcleo definido são:", "opcoes": ["Eucariontes","Procariontes","Vegetais","Animais"], "resposta": "Procariontes", "dica": "Bactérias são procariontes."},
            {"enunciado": "Mudança do estado sólido diretamente para gasoso é:", "opcoes": ["Fusão","Evaporação","Sublimação","Condensação"], "resposta": "Sublimação", "dica": "Gelo seco sublima diretamente."},
            {"enunciado": "A energia cinética de um objeto depende de:", "opcoes": ["Sua posição","Sua temperatura","Sua velocidade e massa","Sua cor"], "resposta": "Sua velocidade e massa", "dica": "Ec = m·v²/2."},
        ]},
    4: {"titulo": "Matemática ENEM — Problemas contextualizados", "texto": "O ENEM privilegia resolução de problemas contextualizados. Exige: regra de três, porcentagem, juros (simples: J = C·i·t; compostos: M = C·(1+i)^t), funções, geometria e estatística. A calculadora não é permitida. Gerencie o tempo: ~1min 50s por questão.",
        "perguntas": [
            {"enunciado": "Para fazer 3 bolos usa-se 6 ovos. Quantos para 5 bolos?", "opcoes": ["8","9","10","12"], "resposta": "10", "dica": "Regra de 3: 3/6 = 5/x → x = 10."},
            {"enunciado": "Produto de R$ 200,00 com desconto de 15%. Preço final:", "opcoes": ["R$ 170,00","R$ 185,00","R$ 150,00","R$ 190,00"], "resposta": "R$ 170,00", "dica": "200 − (15% × 200) = 200 − 30 = 170."},
            {"enunciado": "Juros simples: 2% ao mês sobre R$ 1.000,00 em 3 meses:", "opcoes": ["R$ 20,00","R$ 60,00","R$ 600,00","R$ 1.060,00"], "resposta": "R$ 60,00", "dica": "J = C·i·t = 1000 × 0,02 × 3 = 60."},
            {"enunciado": "Terreno quadrado com área de 400 m². Lado?", "opcoes": ["20 m","40 m","100 m","200 m"], "resposta": "20 m", "dica": "Área = lado² → lado = √400 = 20 m."},
        ]},
    5: {"titulo": "Estratégias e simulado final", "texto": "Dicas para o ENEM: leia o enunciado inteiro antes das alternativas; elimine alternativas claramente erradas; gerencie o tempo (~1min 50s por questão); não deixe questões em branco (chute na dúvida — não há desconto); faça a redação com cuidado (vale 1000 pontos). O ENEM tem 2 dias com 90 questões cada + redação no 2º dia.",
        "perguntas": [
            {"enunciado": "Tempo médio por questão no ENEM:", "opcoes": ["1 minuto","1 min 50 s","2 min 30 s","3 minutos"], "resposta": "1 min 50 s", "dica": "330 min ÷ 180 questões ≈ 1 min 50 s."},
            {"enunciado": "Boa estratégia para questões difíceis:", "opcoes": ["Começar por elas","Eliminar alternativas erradas e depois escolher","Deixar em branco","Responder aleatoriamente"], "resposta": "Eliminar alternativas erradas e depois escolher", "dica": "Eliminação aumenta a probabilidade de acerto."},
            {"enunciado": "Quantas questões o ENEM tem por dia de prova?", "opcoes": ["45","90","180","360"], "resposta": "90", "dica": "São 2 dias × 90 questões + redação no 2º dia."},
            {"enunciado": "Deixar questão em branco no ENEM:", "opcoes": ["Desconta pontos","É igual a errar — não há desconto","Zera a nota","É proibido"], "resposta": "É igual a errar — não há desconto", "dica": "No ENEM não há desconto por erro. Chute se necessário!"},
        ]},
}

# ── ÍNDICE GERAL ────────────────────────────────────────────
MODULOS_MEDIO = {
    "redacao":    {"titulo": "Redação ENEM",   "icone": "✍️",  "cor": "#00C9A7", "licoes": LICOES_REDACAO},
    "matematica": {"titulo": "Matemática",     "icone": "📐",  "cor": "#F4A261", "licoes": LICOES_MATEMATICA},
    "fisica":     {"titulo": "Física",         "icone": "⚡",  "cor": "#F87171", "licoes": LICOES_FISICA},
    "quimica":    {"titulo": "Química",        "icone": "⚗️",  "cor": "#4ADE80", "licoes": LICOES_QUIMICA},
    "biologia":   {"titulo": "Biologia",       "icone": "🧬",  "cor": "#9B72CF", "licoes": LICOES_BIOLOGIA},
    "filosofia":  {"titulo": "Filosofia",      "icone": "🏛️",  "cor": "#FFD166", "licoes": LICOES_FILOSOFIA},
    "enem":       {"titulo": "Simulado ENEM",  "icone": "🎯",  "cor": "#E76F51", "licoes": LICOES_ENEM},
}
