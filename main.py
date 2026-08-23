import string
while True:
    print("""
     ***** Encryt Decrypt *****
     
      choose a category:
     1)Encryt Code
     2)Decrpt Code
     3)EXIT
     \n""")
 #user_choose=u_c
    u_c=input(" Enter the choose the category :").lower()
 
    if u_c=="1" or u_c== "encryt code":
        #encryt=e,m=message,s=shift
        def e(m,s):
            #a=alphahet
            a=string.ascii_lowercase
    
            #e_m=encryt_message
            e_m=""
    
            #l=letter, 
            for l in m:
                if l.lower() in a:
                    #o_p=original_position
                    o_p=a.index(l.lower())
                    #new_position=n_p
                    n_p=(o_p + s) %26
                    #encryt_letter=e_l
                    e_l= a[n_p]
                    #الحرف حالة على حافظ
                    if l.isupper():
                        e_l= e_l.upper()
                    e_m += e_l
                else:
                    e_m += l
            
            return e_m
        
    
        #user_message=u_m
        u_m= input("Enter a message: ")
        #shift_number=s_n
        s_n= int(input("Enter a shift number: "))

        result = e(m=u_m, s=s_n)
        print(f"\n Here is the encryt message \n*****\n{result}\n*****")
    
    elif u_c=="2" or u_c== "decrpt code":
        #encryt=e,m=message,s=shift
        def e(m,s):
            #a=alphahet
            a=string.ascii_lowercase
    
            #e_m=encryt_message
            e_m=""
    
            #l=letter, 
            for l in m:
                if l.lower() in a:
                    #o_p=original_position
                    o_p=a.index(l.lower())
                    #new_position=n_p
                    n_p=(o_p - s) %26
                    #encryt_letter=e_l
                    e_l= a[n_p]
                    #الحرف حالة على حافظ
                    if l.isupper():
                        e_l= e_l.upper()
                    e_m += e_l
                else:
                    e_m += l
            
            return e_m
    
        #user_message=u_m
        u_m= input("Enter a message: ")
        #shift_number=s_n
        s_n= int(input("Enter a shift number: "))

        result=e(m=u_m,s=s_n)
        print(f"\nHere is the original message\n*****\n{result}\n*****")
    elif u_c=="3" or u_c== "exit":
        print("Thank you, and we wish you a nice day.")
        break
    else:
        print("not faound in data, please Try again")