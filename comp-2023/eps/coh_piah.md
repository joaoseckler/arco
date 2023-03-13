## Detecção COH-PIAH

_inspirado na [Tarefa de
Programação](https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/oUnlk/programa-completo-similaridades-entre-textos-caso-coh-piah)
"Similaridade entre textos - caso COH-PIAH"
do curso "Introdução à ciência da computação com Python", Fábio Kon_

### Prólogo

Neste último exercício da Parte 1, iremos praticar não só o que vimos até agora no curso mas também outra habilidade importante de um programador: utilizar e interagir com código escrito por terceiros. Aqui, você não irá implementar o seu programa do zero. Você irá partir de um programa já iniciado e irá completá-lo. Na verdade, esse é o caso mais comum na indústria de software, onde muitos desenvolvedores trabalham colaborativamente em um mesmo programa.
Introdução

Manuel Estandarte é monitor na disciplina Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

*Detecção de autoria*

Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.
Traços linguísticos

Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

* Tamanho médio de palavra: Média simples do número de caracteres por palavra.
* Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
* Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
* Tamanho médio de sentença: Média simples do número de caracteres por sentença.
* Complexidade de sentença: Média simples do número de frases por sentença.
* Tamanho médio de frase: Média simples do número de caracteres por frase.

### Funcionamento do programa

A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que seu programa deve utilizar são calculados da seguinte forma:

* Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
* Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 45=0.8 \frac{4}{5} = 0.8 54​=0.8
* Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 35=0.6 \frac{3}{5} = 0.6 53​=0.6
* Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
* Complexidade de sentença é o número total de frases divido pelo número de sentenças.
* Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

Após calcular esses valores para cada texto, você deve compará-los com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, a a a e b b b, é dado pela fórmula:

TODO: acertar fórmula
Sab=∑i=16∣∣fi,a−fi,b∣∣6 S\_{ab} = \frac{\sum\_{i=1}^6 || f\_{i,a} - f\_{i,b} ||}{6} Sab​=6∑i=16​∣∣fi,a​−fi,b​∣∣​

Onde:

* Sab S\_{ab} Sab​ é o grau de similaridade entre os textos a a a e b b b;
* fi,a f\_{i,a} fi,a​ é o valor de cada traço linguístico i i i no texto a a a; e
* fi,b f\_{i,b} fi,b​ é o valor de cada traço linguístico i i i no texto b b b.

No nosso caso, o texto `b` não é conhecido, mas temos a assinatura correspondente: a assinatura de um aluno infectado com COH-PIAH. Ou seja, sabemos o valor de fi,b f\_{i,b} fi,b​ que é dado como valor de entrada do programa.

Caso você não esteja acostumado com a notação matemática, podemos destrinchar essa fórmula da seguinte maneira:

Para cada traço linguístico `i` (tamanho médio da palavra, relação type-token etc.) se quer a diferença entre o valor obtido em cada texto dado (`a`) e o valor típico do texto de uma pessoa infectada (b b b): fi,a−fi,b f\_{i, a} - f\_{i, b} fi,a​−fi,b​

Dessa diferença se toma o módulo (∣∣…∣∣ || \ldots || ∣∣…∣∣), lembre-se da função abs do python.

Somamos os resultados dos 6 traços linguísticos (∑i=16\sum\_{i=1}^6∑i=16​)

E por final dividimos por 6 ( x6 \frac{x}{6}6x​)

Perceba que quanto mais similares `a` e `b` forem, menor S\_{ab} Sab​ será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

**Exemplo:**

```
$ > python3 coh_piah.py

Bem-vindo ao detector automático de COH-PIAH.
Informe a assinatura típica de um aluno infectado:

Entre o tamanho médio de palavra: 4.51
Entre a relação Type-Token: 0.693
Entre a Razão Hapax Legomana: 0.55
Entre o tamanho médio de sentença: 70.82
Entre a complexidade média da sentença: 1.82
Entre o tamanho médio de frase: 38.5

Digite o texto 1 (aperte enter para sair): Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.

Digite o texto 2 (aperte enter para sair): Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.

Digite o texto 3 (aperte enter para sair): Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.

Digite o texto 4 (aperte enter para sair):

O autor do texto 2 está infectado com COH-PIAH

```

