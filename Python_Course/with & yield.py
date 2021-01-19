# import os
# os.system('touch abc.txt')
# with open('abc.txt', 'w') as abc:
#     abc.write('test')
    

def abc():
    a = 1
    while a < 100:
        yield a
        a+=1
    
    
for i in abc():
    print(i)