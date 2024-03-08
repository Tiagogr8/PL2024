import ply.lex as lex

tokens = (
    'SELECT',
    'COMMA',
    'FROM',
    'WHERE',
    'GREATER_EQUAL',
    'IDENTIFIER',
    'NUMBER'
)


t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_COMMA = r'\,'
t_FROM =r'[Ff][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_GREATER_EQUAL = r'>='
t_IDENTIFIER = r'[a-zA-Z_]\w*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' \t'

def main():
    lexer = lex.lex()
    data = "Select id, nome, salario From empregados Where salario >= 820"
    lexer.input(data)
    for tok in lexer:
        print(tok)

if __name__ == '__main__':
    main()