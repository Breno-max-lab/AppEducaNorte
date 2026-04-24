"""
Módulo de Saúde e Bem-estar — Assistente Ribeirinho
Dicas preventivas adaptadas ao contexto ribeirinho amazônico.
"""

LICOES_SAUDE = {
    1: {
        "titulo": "Higiene Básica",
        "texto": "Lavar as mãos com sabão antes de comer e após usar o banheiro evita doenças. Água para beber deve ser fervida ou filtrada. Manter a casa e o entorno limpos afasta mosquitos e outros vetores de doenças.",
        "perguntas": [
            {
                "enunciado": "Quando devemos lavar as mãos com sabão?",
                "opcoes": ["Só antes de dormir", "Antes de comer e após usar o banheiro", "Apenas quando estiver com gripe", "Uma vez por dia"],
                "resposta": "Antes de comer e após usar o banheiro",
                "dica": "A primeira frase do texto responde isso."
            },
            {
                "enunciado": "Como deve ser a água para beber?",
                "opcoes": ["Diretamente do rio", "Fervida ou filtrada", "Com sal", "Gelada"],
                "resposta": "Fervida ou filtrada",
                "dica": "A segunda frase orienta sobre a água."
            },
            {
                "enunciado": "O que manter a casa limpa ajuda a afastar?",
                "opcoes": ["O frio", "Mosquitos e vetores de doenças", "Animais grandes", "A chuva"],
                "resposta": "Mosquitos e vetores de doenças",
                "dica": "A última frase do texto responde isso."
            }
        ]
    },
    2: {
        "titulo": "Doenças Tropicais",
        "texto": "A malária é transmitida pelo mosquito Anopheles e causa febre alta, calafrios e dor de cabeça. A dengue é transmitida pelo Aedes aegypti. Para se proteger: use repelente, durma com mosquiteiro, elimine água parada e procure o posto de saúde ao primeiro sinal de febre.",
        "perguntas": [
            {
                "enunciado": "Qual mosquito transmite a malária?",
                "opcoes": ["Aedes aegypti", "Anopheles", "Culex", "Pernilongo comum"],
                "resposta": "Anopheles",
                "dica": "O texto cita o nome do mosquito logo após mencionar a malária."
            },
            {
                "enunciado": "Quais são os sintomas da malária?",
                "opcoes": ["Tosse e coriza", "Febre alta, calafrios e dor de cabeça", "Manchas na pele", "Dor nos ossos"],
                "resposta": "Febre alta, calafrios e dor de cabeça",
                "dica": "O texto lista os sintomas após mencionar a malária."
            },
            {
                "enunciado": "O que fazer ao primeiro sinal de febre?",
                "opcoes": ["Tomar qualquer remédio em casa", "Esperar passar", "Procurar o posto de saúde", "Beber água gelada"],
                "resposta": "Procurar o posto de saúde",
                "dica": "O texto orienta ao final sobre febre."
            },
            {
                "enunciado": "Como se proteger de mosquitos transmissores?",
                "opcoes": ["Usar roupas coloridas", "Usar repelente e mosquiteiro", "Ficar dentro de casa sempre", "Comer muito alho"],
                "resposta": "Usar repelente e mosquiteiro",
                "dica": "O texto lista formas de proteção."
            }
        ]
    },
    3: {
        "titulo": "Alimentação Saudável",
        "texto": "A Amazônia oferece alimentos muito nutritivos: o açaí é rico em antioxidantes, o peixe fornece proteínas e ômega-3, a mandioca dá energia e a pupunha tem vitaminas. Comer variedade de alimentos naturais fortalece o corpo e previne doenças.",
        "perguntas": [
            {
                "enunciado": "O que o açaí contém que faz bem à saúde?",
                "opcoes": ["Ferro e cálcio", "Antioxidantes", "Proteínas", "Gordura boa"],
                "resposta": "Antioxidantes",
                "dica": "O texto descreve o benefício do açaí logo após citá-lo."
            },
            {
                "enunciado": "Por que o peixe é um alimento saudável?",
                "opcoes": ["Tem muito açúcar", "Fornece proteínas e ômega-3", "É fácil de cozinhar", "É barato"],
                "resposta": "Fornece proteínas e ômega-3",
                "dica": "O texto explica o benefício do peixe."
            },
            {
                "enunciado": "O que a mandioca fornece ao corpo?",
                "opcoes": ["Vitaminas", "Proteínas", "Energia", "Antioxidantes"],
                "resposta": "Energia",
                "dica": "O texto descreve o benefício da mandioca."
            },
            {
                "enunciado": "Por que é importante comer variedade de alimentos?",
                "opcoes": ["Para gastar mais dinheiro", "Para fortalecer o corpo e prevenir doenças", "Para engordar mais rápido", "Para sentir mais fome"],
                "resposta": "Para fortalecer o corpo e prevenir doenças",
                "dica": "A última frase do texto responde isso."
            }
        ]
    },
    4: {
        "titulo": "Primeiros Socorros",
        "texto": "Em caso de corte: lave com água limpa, pressione com pano limpo e procure atendimento se não parar de sangrar. Para queimaduras: coloque água fria corrente por 10 minutos, nunca pasta de dente ou manteiga. Em caso de picada de cobra: imobilize o membro e vá ao hospital o mais rápido possível.",
        "perguntas": [
            {
                "enunciado": "O que fazer em caso de corte?",
                "opcoes": ["Colocar terra para estancar", "Lavar com água limpa e pressionar com pano limpo", "Deixar sangrar para limpar", "Colocar álcool puro"],
                "resposta": "Lavar com água limpa e pressionar com pano limpo",
                "dica": "O texto orienta sobre cortes logo no início."
            },
            {
                "enunciado": "O que NÃO se deve colocar em queimaduras?",
                "opcoes": ["Água fria", "Gaze limpa", "Pasta de dente ou manteiga", "Curativo"],
                "resposta": "Pasta de dente ou manteiga",
                "dica": "O texto diz 'nunca' para dois produtos."
            },
            {
                "enunciado": "Por quanto tempo colocar água fria em queimaduras?",
                "opcoes": ["1 minuto", "5 minutos", "10 minutos", "30 minutos"],
                "resposta": "10 minutos",
                "dica": "O texto especifica o tempo para queimaduras."
            },
            {
                "enunciado": "O que fazer em caso de picada de cobra?",
                "opcoes": ["Chupar o veneno", "Fazer torniquete", "Imobilizar o membro e ir ao hospital", "Cortar o local da picada"],
                "resposta": "Imobilizar o membro e ir ao hospital",
                "dica": "A última frase do texto orienta sobre picada de cobra."
            }
        ]
    },
    5: {
        "titulo": "Saúde Mental e Comunidade",
        "texto": "A saúde não é só física — a saúde mental também importa. Conversar com pessoas de confiança alivia o estresse. Participar de atividades comunitárias, como festas e mutirões, fortalece os laços sociais. Pedir ajuda é sinal de coragem, não de fraqueza.",
        "perguntas": [
            {
                "enunciado": "O que alivia o estresse segundo o texto?",
                "opcoes": ["Ficar sozinho", "Conversar com pessoas de confiança", "Trabalhar mais", "Dormir pouco"],
                "resposta": "Conversar com pessoas de confiança",
                "dica": "A segunda frase responde isso."
            },
            {
                "enunciado": "O que participar de atividades comunitárias fortalece?",
                "opcoes": ["O corpo físico", "Os laços sociais", "A memória", "A concentração"],
                "resposta": "Os laços sociais",
                "dica": "A terceira frase do texto responde isso."
            },
            {
                "enunciado": "Pedir ajuda é sinal de quê?",
                "opcoes": ["Fraqueza", "Preguiça", "Coragem", "Ignorância"],
                "resposta": "Coragem",
                "dica": "A última frase do texto responde isso."
            }
        ]
    }
}
