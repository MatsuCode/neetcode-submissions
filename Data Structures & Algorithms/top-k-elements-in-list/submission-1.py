class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contar a frequência de cada número
        contagem = {}
        for num in nums:
            if num in contagem:
                contagem[num] = contagem[num] + 1
            else:
                contagem[num] = 1

        # 2. Criar os baldes vazios
        # Precisamos de len(nums) + 1 posições
        baldes = []
        for i in range(len(nums) + 1):
            baldes.append([])

        # 3. Colocar cada número no balde correspondente à sua quantidade
        for num in contagem:
            qtd = contagem[num]
            baldes[qtd].append(num)

        # 4. Pegar os K números com maior frequência
        resultado = []
        
        # Percorrendo os baldes do fim para o começo
        tamanho_baldes = len(baldes)
        for i in range(tamanho_baldes - 1, 0, -1):
            lista_do_balde = baldes[i]
            
            for num in lista_do_balde:
                resultado.append(num)
                
                # Se já pegamos K números, terminamos
                if len(resultado) == k:
                    return resultado