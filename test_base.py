pos = [0,0]
nuova_pos = [0,0]
movimento = [0,0]

for i in range(len(movimento)):
    movimento[i] = nuova_pos[i] - pos[i]

print(movimento)