def acrescimo(preco: float, taxa: float):
    """A função acréscimo realiza o cálculo de aumento 
    do valor do preço do produto de acardo com a taxa 

    args:
        preco(float): Passe o preço do produto
        taxa(float): passe a taxa do acrécimo somente número

    Returns:
        float: Retorna o preço produto com o valor de acréscimo  

    """
    return preco * (1+(taxa / 100))


rs = acrescimo(500, 6)

print(f"O valor final do produto é {rs}")