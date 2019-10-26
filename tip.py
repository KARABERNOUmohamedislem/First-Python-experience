

amount =input('please type the facture amount :')  #to read the facture amount

amount=amount.strip('$')    #to remove the $ sign 
amount =float(amount)            
tip1=amount*15/100
tip2=amount*18/100
tip3=amount*20/100

print (f"""recommended tip :
    15% : {tip1}
    18% : {tip2}
    20% : {tip3}""")
    
          