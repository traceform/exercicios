def get_quantity(prompt: str) -> int:
    """Get a valid positive integer quantity of grades."""
    while True:
        try:
            quantity = int(input(prompt))
            if quantity > 0:
                return quantity
            print("Erro: A quantidade deve ser maior que zero.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")

def get_float(prompt: str) -> float:
    """Prompt the user until a valid floating-point number equal or greater than 0 is entered."""
    while True:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Erro: Nota não pode ser negativa.")
            else:
                return number
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido. Exemplo: 8.7")

def get_grades(qnt_grades: int) -> list[float]:
    """Return a list of floats representing the entered grades."""
    return [get_float(f"Informe a sua nota {n}: ") for n in range(1, qnt_grades + 1)]

def calculate_average(grades: list[float]) -> float:
    """Return the average of the given grades. Raises ValueError if list is empty."""
    if not grades:
        raise ValueError("Grade list cannot be empty.")
    return sum(grades) / len(grades)

def main(): #according to the teacher this section is so small it could be moved to the next instead
    quantity = get_quantity("Quantidade de notas a informar: ")
    grades = get_grades(quantity)
    average = calculate_average(grades)
    print(f"Com base nas notas {', '.join(f"{n:.2f}" for n in grades)} a média é: {average:.2f}")

if __name__ == "__main__":
    main()

