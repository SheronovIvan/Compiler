from parser import Parser
from symbolTable import SymbolTable
from assembly import AssemblyCode
from tokenizer import Tokenizer

def percorrer_arvore(raiz):
    print(raiz.value)
    for i in raiz.children:
        percorrer_arvore(i)


def print_node(node, depth=0):
    indent = '|-- ' * depth
    print(f'{indent}[{depth}] ({node.__class__.__name__})')

    for child in node.children:
        print_node(child, depth + 1)


def read_file(file_name):
    with open(file_name) as file:
        data = file.read()
    return data


def main():
        test = read_file("input3.txt")
        try:
            # Создаем экземпляр токенизатора
            tokenizer = Tokenizer(test)
            # Цикл для получения и вывода всех токенов
            while True:
                # Получаем следующий токен
                token = tokenizer.selectNext()
                # Если достигнут конец файла, выходим из цикла
                if token is None:
                    break
                # Выводим тип и значение токена
                print(f'Type: {token.type}, Value: {token.value}')



            parser = Parser(test)
            symbolTable = SymbolTable(None)
            result = parser.parseProgram()
            print_node(result, 0)
            #percorrer_arvore(result)
            result.Evaluate(symbolTable)
            #print(AssemblyCode.assembly_code)
            #AssemblyCode.writeFile("teste.asm")
        except ValueError as err:
            print(err)


main()
