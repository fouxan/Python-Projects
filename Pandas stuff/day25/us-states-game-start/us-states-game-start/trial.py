alist = [line.rstrip() for line in open('file1.txt')]
blist = [line.rstrip() for line in open('file2.txt')]

result = [int(n) for n in alist if n in blist]

print(result)
