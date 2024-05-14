import csv #biblioteca que sabe ler e escrever em um arquivo no formato csv 

def ler_csv(arquivo_csv):
    dados_csv = []                                         #cria uma lista em branco 
    try:                                                   # tentar / tratamento de erro
        with open(arquivo_csv, newline='') as massa:
                                                           # com o arquivo --> informa o nome e o apelido massa
            tabela = csv.reader(massa, delimiter=',')
                                                          # com os dados do arquivo , menos o cabeçalho , informando que o separador é a virgula
            next(tabela)
            for linha in tabela:
                dados_csv.append(linha)
        #print("Data read from CSV:", dados_csv)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')      
    except Exception as fail:
        print(f'Falha imprevista: {fail}')                 