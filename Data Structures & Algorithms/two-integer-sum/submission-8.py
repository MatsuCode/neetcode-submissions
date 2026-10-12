class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Declara uma variável pra armazenar a diferença
        diff = 0

        # Procura em cada número a diferença dele pro alvo na lista
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return sorted([i, nums.index(diff)])