import re

order_file = "order.txt"
exs_file = "exercicios.md"

with open(order_file, 'r') as f:
    order = list(map(str.strip, f.readlines()))

with open(exs_file, 'r') as f:
    lines = f.readlines()

header = ""
exs = []

for l in lines:
    if re.match('^### ', l):
        exs.append(l)
    else:
        try:
            exs[-1] += l
        except IndexError:
            header += l

assert len(exs) == len(order)


ordered = []
for o in order:
    count = 0
    for e in exs:
        l = e.split('\n')[0]
        if re.match(r'###.*' + o.split()[0][:40].replace('.', '\.') + r"\)?( .*)?$", l):
            count += 1
            ordered.append(e)
            break
    if count == 0:
        print(o)


assert len(ordered) == len(order)

for i in range(len(ordered)):
    ordered[i] = re.sub(
        r"^### Exercício (\S+)?",
        rf"### Exercício {i + 1} (\1)",
        ordered[i]
    )

print(header + ''.join(ordered))
