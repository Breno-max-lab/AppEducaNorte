"""
Conteúdo do Módulo Infantil — EducaNorte
Atividades para crianças em processo de alfabetização.
Interface baseada em imagens, sons e interação visual.
"""

# ─────────────────────────────────────────────
# LETRAS E SONS
# ─────────────────────────────────────────────

ATIVIDADES_LETRAS = {
    1: {
        "titulo": "Vogais",
        "instrucao": "Toque na letra que você ouve!",
        "voz": "Vamos aprender as vogais!",
        "perguntas": [
            {
                "voz": "A de Água!",
                "visual": "💧",
                "letra_alvo": "A",
                "opcoes": ["A", "E", "O"],
                "resposta": "A",
                "voz_acerto": "Isso! A de Água!",
                "voz_erro":   "Não foi essa. É a letra A!",
            },
            {
                "voz": "E de Estrela!",
                "visual": "⭐",
                "letra_alvo": "E",
                "opcoes": ["I", "E", "U"],
                "resposta": "E",
                "voz_acerto": "Muito bem! E de Estrela!",
                "voz_erro":   "Olhe bem! É a letra E.",
            },
            {
                "voz": "I de Ilha!",
                "visual": "🏝️",
                "letra_alvo": "I",
                "opcoes": ["A", "O", "I"],
                "resposta": "I",
                "voz_acerto": "Parabéns! I de Ilha!",
                "voz_erro":   "É a letra I, olhe de novo!",
            },
            {
                "voz": "O de Onça!",
                "visual": "🐆",
                "letra_alvo": "O",
                "opcoes": ["O", "U", "E"],
                "resposta": "O",
                "voz_acerto": "Ótimo! O de Onça!",
                "voz_erro":   "Tente de novo! É a letra O.",
            },
            {
                "voz": "U de Uirapuru!",
                "visual": "🐦",
                "letra_alvo": "U",
                "opcoes": ["A", "U", "I"],
                "resposta": "U",
                "voz_acerto": "Excelente! U de Uirapuru!",
                "voz_erro":   "É a letra U! Tente mais uma vez.",
            },
        ]
    },
    2: {
        "titulo": "Consoantes do rio",
        "instrucao": "Qual letra começa essa palavra?",
        "voz": "Vamos aprender as letras!",
        "perguntas": [
            {
                "voz": "B de Boto!",
                "visual": "🐬",
                "letra_alvo": "B",
                "opcoes": ["B", "P", "D"],
                "resposta": "B",
                "voz_acerto": "Isso! B de Boto!",
                "voz_erro":   "É a letra B! Bo-to.",
            },
            {
                "voz": "P de Peixe!",
                "visual": "🐟",
                "letra_alvo": "P",
                "opcoes": ["F", "P", "V"],
                "resposta": "P",
                "voz_acerto": "Muito bem! P de Peixe!",
                "voz_erro":   "É a letra P! Pei-xe.",
            },
            {
                "voz": "R de Rio!",
                "visual": "🏞️",
                "letra_alvo": "R",
                "opcoes": ["R", "L", "N"],
                "resposta": "R",
                "voz_acerto": "Parabéns! R de Rio!",
                "voz_erro":   "É a letra R! Ri-o.",
            },
            {
                "voz": "C de Canoa!",
                "visual": "🛶",
                "letra_alvo": "C",
                "opcoes": ["G", "C", "Q"],
                "resposta": "C",
                "voz_acerto": "Ótimo! C de Canoa!",
                "voz_erro":   "É a letra C! Ca-no-a.",
            },
        ]
    },
    3: {
        "titulo": "Sílabas simples",
        "instrucao": "Quantas partes tem essa palavra?",
        "voz": "Vamos bater palmas para cada sílaba!",
        "perguntas": [
            {
                "voz": "Bata palmas para: RIO",
                "visual": "🏞️",
                "letra_alvo": "2",
                "opcoes": ["1", "2", "3"],
                "resposta": "2",
                "voz_acerto": "Isso! Ri-o, duas partes!",
                "voz_erro":   "Tente de novo: Ri (palma) - o (palma). São 2!",
            },
            {
                "voz": "Bata palmas para: BOTO",
                "visual": "🐬",
                "letra_alvo": "2",
                "opcoes": ["1", "2", "3"],
                "resposta": "2",
                "voz_acerto": "Muito bem! Bo-to, duas partes!",
                "voz_erro":   "Bo (palma) - to (palma). São 2!",
            },
            {
                "voz": "Bata palmas para: CANOA",
                "visual": "🛶",
                "letra_alvo": "3",
                "opcoes": ["2", "3", "4"],
                "resposta": "3",
                "voz_acerto": "Ótimo! Ca-no-a, três partes!",
                "voz_erro":   "Ca (palma) - no (palma) - a (palma). São 3!",
            },
        ]
    },
}

