import filecmp

f = "text.txt"
f1 = "text2.txt"

result = filecmp.cmp(f,f1)
print(result)