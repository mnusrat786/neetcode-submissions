class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes=[]
        for i in strs:
            sizes.append(len(i))
        header = ",".join(map(str,sizes)) + "#"
        body = "".join(strs)
        return header + body



    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        fence = s.find("#")
        header = s[:fence]
        body = s[fence+1:]
        sizes =[]
        for j in header.split(","):
            sizes.append(int(j))
        decodelist=[]
        pointer = 0
        for k in sizes:
            word = body[pointer:pointer+k]
            decodelist.append(word)
            pointer+=k
        return decodelist






