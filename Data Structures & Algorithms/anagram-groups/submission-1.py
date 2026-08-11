class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for elem in strs:
            try:
                anagram_dict[tuple(sorted(elem))].append(elem)
            except:
                anagram_dict[tuple(sorted(elem))] = [elem]
        return list(anagram_dict.values())