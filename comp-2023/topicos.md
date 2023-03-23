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
  2. Importar uma biblioteca, por exemplo, `import math`

### Tipos

(também conhecidos como classes)

* `int`: número inteiro
* `float`: número real ("quebrado")
* `str`: string (cadeia de caracteres, texto)
* `bool`: booleano (`True` ou `False`, sim ou não, verdadeiro ou falso)

Veja abaixo também a função `type`, que nos diz qual é o tipo de uma
expressão. Vimos também que podemos converter de um tipo para outro
usando o nome do tipo como se fosse uma função:

```python
>>> int("34")
34
>>> type("34")
<class 'str'>
>>> type(int("34"))
<class 'int'>
```

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

### Funções embutidas

* `len`: devolve o comprimento de uma string (ou de outros tipos que se
  apliquem).

  ```python
  >>> len("Olá, mundo!")
  11
  ```

* `type`: Nos diz qual é o tipo da expressão. Exemplo

  ```python
  >>> type(34)
  <class 'int'>
  >>> type(3.3)
  <class 'float'>
  >>> type("Olá!")
  <class 'str'>
  >>> type(4 == 4)
  <class 'bool'>
  ```

* `min` e `max`: Nos devolve o menor e o maior elemento de um conjunto
  de valores, respectivamente.

  ```python
  >>> min(18, -10, 5)
  -10
  >>> min("Alice", "Bruno", "Carla")
  'Alice'
  >>> max(3.88, 3.5, 4.2)
  4.2
  ```

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
* `<=` <!--
* `and`
* `or`
* `not`
* `in`
* `is`-->

### Operações com strings

Aprendemos a:

* concatenar duas strings (`s1 + s2`)
* concatenar sucessivamente a mesma string (`s1 * 4`)
* Acessar os elementos de uma string pelo seu índice (o primeiro
  elemento da string `s` é o `s[0]`, o enésimo elemento de `s` é
  `s[n - 1]`)



