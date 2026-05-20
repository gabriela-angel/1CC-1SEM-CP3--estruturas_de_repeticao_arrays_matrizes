temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

sala = 1
risco = [0] * len(temperaturas)
for t in temperaturas:
    mean = 0
    sum = 0
    for n in t:
        sum += n
        if n >= 33:
           risco[sala - 1] += 1
    mean = sum / len(t)
    print(f"""
Sala {sala}
Média: {mean}
Registros críticos: {risco[sala - 1]}
          """)
    sala += 1


maior_risco = 0;
for r in range(0, len(risco)):
    if r > 0 and (risco[r] > risco[maior_risco]):
        maior_risco = r;
print(f"Sala com maior risco: Sala {maior_risco + 1}")