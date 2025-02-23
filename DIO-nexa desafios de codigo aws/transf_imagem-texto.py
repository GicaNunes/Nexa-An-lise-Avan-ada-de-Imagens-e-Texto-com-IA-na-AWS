# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber um caso de uso e retornar sua respectiva descrição.
def descrever_caso_de_uso(caso):
    # Caso o caso de uso seja "educação"
    if caso == "educação":
        return "organização de registros acadêmicos digitalizados"

    # Caso o caso de uso seja "finanças"
    elif caso == "finanças":
        return "dados extraídos de formulários financeiros"

    # Caso o caso de uso seja "saúde"
    elif caso == "saúde":
        return "digitalização de registros médicos e saúde"

    # Caso o caso de uso seja "governo"
    elif caso == "governo":
        return "dados de formulários governamentais extraídos"

    # Retorna None se o caso de uso não for reconhecido
    else:
        return None


# Imprime a descrição do caso de uso recebido na "entrada" através da função "descrever_caso_de_uso".
print(descrever_caso_de_uso(entrada))
