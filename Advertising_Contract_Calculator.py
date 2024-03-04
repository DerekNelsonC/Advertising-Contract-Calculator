import pickle

def getParameters():
       print("\nWhat is the name of the business (N) for this contract?")
       N=input()
      
       print("\nWhat is the monthly advertising budget(B)?")
       B=validatecheck(input())
      
       print("\nWhat is the agreed Digital Advertising Setup Fee(S)?")
       S=validatecheck(input())

       return N,float(B),float(S)

def validatecheck(i):
       while i.isalpha():
              i=input("Non-numeric values are not accepted. Please provide a numeric value:\n")
           
       while float(i)<0:
                     i = input("Error:enter a positive number:\n")
       return i
            
def load_data(contractlist, f):
       f= open('filename.txt', 'rb')
       contractlist= pickle.load(f)
       f.close()

def store_data(contractlist, f):
       f=open('filename.txt','wb')
       pickle.dump(contractlist,f)
       f.close()
       

def calculate(B, S):
       F=2500+0.12*B
       TAR=S+12*F
       C=TAR*0.045
       return F,TAR,C

    
def inputdata(contractlist):
       loop = True
       contractlist = []
       entry = input("Enter the name of the sales assoicate or q to quit:\n\n")
       while entry != "Q" and entry != "q" :
                     N,B,S= getParameters()
                     F,TAR, C = calculate(B, S)
                     contractlist.append([entry, N, B, S, F, TAR, C])   
                     entry = input("Enter the name of the sales assoicate or q to quit:\n")
       else:
              loop = False
              list(contractlist)       
                  

def list(contractlist):
       print("*********\n")
       print("The Results of Total Revenue and Commission Calculations")
       print("\n*********")
       print("{0:15}{1:30}{2:15}{3:15}{4:15}{5:20}{6:15}".format("Associate", "Business", "Budget", "Setup Fee", "Mgmt Fee", "Annual Revenue", "Commission"))      
       sumF=0
       sumTAR=0
       sumC=0
       for row in contractlist:
              print('{0:15}{1:30}{2:<15.2f}{3:<15.2f}{4:<15.2f}{5:<20.2f}{6:<15.2f}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
               
              sumF += row[4]
              sumTAR += row[5]
              sumC += row[6]             
       print("*********")
       print()
       print()
       print("The total monthly management fee is \u03A3(F)=${0:.2f}".format(sumF),".")
       print("The total annual revenue for all the projects is \u03A3(TAR)= ${0:.2f}".format(sumTAR),".")
       print("The total commission to all the sales associates is \u03A3(C)= ${0:.2f}".format(sumC),".")

        

def main():
       print("Sales and Sales Assoicate Commissions Tracker by Sherry Meng and Derek Nelson")
       contractlist = []
       done=False
    
       while not done:
              cmd = input("\nMain Menu:\nA)dd calculations to an existing file \nL)oad a file and view results \nP)rint current results \nR)eset and perform new TAR calculations \nS)ave current calculations to a file \nQ)uit:\n")
        
        
              if cmd=='A' or cmd == 'a':
                     try:
                            inputdata(contractlist)
                     except UnboundLocalError: 
                            print("\nThere are no calculations to display\nLoad a file or perform new calculations\n")    
            
              elif cmd == 'l'or cmd=='L':
                            try:
                                   filename = input('Enter filename:Hit enter for the default file (contractlist)')
                                   load_data(contractlist, filename)
                                   list(contractlist)
                                          
                            except FileNotFoundError:
                                   print("This file doesn't exist")
                                   
            
              elif cmd == 'p' or cmd=='P':
                     list(contractlist)
            
              elif cmd == 'r'or cmd=='R':
                     contractlist = []
                     inputdata(contractlist)       

              elif cmd == 's' or cmd =='S':
                     filename= input('\nEnter file name. Hit enter for the default file (contractlist)')
                     store_data(contractlist,filename)   
                     
              elif cmd == 'q' or cmd=='Q':
                     list(contractlist)
                     continue

if __name__ == '__main__':
       main()        
            

