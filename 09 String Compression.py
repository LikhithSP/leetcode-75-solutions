class Solution:
    def compress(self, chars: List[str]) -> int:
        b=[]
        d=1
        for i in range(1,len(chars)):
            if(chars[i]==chars[i-1]):
                d+=1
            else:
                b.append(chars[i-1])
                if(d>1):
                    n=str(d)
                    for p in n:
                        b.append(p)
                    d=1
        b.append(chars[-1])  
        if d > 1: 
            for p in str(d):
                b.append(p)
        chars.clear()
        for i in b:
            chars.append(i)
        return len(chars)
        
