

for n in  list(range(1,101)):
    st=""
    if n%3==0 or n%5==0:
       if n % 3==0:
        st=st+"fizz"
       
        if n % 5==0:
            st=st+"buzz"    
   
    else:
        st=st+str(n)
    print (f"{n}-->{st}")


               