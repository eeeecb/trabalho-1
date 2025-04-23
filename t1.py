"""
    Trabalho 1
    Alunos:
    - Eduardo Castro Barbosa - 2324290087
    - Julya dos Santos Alfaiate - 2314290064
    - Yan de Oliveira Nogueira - 2314290122
"""

def calcular_rendimento_caixinha(valor_inicial, dias):
    if not isinstance(valor_inicial, (int, float)) or valor_inicial <= 0:
        raise ValueError("O valor inicial deve ser um número positivo")
    
    if not isinstance(dias, int) or dias <= 0:
        raise ValueError("O número de dias deve ser um número inteiro positivo")
    
    taxa_anual = 0.1415  # 14.15% ao ano
    
    # Cálculo do rendimento bruto (convertendo taxa anual para diária e aplicando juros compostos)
    taxa_diaria = (1 + taxa_anual) ** (1/365) - 1
    rendimento_bruto = valor_inicial * ((1 + taxa_diaria) ** dias - 1)
    valor_bruto = valor_inicial + rendimento_bruto
    
    # Tabela de alíquotas de IOF (em decimal)
    tabela_iof = {
        1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83, 6: 0.80, 7: 0.76, 8: 0.73, 9: 0.70, 10: 0.66,
        11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53, 15: 0.50, 16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33,
        21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16, 26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03
    }
    
    # Cálculo do IOF sobre o rendimento
    if dias <= 29:
        aliquota_iof = tabela_iof.get(dias, 0)
    else:
        aliquota_iof = 0  # Após 30 dias, não há cobrança de IOF
    
    # O IOF é aplicado ao rendimento bruto
    valor_iof = rendimento_bruto * aliquota_iof
    rendimento_apos_iof = rendimento_bruto - valor_iof
    
    # Cálculo do IR sobre o rendimento após o IOF
    if dias <= 180:
        aliquota_ir = 0.225  # 22.5%
    elif 181 <= dias <= 360:
        aliquota_ir = 0.20   # 20%
    elif 361 <= dias <= 720:
        aliquota_ir = 0.175  # 17.5%
    else:
        aliquota_ir = 0.15   # 15%
    
    valor_ir = rendimento_apos_iof * aliquota_ir
    rendimento_liquido = rendimento_apos_iof - valor_ir
    valor_liquido = valor_inicial + rendimento_liquido
    
    # Preparando o resultado
    resultado = {
        "valor_inicial": valor_inicial,
        "dias_investimento": dias,
        "rendimento_bruto": rendimento_bruto,
        "aliquota_iof": aliquota_iof * 100,  # Convertendo para percentual
        "valor_iof": valor_iof,
        "aliquota_ir": aliquota_ir * 100,  # Convertendo para percentual
        "valor_ir": valor_ir,
        "rendimento_liquido": rendimento_liquido,
        "valor_liquido_final": valor_liquido
    }
    
    return resultado


def formatar_resultado(resultado):
    output = f"""
        Resultado do Investimento na Caixinha Super Cofrinho:
        -------------------------------------------------------
        Valor inicial: R$ {resultado['valor_inicial']:.2f}
        Período de investimento: {resultado['dias_investimento']} dias

        Rendimento bruto: R$ {resultado['rendimento_bruto']:.2f}
        Alíquota IOF: {resultado['aliquota_iof']:.2f}%
        Valor IOF: R$ {resultado['valor_iof']:.2f}

        Alíquota IR: {resultado['aliquota_ir']:.2f}%
        Valor IR: R$ {resultado['valor_ir']:.2f}

        Rendimento líquido: R$ {resultado['rendimento_liquido']:.2f}
        Valor líquido final: R$ {resultado['valor_liquido_final']:.2f}
        -------------------------------------------------------
    """
    return output


def main():
    print("Bem-vindo à Calculadora de Investimentos da Caixinha Super Cofrinho!")
    print("Taxa anual de rendimento: 14,15% ao ano")
    
    try:
        valor_inicial = float(input("Digite o valor inicial do investimento (R$): ").replace(',', '.'))
        dias = int(input("Digite o período de investimento (em dias): "))
        
        resultado = calcular_rendimento_caixinha(valor_inicial, dias)
        print(formatar_resultado(resultado))
        
    except ValueError as e:
        if str(e):
            print(f"Erro: {e}")
        else:
            print("Erro: Por favor, digite valores numéricos válidos!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()