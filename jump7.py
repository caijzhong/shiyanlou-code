for i in range(0,101):
    if(i%10==7)or(i//10==7)or(i%7==0):
        continue
    else:
        print(i)
