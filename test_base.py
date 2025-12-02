# Librerie importate
import math

# Variabili iniziali
pos = [0, 0]
nuova_pos = [0, 0]

# Funzione per calcolare il movimento dell'asse X e Y
def calcola_movimento(pos, nuova_pos):
    mov = [0, 0]
    mov[0] = nuova_pos[0] - pos[0]
    mov[1] = nuova_pos[1] - pos[1]
    return mov

def azioni_movimento(mov):
    movimento_x = mov[0]
    movimento_y = mov[1]
    
    azioni  = movimento_x + movimento_y
    rapporto = round(movimento_x / movimento_y)

    if (movimento_x < 0):
        direzione_x = -1
    elif (movimento_x == 0):
        direzione_x = 0
    else (direzione_x):
        direzione_x = 1

    if (movimento_y < 0):
        direzione_y = -1
    elif (movimento_y == 0):
        direzione_y = 0
    else (direzione_y):
        direzione_y = 1

# Funzione main
def richiesta():
    # Variabili globali
    global pos, nuova_pos  

    print("posizione successiva (x,y):")
    nuova_pos[0], nuova_pos[1] = map(int, input().split(","))

    movimento = calcola_movimento(pos, nuova_pos)
    print("movimento:", movimento)

    # Aggiornamento della posizione
    pos = nuova_pos.copy()

while True:
    richiesta()
