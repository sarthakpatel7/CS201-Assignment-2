class DFA:
    def __init__(self):
        self.num_states = 0
        self.states = []  #  states in the DFA
        self.symbols = [0, 1]  # alphabet set in the DFA
        self.i_state = '' # initial state of DFA
        self.f_states = []  # final states of DFA
        self.num_f_states = 0
        self.nf_states = []
        self.num_nf_states = 0
        self.transf_0 = {}
        self.transf_1 = {}
        #self.M = [[0 for i in range(len(self.symbols))] for j in range(len(self.states))]

    def construct_dfa_from_file(self, lines):
        self.states = list(lines[0].strip())
        self.num_states = len(self.states)
        #self.symbols = list(int(lines[2].strip()))
        f_states_line = []
        f_states_line = lines[3].split(" ")
        for i in range(len(f_states_line)):
            if i == 0:
                self.f_states = f_states_line[i]
            else:
                self.f_states += f_states_line[i].strip()
        self.i_state = lines[2]
        nf_states_line = []
        nf_states_line = lines[4].split(" ")
        for i in range(len(nf_states_line)):
            if i == 0:
                self.nf_states = nf_states_line[i]
            else:
                self.nf_states += nf_states_line[i].strip()
        
        for i in range(5, len(lines)):
            transf_line = lines[i].split(" ")
            
            start_state = (transf_line[0].strip())
            trans_symbol = int(transf_line[1])
            end_state = (transf_line[2].strip())

            if trans_symbol == 0 :
                self.transf_0.update({start_state : end_state})
            else :
                self.transf_1.update({start_state : end_state})

            '''trans_func = (start_state, trans_symbol, end_state);
            self.transf.append(trans_func)'''
        print(self.transf_0)
        print(self.transf_1)

    def rm_unreachable_states(self): #function for removing the unreachable states
        pass

    def is_equiv(self,a,b) :
        print(self.transf_0[a])
        print(self.transf_0[b])
        if self.transf_0[a] == self.transf_0[b] :
            if self.transf_1[a] == self.transf_1[b] :
                return True
            for i in range(0, len(self.vset)) :
                for j in vset[i] :
                    if (self.transf_1[a] in vset[i]) and (self.transf_1[b] in vset[i]) :
                        return True
                    else :
                        False
        for i in range(0, len(self.vset)) :
            #for j in self.vset[i] :
                if (self.transf_0[a] in self.vset[i]) and (self.transf_0[b] in self.vset[i]) :
                    if self.transf_1[a] == self.transf_1[b] :
                        return True
                    for i in range(0, len(self.vset)) :
                        #for j in vset[i] :
                            if self.transf_1[a] in self.vset[i] and self.transf_1[b] in self.vset[i] :
                                return True
                            else :
                                False
                else :
                    False

    def minimize_dfa(self):
        self.rm_unreachable_states()
        self.vset = [self.nf_states, self.f_states]
        print(self.vset)
        wset = [self.vset[0]]
        print(wset)
        xset = []
        k = 0
        while xset != wset :
            xset = wset
            for i in range(0,len(self.vset)) :
                var = self.vset[i]
                wset.append(var)
                for j in range(0, len(var)) :
                    #print(var[j])
                    #print(var[j+1])
                    #if var[j+1] :
                        #print(var[j+1])
                        if self.is_equiv(var[j].strip(), var[j+1].strip()) is True:
                            print(wset)
                            wset[k] += var[j+1].strip()
                        else :
                            wset.append(var[j+1])
                            k += 1
                        k += 1
        vset = wset

        transfm_0 = {}
        transfm_1 = {}

        for i in self.transf_0 :
            for j in vset :
                for l in vset[j] :
                    if i is vset[j][l] :
                        for k in vset :
                            for m in vset[k] :
                                if self.transf_0[i] is vset[k][m] :
                                    transfm_0.update({vset[j] : vset[k]})

        for i in self.transf_1 :
            for j in vset :
                for l in vset[j] :
                    if i is vset[j][l] :
                        for k in vset :
                            for m in vset[k] :
                                if self.transf_1[i] is vset[k][m] :
                                    transfm_1.update({vset[j] : vset[k]})

        final_states = []
        for i in vset :
            for j in vset[i] : 
                if self.i_state is vset[i][j] :
                    initial_state = vset[i]
                for j in self.f_states :
                    if f_states[j] is vest[i][j] :
                        final_states.append(vest[i])

        mstates = vset
        num_mstates = len(mstates)
        num_finalstates = len(final_states)

        print(mstates)

                            



'''
            while wset != [] :
                s = extract(wset)
                wset.remove(self.f_states)
                for i in len(self.symbols) :
                    for self.symbols[i] in self.symbols :
                        for x in vset :
                            (x1, x2) = split(x, s, self.symbols[i])
                            vset = vset.difference(set(x))
                            vset = vset + list(x1) + list(x2)
                            if len(x1) < len(x2) :
                                wset = wset + list(x1)
                            else :
                                wset = wset + list(x2)
            return vset

        def split(x, s, a) :

       ''' 

filename = input('Enter the name of the DFA file: ')
file = open(filename, 'r')
lines = file.readlines()
file.close()

dfa = DFA()
dfa.construct_dfa_from_file(lines)
dfa.minimize_dfa()
