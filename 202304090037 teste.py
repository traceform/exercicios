tempFahrenheit = float(input("Temperatura em Fahrenheit: "))
tempCelsius = 5 * ((tempFahrenheit - 32) / 9)
print(f"Celsius: {tempCelsius:.1f}")



quit()


ano = int(input("Ano: "))
print((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0)


quit()

nota = float(input("Nota: "))
print(3.0 <= nota <= 5.0)

