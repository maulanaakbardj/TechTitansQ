#No1 
def chess(x,y):
  for i in range(1, x + 1):
    for j in range(1, y + 1):
      
        if j <= x or (x*2)+1<=j<(x*3)+1 :
            print('x', end='')
        else:
            print('-', end='')
    print()
  for i in range(1, x + 1):
    for j in range(1, y + 1):
      
        if j <= x or (x*2)+1<=j<(x*3)+1 :
            print('-', end='')
        else:
            print('x', end='')
    print()
  for i in range(1, x + 1):
    for j in range(1, y + 1):
      
        if j <= x or (x*2)+1<=j<(x*3)+1 :
            print('x', end='')
        else:
            print('-', end='')
    print()
  for i in range(1, x + 1):
    for j in range(1, y + 1):
      
        if j <= x or (x*2)+1<=j<(x*3)+1 :
            print('-', end='')
        else:
            print('x', end='')
    print()

chess(2,8)
