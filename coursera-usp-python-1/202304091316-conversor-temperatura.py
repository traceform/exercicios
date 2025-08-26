print("=" * 24, "\nCONVERSOR DE TEMPERATURA\n" + "=" * 24)
mode = int(input("Modos disponíveis:\n  Celsius  > Fahrenheit [1]\n  Celsius  >   Kelvin   [2]\nFahrenheit >   Celsius  [3]\nFahrenheit >   Kelvin   [4]\n  Kelvin   >   Celsius  [5]\n  Kelvin   > Fahrenheit [6]\nDigite o número correspondente: "))
if mode == 1:
	tempCelsius = float(input("Temperatura em Celsius: "))
	tempFahrenheit = 9 * (tempCelsius / 5) + 32
	print(f"Fahrenheit: {tempFahrenheit:.1f}")
elif mode == 2:
	tempCelsius = float(input("Temperatura em Celsius: "))
	tempKelvin = tempCelsius + 273
	print(f"Kelvin: {tempKelvin:.1f}")
elif mode == 3:
	tempFahrenheit = float(input("Temperatura em Fahrenheit: "))
	tempCelsius = 5 * ((tempFahrenheit - 32) / 9)
	print(f"Celsius: {tempCelsius:.1f}")
elif mode == 4:
	tempFahrenheit = float(input("Temperatura em Fahrenheit: "))
	tempKelvin = 5 * ((tempFahrenheit - 32) / 9) + 273
	print(f"Kelvin: {tempKelvin:.1f}")
elif mode == 5:
	tempKelvin = float(input("Temperatura em Kelvin: "))
	tempCelsius = tempKelvin - 273
	print(f"Celsius: {tempCelsius:.1f}")
elif mode == 6:
	tempKelvin = float(input("Temperatura em Kelvin: "))
	tempFahrenheit = 9 * ((tempKelvin - 273) / 5) + 32
	print(f"Fahrenheit: {tempFahrenheit:.1f}")
else:
	print("Caractere inválido!")
