with open('1.txt', encoding = 'utf-8') as f:
    for count, line in enumerate(f):
        pass
    t1 = str(count + 1)
with open('2.txt', encoding = 'utf-8') as f:
    for count, line in enumerate(f):
        pass
    t2 = str(count + 1)
with open('3.txt', encoding = 'utf-8') as f:
    for count, line in enumerate(f):
        pass
    t3 = str(count + 1)
with open('3.txt', encoding = 'utf-8') as a, open('2.txt', encoding = 'utf-8') as b, \
        open('1.txt', encoding = 'utf-8') as c, open('123.txt', 'w', encoding = 'utf-8') as f:
    if t1 > t2 and t1 > t3:
        if t2 > t3:
            f.write('1.txt'
                    '\n' + t1 + '\n' + a.read() + '\n2.txt'
                                                  '\n' + t2 + '\n' + b.read() + '\n3.txt\n' + t3 + '\n' + c.read())
        else:
            f.write('1.txt'
                    '\n' + t1 + '\n' + a.read() + '\n3.txt'
                                                  '\n' + t3 + '\n' + c.read() + '\n2.txt\n' + t2 + '\n' + b.read())
    elif t2 > t1 and t2 > t3:
        if t1 > t3:
            f.write('2.txt'
                    '\n' + t2 + '\n' + b.read() + '\n1.txt'
                                                  '\n' + t1 + '\n' + a.read() + '\n3.txt\n' + t3 + '\n' + c.read())
        else:
            f.write('2.txt'
                    '\n' + t2 + '\n' + b.read() + '\n3.txt'
                                                  '\n' + t3 + '\n' + c.read() + '\n1.txt\n' + t1 + '\n' + a.read())
    else:
        if t1 > t2:
            f.write('3.txt'
                    '\n' + t3 + '\n' + c.read() + '\n1.txt'
                                                  '\n' + t1 + '\n' + a.read() + '\n2.txt\n' + t2 + '\n' + b.read())
        else:
            f.write('3.txt'
                    '\n' + t3 + '\n' + c.read() + '\n2.txt'
                                                  '\n' + t2 + '\n' + b.read() + '\n1.txt\n' + t1 + '\n' + a.read())
with open('123.txt', encoding = 'utf-8') as f:
    print(f.read())
