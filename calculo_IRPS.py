from typing import Any


def calcular_imposto_renda(salario_bruto: float, tabela: list[dict[str, Any]], numero_dependentes: int):
    for intervalo in tabela:
        limite_inferior = intervalo['limite_inferior']
        limite_superior = intervalo['limite_superior']
        valores_dependentes = intervalo['valores_dependentes']

        if limite_superior is None:
            # Se não houver limite superior, assumimos que é infinito
            limite_superior = float('inf')

        if limite_inferior <= salario_bruto <= limite_superior:
            # Obter o valor correspondente ao número de dependentes
            if numero_dependentes <= len(valores_dependentes):
                valor_dependentes = valores_dependentes[numero_dependentes]
            else:
                # Se o número de dependentes for maior que o tamanho da lista, usar o último valor
                valor_dependentes = valores_dependentes[0]

            # Calcular o valor base do imposto
            valor_base = salario_bruto - limite_inferior

            # Calcular o valor do imposto sem considerar os dependentes
            imposto_sem_dependentes = valor_base * intervalo['coeficiente']

            # Adicionar o valor correspondente aos dependentes
            imposto_com_dependentes = imposto_sem_dependentes + valor_dependentes

            return imposto_com_dependentes

    return 0  # Retorna 0 se o salário não estiver em nenhum dos intervalos especificados


# Definir tabela de intervalos e valores correspondentes
tabela_imposto = [
    {'limite_inferior': 0.0, 'limite_superior': 20249.99, 'coeficiente': 0.0, 'valores_dependentes': [0.00, 0.00, 0.00, 0.00, 0.00]},
    {'limite_inferior': 20250.00, 'limite_superior': 20749.99, 'coeficiente': 0.10, 'valores_dependentes': [0.00, 0.00, 0.00, 0.00, 0.00]},
    {'limite_inferior': 20750.00, 'limite_superior': 20999.99, 'coeficiente': 0.10, 'valores_dependentes': [50.00, 0.00, 0.00, 0.00, 0.00]},
    {'limite_inferior': 21000.00, 'limite_superior': 21249.99, 'coeficiente': 0.10, 'valores_dependentes': [75.00, 25.00, 0.00, 0.00, 0.00]},
    {'limite_inferior': 21250.00, 'limite_superior': 21749.99, 'coeficiente': 0.10, 'valores_dependentes': [100.00, 50.00, 25.00, 0.00, 0.00]},
    {'limite_inferior': 21750.00, 'limite_superior': 22249.99, 'coeficiente': 0.10, 'valores_dependentes': [150.00, 100.00, 75.00, 50.00, 0.00]},
    {'limite_inferior': 22250.00, 'limite_superior': 32749.99, 'coeficiente': 0.15, 'valores_dependentes': [200.0, 150.00, 125.00, 100.00, 50.00]},
    {'limite_inferior': 32750.00, 'limite_superior': 60749.99, 'coeficiente': 0.20, 'valores_dependentes': [1775.00, 1725.00, 1700.00, 1675.00, 1625.00]},
    {'limite_inferior': 60750.00, 'limite_superior': 144749.99, 'coeficiente': 0.25, 'valores_dependentes': [7375.0, 7325.00, 7300.00, 7275.00, 7225.00]},
    {'limite_inferior': 144750.00, 'limite_superior': None, 'coeficiente': 0.32, 'valores_dependentes': [28375.00, 28325.00, 28300.00, 28275.00, 28225.00]},
]


def main():
    # Salário fornecido
    salario_bruto = float(input("Digite o salario bruto mensal: "))
    numero_dependentes = int(input("Digite o numero de dependentes: "))

    # Calcular o imposto de renda
    imposto_renda = calcular_imposto_renda(salario_bruto, tabela_imposto, numero_dependentes)

    # Exibir o resultado
    if imposto_renda > 0:
        print(f"O valor do imposto a ser retido é: {imposto_renda:.2f} MT")
    else:
        print("O salário não está em nenhum dos intervalos especificados.")


if __name__ == "__main__":
    main()
