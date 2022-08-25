import string, random, os, sys
m = ""
j = ' '.join(sys.argv[1:])
if not os.name in ('nt', 'dos'):
    cmd = "clear"
else:
    cmd = "cls"
for i in j:
    while len(j) > 0:
        os.system(cmd)
        x = random.choices(string.ascii_letters+string.whitespace+string.punctuation, k=1)[0]
        print(m+x)
        if not x != i:
            m+=x
            break
