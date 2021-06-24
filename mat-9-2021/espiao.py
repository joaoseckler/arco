from random import choice, shuffle
import subprocess as sp

ESPIAO = 'O ESPIÃO!!!!'

alunos = [
'Alan Camargo Goberstein',
'Ana Luiza Mori Pusas',
'Arthur Carneiro de Almeida Prado',
'Bruno Manzano Iumatti',
'Clara Utempergher Bodas Romero',
'Francisco Gonçalves Côrtes',
'Gabriel Justo Fernandes Corado',
'Gabriela Arbex Rodrigues Cadaval',
'Gaia Figueiredo Jafet',
'João Danelon Vaisman',
'Jonas Franco Kipersmit',
'Jorge Nasser Marques de Oliveira',
'Manuela Maria Cruz Saraiva',
'Manuela Perez Nagamine',
'Maria Eduarda Alcaldi Soares Ortega de Oliveira ',
'Mateus De Mello Gonçalves',
'Matheus Romão da Motta',
'Paulo Antonio da Silva Lima',
'Pedro Achcar Cardoso',
'Pedro Torres de Carvalho Bechuate',
'Alex Rosa de Souza Santos',
'Tomás Gonzales Krüger',
'Valentina Alcaldi Soares Ortega de Oliveira ',
'Vitor Gomes de Lima'
        ]

n = len(alunos) - 1 # 1 é o espião

opcoes = {
        'aula online do Seckler':
            (n - 1) * ['um aluno'] +
            ['o Seckler'],
        'em um teatro':
            5 * ['um ator'] +
            2 * ['um faxineiro'] +
            ['o técnico de som'] +
            ['o diretor'] +
            (n - 9) * ['está na platéia'],
        'na Revolução Francesa':
            5 * ['um nobre'] +
            5 * ['um sans cullotes'] +
            5 * ['um girondino']  +
            (n - 15) * ['um jacobino'],
        'no "The End" (o fim) do minecraft':
            ['o Ender Dragon'] +
            5 * ['um Enderman'] +
            (n - 6) * ['um jogador'],
        'numa reunião geral (de cooperados) da arco': [
                                            "a Ana",
                                            "o Bigode",
                                            "a Cândida",
                                            "a Cris",
                                            "o Danilo",
                                            "a Dany",
                                            "o Emerson",
                                            "o Enzo",
                                            "o Ferenc",
                                            "o Fred",
                                            "o Gui",
                                            "o João",
                                            "o Jopa",
                                            "a Kim",
                                            "a Lauren",
                                            "o Leo",
                                            "a Lívia",
                                            "o Lucas",
                                            "a Luciana",
                                            "o Luis",
                                            "o Martim",
                                            "o Mauro",
                                            "o Nelson",
                                            "o Rafa",
                                            "a Samanta",
                                            "o Seckler",
                                            "a Suelen",
                                            "o Taiguara",
                                            "a Tati",
                                            "a Thaiara"]
        }

a = ''
while (a != 'y'):
    lugar = choice(list(opcoes.keys()))
    a = input(f"Lugar é {lugar}. Aceita? (y/n)")

n += 1
personagens = opcoes[lugar] + [ESPIAO]
shuffle(personagens)

for i in range(n):
    print(alunos[i], end="\n\n")
    if personagens[i] == ESPIAO:
        p = f"Você é O ESPIÃO!!\n"
    else:
        p = f"Você está {lugar}. Você é {personagens[i]}"

    print(p)
    sp.Popen(['/bin/sh', '-c', f'echo "{p}" | xclip -selection clipboard'])
    input()

shuffle(alunos)
print(alunos)

