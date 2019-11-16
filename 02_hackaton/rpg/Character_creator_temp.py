filename = 'eq.txt'
newfilename = 'neweq.txt'


with open(filename, 'r') as f:
    content = f.readlines()
    print(content)

with open(newfilename, 'w') as f:
    for item in content:
        f.write(item)
