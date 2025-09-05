# Elaborar um código python que realize a impressão da palavra senac que existe dentro da string: "Aula do Senac 04"

# Versão alternativa
def find_string(text: str, target: str) -> str:
    """
    Returns the substring in 'text' that matches 'target', case-insensitive.
    Raises ValueError if not found.
    """
    try:
        # Use casefold() for better Unicode handling (e.g., accented letters)
        start = text.casefold().index(target.casefold())  # index() raises ValueError if not found
        # Return the actual substring from original text
        return text[start:start + len(target)]
    except ValueError:
        raise ValueError(f"'{target}' not found in '{text}'")

def main():
    text = "Aula do Senac 04"
    target = "senac"

    try:
        print(find_string(text, target))
    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()


''' # Versão 3
def find_string(text: str, target: str) -> tuple[int, int]:
    """
    Returns the start and end indices of 'target' in 'text', case-insensitive.
    Raises ValueError if not found.
    """
    text, target = text.lower(), target.lower()
    start = text.find(target)
    if start == -1: # Using find() directly avoids redundant checks, unlike using 'in'
        raise ValueError(f"'{target}' não encontrado em '{text}'") # ValueError makes more sense; error to be displayed
    return start, start + len(target) # No need to create a variable for the latter

def main():
    text = "Aula do Senac 04"
    target = 'senac'
    try:
        start, end = find_string(text, target) # Cleaner than storing values inside a single variable then referencing it
        print(text[start:end])
    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
'''

''' # Versão 2
def find_string(string: str, target: str) -> tuple[int, int]:
    """Recebe uma string e retorna os índices inicial e final de uma string presente nela"""

    string, target = string.lower(), target.lower()
    if target in string:
        start = string.find(target)
        end = start + len(target)
        return start, end
    else:
        print("Erro: Alvo não encontrado.")
        exit()

def main():
    string = "Aula do Senac 04"
    targetString = 'senac'
    location = find_string(string, targetString)
    print(string[location[0]:location[1]])

if __name__ == "__main__": # For scripts that may be imported as modules
    main()
'''

''' # Versão 1

string = "Aula do Senac 04"
targetString = 'senac'

fixedString = string.lower()
startTarget = fixedString.find(targetString)
endTarget = startTarget+len(targetString)

if targetString in string.lower():
    print(string[startTarget:endTarget])
else:
    print("Erro: Alvo não encontrado!")
'''