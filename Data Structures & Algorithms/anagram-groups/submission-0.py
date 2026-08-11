class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        # anagram_dict = {tuple(sorted(strs[0])): [strs[0]]}
        # strs = strs[1:]
        for elem in strs:
            # does sorted(elem) exist in dict keys
                # if yes add it to the list of that dict key
            # else create a new key and add it to that list
            try:
                anagram_dict[tuple(sorted(elem))].append(elem)
            except:
                anagram_dict[tuple(sorted(elem))] = [elem]
        return list(anagram_dict.values())