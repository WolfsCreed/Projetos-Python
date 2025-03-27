
print ('Olá eu sou uma calculadora e gostaria de calcular o seu IMC')
print ('Primeiro precisamos ver algumas informções')
while True:
    try: 
        peso = float(input ('Qual o seu peso'))
        break
    except ValueError: 
            print('Você não inseriu um número valido')
while True: 
    try:
        altura = float(input('qual a sua altura?'))
        break
    except ValueError:
            print('Você não inseriu um número valido')
imc = round(float(peso/altura**2), 2)
print(f"seu imc é {imc}")
ganhar = round(float(18.5*(altura**2)-peso),2 )
perder = round(float(peso-25*altura**2), 2)
if imc < 18.5: 
    print('Seu IMC está abaixo do ideal.')
    print(f"Você precisa ganhar {ganhar}kg para estar no ideal")
if imc > 25:

     print('seu IMC está acima do ideal')
     print(f"você precisa perder {perder}kg para estar no ideal")
if 18.5<imc<25:
     print('seu imc está ideal')
print('IMC calculado com sucesso!')
