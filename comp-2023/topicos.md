## Tópicos vistos em aula

### Discussão

* Computação sem computadores
* Computador como ferramenta
* O trabalho de um cientista da computação
* O que é um computador
* Características de uma linguagem de programação


### Expressões e instruções

* *Expressões* são "frases" (sequências de operações e operandos) que têm
  associadas a si:

  1. Um valor
  2. Um tipo

  Por exemplo, a expressão `2 / 2` tem valor `1.0` e tipo `float`.

* Uma *instrução* ou declaração é um outro tipo de "frase" que não tem
  um valor associado, mas simplesmente indica uma operação que o
  interpretador deve fazer. Até agora vimos dois tipos de intrução:

  1. Atribuição (dar um valor a uma variável), por exemplo, `x = 4`.
     Repare que o lado direito do simbolo de `=` é sempre uma expressão,
     cujo valor é armazenado na variável.
  2. Importar uma biblioteca, por exemplo,`import math`

### Tipos

(também conhecidos como classes)

* `int`: número inteiro
* `float`: número real ("quebrado")
* `str`: string (cadeia de caracteres, texto)
* `bool`: booleano (`True` ou `False`, sim ou não, verdadeiro ou falso)

### Erro

Erros sempre vão aparecer, e temos que saber lidar com eles. É
importante aprender a ler mensagens de erro, por mais confusas que elas
possam ser de vez em quando (a tendência é que vá ficando mais fácil com
o tempo).

Falamos de alguns tipos de erro:
* Erro de sintaxe: escrevemos alguma coisa que não faz sentido para o
  Python
* Erro semântico: o nosso programa executa normalmente, mas ele não faz
  o que a gente gostaria que ele fizesse (esse é o tipo mais perigoso)
* Erro de "runtime": alguma coisa dá errado durante a execução do
  programa.

### Operadores aritméticos

* `+`
* `-`
* `*`
* `/` (divisão "real")
* `//` (divisão inteira)
* `%` (módulo ou resto da divisão)
* `**` (potenciação)

Lembrando que alguns operadores têm precedência sobre outros, então
às vezes precisamos usar parênteses para que as contas sejam feitas na
ordem que escolhermos (diferente da matemática convencional, aqui só
podemos usar o parênteses para esse propósito. O colchete (`[`) e as
chaves (`{`) tem outras funções).

### Operadores booleanos

São aqueles operadores que nos dão um valor booleano. Por exemplo:

```
>>> 10 > 5
True
```

* `>`
* `<`
* `==` (Não confundir com `=`, usado para atribuir valores a variáveis!)
* `>=`
* `<=`

[//]: <> (* `and`)
[//]: <> (* `or`)
[//]: <> (* `not`)
[//]: <> (* `in`)
[//]: <> (* `is`)

### Operações com strings

Aprendemos a:

* concatenar duas strings (`s1 + s2`)
* concatenar sucessivamente a mesma string (`s1 * 4`)
* Acessar os elementos de uma string pelo seu índice (o primeiro
  elemento da string `s` é o `s[0]`, o enésimo elemento de `s` é
  `s[n - 1]`)



