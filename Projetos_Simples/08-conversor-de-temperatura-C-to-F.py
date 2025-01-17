def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = converter_temperatura(celsius)
print(f'A temperatura em graus Fahrenheit é: {fahrenheit:.2f}')