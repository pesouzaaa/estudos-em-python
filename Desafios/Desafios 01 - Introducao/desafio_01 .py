# Leitura da entrada: preço e código de promoção
preco_str, codigo_promocao = input().split()

# Conversão do preço para float
preco = float(preco_str)

if codigo_promocao == "S":
    promocao = (preco * 0.10)
    preco_final = (preco - promocao)
    print(f"O valor da sua compra e: {preco_final:.2f}")

else:
    print(f"{preco:.2f}")