### Funções de suporte

Para facilitar seu trabalho, fornecemos para você um esqueleto do programa completo como base. Use-o! As funções definidas nele devem ser utilizadas no seu programa; algumas já estão implementadas, outras devem ser implementadas por você (conforme indicado pelo comentário "IMPLEMENTAR"). Sinta-se livre para criar funções adicionais, caso necessário.

```
import re

def le_assinatura():
	'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
	print("Bem-vindo ao detector automático de COH-PIAH.")
	print("Informe a assinatura típica de um aluno infectado:")

	wal = float(input("Entre o tamanho médio de palavra:"))
	ttr = float(input("Entre a relação Type-Token:"))
	hlr = float(input("Entre a Razão Hapax Legomana:"))
	sal = float(input("Entre o tamanho médio de sentença:"))
	sac = float(input("Entre a complexidade média da sentença:"))
	pal = float(input("Entre o tamanho medio de frase:"))

	return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
	'''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
	i = 1
	textos = []
	texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
	while texto:
    	textos.append(texto)
    	i += 1
    	texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

	return textos

def separa_sentencas(texto):
	'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
	sentencas = re.split(r'[.!?]+', texto)
	if sentencas[-1] == '':
    	del sentencas[-1]
	return sentencas

def separa_frases(sentenca):
	'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
	return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
	'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
	return frase.split()

def n_palavras_unicas(lista_palavras):
	'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
	freq = dict()
	unicas = 0
	for palavra in lista_palavras:
    	p = palavra.lower()
    	if p in freq:
        	if freq[p] == 1:
            	unicas -= 1
        	freq[p] += 1
    	else:
        	freq[p] = 1
        	unicas += 1

	return unicas

def n_palavras_diferentes(lista_palavras):
	'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
	freq = dict()
	for palavra in lista_palavras:
    	p = palavra.lower()
    	if p in freq:
        	freq[p] += 1
    	else:
        	freq[p] = 1

	return len(freq)

def compara_assinatura(as_a, as_b):
	'''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
	pass

def calcula_assinatura(texto):
	'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
	pass

def avalia_textos(textos, ass_cp):
	'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
	pass
```

Dica: não se preocupe com os detalhes de implementação das funções pré-prontas do esqueleto, como `separa_sentenca()`, `separa_frase()` etc. nem com as definições exatas de frase e sentença. Essas funções já cuidam disso para você, e podem ser pensadas como "caixas pretas": você pode utilizá-las sabendo o que recebem e o que devolvem, mas não é necessário saber sobre os seus detalhes internos. Além de isso ser muito comum ao programar em equipe, usando essas funções você vai fazer o cálculo da maneira esperada pelo corretor automático.

Cuidado: A função `le_textos()` considera que um "texto" é uma linha de texto, ou seja, não é possível inserir parágrafos separados. Se você digitar algum "enter", a função vai entender que você está começando um novo texto. Preste especial atenção a isso se usar "copiar/colar" para inserir os textos! Note também que, no cálculo de similaridade, é preciso encontrar o valor absoluto de cada uma das diferenças.

### Exemplo de Assinatura

Um passo importante para seu programa é calcular a assinatura dos textos corretamente. Para testar se sua função `calcula_assinatura()`  está correta, deixamos aqui um exemplo de execução:

```
>texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
>calcula_assinatura(texto)
>[4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
```

### Concluindo

Basicamente, sua tarefa é implementar corretamente as seguintes funções:

```
	compara_assinatura(as_a, as_b)
	calcula_assinatura(texto)
	avalia_textos(textos, ass_cp)
```

Usando o esqueleto que oferecemos acima e implementando essas 3 funções, seu detector de plágio estará completo e você poderá submetê-lo ao corretor automático. Caso o corretor automático aponte erros, tente ler com bastante cuidado e atenção a mensagem fornecida por ele, pois ela normalmente ajuda a identificar o erro.

Boa sorte! Não desista!

Sabemos que é um desafio, mas você vai aprender muito com ele.

Pense no prazer que você vai sentir quando sua solução final for aceita!!!