# ─────────────────────────────────────────────
# NÚMEROS E CONTAGEM
# ─────────────────────────────────────────────

ATIVIDADES_NUMEROS = {
    1: {
        "titulo": "Contar até 5",
        "instrucao": "Quantos você vê?",
        "voz": "Vamos contar juntos!",
        "perguntas": [
            {
                "voz": "Quantos peixes você vê?",
                "visual": "🐟",
                "quantidade": 1,
                "opcoes": ["1", "2", "3"],
                "resposta": "1",
                "voz_acerto": "Isso! Um peixe!",
                "voz_erro":   "Conte com o dedo. É 1!",
            },
            {
                "voz": "Quantas estrelas você vê?",
                "visual": "⭐⭐",
                "quantidade": 2,
                "opcoes": ["1", "2", "3"],
                "resposta": "2",
                "voz_acerto": "Muito bem! Duas estrelas!",
                "voz_erro":   "Conta: uma, duas. São 2!",
            },
            {
                "voz": "Quantos botos você vê?",
                "visual": "🐬🐬🐬",
                "quantidade": 3,
                "opcoes": ["2", "3", "4"],
                "resposta": "3",
                "voz_acerto": "Parabéns! Três botos!",
                "voz_erro":   "Um, dois, três. São 3!",
            },
            {
                "voz": "Quantas árvores você vê?",
                "visual": "🌳🌳🌳🌳",
                "quantidade": 4,
                "opcoes": ["3", "4", "5"],
                "resposta": "4",
                "voz_acerto": "Ótimo! Quatro árvores!",
                "voz_erro":   "Conta devagar: 1,2,3,4. São 4!",
            },
            {
                "voz": "Quantos pássaros você vê?",
                "visual": "🦜🦜🦜🦜🦜",
                "quantidade": 5,
                "opcoes": ["4", "5", "6"],
                "resposta": "5",
                "voz_acerto": "Excelente! Cinco pássaros!",
                "voz_erro":   "1,2,3,4,5. São 5!",
            },
        ]
    },
    2: {
        "titulo": "Contar até 10",
        "instrucao": "Conta e toque no número certo!",
        "voz": "Agora vamos contar até dez!",
        "perguntas": [
            {
                "voz": "Quantos peixes?",
                "visual": "🐟🐟🐟🐟🐟🐟",
                "quantidade": 6,
                "opcoes": ["5", "6", "7"],
                "resposta": "6",
                "voz_acerto": "Isso! Seis peixes!",
                "voz_erro":   "Conta um por um. São 6!",
            },
            {
                "voz": "Quantas frutas?",
                "visual": "🍌🍌🍌🍌🍌🍌🍌",
                "quantidade": 7,
                "opcoes": ["6", "7", "8"],
                "resposta": "7",
                "voz_acerto": "Muito bem! Sete bananas!",
                "voz_erro":   "Conta com calma. São 7!",
            },
            {
                "voz": "Quantas conchas?",
                "visual": "🐚🐚🐚🐚🐚🐚🐚🐚",
                "quantidade": 8,
                "opcoes": ["7", "8", "9"],
                "resposta": "8",
                "voz_acerto": "Parabéns! Oito conchas!",
                "voz_erro":   "1 a 8. São 8!",
            },
            {
                "voz": "Quantas flores?",
                "visual": "🌺🌺🌺🌺🌺🌺🌺🌺🌺",
                "quantidade": 9,
                "opcoes": ["8", "9", "10"],
                "resposta": "9",
                "voz_acerto": "Ótimo! Nove flores!",
                "voz_erro":   "Conta cada uma. São 9!",
            },
        ]
    },
    3: {
        "titulo": "Mais ou menos?",
        "instrucao": "Qual grupo tem MAIS?",
        "voz": "Qual lado tem mais?",
        "perguntas": [
            {
                "voz": "Qual lado tem mais peixes?",
                "visual_a": "🐟🐟",
                "visual_b": "🐟🐟🐟🐟",
                "qtd_a": 2, "qtd_b": 4,
                "resposta": "B",
                "voz_acerto": "Isso! Quatro é mais que dois!",
                "voz_erro":   "O lado com 4 tem mais!",
                "tipo": "comparacao",
            },
            {
                "voz": "Qual lado tem mais estrelas?",
                "visual_a": "⭐⭐⭐⭐⭐",
                "visual_b": "⭐⭐⭐",
                "qtd_a": 5, "qtd_b": 3,
                "resposta": "A",
                "voz_acerto": "Muito bem! Cinco é mais que três!",
                "voz_erro":   "O lado com 5 tem mais!",
                "tipo": "comparacao",
            },
            {
                "voz": "Qual lado tem mais árvores?",
                "visual_a": "🌳🌳🌳",
                "visual_b": "🌳🌳🌳🌳🌳🌳",
                "qtd_a": 3, "qtd_b": 6,
                "resposta": "B",
                "voz_acerto": "Parabéns! Seis é mais que três!",
                "voz_erro":   "O lado com 6 tem mais!",
                "tipo": "comparacao",
            },
        ]
    },
}

