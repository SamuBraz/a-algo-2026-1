import heapq

# heap global: lista de [-dor, id, nome]
heap = []
contador_id = 0

def inserir(nome, dor):
    global contador_id
    contador_id += 1
    heapq.heappush(heap, [-dor, contador_id, nome])
    print(f"  ✚ {nome} (dor={dor}) → id={contador_id}")
    return contador_id

def atender():
    if not heap:
        print("  Fila vazia.")
        return
    neg_dor, pid, nome = heapq.heappop(heap)
    print(f"  ► Atendendo: {nome} (dor={-neg_dor})")

def ajustar_dor(pid, nova_dor):
    for entrada in heap:
        if entrada[1] == pid:
            print(f"  ✎ {entrada[2]}: dor {-entrada[0]} → {nova_dor}")
            entrada[0] = -nova_dor
            heapq.heapify(heap)   # reconstrói o heap  O(n)
            return
    print(f"  ✗ id={pid} não encontrado.")

def mostrar():
    if not heap:
        print("  (fila vazia)")
        return
    for e in sorted(heap):
        print(f"  [id={e[1]}] {e[2]:12} dor={-e[0]}")

# ── Demo ──────────────────────────────────────────────────
print("=== CADASTRO ===")
id_ana   = inserir("Ana",   7)
id_bruno = inserir("Bruno", 3)
id_carla = inserir("Carla", 9)
inserir("Diego", 5)
inserir("Elena", 8)

print("\n=== FILA ===")
mostrar()

print("\n=== AJUSTE DE PRIORIDADE ===")
ajustar_dor(id_bruno, 10)   # piora → sobe
ajustar_dor(id_carla,  2)   # melhora → desce

print("\n=== FILA APÓS AJUSTES ===")
mostrar()

print("\n=== ATENDIMENTO ===")
while heap:
    atender()

"""
=== COMPLEXIDADE ===
  inserir()      O(log n)
  atender()      O(log n)
  ajustar_dor()  O(n)  — busca linear + heapify
"""