# Librerie importate
import math

# Variabili iniziali
pos = [0, 0]
nuova_pos = [0, 0]

# Funzione per calcolare il movimento dell'asse X e Y
def calcola_movimento(pos, nuova_pos):
    return [nuova_pos[0] - pos[0], nuova_pos[1] - pos[1]]

# Funzione per la direzione del movimento
def azioni_movimento(mov):
    direzione = [0, 0]

    for i in range(2):
        # i = 0 → asse X
        # i = 1 → asse Y
        # Direzione =  0 → Fermo
        # Direzione =  1 → Verso positivo
        # Direzione = -1 → Verso negativo

        # Direzione
        if mov[i] < 0:
            direzione[i] = -1
        elif mov[i] == 0:
            direzione[i] = 0
        else:
            direzione[i] = 1

    print("direzione:", direzione)
    return direzione

# futuro spostamento asse X
def sposta_x(d):
    print("spostato asse X, direzione:", d)

# futuro spostamento asse Y
def sposta_y(d):
    print("spostato asse Y, direzione:", d)

def esegui_movimento(mov):
    quota = [abs(mov[0]), abs(mov[1])]  # quante X e Y
    count = [0, 0]                      # quante fatte
    direzione = [(mov[0] > 0) - (mov[0] < 0),
                 (mov[1] > 0) - (mov[1] < 0)]

    tot = quota[0] + quota[1]

    print("\nSequenza mosse:")

    for step in range(tot):
        # Target teorico basato sui calcoli
        target_x = (step * quota[0]) / tot
        target_y = (step * quota[1]) / tot

        # indietro rispetto al target
        diff_x = target_x - count[0]
        diff_y = target_y - count[1]

        # asse più indietro
        if quota[0] > 0 and (diff_x >= diff_y):
            sposta_x(direzione[0])
            count[0] += 1
        elif quota[1] > 0:
            sposta_y(direzione[1])
            count[1] += 1

# Funzione main
def richiesta():
    global pos, nuova_pos  

    print("posizione originale:", pos)
    print("posizione successiva (x,y):")
    nuova_pos[0], nuova_pos[1] = map(int, input().split(","))

    movimento = calcola_movimento(pos, nuova_pos)
    print("movimento:", movimento)

    azione = azioni_movimento(movimento)
    esegui_movimento(movimento)

    pos = nuova_pos.copy()

# Ciclo principale
while True:
    richiesta()
