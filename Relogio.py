def retorna_angulo_relogio(hora, minuto):
    if hora == 12:
        hora = 0
    
    posicao_ponteiro_hora = 0.5 * (60 * hora + minuto)

    posicao_ponteiro_minuto = 6 * minuto

    angulo = abs(posicao_ponteiro_hora - posicao_ponteiro_minuto)

    angulo = min(360 - angulo, angulo)

    return int(angulo)

# Exemplo de uso
hora = int(input("Digite a hora (0-12): "))
minuto = int(input("Digite o minuto (0-59): "))

angulo = retorna_angulo_relogio(hora, minuto)
print(f"Para {hora:02d}:{minuto:02d}h, o ângulo entre os ponteiros é de {angulo}°.")
