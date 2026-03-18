I = int(input("(I)Informe um valor: "))
A = float(input("(A)Informe um valor: "))
B = float(input("(B)Informe um valor: "))
C = float(input("(C)Informe um valor: "))

if I < 0 or I > 3:
    print("Informe um valor que seja inteiro e positivo (maior que 0)")
else:
    if I == 1:
        if A < B and A < C:
            if B < C: 
                print(A, B, C)
            else:
                print(A, C, B)
        elif B < A and B < C:
            if A < C: 
                print(B, A, C)
            else:
                print(B, C, A)
        else:
            if B < A: 
                print(C, B, A)
            else:
                print(C, A, B)
    elif I == 2 :
        if A > B and A > C:
            if B > C: 
                print(A, B, C)
            else:
                print(A, C, B)
        elif B > A and B > C:
            if A > C: 
                print(B, A, C)
            else:
                print(B, C, A)
        else:
            if B > A: 
                print(C, B, A)
            else:
                print(C, A, B)
    else:
        if A > B and A > C:
            if B > C: 
                print(B, A, C)
            else:
                print(C, A, B)
        elif B > A and B > C:
            if A > C: 
                print(A, B, C)
            else:
                print(C, B, A)
        else:
            if B > A: 
                print(B, C, A)
            else:
                print(A, C, B)
    
