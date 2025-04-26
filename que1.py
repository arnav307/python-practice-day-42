def substring():
    count=0
    letters=[]
    for i in s:
        if i==s:
            count+=1
            letters.append(count)
            return letters
s="aabc"
result=substring()
print(*result)

