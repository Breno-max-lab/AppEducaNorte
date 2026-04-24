"""
Conteúdo do Módulo Visual — para pessoas que não sabem ler.
Todas as atividades usam emojis grandes, cores e voz.
Sem texto para leitura — apenas reconhecimento visual e auditivo.
"""

# ─────────────────────────────────────────────
# Atividades de CONTAGEM (matemática visual)
# ─────────────────────────────────────────────

ATIVIDADES_CONTAGEM = {
    1: {
        "titulo": "Contar peixes",
        "instrucao_voz": "Quantos peixes você vê?",
        "instrucao_visual": "Quantos peixes você vê?",
        "perguntas": [
            {
                "visual": "🐟",
                "quantidade_real": 1,
                "opcoes_visuais": ["1️⃣", "2️⃣", "3️⃣"],
                "opcoes_valores": [1, 2, 3],
                "resposta": 1,
                "voz_acerto": "Isso mesmo! Um peixe!",
                "voz_erro": "Olhe de novo. Conte com o dedo.",
            },
            {
                "visual": "🐟🐟",
                "quantidade_real": 2,
                "opcoes_visuais": ["1️⃣", "2️⃣", "3️⃣"],
                "opcoes_valores": [1, 2, 3],
                "resposta": 2,
                "voz_acerto": "Muito bem! Dois peixes!",
                "voz_erro": "Tente de novo. São dois peixes.",
            },
            {
                "visual": "🐟🐟🐟",
                "quantidade_real": 3,
                "opcoes_visuais": ["1️⃣", "2️⃣", "3️⃣"],
                "opcoes_valores": [1, 2, 3],
                "resposta": 3,
                "voz_acerto": "Parabéns! Três peixes!",
                "voz_erro": "Conte um por um. São três peixes.",
            },
        ]
    },
    2: {
        "titulo": "Contar frutas do mato",
        "instrucao_voz": "Quantas frutas você vê?",
        "instrucao_visual": "Quantas frutas você vê?",
        "perguntas": [
            {
                "visual": "🍌🍌🍌🍌",
                "quantidade_real": 4,
                "opcoes_visuais": ["3️⃣", "4️⃣", "5️⃣"],
                "opcoes_valores": [3, 4, 5],
                "resposta": 4,
                "voz_acerto": "Certo! Quatro bananas!",
                "voz_erro": "Conte com calma. São quatro.",
            },
            {
                "visual": "🍊🍊🍊🍊🍊",
                "quantidade_real": 5,
                "opcoes_visuais": ["4️⃣", "5️⃣", "6️⃣"],
                "opcoes_valores": [4, 5, 6],
                "resposta": 5,
                "voz_acerto": "Isso! Cinco laranjas!",
                "voz_erro": "Tente de novo. São cinco.",
            },
        ]
    },
}

# ─────────────────────────────────────────────
# Atividades de IDENTIFICAÇÃO (o que é isso?)
# ─────────────────────────────────────────────

