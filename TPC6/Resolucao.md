# Resolução

## Símbolos Terminais:
- T = {'?', '!', '=', '+', '-', '*', '/', '(', ')', 'var', 'num'}
---
## Símbolos não Terminais:
- N = {S, Exp, Exp2, Term, Term2, Factor}
---
## Regras de Produção e Look Ahead:
```
S  -> '?' var            {'?'}
    | '!' Exp            {'!'}
    | var '=' Exp        {var}
    | ε                  {$}

Exp -> Term Exp2         {num, var, '('}       

Exp2 -> '+' Exp          {'+'}
      | '-' Exp          {'-'}
      | ε                {')',$}

Term -> Factor Term2     {num,var,'('}

Term2 -> '*' Term        {'*'}
       | '/' Term        {'/'}
       | ε               {'+','-',')',$}          

Factor -> num            {num} 
       | var             {var}
       | '(' Exp ')'     {'('}   
``` 

