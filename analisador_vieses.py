import re

def analisar_engenharia_social(texto):
    gatilhos = {
        "Urgência Artificial (Medo/Pânico)": [
            r"urgente", r"imediatamente", r"bloqueada", r"expira", r"atenção",
            r"último aviso", r"agora mesmo", r"evitar suspensão", r"com urgência"
        ],
        "Falsa Autoridade (Coerção/Validação)": [
            r"banco", r"polícia", r"receita federal", r"gerente", r"suporte técnico",
            r"departamento de segurança", r"comunicado oficial", r"advogado"
        ],
        "Escassez/Ganância (Recompensa Imediata)": [
            r"ganhou", r"sorteio", r"vaga exclusiva", r"recompensa", r"lucro",
            r"herança", r"resgate imediato", r"grátis", r"premiado"
        ]
    }

    print("=" * 60)
    print("        VYRE LABS - RELATÓRIO DE ANÁLISE COMPORTAMENTAL REVERSA        ")
    print("=" * 60)
    print(f"Texto Analisado: \"{texto[:60]}...\"\n")

    total_ameacas = 0

    for vies, termos in gatilhos.items():
        encontrados = []
        for termo in termos:
            if re.search(termo, texto, re.IGNORECASE):
                encontrados.append(termo)

        if encontrados:
            print(f"🔴 VIES DETECTADO: {vies}")
            print(f"   ↳ Padrões identificados: {', '.join(encontrados)}")
            print(f"   ↳ Risco Psicológico: Manipulação cognitiva ativa.\n")
            total_ameacas += len(encontrados)

    print("-" * 60)
    if total_ameacas >= 3:
        print("🔴 DIAGNÓSTICO FORENSE: Alta probabilidade de Engenharia Social / Phishing.")
    elif total_ameacas > 0:
        print("🟡 DIAGNÓSTICO FORENSE: Alerta. Presença de gatilhos persuasivos isolados.")
    else:
        print("🟢 DIAGNÓSTICO FORENSE: Padrões comportamentais limpos ou neutros.")
    print("=" * 60)

# --- Exemplo de Execução ---
if __name__ == "__main__":
    mensagem_suspeita = (
        "Prezado cliente, sua conta bancária será BLOQUEADA imediatamente por motivos de segurança. "
        "O Suporte Técnico do Banco solicita que clique no link agora mesmo para evitar a suspensão."
    )

    analisar_engenharia_social(mensagem_suspeita)
