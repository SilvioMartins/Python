#Importação de Bibliotecas
import os

#Definição de Variáveis
res = num1 = num2 = 0.0
oper = cont = ''

#Definição de Funções
#Função para calculo do resultado
def calcula(num1,num2,oper):
    if (oper=='+'):
        return (num1+num2)
    elif (oper=='-'):
        return (num1-num2)
    elif (oper=='*'):
        return (num1*num2)
    else:
        return (num1/num2)

#Corpo do Programa
while True:
    
    #Trata Exceções Evitando mensagens de erro não formatadas
    try:   
        os.system('cls')                         #Limpa a Tela do Console
        print("CALCULADORA v1.0","\n","\n")      #Título do App
    
        #Recebe as variáveis num1, num2 e oper
        num1 = float(input("Informe o 1o. Número: "))
        oper = input("Informe a operação (+,-,*,/): ")
    
        # Verifica se o operador está correto; senâo gera um exception e trata
        if (oper != '+' and oper != '-' and oper != '*' and oper != '/' ):
            raise OverflowError
           
        num2 = float(input("Informe o 2o. Número: "))

        #Imprme o resultado
        print("\n%.2f %s %.2f = %.2f" %(num1, oper, num2, calcula(num1,num2,oper)))

    except ValueError:
        #Mensagem de erro formatada para erros de Valor 
        print("\nOperando Inválido!")
    
    except ZeroDivisionError:
        #Mensagem de erro formatada para erros de Valor 
        print("\nDivisão por Zero Não Permitido!")

    except OverflowError:
        #Mensagem de erro formatada para erros de Valor 
        print("\nOperador Inválido!")

    #verifica se quer continuar com outra operação
    cont = input("\nDeseja realizar outra Operação? (S->Continua / Qualquer Tecla -> Sai)) ") 
    
    #Sai do programa se não quiser continuar.
    if (cont != 'S' and cont != 's'):
        break
