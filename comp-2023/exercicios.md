## Exercícios

Os exercícios abaixo foram retirados de algumas fontes. Usamos as
siglas abaixo para referenciar a numeração original de cada exercício.

* [Introdução à computação usando Python](https://www.amazon.com.br/Introdu%C3%A7%C3%A3o-Computa%C3%A7%C3%A3o-Python-Desenvolvimento-Aplica%C3%A7%C3%B5es/dp/8521630816), Ljubomir Perkovic - LP ou LPP (exercícios práticos)
* [Introdução à ciência da computação com Python parte 1](https://www.coursera.org/learn/ciencia-computacao-python-conceitos), Fábio Kon (curso no [coursera](https://coursera.org) - FK ou FKQ (exercícios em "Quiz")
* [Pense em Python](https://penseallen.github.io/PensePython2e/), Allen B. Downey - AD

### Exercício 1 (LP1)

Escreva expressões algébricas Python correspondentes aos seguintes comandos:

a. A soma dos 5 primeiros inteiros positivos.
b. A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
c. O número de vezes que 73 cabe em 403.
d. O resto de quando 403 é dividido por 73.
e. 2 à 10a potência.
f. O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
g. O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50

### Exercício 2 (LP2)

Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

a. A soma de 2 e 2 é menor que 4.
b. O valor de `7 // 3` é igual a 1 + 1.
c. A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
d. A soma de 2, 4 e 6 é maior que 12.
e. 1387 é divisível por 19.
f. 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
g. O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.

### Exercício 3 (LP3)

Escreva instruções Python que correspondem às ações a seguir e execute-as:


a. Atribua o valor inteiro `3` à variável `a`.
b. Atribua `4` à variável `b`.
c. Atribua à variável `c` o valor da expressão `a * a + b * b`.

### Exercício 4 (LPP2.4)

Comece executando as instruções de atribuição:

```
>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
```

Escreva expressões Python usando `s1`, `s2` e `s3` e os operadores `+` e `*` a fim de avaliar para:

a. `'ant bat cod'`
b. `'ant ant ant ant ant ant ant ant ant ant'`
c. `'ant bat bat cod cod cod'`
d. `'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'`
e. `'batbatcod batbatcod batbatcod batbatcod batbatcod'`

### Exercício 5 (LPP2.5)

Comece executando a atribuição:

```
s = '0123456789'
```

Agora, escreva expressões usando a string `s` e o operador de indexação que é avaliado como:

a. `'0'`
b. `'1'`
c. `'6'`
d. `'8'`
e. `'9'`

### Exercício 6 (LPP2.6)

Primeiro, execute a atribuição
```
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
```

Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a primeira e a última palavras em `palavras`, na ordem do dicionário.

### Exercício 7 (LPP2.7)

Dada a lista de notas de trabalho de casa dos alunos

```
>>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
```

Escreva:

a. Uma expressão que avalia para o número de 7 notas.
b. Uma instrução que muda a última nota para 4.
c. Uma expressão que avalia para a nota mais alta.
d. Uma instrução que classifica as notas da lista.
e. Uma expressão que avalia para a média das notas

### Exercício 8 (LPP2.8)

Em que ordem os operadores nas expressões a seguir são avaliados?

a. `2 + 3 == 4 or a >= 5`
b. `lst[1] * -3 < -10 == 0`
c. `(lst[1] * -3 < -10) in [0, True]`
d. `2 * 3**2`
e. `4 / 2 in [1, 2, 3]`

### Exercício 9 (LPP2.9)

Qual é o tipo do objeto ao qual essas expressões são avaliadas?

a. `False + False`
b. `2 * 3**2.0`
c. `4 // 2 + 4 % 2`
d. `2 + 3 == 4 or 5 >= 5`


### Exercício 10 (LPP2.10)

Escreva expressões Python correspondentes ao seguinte:

a. O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b

b. O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
c. A área de um disco com raio a
d. O valor da expressão Booleana que verifica se um ponto com coordenadas `x` e `y` está dentro de um círculo com centro `(a, b)` e raio `r`

### Exercício 11 (AD1.1)

É uma boa ideia ler este livro em frente a um computador para testar os exemplos durante
a leitura.
Sempre que estiver testando um novo recurso, você deve tentar fazer erros. Por exemplo,
no programa “Hello, World!”, o que acontece se omitir uma das aspas? E se omitir ambas?
E se você soletrar a instrução print de forma errada?

Este tipo de experimento ajuda a lembrar o que foi lido; também ajuda quando você
estiver programando, porque assim conhecerá o significado das mensagens de erro. É
melhor fazer erros agora e de propósito que depois e acidentalmente.

1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou
ambas?
3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que
acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que
acontece se você tentar usar isso no Python?
5. O que acontece se você tiver dois valores sem nenhum operador entre eles?

### Exercício 12 (AD1.2)

Inicialize o interpretador do Python e use-o como uma calculadora.

1. Quantos segundos há em 42 minutos e 42 segundos?
2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo
médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em
milhas por hora?

### Exercício 13 (AD2.1)

Repetindo o meu conselho do capítulo anterior, sempre que você aprender um recurso
novo, você deve testá-lo no modo interativo e fazer erros de propósito para ver o que acontece.

* Vimos que n = 42 é permitido. E 42 = n?
* Ou x = y = 1?
* Em algumas linguagens, cada instrução termina em um ponto e vírgula (`;`). O que
acontece se você puser um ponto e vírgula no fim de uma instrução no Python?
E se puser um ponto no fim de uma instrução?
* Em notação matemática é possível multiplicar x e y desta forma: xy. O que acontece
se você tentar fazer o mesmo no Python?

### Exercício 14 (AD2.2)
Pratique o uso do interpretador do Python como uma calculadora:

1. O volume de uma esfera com raio r é (4/3)πr³. Qual é o volume de uma esfera com raio
5?
2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por
quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e
1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa
para o café da manhã?

### Exercício 15 (FKQ1.1)

O que o interpretador de Python responderá se você digitar: 2 + 5 * 3

* 13
* 30
* 21
* 17

### Exercício 16 (FKQ1.2)

Considerando a versão 3.x do Python, qual é o resultado da expressão: 20 / 3

* 6
* 0
* 6.666666666667
* 7

### Exercício 17 (FKQ1.3)

Qual é o resultado de: 20.0 / 3

* 0
* 6.666666666667
* 6
* 7

### Exercício 18 (FKQ1.4)

O que o interpretador de Python responderá se você digitar o seguinte comando? `10 > 10`

* Syntax error
* Type mismatch
* True
* False

### Exercício 19 (FKQ1.5)

O que o interpretador de Python responderá se você digitar o seguinte comando? `9 ** 2 == 80 + 1`

* Type mismatch
* True
* False
* Syntax error

### Exercício 20 (FKQ1.6)

Qual o resultado gerado pelo comando ((5 - 3) ** 3)?

* -8
* 8
* 22
* -22

### Exercício 21 (FKQ1.7)

Como devo escrever a seguinte expressão para que o interpretador de Python a calcule corretamente? `{ 4 x [ ( 33 - 31 ) x 2 ] }`

* { 4 * [ ( 33 - 31 ) * 2 ] }
* ( 4 * ( ( 33 - 31 ) * 2 ) )
* ( 4 x ( ( 33 - 31 ) x 2 ) ) 
* ( 4 * ( 33 - 31 * 2 ) )

### Exercício 22 (FKQ2.1)

A extensão de um arquivo fonte escrito em Python normalmente costuma ser:

* .prg
* .exe
* .obj
* .py

### Exercício 23 (FKQ2.2)

Qual será o resultado desta sequência de comandos?

```
x = 10
y = 15
x + y
```


* 10 + 15
* Syntax error
* True
* 25

### Exercício 24 (FKQ2.3)

Qual será exatamente a resposta do interpretador para o código abaixo?

```
soma = 5.5
print("soma =", soma)
```

* soma = 5.5
* soma 5.5
* 5.55.5
* 5.5 5.5

### Exercício 25 (FKQ2.4)

No Python, qual o valor final que estará armazenado em x?

```
x = 10
y = 30
x = x + 10
y = x + 10
x = x + y
```

* 40
* 60
* 50
* 70

### Exercício 26 (FKQ2.5)

No Python, qual o valor final que estará armazenado em x e em y?

```
x = 50
y = 20
aux = x
x = y
y = aux
```

* x terá o valor 50 e y terá 20
* x terá o valor 50 e y terá 50
* Nenhuma das alternativas
* x terá o valor 20 e y terá 50
* x terá o valor 20 e y terá 20

### Exercício 27 (FKQ2.6)

Qual será a saída do seguinte código?

```
a = 1
b = 2
print(a + 2 * b)
```

* 5
* a + 2 * b
* 1
* 2

### Exercício 28 (FKQ2.7)

Suponha que `x` = 2, qual declaração é verdadeira? (True)

* x == 8
* x > 2
* x != 8
* x != 2

### Exercício 29 (FKQ2.8)

Suponha que  x = 1. Assinale todas as alternativas verdadeiras (True)

* x >= 1
* x < 1
* x == 1
* x != 1

### Exercício 30 (LP2.12)

Escreva expressões Python correspondentes a estas instruções:

a. A soma dos sete primeiros inteiros positivos
b. A idade média de Sara (idade 65), Fátima (idade 56) e Mark (idade 45)
c. 2 à 20ª potência
d. O número de vezes que 61 cabe em 4356
e. O resto de quando 4365 é dividido por 61

### Exercício 31 (LP2.13)

Comece avaliando, no shell interativo, a atribuição:

```
>>> s1 = '-'
>>> s2 = '+'
```

Agora, escreva expressões de string envolvendo s1 e s2 e os operadores de string + e * que são avaliados como:

a. `'-+'`
b. `'–+'`
c. `'+––'`
d. `'+––+––'`
e. `'+––+––+––+––+––+––+––+––+––+––+'`
f. `'+–+++––+–+++––+–+++––+–+++––+–+++––'`

Tente tornar suas expressões de string as menores possíveis.


### Exercício 32 (LP2.17)

Escreva expressões Booleanas correspondentes às instruções lógicas a seguir e avalie as expressões:
a. A soma de 16 e –9 é menor que 10.
b. O comprimento da lista `inventário` é mais de cinco vezes o comprimento da string `nomecompleto`.
c. `c` não é maior que 24.
d. 6,75 está entre os valores dos inteiros `a` e `b`.
e. O comprimento da string `meio` é maior que o comprimento da string `primeiro` e
menor que o comprimento da string `último`.
f. Ou a lista `estoque` está vazia ou tem mais de 10 objetos nela.


### Exercício 33 (FKQ3.1)

Qual o tipo de dado armazenado na variável x pelo comando abaixo?
```
x = input ("Qual a idade? ")
```


* a função input sempre devolve um string
* float (número real), pois considera a idade fracionada do usuário
* inteiro, pois considera apenas a idade completa do usuário
* booleano, pois o sinal de igualdade é operador relacional

### Exercício 34 (FKQ3.2)

Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?

```
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
a = b
b = a
print(a)
print(b)
```


* a e b serão 2
* a será 1 e b será 2
* a e b serão 1
* a será 2 e b será 1

### Exercício 35 (FKQ3.3)

Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?

```
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)
```

* a e b serão 2
* a será 2 e b será 1
* a será 1 e b será 2
* a e b serão 1

### Exercício 36 (LPP3.2)

Traduza estas instruções condicionais em instruções if do Python:

a. Se `idade` é maior que 62, exiba `Você pode obter benefícios de pensão`.
b. Se o nome está na lista `['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']`, exiba `Um dos 5 maiores jogadores de beisebol de todos os tempos!`.
c. Se golpes é maior que `10` e defesas é `0`, exiba `Você está morto...`.
d. Se pelo menos uma das variáveis booleanas `norte`, `sul`, `leste` e oeste for `True`, exiba `Posso escapar.`.

### Exercício 37 (LPP3.3)

Traduza estas declarações em instruções if/else do Python:

a. Se `ano` é divisível por 4, exiba `Pode ser um ano bissexto.`; caso contrário, exiba `Definitivamente não é um ano bissexto.`
b. Se a lista `bilhete` é igual à lista `loteria`, exiba `Você ganhou!`; se não, exiba `Melhor sorte da próxima vez...`.

### Exercício 38 (LP2.21)

Escreva uma expressão envolvendo uma string de três letras `s` cujo valor é o de uma string cujos caracteres são os caracteres de `s` em ordem contrária. Se `s` for `'top'`, a expressão deverá
ser avaliada como `'pot'`.

### Exercício 39 (LP2.22)

Escreva uma expressão envolvendo a string `s` contendo o último e o primeiro nome de uma
pessoa — separados por um espaço em branco — que seja avaliada para as iniciais da pessoa. Se
a string tivesse meu primeiro e último nome, a expressão seria avaliada como `'LP'`.

### Exercício 40 (LP2.14)

Comece executando, no shell, a seguinte instrução de atribuição:
```
>>> s = 'abcdefghijklmnopqrstuvwxyz'
```

Agora, escreva expressões usando a string s e o operador de indexação que é avaliado
como `'a'`, `'c'`, `'z'`, `'y'` e `'q'`.

### Exercício 41 (LP2.15)

Comece executando

```
s = 'goodbye'
```

Depois, escreva uma expressão Booleana que verifica se:

a. O primeiro caractere da string `s` é `'g'`
b. O sétimo caractere de `s` é `g`
c. Os dois primeiros caracteres de `s` são `g` e `a`
d. O penúltimo caractere de `s` é `x`
e. O caractere do meio de `s` é `d`
f. O primeiro e último caracteres da string `s` são iguais
g. Os 4 últimos caracteres da string `s` correspondem à string `'tion'`

Nota: Essas sete instruções devem ser avaliadas
como `True`, `False`, `False`, `False`, `True`, `False` e `False`, respectivamente.

### Exercício 42 (LP2.16)

Escreva as instruções de atribuição Python correspondentes a:

a. Atribuir 6 à variável `a` e 7 à variável `b`.
b. Atribuir à variável `c` a média das variáveis `a` e `b`.
c. Atribuir à variável estoque a lista contendo as
strings `'papel'`, `'grampos'` e `'lápis'`.
d. Atribuir às variáveis `primeiro`, `meio` e `último` as
strings 'John'`, 'Fitzgerald'` e `'Kennedy'`.
e. Atribuir à variável `nomecompleto` a concatenação das variáveis de
string `primeiro`, `meio` e `último`. Lembre-se de incorporar os espaços em branco de modo apropriado.


### Exercício 43 (LP2.18)

Escreva instruções Python correspondentes ao seguinte:
a. Atribua à variável `flores` uma lista contendo as
strings `'rosa'`, `'buganvília'`, `'iúca'`, `'margarida'`, `'dália'` e `'lírio`
dos vales'.
b. Escreva uma expressão Booleana que é avaliada como `True` se a
string `'batata'` estiver na lista `flores` e avalie a expressão.
c. Atribua à lista `espinhosas` a sublista da lista `flores` consistindo nos três primeiros objetos na lista.
d. Atribua à lista `venenosas` a sublista da lista `flores` consistindo apenas no último
objeto da lista `flores`.
e. Atribua à lista `perigosas` a concatenação das listas `espinhosas` e venenosas.

### Exercício 44 (LP2.19)

Um alvo de dardos de raio 10 e a parede em que está pendurado são representados usando o sistema de coordenadas bidimensionais, com o centro do alvo na coordenada (0,0). As variáveis `x` e `y` armazenam as coordenadas x e y de um lançamento de dardo. Escreva uma expressão usando as variáveis `x` e `y` que avalia como `True` se o dardo atingir o (estiver dentro do) alvo, e avalie a expressão para estas coordenadas do dardo:

a. (0, 0)
b. (10, 10)
c. (6, –6)
d. (–7, 8)

### Exercício 45 (LP2.20)

Uma escada encostada diretamente contra uma parede cairá a menos que colocada em um certo ângulo menor que 90 graus. Dadas as variáveis comprimento e `ângulo` armazenando o
comprimento da escada e o ângulo que ela forma com o solo enquanto encostada na parede,
escreva uma expressão Python envolvendo `comprimento` e `ângulo`, que calcule a altura
alcançada pela escada. Avalie a expressão para estes valores de `comprimento` e `ângulo`:

a. 16 pés e 75 graus
b. 20 pés e 0 graus
c. 24 pés e 45 graus
d. 24 pés e 80 graus

Nota: Você precisará usar a fórmula trigonométrica: A função `sin()` do módulo `math` toma sua entrada em radianos. Assim, você precisará
converter o ângulo dado em graus para o ângulo dado em radianos, usando:

TODO: inserir fórmula

### Exercício 46 (LP2.23)

O intervalo de uma lista de números é a maior diferença entre dois números quaisquer na
lista. Escreva uma expressão em Python que calcule o intervalo de uma lista de números `lst`. Se
a lista `lst` for, digamos, `[3, 7, -2, 12]`, a expressão deverá ser avaliada como 14 (a diferença entre 12 e –2).

### Exercício 47 (LP2.24)

Escreva a expressão ou instrução Python relevante, envolvendo uma lista de números `lst` e
usando operadores e métodos de lista para estas especificações.
a. Uma expressão que é avaliada como o índice do elemento do meio de `lst`
b. Uma expressão que é avaliada como o elemento do meio de `lst`
c. Uma instrução que classifica a lista `lst` em ordem decrescente
d. Uma instrução que remove o primeiro número da lista `lst` e o coloca no final

### Exercício 48 (LP2.25)

Acrescente um par de parênteses a cada expressão de modo que ela seja avaliada como `True`.
a. `0 == 1 == 2`
b. `2 + 3 == 4 + 5 == 7`
c. `1 < –1 == 3 > 4`

Para cada expressão, explique em que ordem os operadores foram avaliados.

### Exercício 49 (LP3.17)

Suponha que `a`, `b` e `c` tenham sido definidas no shell interativo conforme mostrado:

```
>>> a, b, c = 3, 4, 5
```

Dentro do shell interativo, escreva instruções `if` que exibem `'OK'` se:

a. `a` for menor que `b`.
b. `c` for menor que `b`.
c. A soma de `a` e `b` for igual a `c`.
d. A soma dos quadrados de `a` e `b` for igual ao quadrado de `c`.

### Exercício 50 (LP3.18)

Repita o exercício anterior com o requisito adicional de que `'NÃO OK'` é exibido na tela se a condição for falsa.

### Exercício 51 (FK1.1)

Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:

Exemplo:

* Entrada de Dados: `Digite o valor correspondente ao lado de um quadrado: 3`
* Saída de Dados: `perímetro: 12 - área: 9`

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez

### Exercício 52 (FK1.2)

Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

	Entrada de Dados:

```
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7
```

	Saída de Dados:

```
A média aritmética é 5.5
```

**Dica: uso do print**

Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente espaços entre os argumentos impressos. Cuidado para não incluir espaços demais na sua resposta! O corretor perceberá e tirará pontos

```
>>>print("uma coisa", "outra coisa")
uma coisa outra coisa
>>>print("aqui tem ", 2, "espaços")
aqui tem  2 espaços
```

### Exercício 53 (FK2.1)

Par ou ímpar?

Receba um número inteiro na entrada e imprima `par` quando o número for par ou `ímpar` quando o número for ímpar.

### Exercício 54 (FK3.2) - FizzBuzz parcial, parte 1

Receba um número inteiro na entrada e imprima `Fizz` se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

### Exercício 55 (FK3.3) - FizzBuzz parcial, parte 2

Receba um número inteiro na entrada e imprima `Buzz` se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

### Exercício 56 (FK3.4) - FizzBuzz parcial, parte 3

Receba um número inteiro na entrada e imprima `FizzBuzz` na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

### Exercício 57 (FK3.5) - Verificando ordenação

Receba 3 números inteiros na entrada e imprima `crescente` se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente.

### Exercício 58 (LPP3.1)

Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula

TODO: inserir fórmula

Seu programa deverá ser executado da seguinte forma:

```
>>>
Digite a temperatura em graus Fahrenheit: 50
A temperatura em graus Celsius é 10.0
```

### Exercício 59 (LPP3.4)

Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string). O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos. Dependendo do resultado, uma mensagem apropriada deverá ser impressa. Não importando o resultado, sua
função deverá exibir 'Fim.' antes de terminar. Aqui está um exemplo de um login bem-sucedido:

```
>>>
Login: joe
Você entrou!
Fim.
```

E aqui está um que não tem sucesso:

```
>>>
Login: john
Usuário desconhecido.
Fim.
```

### Exercício 60 (LP3.26)

Implemente um programa que solicita um inteiro `n` do usuário e imprime na tela os quadrados de todos os números de 0 até, mas não incluindo, `n`.

```
>>>
Digite n: 4
0
1
4
9
```
### Exercício 61 (LP3.27)

Implemente um programa que solicita um inteiro positivo `n` e exibe na tela todos os divisores positivos de `n`. Note que 0 não é um divisor de qualquer inteiro, e que `n` é divisível por si mesmo.

```
>>>
Digite n: 49
1
7
49
```

### Exercício 62 (LP3.28)

Implemente um programa que solicita quatro números (inteiros ou ponto flutuante) do usuário.
Seu programa deverá calcular a média dos três primeiros números e comparar a média com o
quarto número. Se elas forem iguais, seu programa deverá exibir 'Igual' na tela.

```
>>>
Digite o primeiro número: 4.5
Digite o segundo número: 3
Digite o terceiro número: 3
Digite o quarto número: 3.5
Igual
```

### Exercício 63 (LP3.29)

Implemente um programa que solicita ao usuário que entre com as coordenadas x e y (cada
um entre –10 e 10) de um dardo e calcula se o dardo atingiu o alvo, um círculo com centro (0,0)
e raio 8. Se tiver atingido, a string `Está dentro!` deverá ser exibida na tela.

```
>>>
Digite x: 2.5
Digite y: 4
Está dentro!
```

### Exercício 64 (LP3.30)

Escreva um programa que solicita um inteiro positivo de quatro dígitos do usuário e exibe
seus dígitos. Você não poderá usar as operações do tipo de dados string para realizar essa tarefa.
Seu programa deverá simplesmente ler a entrada como um inteiro e processá-la como um inteiro,
usando as operações aritméticas padrão (+, \*, -, /, % etc.).

```
>>>
Digite n: 1234
1
2
3
4
```

### Exercício 65 (LPP3.5)

Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.

```
>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare
pote
```

### Exercício 66 (FK4.1) - Quantas vezes o código abaixo imprimirá “Olá Mundo!”?

```
count = 0
while (count <= 10):
	print (count, "Olá Mundo!")
	count = count + 1
```

### Exercício 67 (FK4.2) - O que faz o trecho de programa abaixo?

```
x = 10
while not (x == 0):
	x = x-1
	if x % 2 != 0:
  	print(x)
```

* Imprime os números de 10 a 0.
* não imprime nada.
* imprime apenas os pares menores que 10.
* imprime apenas os ímpares menores que 10.

### Exercício 68 (FK4.3)

Analise o trecho de programa abaixo e responda: quantas vezes os comandos representados aqui por "iteração" serão executados?

Observe que, se você tentar executar este trecho no interpretador, ele dará erro pois o valor de "n" não está definido. Considere que "n" é uma variável que armazena um valor inteiro positivo e assinale a alternativa correta.

```
i = 1
while i < n:
  	"iteração"
  	i = i + 1
```

* n + 1
* 2 * n
* n - 1
* n

### Exercício 69 (FK4.4)

O que faz o programa abaixo?

```
terminou = False
p = i = 0

while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)
```

* Lê dez números e conta a quantidade de números pares e ímpares digitados pelo usuário. No final, imprime o resultado.
* Conta a quantidade de números pares e ímpares digitados pelo usuário e imprime o resultado após o usuário digitar 0 (zero)
* Verifica se um determinado número é par ou ímpar. Caso seja 0 (zero), ele informa ao usuário que ele é neutro.
* De um conjunto de n números, imprime se há números pares e ímpares ou não.

### Exercício 70 (LPP3.6)

Escreva o laço `for` que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python.

a. Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
b.  Inteiros de 0 a 1 (isto é, 0, 1).

A função `range()` também pode ser usada para percorrer sequências de números mais complexas. Se quisermos que a sequência comece em determinado número diferente de zero `início` e termine antes do número `fim`, fazemos com que a função
chame `range(início, fim)`. Por exemplo, esse laço `for` percorre a sequência 2, 3, 4:

```
>>> for i in range(2, 5):
print(i)
2
3
4
```

### Exercício 71 (LPP3.7)

Escreva um laço `for` que exiba a seguinte sequência de números, um por linha.

a. Inteiros de 3 até 12, inclusive este.
b.  Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto
é, 0, 2, 4, 6, 8).
c.  Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
d.  Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.

### Exercício 72 (LP3.19)

Escreva um laço `for` que percorra uma lista de strings `lst` e exiba os três primeiros caracteres de cada palavra. Se `lst` for a lista `['Janeiro' , 'Fevereiro' , 'Março']`,
então o seguinte deve ser exibido na tela:

```
Jan
Fev
Mar
```

### Exercício 73 (LP3.20)

Escreva um laço `for` que percorre uma lista de números `lst` e exibe na tela os números na lista cujo quadrado seja divisível por 8. Por exemplo, se `lst` for `[2, 3, 4, 5, 6, 7, 8, 9]`, então os números 4 e 8 devem ser exibidos.

### Exercício 74 (LP3.21)

Escreva laços `for` que usam a função `range()` e exibem as seguintes sequências:

a. 0 1
b. 0
c. 3 4 5 6
d. 1
e. 0 3
f. 5 9 13 17 21

### Exercício 75 (FK5.1)

Escreva um programa que receba um número natural n n n na entrada e imprima n! n! n! (fatorial) na saída.

Exemplo:

```
Digite o valor de n: 5
120
```

Dica: lembre-se que o fatorial de 0 vale 1!


### Exercício 76 (FK5.2)

Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

Exemplo:

```
Digite o valor de n: 5
1
3
5
7
9
```

### Exercício 77 (FK5.3)

Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

```
Digite um número inteiro: 123
6
```

Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.


### Exercício 78 (LP3.22)

Implemente um programa que solicita uma lista de palavras do usuário e depois exibe cada
palavra na lista que não seja `'segredo'`.

```
>>>
Digite lista de palavras: ['cia', 'segredo', 'mi6', 'isi', 'segredo']
cia
mi6
isi
```

### Exercício 79 (LP3.23)

Implemente um programa que solicita uma lista de nomes de aluno do usuário e exiba aqueles nomes que começam com as letras de A até M.

```
>>>
Digite a lista: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
Ellie
Gavin
```

### Exercício 80 (LP3.24)

Implemente um programa que solicite uma lista não vazia do usuário e exiba na tela uma
mensagem mostrando o primeiro e o último elemento da lista.

```
>>>
Digite uma lista: [3, 5, 7, 9]
O primeiro elemento da lista é 3
O último elemento da lista é 9
```

### Exercício 81 (LP3.25)

Implemente um programa que solicita um inteiro positivo n do usuário e exiba os quatro primeiros múltiplos de `n`:

```
>>>
Digite n: 5
0
5
10
15
```

### Exercício 82 (FK6.1)

Qual será o resultado apresentado pelo programa abaixo?

```
multiplica (a, b):
	return a * b

print(multiplica(4,5))
```

* 4 * 5 = 20
* 20
* multiplica(4,5)
* Dará um erro de sintaxe



### Exercício 83 (FK6.2)

O que o código abaixo irá imprimir?

```
def troca(x, y):
	aux = x
	x = y
	y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)
```

* x = 20 e y = 10
* Todas as opções estão erradas
* x = 10 e y = 10
* x = 10 e y = 20
* x = 20 e y = 20


### Exercício 84 (FK6.3)

Assinale qual (ou quais) das opções abaixo apresenta a função que retorna a soma dos comprimentos de 3 palavras ou frases:

* ```
def total_Caracteres (x, y, z):
	return len(x)+len(y)+len(z)
```
* ```
def total_Caracteres (x, y, z):
	return sum(len(x,y,z))
```
* ```
def total_Caracteres (x, y, z):
	return len(x,y,z)
```
* ```
def total_Caracteres (x, y, z):
	return sum(len(x)+len(y)+len(z))
```

### Exercício 85 (FK6.4)

O quê a função abaixo devolve? O que é math?

```
import math

def suspense(x):
	return math.sqrt(x)
```

* Todas as opções estão erradas.
* Devolve o quadrado de x. "math" é um módulo
* Devolve a raiz quadrada de x. "math" é uma função
* Devolve o quadrado de x. "math" é uma função
* Devolve a raiz quadrada de x. "math" é um módulo

### Exercício 86 (FK6.5)

Se você tivesse que resolver o seguinte exercício:

"Desenvolva uma função que devolva um número lido, maior que zero", qual(is) das opções abaixo resolveria(m) seu problema?

* ```
import math

def suspense(x):
	return math.sqrt(x)

```
* ```
leitura():
	x = -1
	while x <= 0:
    	x = int(input("Digite um valor: "))
	return x
```
* ```
def leitura():
	x = -1
	while x > 0:
    	x = int(input("Digite um valor: "))
	return x
```
* ```
leitura():
	x = -1
	while x > 0:
    	x = int(input("Digite um valor: "))
	return x
```
* ```
def leitura():
	x = int(input("Digite um valor: "))
	while x <= 0:
    	x = int(input("Digite um valor: "))
	return x
```


### Exercício 87 (FK6.6)

Assinale as afirmações CORRETAS:

* Parâmetros de uma função são valores que ela recebe para trabalhar
* A função pode receber ou não parâmetros
* return é usado para a função devolver um determinado valor para quem a chamou
* A função pode ou não devolver valor
* Em código bem feito, o nome da função deve representar a tarefa que ela irá executar

### Exercício 88 (LPP3.8)

Defina, diretamente no shell interativo, a função `média()`, que aceita dois números como entrada e retorna a média dos números. Um exemplo de uso é:

```
>>> average(2, 3.5)
```

### Exercício 89 (LPP3.9)

Implemente a função `perímetro()`, que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua implementação em um módulo chamado `perímetro.py`. Um exemplo de uso é:

```
>>> perimeter(1)
6.283185307179586
```


### Exercício 90 (LPP3.10)

Escreva a função `negativos()`, que aceita uma lista como entrada e exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada.

```
>>> negativos([4, 0, -1, -3, 6, -9])
-1
-3
-9
```

### Exercício 91 (FK7.1) - Máximo

Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:

```
>>> maximo(3, 4)
4
>>> maximo(0, -1)
0
```

### Exercício 92 (FK7.2) - Primos

Escreva a função `maior_primo` que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:

```
>>> maior_primo(100)
97
>>> maior_primo(7)
7
```

Dica: escreva uma função `éPrimo(k)` e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.


### Exercício 93 (FK7.3) - Vogais

Escreva a função `vogal` que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python

```
>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True
```

Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.


### Exercício 94 (FK8.1)

Escreva um programa que recebe como entradas (utilize a função `input`) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

Por exemplo:

```
digite a largura: 10
digite a altura: 3
##########
#    	#
##########
```

Dica: lembre-se que a função print pode receber um parâmetro 'end', que altera o último caractere da cadeia, tornando possível a remoção da quebra de linha (reveja as vídeo-aulas)


### Exercício 95 (FK8.2)

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:
```
digite a largura: 2
digite a altura: 2
##
##
```

### Exercício 96 (AD3.1)

Escreva uma função chamada `right_justify`, que receba uma string chamada `s` como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:
```
>>> right_justify('monty')
                                                                  monty
```

Dica: Use concatenação de strings e repetição. Além disso, o Python oferece uma função
integrada chamada `len`, que apresenta o comprimento de uma string, então o valor de `len('monty')` é 5.

### Exercício 97 (AD3.2)

Uma função também pode ser vista com um valor que pode ser atribuído a uma variável ou passado como
argumento. Por exemplo, `do_twice` é uma função que toma uma função como
argumento e a chama duas vezes:
```
def do_twice(f):
    f()
    f()
```

Aqui está um exemplo que usa `do_twice` para chamar uma função chamada `print_spam` duas vezes:
```
def print_spam():
    print('spam')
    do_twice(print_spam)
```

1. Digite este exemplo em um script e teste-o.
2. Altere do\_twice para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como um argumento.
3. Copie a definição de `print_twice` que aparece anteriormente neste capítulo no seu
script.
4. Use a versão alterada de `do_twice` para chamar `print_twice` duas vezes, passando `'spam'` como um argumento.
5. Defina uma função nova chamada `do_four` que receba um objeto de função e um valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.

*Solução: [do\_four.py](http://thinkpython2.com/code/do\_four.py).*

### Exercício 98 (AD3.3)

Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros
recursos que aprendemos até agora.

1. Escreva uma função que desenhe uma grade como a seguinte:

```
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

```

Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de
valores separados por vírgula: `print('+', '-')`

Por padrão, print avança para a linha seguinte, mas podemos ignorar esse
comportamento e inserir um espaço no fim, desta forma:

```
python print('+', end='')
print('-')
```

A saída dessas instruções é `+ -`. Uma instrução `print` sem argumento
termina a linha atual e vai para a próxima linha.

2. Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.

*Solução: [grid.py](http://thinkpython2.com/code/grid.py).*

Crédito: Este exercício é baseado em outro apresentado por Oualline, em Practical C Programming, Third Edition, O’Reilly Media, 1997.

### Exercício 99 (FK9.1) - Removendo elementos repetidos

Escreva a função `remove_repetidos` que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar `lista.sort() ou `sorted(lista)`. Qual a diferença?

Exemplo:

```
>>>lista = [2, 4, 2, 2, 3, 3, 1]
>>>remove_repetidos(lista)
[1, 2, 3, 4]
>>>remove_repetidos([1, 2, 3, 3, 3, 4])
[1, 2, 3, 4]
```

### Exercício 100 (FK9.2) - Soma dos elementos de uma lista

Escreva a função `soma_elementos` que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

### Exercício 101 (AD10.1)

Escreva uma função chamada `nested_sum` que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:

```
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum
21
```

### Exercício 102 (AD10.2)

Escreva uma função chamada `cumsum` que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Por exemplo:

```
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
```

### Exercício 103 (AD10.3)

Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos. Por exemplo:

```
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
```

### Exercício 104 (AD10.4)

Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne `None`. Por exemplo:

```
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
```

### Exercício 105 (AD10.5)

Escreva uma função chamada `is_sorted` que tome uma lista como parâmetro e retorne `True` se a lista estiver classificada em ordem ascendente, e False se não for o caso. Por exemplo:

```
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
```

### Exercício 106 (AD10.6)

Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra.
Escreva uma função chamada `is_anagram` que tome duas strings e retorne `True` se forem anagramas.

### Exercício 107 (AD10.7)

Escreva uma função chamada `has_duplicates` que tome uma lista e retorne `True` se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

### Exercício 108 (LP3.31)

Implemente a função `inverte_string()` que aceita como entrada uma string de três letras e retorne a string com seus caracteres invertidos.

```
>>> inverte_string('abc')
'cba'
>>> inverte_string('dna')
'and'
```

### Exercício 109 (LP3.32)

Implemente a função `pagar()` que toma como entrada dois argumentos: um salário horário
e o número de horas que um empregado trabalhou na última semana. Sua função deverá calcular
e retornar o pagamento do empregado. Quaisquer horas trabalhadas além de 40 é hora extra, e
deve ser paga a 1,5 vez o salário horário normal.

```
>>> pagar(10, 10)
100
>>> pagar(10, 35)
350
>> pagar(10, 45)
475
```

### Exercício 110 (LP3.33)

A probabilidade de conseguir n caras em sequência ao lançar uma moeda não
viciada n vezes é 2<sub>-n</sub>. Implemente a função `prob()` que aceita um inteiro não negativo n como
entrada e retorna a probabilidade de n caras em seguida ao lançar uma moeda não viciada n vezes.

```
>>> prob(1)
0.5
>>> prob(2)
0.25
```

### Exercício 111 (LP3.34)

Implemente a função `inverte_int()` que aceita um inteiro de três dígitos como entrada
e retorna o inteiro obtido invertendo seus dígitos. Por exemplo, se a entrada for 123, sua função
deverá retornar 321. Você não poderá usar operações do tipo de dado de string para realizar essa
tarefa. Seu programa deve simplesmente ler a entrada como um inteiro e processá-la como um
inteiro usando operadores como // e %. Você pode considerar que o inteiro informado não
termina com o dígito 0.

```
>>> inverte_int(123)
321
>>> inverte_int(908)
809
```

### Exercício 112 (LP3.35)

Implemente a função pontos() que aceita como entrada quatro números x<sub>1</sub> , y<sub>1</sub>, x<sub>2</sub> , y<sub>1</sub>, que são as coordenadas de dois-pontos (x<sub>1</sub>, y<sub>1</sub>) e (x<sub>2</sub>,, y<sub>2</sub>) no plano. Sua função deverá calcular:

* A inclinação da linha passando pelos pontos, a menos que a linha seja vertical.
* A distância entre os dois-pontos.

Sua função deverá exibir a inclinação e a distância calculadas no formato a seguir. Se a linha for
vertical, o valor da inclinação deverá ser a string 'infinito'. Nota: Não se esqueça de
converter os valores de inclinação e distância para uma string antes de exibi-los.

```
>>> pontos(0, 0, 1, 1)
A inclinação é 1.0 e a distância é 1.41421356237
>>> pontos(0, 0, 0, 1)
A inclinação é infinita e a distância é 1.0
```

### Exercício 113 (FK10.1)

Observe as linhas de comandos abaixo:

```
a = "cavalo"
b = "cachorro"
c = "gato"
d = "cachorro"
```


Assinale as alternativas CORRETAS:

* O comando “a is c” dará como resultado False.
* O comando “a is b” dará como resultado True.
* O comando “d is b” dará como resultado False.
* O comando “c is a” dará como resultado True.
* O comando “b is d” dará como resultado True.

### Exercício 114 (FK10.2)

Observe as linhas de comandos abaixo:

```
lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]
```

Assinale as alternativas CORRETAS:

* O comando “lista1 is lista3” dará como resultado False.
* O comando “lista2 == lista1” dará como resultado True.
* O comando “lista1 is lista2” dará como resultado False.
* O comando “lista3 == lista1” dará como resultado True.
* O comando “lista2 is lista3” dará como resultado True.
* O comando “lista3 is lista2” dará como resultado True.



### Exercício 115 (LP3.36)

Implemente a função `abreviação()` que aceita um dia da semana como entrada e retorna
sua abreviação em três letras.

```
>>> abreviação('Terça-feira')
'Ter'
```

### Exercício 116 (LP3.37)

A função de jogo de computador `collision()` verifica se dois objetos circulares colidem; ela retorna `True` se eles colidirem e `False` se não colidirem. Cada objeto circular será dado pelo seu raio e as coordenadas (x, y) do seu centro. Assim, a função apanhará seis números
como entrada: as coordenadas (x1, y1) do centro e o raio r1 do primeiro círculo, e as coordenadas
(x2, y2) do centro e o raio r2 do segundo círculo.

```
>>> colisão(0, 0, 3, 0, 5, 3)
True
>>> colisão(0, 0, 1.4, 2, 2, 1.4)
False
```

### Exercício 117 (LP3.38)

Implemente a função `partição()` que divide uma lista de jogadores de futebol em dois
grupos. Mais precisamente, ela toma uma lista de nomes (strings) como entrada e exibe os nomes
dos jogadores de futebol cujo nome começa com uma letra entre A e M, inclusive.

```
>>> partição(['Elano', 'Edinho', 'Silas', 'Obina', 'Gerson'])
Elano
Edinho
Gerson
>>> partição(['Neymar', 'Silas', 'Obina'])
>>>
```

### Exercício 118 (LP3.39)

Escreva a função `inverteNome()`, que aceita como entrada uma string na forma `'Nome Sobrenome'` e retorna uma string na forma `'Sobrenome, N.'`. (Somente a letra inicial deverá ser exibida para o nome.)

```
>>> inverteNome('João Lourenço')
'Lourenço, J.'
>>> inverteNome('Alberto Carlos')
'Carlos, A.'
```

### Exercício 119 (LP3.40)

Implemente a função `med()`, que aceita como entrada uma lista que contém listas de números. Cada lista de números representa as notas que determinado aluno recebeu para um curso. Por exemplo, aqui está uma lista de entrada para uma classe de quatro alunos:
```
[[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]
```

A função `avg` deverá exibir, uma por linha, a nota média de cada aluno. Você pode considerar
que cada lista de notas não é vazia, mas não deve considerar que todo aluno tem o mesmo número
de notas.

```
>>> med([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])
90.0
60.0
87.0
11.0
```

### Exercício 120 (LP3.41)

A função de jogo de computador `acerto()` utiliza cinco números como entrada: as
coordenadas x e y do centro e o raio de um círculo C, e as coordenadas x e y de um ponto P. A
função deverá retornar `True` se o ponto P estiver dentro ou sobre o círculo C e `False` caso contrário.

```
>>> acerto(0, 0, 3, 3, 0)
True
>>> acerto(0, 0, 3, 4, 0)
False
```

### Exercício 121 (LP3.42)

Implemente a função `ion2e()` que aceita uma string como entrada e retorna uma cópia da palavra de volta com a seguinte mudança: se a palavra informada terminar com 'ion',
então 'ion' é substituído por 'e'.

```
>>> ion2e('congratulation')
'congratulate'
>>> ion2e('maratona')
'Maratona'
```

### Exercício 122 (LP3.43)

Escreva uma função `distância()` que tome como entrada um número: o tempo decorrido (em segundos) entre o raio e o som do trovão. Sua função deverá retornar a distância até o local
em que o raio atinge o solo em quilômetros. Sabe-se que a velocidade do som é de
aproximadamente 340,29 metros por segundo e que há 1000 metros em um quilômetro.

```
>>> distância(3)
1.0208700000000002
>>> distância(6)
2.0417400000000003
```

### Exercício 123 (LP4.12)

Comece executando, no shell interativo, esta instrução de atribuição:

```
>>> s = 'abcdefghijklmnopqrstuvwxyz'
```

Agora, usando a string `s` e o operador de indexação, escreva expressões que sejam avaliadas
como `'bcd'`, `'abc'`, `'defghijklmnopqrstuvwx'`, `'wxy'` e `'wxyz'`.

### Exercício 124 (LP4.13)

Considere que a string s seja definida como: `s = 'goodbye'`. Escreva expressões booleanas em Python que correspondam a estas proposições:

a. O pedaço que consiste no segundo e terceiro caracteres de `s` seja `'bc'`.
b. O pedaço que consiste nos primeiros 14 caracteres de `s` seja `'abcdefghijklmn'`.
c. O pedaço de `s` excluindo os primeiros caracteres seja `'opqrstuvwxyz'`.
d. O pedaço de `s` excluindo o primeiro e o último caracteres
seja `'bcdefghijklmnopqrstuvw'`.

### Exercício 125 (LP4.14)

Traduza cada linha para uma instrução Python:

a.  Atribua à variável `log` a string a seguir, que por acaso é o fragmento de um log para uma solicitação de um arquivo de texto de um servidor Web: `128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"`
b. Atribua à variável `endereco` a substring de `log` que termina antes do primeiro
espaço em branco em `log`, usando o método de string `split()` e o operador de
indexação sobre a string `log`.
c.  Atribua à variável `data` o pedaço da string `log` contendo a data `(12/Feb ... - 6000)`, usando o operador de indexação sobre a string `log`.

### Exercício 126 (LP4.15)

Para cada um dos valores de string de `s` a seguir, escreva a expressão envolvendo `s` e o
método de string `split()` que é avaliado para a lista: `['10', '20', '30', '40', '50', '60']`
a. `s = '10 20 30 40 50 60'`
b. `s = '10,20,30,40,50,60'`
c. `s = '10&20&30&40&50&60'`
d. `s = '10 - 20 - 30 - 40 - 50 - 60'`

### Exercício 127 (LP4.16)

Implemente um programa que solicite três palavras (strings) do usuário. Seu programa deverá exibir o valor booleano `True` se as palavras forem inseridas na ordem do dicionário; caso contrário, nada é exibido.

```
Digite primeira palavra: baiacu
Digite segunda palavra: salmão
Digite terceira palavra: tucunaré
True
```

### Exercício 128 (LP4.17)

Traduza cada linha para uma instrução Python usando métodos de string:

a.  Atribua à variável mensagem a string `'O segredo desta mensagem é que a mensagem é secreta'`.
b.  Atribua à variável `tamanho` o tamanho da string mensagem, usando o operador `len()`.
c.  Atribua à variável `conta` o número de vezes que a substring `'secreta'` aparece na string mensagem, usando o método count().
d.  Atribua à variável `censurado` uma cópia da string mensagem com cada ocorrência da substring `'mensagem'` substituída por `'xxxxxxxx'`, usando o
método replace().

### Exercício 129 (LP4.18)

Suponha que a variável `s` tenha sido atribuída desta maneira:

```
s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ...'''
```

(O início de A Tale of Two Cities [Um conto de duas cidades], de Charles Dickens.) Depois, faça
o seguinte, em ordem, a cada vez:

a.  Escreva uma sequência de instruções que produzam uma cópia de `s`,
chamada `novaS`, na qual os caracteres `.`,`,`, `;` e `\n` sejam substituídos por espaços em branco.
b. Remova os espaços em branco iniciais e finais em `novaS` (e chame a nova string de `novaS`).
c. Torne todos os caracteres em `novaS` minúsculos (e chame a nova string de `novaS`).
d. Calcule o número de ocorrências em `novaS` da string `'it was'`.
e. Mude cada ocorrência de `was` para `is` (e chame a nova string de `novaS`).
f. Divida `novaS` em uma lista de palavras e chame a lista de `listaS`.

### Exercício 130 (LP4.19)

Escreva instruções Python que exibam as saídas formatadas a seguir usando as variáveis já atribuídas `primeiro`, `meio` e `último`:

```
>>> primeiro = 'Marlena'
>>> meio = 'Sigel'
>>> último = 'Mae'
```

a. Sigel, Marlena Mae
b. Sigel, Marlena M.
c. Marlena M. Sigel
d. M. M. Sigel

### Exercício 131 (LP4.20)

Dados os valores de string para o remetente, destinatário e assunto de um e-mail, escreva uma expressão em formato de string que use as variáveis remetente, destinatário e assunto e que exiba conforme o trecho a seguir:

```
>>> remetente = 'tim@abc.com'
>>> destinatário = 'tom@xyz.org'
>>> assunto = 'Hello!'
>>> print(???) # preencha
De: tim@abc.com
Para: tom@xyz.org
Assunto: Hello!
```

### Exercício 132 (LP4.21)

Escreva instruções Python que exibam os valores de pi e a constante de Euler e nos formatos mostrados:

a. `pi = 3.1, e = 2.7`
b. `pi = 3.14, e = 2.72`
c. `pi = 3.141593e+00, e = 2.718282e+00`
d. `pi = 3.14159, e = 2.71828`

### Exercício 133 (LP4.22)

Escreva uma função `mês()` que aceite um número entre 1 e 12 como entrada e retorne a abreviação em três letras do mês correspondente. Faça isso sem usar uma instrução if, apenas operações de strings. Dica: use uma string para armazenar as abreviações em ordem.

```
>>> mês(1)
'Jan'
>>> mês(11)
'Nov'
```

### Exercício 134 (LP4.23)

Escreva uma função `média()` que não aceite entrada, mas solicite que o usuário entre com uma sentença. Sua função deverá retornar o tamanho médio de uma palavra na sentença.

```
>>> médio()
Digite uma sentença: A sample sentence
5.0
```

### Exercício 135 (LP4.24)

Implemente a função `animar()`, que apanhe como entrada um nome de um time (como uma string) e imprima uma saudação conforme mostramos:

```
>>> animar('Vitória')
Como se soletra campeão?
Eu sei, eu sei!
V I T Ó R I A !
É assim que se soletra campeão!
Vai, Vitória!
```

### Exercício 136 (LP4.25)

Escreva a função `contaVogal()`, que aceita uma string como entrada e conta e exibe o número de ocorrências de vogais na string.

```
>>> contaVogal('Le Tour de France')
a, e, i, o e u aparecem, respectivamente, 1, 3, 0, 1, 1 vezes.
```

### Exercício 137 (LP4.26)

A função de criptografia `crypto()` aceita como entrada uma string (isto é, o nome de um arquivo no diretório ativo). A função deve exibir o arquivo na tela com esta modificação: cada ocorrência da string 'secret' no arquivo deve ser substituída pela string 'xxxxxx'.

Arquivo: [crypto.txt](files/crypto.txt)

```
>>> crypto('crypto.txt')
I will tell you my xxxxxx. But first, I have to explain
why it is a xxxxxx.
And that is all I will tell you about my xxxxxx.
```

### Exercício 138 (AD5.1)

O módulo `time` fornece uma função, também chamada time, que devolve a Hora Média de Greenwich na “época”, que é um momento arbitrário usado como ponto de referência. Em sistemas UNIX, a época é primeiro de janeiro de 1970.

```
>>> import time
>>> time.time()
1437746094.5735958
```

Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e segundos, mais o número de dias desde a época.

### Exercício 139 (AD5.2)

O último teorema de Fermat diz que não existem números inteiros a, b e c tais que `a**n + b**n == c**n` para quaisquer valores de `n` maiores que 2.

1. Escreva uma função chamada `check_fermat` que receba quatro parâmetros – `a`, `b`, `c` e `n` – e verifique se o teorema de Fermat se mantém. Se `n` for maior que 2 e `a**n + b**n == c**n` o programa deve imprimir, `“Holy smokes, Fermat was wrong!”`. Senãoo programa deve exibir `“No, that doesn’t work.”`
2. Escreva uma função que peça ao usuário para digitar valores para `a`, `b`, `c` e `n`, os converta em números inteiros e use `check_fermat` para verificar se violam o teorema de Fermat.

### Exercício 140 (AD5.3)

Se você tiver três gravetos, pode ser que consiga arranjá-los em um triângulo ou não. Por exemplo, se um dos gravetos tiver 12 polegadas de comprimento e outros dois tiverem uma polegada de comprimento, não será possível fazer com que os gravetos curtos se encontrem no meio. Há um teste simples para ver se é possível formar um triângulo para quaisquer três comprimentos:
Se algum dos três comprimentos for maior que a soma dos outros dois, então você não
pode formar um triângulo. Senão, você pode. (Se a soma de dois comprimentos igualar o
terceiro, eles formam um triângulo chamado “degenerado”.)

1. Escreva uma função chamada `is_triangle` que receba três números inteiros como
argumentos, e que imprima `“Yes”` ou `“No”`, dependendo da possibilidade de formar ou não um triângulo de gravetos com os comprimentos dados.
2. Escreva uma função que peça ao usuário para digitar três comprimentos de gravetos,
os converta em números inteiros e use `is_triangle` para verificar se os gravetos com os comprimentos dados podem formar um triângulo.

### Exercício 141 (AD5.4)

Qual é a saída do seguinte programa? Desenhe um diagrama da pilha que mostre o estado do programa quando exibir o resultado.

```
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
```

1. O que aconteceria se você chamasse esta função desta forma: recurse(-1, 0)?
2. Escreva uma docstring que explique tudo o que alguém precisaria saber para usar esta função (e mais nada).

### Exercício 142 (AD6.1)

Desenhe um diagrama da pilha do seguinte programa. O que o programa exibe?

```
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
```

### Exercício 143 (AD6.2)

A função de Ackermann, A(m, n), é definida assim:

![fórmula de ackermann](img/ackermann.png)

Veja também [http://en.wikipedia.org/wiki/Ackermann\_function](http://en.wikipedia.org/wiki/Ackermann_function). Escreva uma função denominada `ack` que avalie a função de Ackermann. Use a sua função para avaliar `ack(3, 4)`, cujo
resultado deve ser 125. O que acontece para valores maiores de m e n?

*Solução: [ackermann.py](http://thinkpython2.com/code/ackermann.py).*

### Exercício 144 (AD6.3)

Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Recursivamente, uma palavra é um palíndromo se a primeira e última letras forem iguais e o meio for um palíndromo.
As funções seguintes recebem uma string como argumento e retornam as letras iniciais, finais e do meio das palavras:

```
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
```

Veremos como funcionam no Capítulo 8.

1. Digite essas funções em um arquivo chamado `palindrome.py` e teste-as. O que acontece se chamar middle com uma string de duas letras? Uma letra? E se a string estiver vazia, escrita com `''` e não contiver nenhuma letra?
2. Escreva uma função chamada `is_palindrome` que receba uma string como
argumento e retorne True se for um palíndromo e False se não for. Lembre-se de que você pode usar a função integrada `len` para verificar o comprimento de uma string.

*Solução: [palindrome\_soln.py](http://thinkpython2.com/code/palindrome_soln.py).*

### Exercício 145 (AD6.4)

Um número `a` é uma potência de `b` se for divisível por `b` e `a/b` for uma potência de `b`. Escreva uma função chamada `is_power` que receba os parâmetros `a` e `b` e retorne `True` se a for uma potência de `b`. *Dica: pense no caso-base*.

### Exercício 146 (AD6.5)

O maior divisor comum (MDC, ou GCD em inglês) de `a` e `b` é o maior número que divide ambos sem sobrar resto.
Um modo de encontrar o MDC de dois números é observar qual é o resto `r` quando `a` é
dividido por `b`, sabendo que `gcd(a, b)` = `gcd(b, r)`. Como caso-base, podemos usar `gcd(a, 0)` = a.

Escreva uma função chamada `gcd` que receba os parâmetros `a` e `b` e devolva o maior divisor comum.
*Crédito: Este exercício é baseado em um exemplo do livro de Abelson e Sussman, Structure and Interpretation of Computer Programs (Estrutura e interpretação de programas de computador, MIT Press, 1996).*

### Exercício 147 (AD7.1)

Copie o loop de “Raízes quadradas” abaixo, e encapsule-o em uma função
chamada `mysqrt` que receba `a` como parâmetro, escolha um valor razoável de `x` e devolva uma estimativa da raiz quadrada de `a`.

```
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
```

Para testar, escreva uma função denominada `test_square_root`, que exibe uma tabela como esta:

```
a   mysqrt(a) 	math.sqrt(a)  diff
- --------- ------------ ----
1.0 1.0       	1.0       	0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0       	2.0       	0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0       	3.0       	0.0

```

A primeira coluna é um número, `a`; a segunda coluna é a raiz quadrada de a calculada com
`mysqrt`; a terceira coluna é a raiz quadrada calculada por `math.sqrt`; a quarta coluna é o
valor absoluto da diferença entre as duas estimativas.

### Exercício 148 (AD7.3)
O matemático Srinivasa Ramanujan encontrou uma série infinita que pode ser usada para
gerar uma aproximação numérica de 1/π:
Fórmula – Aproximação de π pela série de Ramanujan.
Escreva uma função chamada `estimate_pi` que use esta fórmula para computar e devolver uma estimativa de π. Você deve usar o loop while para calcular os termos da
adição até que o último termo seja menor que 1e-15 (que é a notação do Python para 10 ** 15). Você pode verificar o resultado comparando-o com math.pi

### Exercício 149 (AD8.1)

Leia a documentação dos métodos de strings em
http://docs.python.org/3/library/stdtypes.html#string-methods. Pode ser uma boa ideia experimentar alguns deles para entender como funcionam. `strip` e `replace` são especialmente úteis.

A documentação usa uma sintaxe que pode ser confusa. Por exemplo, em `find(sub[, start[, end]])`, os colchetes indicam argumentos opcionais. Então `su` é exigido, mas `start` é opcional, e se você incluir `start`, então `end` é opcional.

### Exercício 150 (AD8.2)

Há um método de string chamado `count`, que é semelhante à função em “Loop e contagem”, na página 123. Leia a documentação deste método e escreva uma invocação que conte o número de letras `'a'` em `‘banana’`.

### Exercício 151 (AD8.3)

Uma fatia de string pode receber um terceiro índice que especifique o “tamanho do passo”; isto é, o número de espaços entre caracteres sucessivos. Um tamanho de passo 2 significa tomar um caractere e outro não; 3 significa tomar um e dois não etc.

```
>>> fruit = 'banana'
>>> fruit[0:5:2]
'Bnn'
```

Um tamanho de passo -1 atravessa a palavra de trás para a frente, então a fatia `[::-1]` gera uma string invertida.
Use isso para escrever uma versão de uma linha de `is_palindrome` do

### Exercício 152 (AD8.4)

As seguintes funções pretendem verificar se uma string contém alguma letra minúscula,
mas algumas delas estão erradas. Para cada função, descreva o que ela faz (assumindo que o parâmetro seja uma string).

```
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
```

### Exercício 153 (AD8.5)

Uma cifra de César é uma forma fraca de criptografia que implica “rotacionar” cada letra por um número fixo de lugares. Rotacionar uma letra significa deslocá-lo pelo alfabeto, voltando ao início se for necessário, portanto ‘A’ rotacionado por 3 é ‘D’ e ‘Z’ rotacionado por 1 é ‘A’.
Para rotacionar uma palavra, faça cada letra se mover pela mesma quantidade de posições.
Por exemplo, “cheer” rotacionado por 7 é “jolly” e “melon” rotacionado por -10 é “cubed”. No filme 2001: Uma odisseia no espaço, o computador da nave chama-se HAL, que é IBM rotacionado por -1.
Escreva uma função chamada `rotate_word` que receba uma string e um número inteiro
como parâmetros, e retorne uma nova string que contém as letras da string original rotacionadas pelo número dado.

Você pode usar a função integrada `ord`, que converte um caractere em um código numérico e `chr`, que converte códigos numéricos em caracteres. As letras do alfabeto são codificadas em ordem alfabética, então, por exemplo:

```
>>> ord('c') - ord('a')
2
```

Porque `'c'` é a “segunda” letra do alfabeto. Mas tenha cuidado: os códigos numéricos de letras maiúsculas são diferentes.

Piadas potencialmente ofensivas na internet às vezes são codificadas em ROT13, que é uma cifra de César com rotação 13. Se não se ofender facilmente, encontre e decifre algumas delas.

### Exercício 154 (LP4.27)

Escreva uma função `fcopy()` que aceite como entrada dois nomes de arquivo (como
strings) e copie o conteúdo do primeiro arquivo para o segundo.

Arquivo: [crypto.txt](files/crypto.txt)

```
>>> fcopy('exemplo.txt','saída.txt')
>>> open('saída.txt').read()
'As 3 linhas desse arquivo terminam com o caractere de nova linha.\n\n
Há uma linha em branco acima desta linha.\n'
```

### Exercício 155 (LP4.28)

Implemente a função `links()` que aceita como entrada o nome de um arquivo HTML
(como uma string) e retorna o número de hyperlinks nesse arquivo. Para fazer isso, você assumirá
que cada hyperlink aparece em uma tag de âncora. Você também precisa saber que cada tag de
âncora termina com a substring</a>.
Teste seu código no arquivo HTML `twolinks.html` ou em qualquer arquivo HTML
baixado da Web para a pasta na qual seu programa se encontra.

Arquivo: [links.html](files/links.html)

```
>>> links('twolinks.html')
2
```

### Exercício 156 (LP4.29)

Escreva uma função `stats()` que aceita um argumento de entrada: o nome de um arquivo
de texto. A função deverá exibir, na tela, o número de linhas, palavras e caracteres no arquivo;
sua função deverá abrir o arquivo apenas uma vez.

Arquivo: (example.txt)(files/example.txt)

```
>>> stats('example.txt')
número de linhas: 3
número de palavras: 20
número de caracteres: 98
```

### Exercício 157 (LP4.30)

Implemente a função `distribuição()`, que aceita como entrada o nome de um arquivo
(como uma string). Esse arquivo de única linha terá notas em forma de letra, separadas por espaços.

Sua função deverá exibir a distribuição de notas, conforme mostrado a seguir.

Arquivo: [grades.txt](files/grades.txt)

```
>>> distribuição('grades.txt')
6 alunos tiveram A
2 alunos tiveram A-
3 alunos tiveram B+
2 alunos tiveram B
2 alunos tiveram B-
4 alunos tiveram C
1 aluno teve C-
2 alunos tiveram F
```

### Exercício 158 (LP4.31)

Implemente a função `duplicata()`, que aceita como entrada a string e o nome de um
arquivo no diretório atual e retorna `True` se o arquivo tiver palavras duplicadas e `False` em
caso contrário.


Arquivo: [Duplicates.txt](files/Duplicates.txt)

Arquivo: [noDuplicates.txt](files/noDuplicates.txt)

```
>>> duplicata('Duplicates.txt')
True
>>> duplicata('noDuplicates.txt')
False
```

### Exercício 159 (LP4.32)

A função `censura()` recebe o nome de um arquivo (uma string) como entrada. A função deverá abrir o arquivo, lê-lo e depois gravá-lo no arquivo `censurado.txt` com esta modificação: cada ocorrência de uma palavra de quatro letras no arquivo deverá ser substituída pela string 'xxxx'.

Arquivo: example.txt

```
>>> censura('example.txt')
```
Observe que essa função não produz saída, mas cria o arquivo censurado.txt na pasta atual.


### Exercício 160 (AD9.1)

Escreva um programa que leia o arquivo [words.txt](http://thinkpython2.com/code/words.txt) e imprima apenas as palavras com mais de 20 caracteres (sem contar whitespace).

### Exercício 161 (AD9.2)

Em 1939, Ernest Vincent Wright publicou uma novela de 50.000 palavras, chamada Gadsby, que não contém a letra “e”. Como o “e” é a letra mais comum em inglês, isso não é algo fácil de fazer.

Na verdade, é difícil até construir um único pensamento sem usar o símbolo mais comum do idioma. No início é lento, mas com prudência e horas de treino, vai ficando cada vez mais fácil.

```
Muito bem, agora eu vou parar.
```

Escreva uma função chamada `has_no_e` que retorne `True` se a palavra dada não tiver a letra “e” nela. Altere seu programa na seção anterior para imprimir apenas as palavras que não têm “e” e calcule a porcentagem de palavras na lista que não têm “e”.

### Exercício 162 (AD9.3)

Escreva uma função chamada `avoids` que receba uma palavra e uma série de letras proibidas, e retorne `True` se a palavra não usar nenhuma das letras proibidas. Altere o código para que o usuário digite uma série de letras proibidas e o programa imprima o número de palavras que não contém nenhuma delas. Você pode encontrar uma combinação de cinco letras proibidas que exclua o menor número possível de palavras?

### Exercício 163 (AD9.5)

Escreva uma função chamada `uses_all` que receba uma palavra e uma série de letras obrigatórias e retorne `True` se a palavra usar todas as letras obrigatórias pelo menos uma vez. Quantas palavras de [words.txt](http://thinkpython2.com/code/words.txt) usam todas as vogais (aeiou)? E que tal aeiouy?

### Exercício 164 (AD9.6)

Escreva uma função chamada `is_abecedarian` que retorne `True` se as letras numa palavra aparecerem em ordem alfabética (tudo bem se houver letras duplas). Quantas palavras em ordem alfabética existem em [words.txt](http://thinkpython2.com/code/words.txt)?

### Exercício 165 (AD9.7)

Esta pergunta é baseada em um quebra-cabeça veiculado em um programa de rádio chamado [Car Talk](http://www.cartalk.com/content/puzzlers):
Dê uma palavra com três letras duplas consecutivas. Vou dar exemplos de palavras que quase cumprem a condição, mas não chegam lá. Por exemplo, a palavra committee, c-o-m-m-i-t-t-e-e. Seria perfeita se não fosse aquele ‘i’ que se meteu ali no meio. Ou Mississippi: M-i-s-s-i-s-s-i-p-p-i. Se pudesse tirar aqueles ‘is’, daria certo. Mas há uma palavra que tem três pares consecutivos de letras e, que eu saiba, pode ser a única palavra que existe. É claro que provavelmente haja mais umas 500, mas só consigo pensar nessa. Qual é a palavra?

Escreva um programa que a encontre.

*Solução: [cartalk1.py](http://thinkpython2.com/code/cartalk1.py).*

### Exercício 166 (AD9.8)

Aqui está outro quebra-cabeça do programa [Car Talk](http://www.cartalk.com/content/puzzlers):

“Estava dirigindo outro dia e percebi algo no hodômetro que chamou a minha atenção. Como a maior parte dos hodômetros, ele mostra seis dígitos, apenas em milhas inteiras. Por exemplo, se o meu carro tivesse 300.000 milhas, eu veria 3-0-0-0-0-0. “Agora, o que vi naquele dia foi muito interessante. Notei que os últimos 4 dígitos eram um palíndromo; isto é, podiam ser lidos da mesma forma no sentido correto e no sentido inverso. Por exemplo, 5-4-4-5 é um palíndromo, então no meu hodômetro poderia ser 3-1- 5-4-4-5. “Uma milha depois, os últimos 5 números formaram um palíndromo. Por exemplo,
poderia ser 3-6-5-4-5-6. Uma milha depois disso, os 4 números do meio, dentro dos 6, formavam um palíndromo. E adivinhe só? Um milha depois, todos os 6 formavam um palíndromo!

“A pergunta é: o que estava no hodômetro quando olhei primeiro?”

Escreva um programa Python que teste todos os números de seis dígitos e imprima qualquer número que satisfaça essas condições.

*Solução: [cartalk2.py](http://thinkpython2.com/code/cartalk2.py).*

### Exercício 167 (AD9.9)

Aqui está outro problema do [Car Talk](http://www.cartalk.com/content/puzzlers) que você pode resolver com uma busca:

“Há pouco tempo recebi uma visita da minha mãe e percebemos que os dois dígitos que compõem a minha idade, quando invertidos, representavam a idade dela. Por exemplo, se ela tem 73 anos, eu tenho 37 anos. Ficamos imaginando com que frequência isto aconteceu nos anos anteriores, mas acabamos mudando de assunto e não chegamos a uma resposta.

“Quando cheguei em casa, cheguei à conclusão de que os dígitos das nossas idades tinham sido reversíveis seis vezes até então. Também percebi que, se tivéssemos sorte, isso aconteceria novamente dali a alguns anos, e se fôssemos muito sortudos, aconteceria mais uma vez depois disso. Em outras palavras, aconteceria 8 vezes no total. Então a pergunta é: quantos anos tenho agora?”

Escreva um programa em Python que busque soluções para esse problema.

**Dica**: pode ser uma boa ideia usar o método de string zfill.

### Exercício 168 (AD10.8)

Este exercício pertence ao assim chamado Paradoxo de aniversário, sobre o qual você pode ler em [http://en.wikipedia.org/wiki/Birthday_paradox](http://en.wikipedia.org/wiki/Birthday_paradox).

Se há 23 alunos na sua sala, quais são as chances de dois deles fazerem aniversário no mesmo dia? Você pode estimar esta probabilidade gerando amostras aleatórias de 23 dias de aniversário e verificando as correspondências. Dica: você pode gerar aniversários aleatórios com a função randint no módulo `random`.

*Se quiser, você pode baixar minha solução em [birthday.py](http://thinkpython2.com/code/birthday.py).*

### Exercício 169 (AD10.9)

Escreva uma função que leia o arquivo [words.txt](http://thinkpython2.com/code/words.txt) e construa uma lista com um elemento por palavra. Escreva duas versões desta função, uma usando o método append e outra usando a expressão t = t + [x]. Qual leva mais tempo para ser executada? Por quê?

*Solução: [wordlist.py](http://thinkpython2.com/code/wordlist.py).*

### Exercício 170 (AD10.10)

Para verificar se uma palavra está na lista de palavras, você pode usar o operador `in`, mas isso seria lento porque pesquisaria as palavras em ordem.
Como as palavras estão em ordem alfabética, podemos acelerar as coisas com uma busca por bisseção (também conhecida como pesquisa binária), que é semelhante ao que você faz quando procura uma palavra no dicionário. Você começa no meio e verifica se a palavra que está procurando vem antes da palavra no meio da lista. Se for o caso, procura na primeira metade da lista. Se não, procura na segunda metade. De qualquer forma, você corta o espaço de busca restante pela metade. Se a lista de palavras tiver 113.809 palavras, o programa seguirá uns 17 passos para encontrar a palavra ou concluir que não está lá.

Escreva uma função chamada `in_bisect` que receba uma lista ordenada, um valor-alvo e devolva o índice do valor na lista se ele estiver lá, ou `None` se não estiver.

Ou você pode ler a documentação do módulo bisect e usá-lo!

*Solução: [inlist.py](http://thinkpython2.com/code/inlist.py).*

### Exercício 171 (AD10.11)

Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva um programa que encontre todos os pares inversos na lista de palavras.

*Solução: [reverse_pair.py](http://thinkpython2.com/code/reverse_pair.py).*

### Exercício 172 (AD10.12)

Duas palavras “interligam-se” quando, ao tomarmos letras alternadas de cada uma, formamos uma palavra nova. Por exemplo, “shoe” e “cold” interligam-se para formar “schooled”.

1. Escreva um programa que encontre todos os pares de palavras que se interligam. Dica: não enumere todos os pares!
2. Você pode encontrar palavras que sejam interligadas de três em três; isto é, cada terceira letra forma uma palavra, começando da primeira, segunda ou terceira?

*Solução: [interlock.py](http://thinkpython2.com/code/interlock.py).*

Crédito: este exercício foi inspirado por um exemplo em http://puzzlers.org.


### Exercício 173 (AD11.1)

Escreva uma função que leia as palavras em [words.txt](http://thinkpython2.com/code/words.txt) e guarde-as como chaves em um dicionário. Não importa quais são os valores. Então você pode usar o operador in como uma forma rápida de verificar se uma string está no dicionário. Se fez o Exercício AD10.10, você pode comparar a velocidade desta implementação com o operador in de listas e a busca por bisseção.

### Exercício 174 (AD11.2)

Leia a documentação do método de dicionário `setdefault` e use-o para escrever uma versão mais concisa de `invert_dict`.

*Solução: [invert_dict](http://thinkpython2.com/code/invert_dict.py)*.

### Exercício 175 (AD11.3)

Memorize a função de Ackermann do Exercício AD6.2 e veja se a memorização permite avaliar a função com argumentos maiores. Dica: não.

*Solução: [ackermann_memo.py](http://thinkpython2.com/code/ackermann_memo.py).*

### Exercício 176 (AD11.4)

Se fez o Exercício AD10.7, você já tem uma função chamada `has_duplicates`, que recebe uma lista como parâmetro e retorna `True` se houver algum objeto que aparece mais de uma vez na lista. Use um dicionário para escrever uma versão mais rápida e simples de `has_duplicates`.

*Solução: [has_duplicates.py](http://thinkpython2.com/code/has_duplicates.py).*

### Exercício 177 (AD11.5)

Duas palavras são “pares rotacionados” se for possível rotacionar um deles e chegar ao outro (ver `rotate_word` no Exercício AD8.5).
Escreva um programa que leia uma lista de palavras e encontre todos os pares
rotacionados.

*Solução: [rotate_pairs.py](http://thinkpython2.com/code/rotate_pairs.py).*

### Exercício 178 (AD11.6)

Aqui está outro quebra-cabeça do programa [Car Talk](http://www.cartalk.com/content/puzzlers):

Ele foi enviado por Dan O’Leary. Dan descobriu uma palavra comum, com uma sílaba e cinco letras que tem a seguinte propriedade única. Ao removermos a primeira letra, as letras restantes formam um homófono da palavra original, que é uma palavra que soa exatamente da mesma forma. Substitua a primeira letra, isto é, coloque-a de volta, retire a segunda letra e o resultado é um outro homófono da palavra original. E a pergunta é, qual é a palavra?

Agora vou dar um exemplo que não funciona. Vamos usar a palavra de cinco letras, ‘wrack’ (mover, eliminar). W-R-A-C-K, como na expressão ‘wrack with pain’ (se contorcer de dor). Se eu retirar a primeira letra, sobra uma palavra de quatro letras, ‘R-A- C-K’ (galhada). Como na frase, ‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’ (‘Minha nossa, você viu a galhada daquele cervo! Deve ter nove pontas!’). É um homófono perfeito. Se puser o ‘w’ de volta e retirar o ‘r’ em vez disso, sobra a palavra ‘wack’, que é uma palavra de verdade, mas não é um homófono das outras duas palavras.
Mas há pelo menos uma palavra que Dan e eu conhecemos, que produz dois homófonos se você retirar qualquer uma das duas primeiras letras, e duas novas palavras de quatro letras são formadas. A pergunta é, qual é a palavra?

Você pode usar o dicionário do Exercício AD11.1 para verificar se uma string está na lista de palavras.

Para verificar se duas palavras são homófonas, você pode usar o Dicionário de pronúncia CMU. Ele pode ser baixado em [http://www.speech.cs.cmu.edu/cgi-bin/cmudict](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) ou em
[http://thinkpython2.com/code/c06d](http://thinkpython2.com/code/c06d). Você também pode baixar [pronouncy.py](http://thinkpy thon2.com/code/pronounce.py), que tem uma função chamada `read_dictionary`, que lê o dicionário de pronúncia e retorna um dicionário de Python que mapeia cada palavra a uma string que descreve sua pronúncia primária.

Escreva um programa que liste todas as palavras que resolvem o quebra-cabeça.

*Solução: [homophone.py](http://thinkpython2.com/code/homophone.py).*

### Exercício 179 (AD12.1)

Escreva uma função chamada `most_frequent` que receba uma string e exiba as letras em ordem decrescente de frequência. Encontre amostras de texto de vários idiomas diferentes e veja como a frequência das letras varia entre os idiomas. Compare seus resultados com
as tabelas em [http://en.wikipedia.org/wiki/Letter\_frequencies](http://en.wikipedia.org/wiki/Letter_frequencies).

*Solução: [most_frequent.py](http://thinkpython2.com/code/most_frequent.py).*

### Exercício 180 (AD12.2)

Mais anagramas!

1. Escreva um programa que leia uma lista de palavras de um arquivo e imprima todos os conjuntos de palavras que são anagramas.

Aqui está um exemplo de como a saída pode parecer:

```
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
```

Dica: você pode querer construir um dicionário que mapeie uma coleção de letras a uma lista de palavras que podem ser soletradas com essas letras. A pergunta é: como representar a coleção de letras de forma que possa ser usada como uma chave?

2. Altere o programa anterior para que exiba a lista mais longa de anagramas primeiro, seguido pela segunda mais longa, e assim por diante.
3. No Scrabble, um “bingo” é quando você joga todas as sete peças na sua mesa, junto com uma peça no tabuleiro, para formar uma palavra de oito letras. Que coleção de oito letras forma o maior número possível de bingos? Dica: há sete.


*Solução: [anagram_sets](http://thinkpython2.com/code/anagram_sets.py).*

### Exercício 181 (AD12.3)

Duas palavras formam um “par de metátese” se você puder transformar uma na outra trocando duas letras, por exemplo, “converse” e “conserve”. Escreva um programa que descubra todos os pares de metátese no dicionário. Dica: não teste todos os pares de palavras e não teste todas as trocas possíveis.

*Solução: [metathesis](http://thinkpython2.com/code/metathesis.py).*

Crédito: este exercício foi inspiradopor um exemplo em http://puzzlers.org.

### Exercício 182 (AD12.4)

Aqui está outro quebra-cabeça do programa [Car Talk](http://www.cartalk.com/content/puzzlers):

Qual é a palavra inglesa mais longa, que permanece uma palavra inglesa válida, conforme vai removendo suas letras, uma após a outra?

Agora, as letras podem ser retiradas do fim ou do meio, mas você não pode reajustar nenhuma delas. Cada vez que remove uma letra, você acaba com outra palavra inglesa. Se fizer isto, eventualmente você acabará com uma letra e isso também será uma palavra inglesa; uma encontrada no dicionário. Quero saber qual é a palavra mais longa e quantas letras tem?

Vou dar um pequeno exemplo modesto: Sprite. Ok? Você começa com sprite, tira uma letra do interior da palavra, tira o r, e ficamos com a palavra spite, então tiramos o e do fim, ficamos com spit, tiramos o s, ficamos com pit, it e I.

Escreva um programa que encontre todas as palavras que podem ser reduzidas desta forma, e então encontre a mais longa.

Este exercício é um pouco mais desafiador que a maioria, então aqui estão algumas sugestões:

1. Você pode querer escrever uma função que receba uma palavra e calcule uma lista de todas as palavras que podem ser formadas retirando uma letra. Esses são os “filhos” da palavra.

2. Recursivamente, uma palavra é redutível se algum de seus filhos for redutível. Como caso base, você pode considerar a string vazia redutível.

3. A lista de palavras que forneci, [words.txt](http://thinkpython2.com/code/words.txt), não contém palavras de uma letra só. Portanto, você pode querer acrescentar “I”, “a”, e a string vazia.

4. Para melhorar o desempenho do seu programa, você pode querer memorizar as palavras conhecidas por serem redutíveis.

*Solução: [reducible.py](http://thinkpython2.com/code/reducible.py).*

### Exercício 183 (LP2.26)

Escreva instruções Python que desenham um quadrado com 100 pixels de lado usando Turtle graphics. Não se esqueça de importar o módulo turtle primeiro. As duas primeiras e a última instrução deverão ser conforme mostrado:

```
>>>s = turtle.Screen() # cria tela
>>>t = turtle.Turtle() # cria tartaruga
... # agora escreve uma sequência de instruções
... # que desenha o quadrado
>>> s.bye() # remove a tela quando termina
```

### Exercício 184 (LP2.27)

Usando a técnica do Exercício 2.26, escreva instruções Python que desenham um losango com 100 pixels de comprimento de lado usando Turtle graphics.

### Exercício 185 (LP2.28)
Usando a técnica do Exercício 2.26, escreva instruções Python que desenham um pentágono com 100 pixels de comprimento de lado usando Turtle graphics. Depois faça um hexágono, um heptágono e um octógono.

### Exercício 186 (LP2.29)

Usando a técnica do Exercício 2.26, escreva instruções Python que desenham os círculos sobrepostos com raio de 100 pixels, mostrados a seguir, usando o Turtle graphics:

Os tamanhos dos círculos não importam; seus centros deverão ser, mais ou menos, os pontos de um triângulo equilátero.

### Exercício 187 (LP2.30)

Usando a técnica do Exercício 2.26, escreva instruções Python que desenham quatro círculos concêntricos semelhantes aos círculos concêntricos de um alvo de dardos.

### Exercício 188 (LP2.31)

Usando Turtle graphics, ilustre o tamanho relativo do sol e da terra desenhando dois círculos. O círculo representando a Terra deverá ter um raio de 1 pixel. O círculo representando o sol deterá
ter um raio de 109 pixels.

### Exercício 189 (LP2.33)

Usando Turtle graphics, desenhe uma estrela de cinco pontas repetindo o seguinte cinco vezes: mova a tartaruga a por 100 pixels e depois gire-a para a direita por 144 graus. Quando terminar, considere como desenhar a estrela de seis pontas (normalmente conhecida como Estrela de Davi).

### Exercício 190 (LP2.34)

Usando Turtle graphics, desenhe uma imagem mostrando os seis lados de um dado. Você pode representar cada lado dentro de um quadrado separado.

### Exercício 191 (LP2.35)

Usando Turtle graphics, desenhe as linhas de uma quadra de basquete. Você pode escolher as especificações da National Basketball Association (NBA) ou da International Basketball Federation (FIBA), que você pode encontrar facilmente na Web.

### Exercício 192 (LP2.36)

Usando Turtle graphics, desenhe uma imagem mostrando as fases (visíveis) da lua conforme vista do seu hemisfério: quarto crescente, lua cheia, quarto minguante, lua nova. Você pode achar ilustrações das fases da lua na Web.

### Exercício 193 (AD4.3.1-5)

A seguir, uma série de exercícios usando TurtleWorld. Eles servem para divertir, mas também têm outro objetivo. Enquanto trabalha neles, pense que objetivo pode ser. As seções seguintes têm as soluções para os exercícios, mas não olhe até que tenha terminado (ou, pelo menos, tentado).

1. Escreva uma função chamada `square` que receba um parâmetro chamado `t`, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe `bob` como um argumento para o square e então execute o programa novamente.
2. Acrescente outro parâmetro, chamado `length`, ao `square`. Altere o corpo para que o comprimento dos lados seja `length` e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o seu programa com uma variedade de valores para length.
3. Faça uma cópia do square e mude o nome para `polygon`. Acrescente outro parâmetro
chamado `n` e altere o corpo para que desenhe um polígono regular de `n` lados.
(Dica: os ângulos exteriores de um polígono regular de `n` lados são 360/`n` graus.)
4. Escreva uma função chamada `circle` que use o turtle, `t` e um raio `r` como parâmetros e desenhe um círculo aproximado ao chamar `polygon` com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de `r`.
(Dica: descubra a circunferência do círculo e certifique-se de que `length * n =
circumference`.)
5. Faça uma versão mais geral do circle chamada `arc`, que receba um parâmetro
adicional de `angle`, para determinar qual fração do círculo deve ser desenhada. `angle` está em unidades de graus, então quando `angle == 360`, o `arc` deve desenhar um círculo completo.

### Exercício 194 (AD4.1)

Baixe o código deste capítulo no site [http://thinkpython2.com/code/polygon.py](http://thinkpython2.com/code/polygon.py).

1. Desenhe um diagrama da pilha que mostre o estado do programa enquanto executa circle (bob, radius). Você pode fazer a aritmética à mão ou acrescentar instruçõesprint ao código.
2. A versão de `arc` na seção 4.7 - Refatoração não é muito necessária porque a aproximação linear do círculo está sempre do lado de fora do círculo verdadeiro. Consequentemente, o Turtle acaba ficando alguns píxeis de distância do destino correto. Minha solução mostra um modo de reduzir o efeito deste erro. Leia o código e veja se faz sentido para você. Se desenhar um diagrama, poderá ver como funciona.

### Exercício 195 (AD4.2)

Escreva um conjunto de funções adequadamente geral que possa desenhar flores como as da figura abaixo.

![flores de tartaruga](img/flores-de-tartaruga.png)

*Solução: [flower.py](http://thinkpython2.com/code/flower.py), também exige
[polygon.py](http://thinkpython2.com/code/polygon.py).

### Exercício 196 (AD4.3)

Escreva um conjunto de funções adequadamente geral que possa desenhar formas como as da figura abaixo.

![tortas de tartaruga](img/tortas-de-tartaruga.png)

Solução: [pie.py](http://thinkpython2.com/code/pie.py).

### Exercício 197 (AD4.4)

As letras do alfabeto podem ser construídas a partir de um número moderado de elementos
básicos, como linhas verticais e horizontais e algumas curvas. Crie um alfabeto que possa
ser desenhado com um número mínimo de elementos básicos e então escreva funções que
desenhem as letras.
Você deve escrever uma função para cada letra, com os nomes `draw_a`, `draw_b` etc., e
colocar suas funções em um arquivo chamado letters.py. Você pode baixar uma “máquina de escrever de turtle” no site (http://thinkpython2.com/code/typewriter.py)[http://thinkpython2.com/code/typewriter.py] para ajudar a
testar o seu código.

Você pode ver uma solução no site (code_letters.py)[http://thinkpython2.com/code/letters.py]; ela também exige (polygon.py)[http://thinkpython2.com/code/polygon.py].

### Exercício 198 (AD4.5)

Leia sobre espirais em https://pt.wikipedia.org/wiki/Espiral; então escreva um programa que desenhe uma espiral de Arquimedes (ou um dos outros tipos).

### Exercício 199 (LP3.44)

(Esse problema é baseado no Problema 2.28.) Implemente a função `polígono()` que
utiliza um número n ≥ 3 como entrada e desenha, usando Turtle graphics, um polígono regular
com n lados.

### Exercício 200 (LP3.45)

Usando Turtle graphics, implemente a função `planetas()`, que simulará o movimento
planetário de Mercúrio, Vênus, Terra e Marte durante uma rotação do planeta Marte. Você pode
considerar que:

a. No início da simulação, todos os planetas estão alinhados (digamos, ao longo do
eixo y negativo).
b. As distâncias de Mercúrio, Vênus, Terra e Marte a partir do Sol (o centro de rotação)
são representadas com 58, 108, 150 e 228 pixels.
c. Para cada 1 grau de movimento circular de Marte, Terra, Vênus e Mercúrio se
moverão 2, 3 e 7,5 graus, respectivamente.
A figura a seguir mostra o estado da simulação quando a Terra está a cerca de um quarto do
caminho em torno do Sol. Observe que Mercúrio quase completou sua primeira rotação.

### Exercício 201 (AD5.5)

Leia a próxima função e veja se consegue compreender o que ela faz. Então execute-a e veja se acertou.

```
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)
```


### Exercício 202 (AD5.6)

![curva de koch](img/curva-de-koch.png)

A curva de Koch é um fractal que parece com o da acima. Para desenhar uma curva de Koch com o comprimento x, tudo o que você tem que fazer é:

1. Desenhe uma curva de Koch com o comprimento x/3.
2. Vire 60 graus à esquerda.
3. Desenhe uma curva de Koch com o comprimento x/3.
4. Vire 120 graus à direita.
5. Desenhe uma curva de Koch com o comprimento x/3.
6. Vire 60 graus à esquerda.
7. Desenhe uma curva de Koch com o comprimento x/3.

A exceção é se x for menor que 3: neste caso, você pode desenhar apenas uma linha reta com o comprimento x.

1. Escreva uma função chamada koch que receba um turtle e um comprimento como parâmetros, e use o turtle para desenhar uma curva de Koch com o comprimento dado.
2. Escreva uma função chamada snowflake que desenhe três curvas de Koch para fazer o traçado de um floco de neve.
3. A curva de Koch pode ser generalizada de vários modos. Veja exemplos em
[http://en.wikipedia.org/wiki/Koch\_snowflake](http://en.wikipedia.org/wiki/Koch_snowflake) e implemente o seu favorito.

*Solução de 1 e 2: [koch.py](http://thinkpython2.com/code/koch.py).*


