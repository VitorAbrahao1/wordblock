import os
os.chdir(os.path.join("Python", "wordblock"))

f = open('lista0.txt', 'r', encoding='utf-8')
r = open('listalimpa.txt', 'w', encoding='utf-8')
for line in f:
    p = f.readline()
    if len(p)-1 ==4:
        r.write(f'{p}')