f = open('test.txt','w')
f.write('test1\n')
f.write('test2\n')

f.close()

f = open('test.txt','r')

print(f.readline())
f.close()

f = open('test.txt','a')
f.write('apend\n')
f.close()

f = open('test.txt','r')

count = 1
for lines in f:
    print (count,lines)
    count +=1
f.close()
