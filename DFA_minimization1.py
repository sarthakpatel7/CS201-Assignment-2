import xlrd
import os

class Minimization:

    def __init__(self):
        self.location='' #storing the file location

        self.Q =[] #list of finite states in the xlrd
        self.A =[] #alphabet set in the DFA
        self.q0 = '' # initial state of DFA
        self.F = [] # accepting states of DFA
        self.M =[] 
        self.p0=[] #storing the initial partition
        self.q1=''
        self.q2=''
        self.newDF=[] #storing the states of the newly formed minimized DFA
        self.insDFA=[] #storing the initial state of the newly formed minimized DFA
        self.Fmindfa=[] 
        self.newdelta=[] # matrix for storing the new transition values(states) of the new states after being acted upon by the given alphabets 

        self.Tel=[]

    def filelocation(self):
        self.location =input('give the location of the excel file'+ " :")

        #self.location ='C:\Users\dell\OneDrive\Desktop\xlrd.xlsx'





    def stateDFA(self):  

        worksheet=xlrd.open_worksheet(self.location)
        sheet=worksheet.sheet_by_index(0)  

        self.Q=sheet.rowval(0)
        print(self.Q)



    def alpahabet(self):  
        worksheet = xlrd.open_worksheet(self.location)
        sheet = worksheet.sheet_by_index(1)  # sheet in which the alphabets of the DFA are present in the first row
        self.alpha= sheet.rowval(0)
        print(self.alpha)

    def ini_state(self):
        worksheet = xlrd.open_worksheet(self.location)
        sheet = worksheet.sheet_by_index(2)  
        self.q0= sheet.rowval(0)
        print(self.q0)

    def delfunc_matrix(self):
        worksheet = xlrd.open_worksheet(self.location)
        sheet = worksheet.sheet_by_index(3)
        self.M = [[sheet.cell_value(r,c) for c in range(sheet.cols)] for r in range(sheet.rows)]
        print(self.M)



    def accept_DFA(self):  
        worksheet = xlrd.open_worksheet(self.location)
        sheet = worksheet.sheet_by_index(4)  # excel file in which the final states of the DFA are stored in the first row.
        self.F = sheet.rowval(0)
        print(self.F)

    def zero_level_partition(self):
        S1=[]

        for i in range(0,len(self.Q)):
            if self.Q[i] not in self.F:
                S1.append(self.Q[i])  # S1 is the list of all states that are not accepting

        self.p0=[S1,self.F] 
        print(self.p0)




    def partition(self,P):

        P1=[]
        T=[]
        U=[]

        for i in range(0,len(P)):
            T=self.partition_1(P[i],P) 
            U=U+T
            print(U) 
            
            
        ctr=0
        for i in range(0,len(U)):
            
            if U[i] in P:
                ctr=ctr+1
        if ctr==len(U):
            
            print(P)
            self.newDF=P
            return P
                        #base case
                                
        else:
            self.partition(U)  


    def partition_1(self, P_i, P):
        L=[]
        t=0
        lst=[]
        j=0
        i=0

        for i in range(0, len(P_i)):
            print(len(P_i))
            lst=[P_i[i]]
            print(lst)

            for j in range(0,len(P_i)):
                ctr=0

                if j!=i:
                    
                    for k in range(0, len(self.alpha)):

                        self.q1= self.transition(P_i[i],self.alpha[k])
                        self.q2= self.transition(P_i[j],self.alpha[k])
                        print(self.alpha[k])
                        print(P_i[i]+" "+P_i[j])
                        print( self.q1 +" "+self.q2 )

                        flag=0

                        for l in range(0,len(P)):

                            if self.q1 in P[l] and self.q2 in P[l]: 
                            
                                flag=1  

                    

                        if flag==1:
                        
                            ctr=ctr+1

                    if ctr== len(self.alpha):
                        print(ctr)
                        lst.append(P_i[j])
                        print(lst)

            if L==[]:
                print(len(L))
                L.append(lst)
                print(L)
            else:

                for i in range(0,len(L)):
                    print(len(L))
                    print(L)
                    if set(lst)!=set(L[i]):
                        t=t+1
                        print(t)
                if t==len(L):
                    L.append(lst)
                    print(L)

        print(L)
        return L #returning the collection of all the partitions of P_i where P_i is an element of P

    def transition(self, q, s):
        state_index= self.Q.index(q)
        
        
        alphabet_index=self.alpha.index(s)
        
        print(self.M[state_index][alphabet_index])

        return self.M[state_index][alphabet_index]  #returning the state at which 'q' will reach after acting upon the alphabet 's'
    
    def final_states_new(self):
        for i in range(0,len(self.newDF)):
            if self.subset(self.newDF[i],self.F):
                self.Fmindfa.append(self.newDF[i])
        print(" The accepting states of the newly formed minimized DFA---->"+ str(self.Fmindfa))

    def subset(self,L_1,L_2):
        ctr=0
        for i in range(0,len(L_1)):
            if L_1[i] in L_2:
                ctr=ctr+1
        if ctr==len(L_1):
            return True
        else:
            return False

    def new_initial_state(self):
        for i in range(0,len(self.newDF)):
            if self.q0[0] in self.newDF[i]:
                self.insDFA=self.newDF[i]
        print("The initial state of the modified DFA---->"+str(self.insDFA))

    def transit_value_storing(self):
        for i in range(0,len(self.newDF)):
            self.newdelta.append(self.new_transition(self.newDF[i]))
    
    def new_transition(self,L):
        lst=[]
        trans_L=[]

        for i in range(0,len(self.alpha)):
            lst=self.new_transition_func(L,self.alpha[i])
            
            trans_L.append(lst)
            print("delta( " + str(L)+" , "+str(self.alpha[i])+" )--->"+str(lst))
        
        print(trans_L)
        return trans_L
    
    def new_transition_func(self, L, c):
        state_0=L[0]
        state_T=self.M[self.Q.index(state_0)][self.alpha.index(c)]
        print(state_T)

        for i in range(0,len(self.newDF)):
            if state_T in self.newDF[i]:
                print(i)
                break
        print(self.newDF[i])
        return self.newDF[i]









M= Minimization()
M.filelocation()
M.stateDFA()
M.alpahabet()
M.ini_state()
M.delfunc_matrix()
M.accept_DFA()

M.zero_level_partition()

M.partition_1()
M.transition()
M.partition(M.p0)
M.final_states_new()
M.new_initial_state()
M.transit_value_storing()
M.new_transition_func(['a','d'],M.A[1])
M.new_transition(['a','d'])







