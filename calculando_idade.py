#calculando a idade de uma pessoa
from datetime import date

def calcular_idade(dia, mes, ano):
    hoje = date.today()
    idade = hoje.year - ano
    # Ajuste se ainda não fez aniversário este ano
    if (hoje.month, hoje.day) < (mes, dia):
        idade -= 1
    return idade

def main():
    data = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    dia, mes, ano = map(int, data.split("/"))
    idade = calcular_idade(dia, mes, ano)
    print(f"Você tem {idade} anos.")

if __name__ == "__main__":
    main()