# ─────────────────────────────────────────────
# ANIMAIS DA AMAZÔNIA
# ─────────────────────────────────────────────

ATIVIDADES_ANIMAIS = {
    1: {
        "titulo": "Animais do rio",
        "instrucao": "Toque no animal certo!",
        "voz": "Vamos conhecer os animais!",
        "perguntas": [
            {
                "voz": "Onde está o BOTO, o golfinho rosado?",
                "opcoes": [
                    {"emoji": "🐬", "nome": "Boto",     "correto": True},
                    {"emoji": "🐊", "nome": "Jacaré",   "correto": False},
                    {"emoji": "🐢", "nome": "Tartaruga","correto": False},
                ],
                "voz_acerto": "Isso! O boto é o golfinho rosado do rio Amazonas!",
                "voz_erro":   "Não é esse! O boto parece um golfinho.",
            },
            {
                "voz": "Onde está o JACARÉ?",
                "opcoes": [
                    {"emoji": "🐟", "nome": "Peixe",  "correto": False},
                    {"emoji": "🐊", "nome": "Jacaré", "correto": True},
                    {"emoji": "🐬", "nome": "Boto",   "correto": False},
                ],
                "voz_acerto": "Muito bem! O jacaré vive nos rios da Amazônia!",
                "voz_erro":   "Esse não é o jacaré. Tente de novo!",
            },
            {
                "voz": "Onde está o PIRARUCU, o maior peixe do rio?",
                "opcoes": [
                    {"emoji": "🦋", "nome": "Borboleta", "correto": False},
                    {"emoji": "🐟", "nome": "Pirarucu",  "correto": True},
                    {"emoji": "🦜", "nome": "Arara",     "correto": False},
                ],
                "voz_acerto": "Parabéns! O pirarucu é o maior peixe de água doce!",
                "voz_erro":   "O pirarucu é um peixe grande. Tente de novo!",
            },
        ]
    },
    2: {
        "titulo": "Animais da floresta",
        "instrucao": "Toque no animal que você ouvir!",
        "voz": "Agora vamos ver os animais da floresta!",
        "perguntas": [
            {
                "voz": "Onde está a ARARA, o pássaro colorido?",
                "opcoes": [
                    {"emoji": "🦜", "nome": "Arara",   "correto": True},
                    {"emoji": "🐸", "nome": "Sapo",    "correto": False},
                    {"emoji": "🦁", "nome": "Leão",    "correto": False},
                ],
                "voz_acerto": "Isso! A arara é um lindo pássaro da Amazônia!",
                "voz_erro":   "A arara é um pássaro colorido. Tente de novo!",
            },
            {
                "voz": "Onde está a ONÇA PINTADA?",
                "opcoes": [
                    {"emoji": "🐆", "nome": "Onça",   "correto": True},
                    {"emoji": "🐘", "nome": "Elefante","correto": False},
                    {"emoji": "🦒", "nome": "Girafa",  "correto": False},
                ],
                "voz_acerto": "Muito bem! A onça pintada é o maior felino do Brasil!",
                "voz_erro":   "A onça tem manchas. Tente de novo!",
            },
            {
                "voz": "Onde está o MACACO?",
                "opcoes": [
                    {"emoji": "🐍", "nome": "Cobra",  "correto": False},
                    {"emoji": "🐒", "nome": "Macaco", "correto": True},
                    {"emoji": "🦅", "nome": "Águia",  "correto": False},
                ],
                "voz_acerto": "Parabéns! Os macacos vivem nas árvores da floresta!",
                "voz_erro":   "O macaco pula nas árvores. Tente de novo!",
            },
        ]
    },
}