ATIVIDADES_IDENTIFICACAO = {
    1: {
        "titulo": "Animais do rio",
        "instrucao_voz": "Toque no boto, o golfinho rosado do rio.",
        "instrucao_visual": "Toque no boto 🐬",
        "perguntas": [
            {
                "pergunta_voz": "Qual desses é o boto, o golfinho do rio?",
                "pergunta_visual": "Qual é o boto?",
                "opcoes": [
                    {"emoji": "🐊", "nome": "jacaré", "correto": False},
                    {"emoji": "🐬", "nome": "boto", "correto": True},
                    {"emoji": "🐢", "nome": "tartaruga", "correto": False},
                ],
                "voz_acerto": "Isso! O boto é o golfinho rosado do rio Amazonas!",
                "voz_erro": "Não é esse. O boto parece um golfinho.",
            },
            {
                "pergunta_voz": "Qual desses é o pirarucu, o maior peixe do rio?",
                "pergunta_visual": "Qual é o pirarucu?",
                "opcoes": [
                    {"emoji": "🦜", "nome": "arara", "correto": False},
                    {"emoji": "🦋", "nome": "borboleta", "correto": False},
                    {"emoji": "🐟", "nome": "pirarucu", "correto": True},
                ],
                "voz_acerto": "Muito bem! O pirarucu é o maior peixe de água doce!",
                "voz_erro": "Esse não é. O pirarucu é um peixe grande.",
            },
            {
                "pergunta_voz": "Qual desses é a arara, o pássaro colorido da floresta?",
                "pergunta_visual": "Qual é a arara?",
                "opcoes": [
                    {"emoji": "🦜", "nome": "arara", "correto": True},
                    {"emoji": "🐸", "nome": "sapo", "correto": False},
                    {"emoji": "🐟", "nome": "peixe", "correto": False},
                ],
                "voz_acerto": "Parabéns! A arara é um lindo pássaro da Amazônia!",
                "voz_erro": "Olhe de novo. A arara é um pássaro colorido.",
            },
        ]
    },
    2: {
        "titulo": "Plantas da floresta",
        "instrucao_voz": "Vamos conhecer as plantas da nossa floresta!",
        "instrucao_visual": "Plantas da floresta 🌿",
        "perguntas": [
            {
                "pergunta_voz": "Qual desses é o açaí, a frutinha roxa que a gente come?",
                "pergunta_visual": "Qual é o açaí?",
                "opcoes": [
                    {"emoji": "🍇", "nome": "açaí", "correto": True},
                    {"emoji": "🌵", "nome": "cacto", "correto": False},
                    {"emoji": "🍄", "nome": "cogumelo", "correto": False},
                ],
                "voz_acerto": "Isso mesmo! O açaí é uma fruta roxa muito nutritiva!",
                "voz_erro": "Não é esse. O açaí parece uma uva roxa pequena.",
            },
            {
                "pergunta_voz": "Qual desses é o sol que dá energia pras plantas crescerem?",
                "pergunta_visual": "O que faz as plantas crescerem?",
                "opcoes": [
                    {"emoji": "🌧️", "nome": "chuva", "correto": False},
                    {"emoji": "☀️", "nome": "sol", "correto": True},
                    {"emoji": "🌙", "nome": "lua", "correto": False},
                ],
                "voz_acerto": "Muito bem! O sol dá energia para as plantas e para nós!",
                "voz_erro": "Tente de novo. Pense no que aquece e ilumina de dia.",
            },
        ]
    },
}

# ─────────────────────────────────────────────
# Atividades de COMPARAÇÃO (maior/menor, igual)
# ─────────────────────────────────────────────

ATIVIDADES_COMPARACAO = {
    1: {
        "titulo": "Qual tem mais?",
        "instrucao_voz": "Toque no grupo que tem mais!",
        "instrucao_visual": "Qual grupo tem mais? 👆",
        "perguntas": [
            {
                "pergunta_voz": "Qual lado tem mais peixes?",
                "opcoes": [
                    {"visual": "🐟🐟", "valor": 2, "correto": False},
                    {"visual": "🐟🐟🐟🐟", "valor": 4, "correto": True},
                ],
                "voz_acerto": "Certo! Quatro é mais que dois!",
                "voz_erro": "Conte os dois lados. Um lado tem mais.",
            },
            {
                "pergunta_voz": "Qual lado tem mais árvores?",
                "opcoes": [
                    {"visual": "🌳🌳🌳", "valor": 3, "correto": False},
                    {"visual": "🌳🌳🌳🌳🌳", "valor": 5, "correto": True},
                ],
                "voz_acerto": "Isso! Cinco árvores é mais que três!",
                "voz_erro": "Olhe bem os dois lados.",
            },
            {
                "pergunta_voz": "Qual lado tem mais estrelas?",
                "opcoes": [
                    {"visual": "⭐⭐⭐⭐⭐⭐", "valor": 6, "correto": True},
                    {"visual": "⭐⭐⭐", "valor": 3, "correto": False},
                ],
                "voz_acerto": "Parabéns! Seis é mais que três!",
                "voz_erro": "Conte com cuidado os dois lados.",
            },
        ]
    },
}
