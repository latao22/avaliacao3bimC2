
candidatos = {
  1: {"nome candidato": "romario", "vice": "higor", "partido": "bola", "Cargos": "prefeito", "idade": 54},
  2: {"nome candidato": "jonas", "vice": "pedro", "partido": "magro", "Cargos": "prefeito", "idade": 45}

}

def exibir_informacoes(numero):
  if numero in candidatos:
    print(f"Nome: {candidatos[numero]['nome candidato']}")
    print(f"Vice: {candidatos[numero]['vice']}")
    print(f"Partido: {candidatos[numero]['partido']}")
    print(f"Cargos: {candidatos[numero]['Cargos']}")
    print(f"Idade: {candidatos[numero]['idade']}")
  else:
    print("Candidato não encontrado.")

numero_candidato = int(input("Digite o numero candidato: "))
exibir_informacoes(numero_candidato)
