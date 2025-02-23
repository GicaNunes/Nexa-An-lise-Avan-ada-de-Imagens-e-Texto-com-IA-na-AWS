# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber um caso de uso e retornar sua respectiva descrição.
def descrever_caso_de_uso(caso):
    # Caso o caso de uso seja "análise de chamadas e assistência do atendente"
    if caso == "análise de chamadas e assistência do atendente":
        return "transcrição de chamadas para melhorar a qualidade do atendimento"

    # Caso o caso de uso seja "legendas para vídeos e reuniões"
    elif caso == "legendas para vídeos e reuniões":
        return "geração automática de legendas para vídeos e reuniões"

    # Caso o caso de uso seja "detecção de toxicidade"
    elif caso == "detecção de toxicidade":
        return "identificação de linguagem ofensiva ou inapropriada em textos"

    # Caso o caso de uso seja "documentação clínica"
    elif caso == "documentação clínica":
        return "transcrição de consultas médicas para documentação precisa"

    # Retorna None se o caso de uso não for reconhecido
    else:
        return None


# Imprime a descrição do caso de uso recebido na "entrada" através da função "descrever_caso_de_uso".
print(descrever_caso_de_uso(entrada))
