def getMin(S):aa
	balance = insertLeft = 0 
        
	for s in S:
		if s == '(': balance += 1
		else: balance -= 1
		if balance == -1:
		    insertLeft += 1
			balance += 1
			
	# remaining balance is the extra left parentheses
	return insertLeft + balance
