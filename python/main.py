file_name = "./ex-2-data.txt"
# file_name = "./sample-data.txt"

vetor_de_vetores = []

with open(file_name, "r") as arquivo:
    for linha in arquivo:
        numeros = list(map(int, linha.strip().split()))
        vetor_de_vetores.append(numeros)


def verificar_seq_crescente(vetor):
    is_next_pos_crescente = True
    for index in range(len(vetor) - 1):
        item = vetor[index]
        for i in range(1,4):
            if (item+i) == vetor[(index+1)]:
                is_next_pos_crescente = True
                break
            else: 
                is_next_pos_crescente = False
        if index == (len(vetor) - 2):
            return is_next_pos_crescente
        if is_next_pos_crescente:
            continue
        else:
            return is_next_pos_crescente
        
def verificar_seq_decrescente(vetor):
    is_next_pos_decrescente = True
    for index in range(len(vetor) - 1):
        item = vetor[index]
        for i in range(1,4):
            if (item-i) == vetor[(index+1)]:
                is_next_pos_decrescente = True
                break
            else:
                is_next_pos_decrescente = False    
        if index == (len(vetor) - 2):
            return is_next_pos_decrescente
        if is_next_pos_decrescente:
            continue
        else:
            return is_next_pos_decrescente

def encontrar_sequencia_valida(vetor):
    if verificar_seq_crescente(vetor) or verificar_seq_decrescente(vetor):
        return vetor  

    for i in range(len(vetor)):
        novo_vetor = vetor[:i] + vetor[i + 1:]
        if verificar_seq_crescente(novo_vetor) or verificar_seq_decrescente(novo_vetor):
            return novo_vetor
    
    return None
        
vetor_filtrado = [vetor for vetor in vetor_de_vetores if encontrar_sequencia_valida(vetor)]

print(len(vetor_filtrado))
print("fim")
# print(len(vetor_de_vetores))
