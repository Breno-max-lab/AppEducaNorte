"""
Banco de conteúdo para o módulo de Alfabetização e Aprendizado Básico.
Adaptado ao contexto ribeirinho amazônico.
"""

LICOES_LEITURA = {
    1: {
        "titulo": "Vogais",
        "texto": "O rio é lindo. A água é boa. O peixe nada no rio.",
        "perguntas": [
            {
                "enunciado": "Qual letra começa a palavra 'rio'?",
                "opcoes": ["A", "R", "O", "I"],
                "resposta": "R",
                "dica": "Pense no som do começo da palavra: rrr-io."
            },
            {
                "enunciado": "Quantas vogais tem a palavra 'peixe'?",
                "opcoes": ["1", "2", "3", "4"],
                "resposta": "3",
                "dica": "As vogais são: a, e, i, o, u. Procure cada uma em 'peixe'."
            },
            {
                "enunciado": "Qual palavra rima com 'rio'?",
                "opcoes": ["pato", "frio", "boto", "canoa"],
                "resposta": "frio",
                "dica": "Rimar é ter o mesmo som no final: ri-o, fri-o."
            }
        ]
    },
    2: {
        "titulo": "Sílabas simples",
        "texto": "A canoa vai no rio. O boto pula na água. A criança vê o ninho.",
        "perguntas": [
            {
                "enunciado": "Quantas sílabas tem a palavra 'ca-no-a'?",
                "opcoes": ["1", "2", "3", "4"],
                "resposta": "3",
                "dica": "Bata palmas para cada pedaço: ca (palma) - no (palma) - a (palma)."
            },
            {
                "enunciado": "Qual sílaba está no meio de 'boto'?",
                "opcoes": ["bo", "to", "ot", "ob"],
                "resposta": "to",
                "dica": "Separe a palavra: bo-to. A segunda parte é..."
            },
            {
                "enunciado": "Qual palavra tem 2 sílabas?",
                "opcoes": ["rio", "criança", "boto", "água"],
                "resposta": "boto",
                "dica": "Conte: bo-to = 2 sílabas."
            }
        ]
    },
    3: {
        "titulo": "Leitura de frases",
        "texto": "O pescador acorda cedo. Ele pega a rede e vai ao rio. Os peixes estão nadando perto da margem.",
        "perguntas": [
            {
                "enunciado": "O que o pescador pega antes de ir ao rio?",
                "opcoes": ["o anzol", "a rede", "a canoa", "o chapéu"],
                "resposta": "a rede",
                "dica": "Releia a segunda frase do texto."
            },
            {
                "enunciado": "Quando o pescador acorda?",
                "opcoes": ["tarde", "à noite", "cedo", "ao meio-dia"],
                "resposta": "cedo",
                "dica": "A resposta está na primeira frase."
            },
            {
                "enunciado": "Onde os peixes estão nadando?",
                "opcoes": ["no fundo", "no meio do rio", "perto da margem", "na superfície"],
                "resposta": "perto da margem",
                "dica": "Leia a última frase com atenção."
            }
        ]
    }
}

LICOES_MATEMATICA = {
    1: {
        "titulo": "Contagem com objetos do rio",
        "contexto": "Vamos contar usando coisas do nosso rio!",
        "perguntas": [
            {
                "enunciado": "O pescador pegou 3 peixes de manhã e 2 de tarde. Quantos peixes pegou no total?",
                "opcoes": ["4", "5", "6", "3"],
                "resposta": "5",
                "dica": "Some os peixes da manhã com os da tarde: 3 + 2 = ?"
            },
            {
                "enunciado": "Havia 8 pássaros na árvore. 3 voaram. Quantos ficaram?",
                "opcoes": ["4", "5", "6", "11"],
                "resposta": "5",
                "dica": "Tire os que foram embora: 8 - 3 = ?"
            },
            {
                "enunciado": "Ana tem 4 conchas e João tem 4 conchas. Quantas conchas eles têm juntos?",
                "opcoes": ["6", "7", "8", "9"],
                "resposta": "8",
                "dica": "4 + 4 = ?"
            }
        ]
    },
    2: {
        "titulo": "Números até 20",
        "contexto": "Agora vamos trabalhar com números maiores!",
        "perguntas": [
            {
                "enunciado": "Qual número vem depois do 15?",
                "opcoes": ["14", "16", "17", "13"],
                "resposta": "16",
                "dica": "Na sequência: ...14, 15, ?, 17..."
            },
            {
                "enunciado": "Qual é o maior número: 9, 12, 7 ou 18?",
                "opcoes": ["9", "12", "7", "18"],
                "resposta": "18",
                "dica": "O maior número é o que tem mais unidades."
            },
            {
                "enunciado": "10 + 5 = ?",
                "opcoes": ["14", "15", "16", "5"],
                "resposta": "15",
                "dica": "Comece do 10 e conte mais 5."
            }
        ]
    },
    3: {
        "titulo": "Problemas do cotidiano ribeirinho",
        "contexto": "Matemática no dia a dia do rio!",
        "perguntas": [
            {
                "enunciado": "Uma canoa carrega 6 pessoas. Já entraram 4. Quantas ainda podem entrar?",
                "opcoes": ["1", "2", "3", "4"],
                "resposta": "2",
                "dica": "6 - 4 = ?"
            },
            {
                "enunciado": "Maria colheu 5 açaís na segunda e 7 na terça. Quantos colheu nos dois dias?",
                "opcoes": ["10", "11", "12", "13"],
                "resposta": "12",
                "dica": "5 + 7 = ?"
            },
            {
                "enunciado": "O rio tem 3 margens com 4 árvores cada. Quantas árvores no total?",
                "opcoes": ["7", "12", "9", "8"],
                "resposta": "12",
                "dica": "Multiplicação: 3 × 4 = ? (ou some 4+4+4)"
            }
        ]
    }
}

