def defArgs(x):
    if x == 5:
        return 1
    else:
        
        return x + defArgs(x+1)
print(defArgs(0))
