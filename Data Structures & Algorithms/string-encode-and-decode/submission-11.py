class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            message += f"{len(s)}#{s}"
        
        return message
    
    def decode(self, s: str) -> List[str]:
        messages = []
        i = 0

        while i <len(s):
            j=i
            while s[j]!= '#':
                j+=1
            length = int(s[i:j])
            string = s[j+1 : j+1+length]
            messages.append(string)
            i = j+1+length
        return messages