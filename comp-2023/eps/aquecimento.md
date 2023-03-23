## Aquecimento de Programação em Python

_Adaptado do [oferecimento](https://paca.ime.usp.br/course/view.php?id=1259)
de MAC0110 - Introdução à computação de 2018, professor Marcelo Queiroz_


### Introdução

Neste exercício-programa treinaremos os conhecimentos vistos em aula até o momento, como a utilização de operações aritméticas e comparações, comandos condicionais (if-else), leitura da entrada (input()),
impressão de mensagens para o usuário (print), etc. Este será uma ótima oportunidade para treinarmos a implementação de um primeiro programa em Python.

O objetivo do EP é implementar um jogo de adivinhação de números, no qual o computador pedirá para o usuário responder uma série de questões e usará as respostas para “adivinhar” o número pensado. A seção seguinte explica o passo-a-passo desse processo de adivinhação.

Atenção: você não pode usar estruturas que não foram vistas em aula.

### Jogo de adivinhação

Nesse jogo o usuário deve pensar em um número de 0 a 10, e o computador pode fazer até 4 perguntas do tipo “par ou ímpar”, além de pedir para o usuário fazer manipulações aritméticas simples, como subtrair 1 ou dividir por 2. Você é quem deve descobrir como usar esses mecanismos para de fato permitir ao computador adivinhar o número pensado... Os dois exemplos abaixo ilustram o comportamento esperado
do programa:

#### Exemplo 1

```
$ python3 ep0.py
Pense em um número entre 0 e 10.
O número é par (digite 0) ou ímpar (digite 1)? 0
Divida o resultado por 2.
O número resultante é par (digite 0) ou ímpar (digite 1)? 1
Subtraia 1 do número.
Divida o resultado por 2.
O número resultante é par (digite 0) ou ímpar (digite 1)? 0
Divida o resultado por 2.
O número resultante é par (digite 0) ou ímpar (digite 1)? 1
O número que você pensou é 10 ?
Digite 1 para sim, 0 para não: 1
Já consigo ler mentes... agora só me falta dominar o mundo! huahuahua
```

#### Exemplo 2

```
$ python3 ep0.py
Pense em um número entre 0 e 10.
O número é par (digite 0) ou ímpar (digite 1)? 1
Subtraia 1 do número.
Divida o resultado por 2.
O número resultante é par (digite 0) ou ímpar (digite 1)? 1
Subtraia 1 do número.
Divida o resultado por 2.
O número resultante é par (digite 0) ou ímpar (digite 1)? 0
Divida o resultado por 2.
O número resultante é par (digite 0) ou ímpar (digite 1)? 0
O número que você pensou é 3 ?
Digite 1 para sim, 0 para não: 0
Até parece! Você que errou nas contas... kkkk
```

No seu programa, você deve usar exatamente as frases como aparecem no exemplo, para permitir a verifi-
cação automática do seu código.

### Entrega

Você deverá entregar um arquivo `.py` com sua implementação do jogo descrito acima.

Lembre-se de documentar bem o seu código. Além de torná-lo mais compreensível para o leitor, seus
comentários irão explicitar o que você pretendia fazer, caso venha a implementar algo levemente errado.

Boas implementações! =)

