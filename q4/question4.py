def fact(x) :
    if(x == 0): return 1
    return x * fact(x - 1)
        
if __name__ == "__main__" :
	for i in range(0, 16, 2) :
		print(i, "->", fact(i))
	