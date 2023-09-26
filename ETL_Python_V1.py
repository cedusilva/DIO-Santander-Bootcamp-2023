##Extract - Extracao
# Obter os dados da plan
nomeRestaurante = input()
tempoEstimadoEntrega = int(input())

##TODO: Imprimir a saída no padrão definido no enunciado deste desafio.
##//Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.

mensagem = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."

print(mensagem)



valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

##//TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
tt_ham = valorHamburguer * quantidadeHamburguer
tt_beb = valorBebida * quantidadeBebida

total_pedido = tt_ham + tt_beb



##//TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

troco = valorPago - total_pedido

##//TODO: Imprimir a saída no formato especificado neste desafio.

extrato = f"O preço final do pedido é R$ {total_pedido:.2f}. Seu troco é R$ {troco:.2f}." 

print(extrato)



def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    
    cupom = input()
    if cupom == "10%":
      total_pedido = total*0.9
    else: 
      total_pedido = total*0.8

    extrato = f"Valor total:  {total_pedido:.2f}\n"
    print (extrato)
 
  ##//TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).
 
 
if __name__ == "__main__":
    main()













    saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.

saldo_tem = saldo_atual + (valor_deposito-valor_retirada)

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).

extrato = f"Saldo atualizado na conta: {saldo_tem:.1f}\n"
print (extrato)



numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    tipoprato = input()
    if tipoprato == 's':
      ehVegano = True 
    else:
      ehVegano = False
    pratovegano = "(Vegano)" if ehVegano else "(Nao-vegano)"
    print(f"Pedido {i}: {prato} {pratovegano} - {calorias} calorias")


    -----------


    

ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
    print(ativo)


    ---


    # Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
  saldo_total -= valor_saque
  extrato = f"Saque realizado com sucesso. Novo saldo: {saldo_total}"
else: 
  extrato = "Saldo insuficiente. Saque nao realizado!"
print(extrato)
