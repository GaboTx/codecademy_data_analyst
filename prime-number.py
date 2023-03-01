def prime_finder(n):
  # Write your code here
  #lists to save prime numbers: who are divided only by 1 and itself
  lists = []
  #check each number from 2 to max number input
  for valor in range(2,n+1):
    flag = False
    valor_flag = valor
    cont = 0
    #check if value is divided more than once by others numbers from max to min:
    #Example: 3 divided by 3,  then by 2 then by 1...
    while valor_flag > 0:
      if valor % valor_flag == 0:
        cont +=1
      valor_flag -= 1
      if cont > 2:
        flag = True
        break
    #appending to the list those numbers who are divided just by 1 and itself
    if flag == False:
      lists.append(valor)
      
      
    #Semi prime numbers
    semi_prime_list = []
    #loop for multiplying
    for x in lists:
      for y in range(0,len(lists)):
        op = x*lists[y]
        if op  in semi_prime_list:
          continue
        if op < n:
          semi_prime_list.append(op) 
        
      
  #fuction return  
  return semi_prime_list
print(prime_finder(100))