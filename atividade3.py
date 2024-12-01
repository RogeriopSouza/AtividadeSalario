def calcular_reajuste(salario_atual):
    
    if salario_atual <= 280:
        percentual_aumento = 20
    elif salario_atual <= 700:
        percentual_aumento = 15
    elif salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    
    valor_aumento = salario_atual * (percentual_aumento / 100)
    
    
    novo_salario = salario_atual + valor_aumento
    
  
    inflacao = 3.8
    valor_aumento_real = valor_aumento - (valor_aumento * (inflacao / 100))
    
 
    aumento_emojis = "🎉💸✨"
    seta = "➡️"
    
   
    print(f"\n{aumento_emojis} **Resultados do Reajuste Salarial** {aumento_emojis}")
    print(f"Salário antes do reajuste: {seta} R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {seta} {percentual_aumento}%")
    print(f"Valor do aumento: {seta} R$ {valor_aumento:.2f}")
    print(f"Novo salário, após o aumento: {seta} R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontado a inflação: {seta} R$ {valor_aumento_real:.2f}")
    print(f"\n🎉🎉 Parabéns pelo aumento! Que você continue brilhando! 🎉🎉\n")


salario_atual = float(input("Digite o salário atual do colaborador: "))
calcular_reajuste(salario_atual)

