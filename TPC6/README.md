# TPC6: Gramática Independente de Contexto LL(1)
## 2024-03-21

## Autor:
- A100827
- Tiago Granja Rodrigues

## Resumo
Construir uma gramática independente de contexto LL(1) para a seguinte linguagem:
```
?a
b = a*2/(27-3)
!a+b
c = a*b/(a/b)
```
Tendo em conta que:
- É necessário garantir a prioridade dos operadores
- Temos de garantir que a gramática é LL(1)
- É necessário calcular os Look Ahead para todas as produções
