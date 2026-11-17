class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for word in strs:
            anagram = tuple(sorted(word))
            try:
                anagram_groups[anagram].append(word)
            except:
                anagram_groups[anagram] = [word]
        return list(anagram_groups.values())