# ─── Níveis extras de Leitura ───────────────

LICOES_LEITURA[4] = {
    "titulo": "Palavras do rio",
    "texto": "O ribeirinho acorda com o canto dos pássaros. Ele pesca com a tarrafa no rio largo. A piranha e o tucunaré nadam nas águas escuras.",
    "perguntas": [
        {
            "enunciado": "O que o ribeirinho usa para pescar?",
            "opcoes": ["anzol", "tarrafa", "rede", "caniço"],
            "resposta": "tarrafa",
            "dica": "Releia a segunda frase do texto."
        },
        {
            "enunciado": "Qual desses é um peixe citado no texto?",
            "opcoes": ["boto", "pirarucu", "tucunaré", "pacu"],
            "resposta": "tucunaré",
            "dica": "Procure os nomes de peixes na última frase."
        },
        {
            "enunciado": "Como são as águas do rio no texto?",
            "opcoes": ["cristalinas", "verdes", "escuras", "frias"],
            "resposta": "escuras",
            "dica": "A última frase descreve as águas."
        },
        {
            "enunciado": "O que acorda o ribeirinho?",
            "opcoes": ["o sol", "o canto dos pássaros", "o barulho do rio", "o vento"],
            "resposta": "o canto dos pássaros",
            "dica": "Releia a primeira frase."
        }
    ]
}

LICOES_LEITURA[5] = {
    "titulo": "Interpretação avançada",
    "texto": "A várzea é uma terra especial: quando o rio sobe, ela fica debaixo d'água. Os peixes entram na floresta alagada para comer frutos que caem das árvores. Por isso, as árvores e os peixes dependem uns dos outros.",
    "perguntas": [
        {
            "enunciado": "O que acontece com a várzea quando o rio sobe?",
            "opcoes": ["ela seca", "ela fica debaixo d'água", "ela vira ilha", "ela cresce"],
            "resposta": "ela fica debaixo d'água",
            "dica": "A resposta está na primeira parte do texto."
        },
        {
            "enunciado": "Por que os peixes entram na floresta alagada?",
            "opcoes": ["para se esconder", "para dormir", "para comer frutos", "para desovar"],
            "resposta": "para comer frutos",
            "dica": "Procure o motivo na segunda frase."
        },
        {
            "enunciado": "Qual é a ideia principal do texto?",
            "opcoes": ["os rios são perigosos", "árvores e peixes se ajudam", "a várzea é seca", "os peixes comem folhas"],
            "resposta": "árvores e peixes se ajudam",
            "dica": "Leia a última frase — ela resume tudo."
        }
    ]
}

# ─── Níveis extras de Matemática ────────────

LICOES_MATEMATICA[4] = {
    "titulo": "Multiplicação ribeirinha",
    "contexto": "Vamos resolver problemas do dia a dia do rio com multiplicação!",
    "perguntas": [
        {
            "enunciado": "Um pescador tem 4 redes. Cada rede pega 6 peixes. Quantos peixes no total?",
            "opcoes": ["20", "22", "24", "26"],
            "resposta": "24",
            "dica": "4 × 6 = ? (some 6 quatro vezes)"
        },
        {
            "enunciado": "Há 3 canoas. Cada canoa leva 5 pessoas. Quantas pessoas no total?",
            "opcoes": ["12", "15", "18", "8"],
            "resposta": "15",
            "dica": "3 × 5 = ? (some 5 três vezes)"
        },
        {
            "enunciado": "Uma árvore dá 7 frutos por semana. Quantos frutos em 4 semanas?",
            "opcoes": ["21", "24", "28", "32"],
            "resposta": "28",
            "dica": "7 × 4 = ? (some 7 quatro vezes)"
        },
        {
            "enunciado": "Se 2 × 8 = 16, quanto é 2 × 9?",
            "opcoes": ["16", "17", "18", "20"],
            "resposta": "18",
            "dica": "2 × 9 é apenas 2 a mais que 2 × 8."
        }
    ]
}

LICOES_MATEMATICA[5] = {
    "titulo": "Divisão e frações simples",
    "contexto": "Compartilhar é importante na comunidade ribeirinha!",
    "perguntas": [
        {
            "enunciado": "12 peixes divididos igualmente entre 4 famílias. Quantos cada uma recebe?",
            "opcoes": ["2", "3", "4", "6"],
            "resposta": "3",
            "dica": "12 ÷ 4 = ?"
        },
        {
            "enunciado": "Metade de 20 açaís é quanto?",
            "opcoes": ["5", "8", "10", "12"],
            "resposta": "10",
            "dica": "Metade = dividir por 2. 20 ÷ 2 = ?"
        },
        {
            "enunciado": "Uma canoa tem 8 lugares. Metade já está ocupada. Quantos lugares livres?",
            "opcoes": ["2", "3", "4", "6"],
            "resposta": "4",
            "dica": "Metade de 8 = 4 ocupados. 8 - 4 = ?"
        },
        {
            "enunciado": "18 bananas divididas entre 3 crianças. Quantas cada criança recebe?",
            "opcoes": ["4", "5", "6", "9"],
            "resposta": "6",
            "dica": "18 ÷ 3 = ?"
        }
    ]
}
