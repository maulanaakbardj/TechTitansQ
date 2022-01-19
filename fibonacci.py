def fibonacci(n):
  n1, n2 = 0, 1
  count = 0
  if n <= 0 :
    print("Error")
  elif n==1:
    print(n1)
  else:
    while count < n :
      print(n1)
      nterm=n1+n2
      n1=n2
      n2=nterm
      count +=1

fibonacci(10)
