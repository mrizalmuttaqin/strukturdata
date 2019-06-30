i=0.05
L=input("Please enter Loan amount: ")
n=input("Please enter number of payments: ")
M=float(L)*float(n)*i*1+i/float(n)-1*1+i
print("Monthly Payment: $"+ str(M))