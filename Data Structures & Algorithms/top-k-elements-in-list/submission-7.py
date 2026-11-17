class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            try:
                counts[num] += 1
            except:
                counts[num] = 1
        count_keys, count_vals = counts.keys(), counts.values()
        # print(counts)

        freq_counts = {}
        for key, val in zip(counts.keys(), counts.values()):
            # print(key, val)
            try:
                freq_counts[val].append(key)
            except:
                freq_counts[val] = [key]

        # print(freq_counts)
        top_k_counts = sorted(freq_counts.keys(), reverse=True)
        top_k_counts = [i for k in top_k_counts for i in freq_counts[k]]

        return top_k_counts[:k]