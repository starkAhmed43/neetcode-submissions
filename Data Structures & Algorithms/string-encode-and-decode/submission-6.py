class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == list():
            return "None"
        return "\u0000".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split("\u0000")