# ─────────────────────────────────────────────
# CORES E FORMAS
# ─────────────────────────────────────────────

ATIVIDADES_CORES = {
    1: {
        "titulo": "Cores da natureza",
        "instrucao": "Toque na cor certa!",
        "voz": "Vamos aprender as cores!",
        "perguntas": [
            {
                "voz": "Qual é a cor do céu?",
                "visual": "☁️🌤️",
                "opcoes": [
                    {"cor": "#2196F3", "nome": "Azul",    "correto": True},
                    {"cor": "#4CAF50", "nome": "Verde",   "correto": False},
                    {"cor": "#FF5722", "nome": "Laranja", "correto": False},
                ],
                "voz_acerto": "Isso! O céu é azul!",
                "voz_erro":   "O céu é azul! Tente de novo.",
            },
            {
                "voz": "Qual é a cor da floresta?",
                "visual": "🌿🌳",
                "opcoes": [
                    {"cor": "#F44336", "nome": "Vermelho","correto": False},
                    {"cor": "#4CAF50", "nome": "Verde",   "correto": True},
                    {"cor": "#9C27B0", "nome": "Roxo",    "correto": False},
                ],
                "voz_acerto": "Muito bem! A floresta é verde!",
                "voz_erro":   "A floresta é verde! Olhe as folhas.",
            },
            {
                "voz": "Qual é a cor do sol?",
                "visual": "☀️",
                "opcoes": [
                    {"cor": "#FFEB3B", "nome": "Amarelo", "correto": True},
                    {"cor": "#2196F3", "nome": "Azul",    "correto": False},
                    {"cor": "#9C27B0", "nome": "Roxo",    "correto": False},
                ],
                "voz_acerto": "Ótimo! O sol é amarelo!",
                "voz_erro":   "O sol é amarelo! Tente de novo.",
            },
            {
                "voz": "Qual é a cor do rio?",
                "visual": "🌊💧",
                "opcoes": [
                    {"cor": "#FF5722", "nome": "Laranja", "correto": False},
                    {"cor": "#4CAF50", "nome": "Verde",   "correto": False},
                    {"cor": "#2196F3", "nome": "Azul",    "correto": True},
                ],
                "voz_acerto": "Parabéns! O rio é azul!",
                "voz_erro":   "O rio é azul como a água!",
            },
        ]
    },
}

# ─────────────────────────────────────────────
# ÍNDICE GERAL
# ─────────────────────────────────────────────

MODULOS_INFANTIL = {
    "letras":  {"titulo": "Letras e Sons",    "icone": "🔤", "cor": "#FFD166", "atividades": ATIVIDADES_LETRAS},
    "numeros": {"titulo": "Números",           "icone": "🔢", "cor": "#00C9A7", "atividades": ATIVIDADES_NUMEROS},
    "animais": {"titulo": "Animais",           "icone": "🐬", "cor": "#F4A261", "atividades": ATIVIDADES_ANIMAIS},
    "cores":   {"titulo": "Cores da Natureza", "icone": "🎨", "cor": "#9B72CF", "atividades": ATIVIDADES_CORES},
}
