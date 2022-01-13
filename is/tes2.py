try:
    my_list = []
     
    while True:
        my_list.append(int(input()))
         
except:
    print(my_list)
    
b = sorted([item for item in my_list if item%2 != 0])
odd_int = 0
for i in range(len(my_list)):
    if  my_list[i] %2 != 0:
        my_list[i] = b[odd_int]
        odd_int += 1

print(b)
with open('odd.txt', 'w') as f:
    f.write('\n'.join(str(c) for c in b))
