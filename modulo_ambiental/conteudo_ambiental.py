"""
Módulo de Educação Ambiental — Assistente Ribeirinho
Conteúdo sobre sustentabilidade, fauna, flora e preservação ribeirinha.
"""

LICOES_AMBIENTAL = {
    1: {
        "titulo": "O Rio e a Vida",
        "texto": "O rio Amazonas é o maior rio do mundo em volume de água. Ele abriga milhares de espécies de peixes, plantas e animais. As comunidades ribeirinhas dependem do rio para beber, pescar e se locomover.",
        "perguntas": [
            {
                "enunciado": "Por que o rio Amazonas é especial?",
                "opcoes": ["É o mais rápido", "É o maior em volume de água", "É o mais fundo", "É o mais frio"],
                "resposta": "É o maior em volume de água",
                "dica": "A resposta está na primeira frase do texto."
            },
            {
                "enunciado": "Para que as comunidades ribeirinhas usam o rio?",
                "opcoes": ["Apenas para pescar", "Apenas para beber", "Para beber, pescar e se locomover", "Apenas para nadar"],
                "resposta": "Para beber, pescar e se locomover",
                "dica": "A última frase lista os três usos."
            },
            {
                "enunciado": "O que o rio Amazonas abriga?",
                "opcoes": ["Apenas peixes", "Apenas plantas", "Milhares de espécies de peixes, plantas e animais", "Apenas animais terrestres"],
                "resposta": "Milhares de espécies de peixes, plantas e animais",
                "dica": "Releia a segunda frase."
            }
        ]
    },
    2: {
        "titulo": "Preservação das Matas",
        "texto": "A floresta amazônica regula o clima do planeta. Suas árvores absorvem gás carbônico e liberam oxigênio. O desmatamento destrói o habitat de animais e aumenta as enchentes porque o solo sem raízes não retém água.",
        "perguntas": [
            {
                "enunciado": "O que a floresta amazônica faz pelo clima?",
                "opcoes": ["Aquece o planeta", "Regula o clima do planeta", "Causa chuvas ácidas", "Não tem efeito no clima"],
                "resposta": "Regula o clima do planeta",
                "dica": "A primeira frase responde isso."
            },
            {
                "enunciado": "O que as árvores liberam no ar?",
                "opcoes": ["Gás carbônico", "Nitrogênio", "Oxigênio", "Vapor d'água"],
                "resposta": "Oxigênio",
                "dica": "As árvores absorvem CO₂ e liberam..."
            },
            {
                "enunciado": "Por que o desmatamento aumenta as enchentes?",
                "opcoes": ["Porque chove mais", "Porque o solo sem raízes não retém água", "Porque os rios ficam mais largos", "Porque o sol esquenta mais"],
                "resposta": "Porque o solo sem raízes não retém água",
                "dica": "A última parte do texto explica isso."
            },
            {
                "enunciado": "O que o desmatamento destrói?",
                "opcoes": ["Apenas rios", "O habitat dos animais", "Apenas plantas pequenas", "Apenas insetos"],
                "resposta": "O habitat dos animais",
                "dica": "A última frase menciona isso."
            }
        ]
    },
    3: {
        "titulo": "Animais Ameaçados",
        "texto": "Vários animais da Amazônia estão ameaçados de extinção por causa da caça e do desmatamento. O peixe-boi, a onça-pintada e o boto-cor-de-rosa precisam de proteção. Quando uma espécie desaparece, toda a cadeia alimentar é afetada.",
        "perguntas": [
            {
                "enunciado": "Qual desses animais está ameaçado de extinção?",
                "opcoes": ["Galinha", "Peixe-boi", "Porco", "Cachorro"],
                "resposta": "Peixe-boi",
                "dica": "O texto cita três animais ameaçados."
            },
            {
                "enunciado": "Quais são as causas da ameaça aos animais?",
                "opcoes": ["Chuva e frio", "Caça e desmatamento", "Poluição sonora", "Falta de comida natural"],
                "resposta": "Caça e desmatamento",
                "dica": "A primeira frase explica as causas."
            },
            {
                "enunciado": "O que acontece quando uma espécie desaparece?",
                "opcoes": ["Nada muda", "Toda a cadeia alimentar é afetada", "Só os predadores sofrem", "Apenas as plantas sofrem"],
                "resposta": "Toda a cadeia alimentar é afetada",
                "dica": "A última frase do texto responde isso."
            }
        ]
    },
    4: {
        "titulo": "Água Limpa e Saúde",
        "texto": "A poluição dos rios por lixo e agrotóxicos contamina a água e mata os peixes. Água poluída causa doenças graves nas pessoas. Para proteger o rio, não jogue lixo na água, não use agrotóxicos perto das margens e plante árvores nativas nas beiradas.",
        "perguntas": [
            {
                "enunciado": "O que contamina os rios?",
                "opcoes": ["Chuva forte", "Lixo e agrotóxicos", "Peixes grandes", "Vento"],
                "resposta": "Lixo e agrotóxicos",
                "dica": "A primeira frase cita os dois causadores."
            },
            {
                "enunciado": "O que água poluída causa nas pessoas?",
                "opcoes": ["Alegria", "Doenças graves", "Força extra", "Sono"],
                "resposta": "Doenças graves",
                "dica": "A segunda frase responde isso."
            },
            {
                "enunciado": "O que você pode fazer para proteger o rio?",
                "opcoes": ["Jogar lixo longe da margem", "Não jogar lixo na água", "Usar mais agrotóxicos", "Pescar todos os dias"],
                "resposta": "Não jogar lixo na água",
                "dica": "O texto lista três ações de proteção."
            }
        ]
    },
    5: {
        "titulo": "Pesca Sustentável",
        "texto": "A pesca sustentável garante que sempre haverá peixes no rio. Para isso, respeite os períodos de defeso (quando os peixes se reproduzem), não use redes com malha muito pequena e devolva peixes pequenos ao rio. Pescar só o necessário protege o futuro da comunidade.",
        "perguntas": [
            {
                "enunciado": "O que é o período de defeso?",
                "opcoes": ["Quando proibido pescar à noite", "Quando os peixes se reproduzem e a pesca é restrita", "Quando o rio está seco", "Quando os peixes migram para o mar"],
                "resposta": "Quando os peixes se reproduzem e a pesca é restrita",
                "dica": "O texto explica entre parênteses."
            },
            {
                "enunciado": "O que fazer com peixes pequenos?",
                "opcoes": ["Vender no mercado", "Guardar para comer", "Devolver ao rio", "Dar para animais"],
                "resposta": "Devolver ao rio",
                "dica": "O texto orienta sobre os peixes pequenos."
            },
            {
                "enunciado": "Por que pescar só o necessário é importante?",
                "opcoes": ["Para economizar combustível", "Para proteger o futuro da comunidade", "Para não cansar", "Para vender mais caro"],
                "resposta": "Para proteger o futuro da comunidade",
                "dica": "A última frase responde isso."
            }
        ]
    }
}
