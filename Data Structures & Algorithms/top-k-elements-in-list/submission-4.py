class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {key:0 for key in set(nums)}
        for i in nums:
            freq_dict[i] += 1
        
        inv_freq_dict = {key:[] for key in freq_dict.values()}
        for key in freq_dict.keys():
            inv_freq_dict[freq_dict[key]].append(key)

        count = 0
        topk = []
        for key in sorted(inv_freq_dict.keys(), reverse=True):
            topk.extend(inv_freq_dict[key])
            count+=len(inv_freq_dict[key])
            if count > k:
                break
        return topk[:k]