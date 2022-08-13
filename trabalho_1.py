#Henrique Alves Semmer
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 4 U 3, 5, 67, 7 1, 2, 3, 4  I 1, 2, 3, 4, 5 4, 5 D 1, A, C, 34 A, C, D, 23 C 3, 4, 5, 5, A, B, R 1, B, C, D, 1 Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e {𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).  A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir:    União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}   Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.  No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
file = open('text1.txt')
content = file.readlines()

operations = int(content[0])
operator = 1

list = ["U","I","D","C"]
value = []

def run(operation,list1,list2):
    list1 = list1.split(',')
    list2 = list2.split(',')
    result = []
    if operation == "U":
        for i in list1:
            result.append(i)
        for f in list2:
            if f not in result:
                result.append(f)
    elif operation == "I":
        for i in list1:
            if i in list2:
                result.append(i)
    elif operation == "D":
        for i in list1:
            if i not in list2:
                result.append(i)
    elif operation == "C":
        for i in list1:
            vetor = []
            for j in list2:
                vetor.append([i,j])
            result.append(vetor)
    return result

def printer(results, operation):
    if operation == "U":
        print("União:", end = "")
    elif operation == "I":
        print("Interseção:", end = "")
    elif operation == "D":
        print("Diferença:", end = "")
    elif operation == "C":
        print("Produto Cartesiano:", end = "")
    for i in range(int(content[0])*3+1):
        if (content[i].replace('\n','')).replace(' ','') == operation:
            print(" conjunto 1 {"+(content[i+1].replace(' ','')).replace('\n','')+"}, conjunto 2 {"+(content[i+2].replace(' ','')).replace('\n','')+"}. Resultado: {", end = "")
            num = int(i/3)
            result = results[num]
            if (content[i].replace('\n','')).replace(' ','') == "C":
                for l in range(len(result)):
                    for c in range (len(result[l])):
                        if l == len(result)-1 and c == len(result[l])-1:
                            print("("+" ".join(result[l][c]).replace(' ',',')+")}", end = "")
                        else:
                            print("("+" ".join(result[l][c]).replace(' ',',')+"),", end = "")
            elif (content[i].replace('\n','')).replace(' ',''):
                print((" ".join(result)).replace(' ',',')+"}", end = "")
                            
while operations > 0:
    code = (content[operator].replace('\n','')).replace(' ','')
    if code in list:
        list1 = (content[operator+1].replace(' ','')).replace('\n','')
        list2 = (content[operator+2].replace(' ','')).replace('\n','')
        value.append(run(code,list1,list2))
    operator+=3
    operations-=1

for l in list:
    printer(value,l)
    print("\n",end = "")