import random as rand  		  	   		  	  		  		  		    	 		 		   		 		  

import numpy as np  		  	   		  	  		  		  		    	 		 		   		 		  

class QLearner(object):  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    This is a Q learner object.  
    :param num_states: The number of states to consider.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type num_states: int  		  	   		  	  		  		  		    	 		 		   		 		  
    :param num_actions: The number of actions available..  		  	   		  	  		  		  		    	 		 		   		 		  
    :type num_actions: int  		  	   		  	  		  		  		    	 		 		   		 		  
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type alpha: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type gamma: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type rar: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type radr: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type dyna: int  		  	   		  	  		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  	  		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    def __init__(  		  	   		  	  		  		  		    	 		 		   		 		  
        self,  		  	   		  	  		  		  		    	 		 		   		 		  
        num_states=100,  		  	   		  	  		  		  		    	 		 		   		 		  
        num_actions=4,  		  	   		  	  		  		  		    	 		 		   		 		  
        alpha=0.2,  		  	   		  	  		  		  		    	 		 		   		 		  
        gamma=0.9,  		  	   		  	  		  		  		    	 		 		   		 		  
        rar=0.5,  		  	   		  	  		  		  		    	 		 		   		 		  
        radr=0.99,  		  	   		  	  		  		  		    	 		 		   		 		  
        dyna=0,  		  	   		  	  		  		  		    	 		 		   		 		  
        verbose=False,  		  	   		  	  		  		  		    	 		 		   		 		  
    ):  		  	   		  	  		  		  		    	 		 		   		 		  
        """  		  	   		  	  		  		  		    	 		 		   		 		  
        Constructor method  		  	   		  	  		  		  		    	 		 		   		 		  
        """  		  	   		  	  		  		  		    	 		 		   		 		  
        self.verbose = verbose	  	  		  		  		    	 		 		   		 		  
        self.num_actions = num_actions  		  	   		  	  		  		  		    	 		 		   		 		  
        self.s = 0  		  	   		  	  		  		  		    	 		 		   		 		  
        self.a = 0  	
        self.rar = rar
        self.radr = radr
        self.alpha = alpha
        self.gamma = gamma
        self.dyna = dyna
        self.Qtable = np.full((num_states,num_actions),1e-16,dtype="float32") 
        self.Qtable = self.Qtable.astype('float32')
        if dyna > 0:
            self.Ttable = np.full((num_states,num_actions,num_states),1e-16,dtype="float32")
            self.Ttable = self.Ttable.astype('float32')
            self.Tctable = np.full((num_states,num_actions,num_states),1e-16,dtype="float32")
            self.Tctable = self.Tctable.astype('float32')
            self.Rtable = np.full((num_states,num_actions),1e-16,dtype="float32") 
            self.Rtable = self.Rtable.astype('float32')
            self.dynaTrack = np.zeros((num_states,num_actions),dtype="float32")
        

    def querysetstate(self, s,random=True):  		  	   		  	  		  		  		    	 		 		   		 		  
        """  		  	   		  	  		  		  		    	 		 		   		 		  
        Update the state without updating the Q-table  		  	   		  	  		  		  		    	 		 		   		 		  
        :param s: The new state  		  	   		  	  		  		  		    	 		 		   		 		  
        :type s: int  		  	   		  	  		  		  		    	 		 		   		 		  
        :return: The selected action  		  	   		  	  		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		  	  		  		  		    	 		 		   		 		  
        """  		  	   		  	  		  		  		    	 		 		   		 		  
        self.s = s  	
        # select from possible number of actions and perform random one	  	   		  	  		  		  		    	 		 		   		 		  
        action = rand.randint(0, self.num_actions - 1)  
        # log to object
        if not random:
            next_action = np.argmax(self.Qtable[s])
        self.a = action	   			  	   		  	  		  		  		    	 		 		   		 		  
        if self.verbose:  		  	   		  	  		  		  		    	 		 		   		 		  
            print(f"s = {s}, a = {action}")  		  	  		  		    	 		 		   		 		  
        return action  		  	   		  	  		  		  		    	 		 		   		 		  

    def query(self, s_prime, r):  		  	   		  	  		  		  		    	 		 		   		 		  
        """  		  	   		  	  		  		  		    	 		 		   		 		  
        Update the Q table and return an action  		
        :param s_prime: The new state  		  	   		  	  		  		  		    	 		 		   		 		  
        :type s_prime: int  		  	   		  	  		  		  		    	 		 		   		 		  
        :param r: The immediate reward  		  	   		  	  		  		  		    	 		 		   		 		  
        :type r: float  		  	   		  	  		  		  		    	 		 		   		 		  
        :return: The selected action  		  	   		  	  		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		  	  		  		  		    	 		 		   		 		  
        """  		  	   	
        # first, find the best next action
        
        next_action = np.argmax(self.Qtable[s_prime])

        # from CS7646 lecture 3-06 on Q learning 
        # Q'[s,a] = (1-alpha)*Q[s,a] + alpha * (r+discount_rate*Q[next])
        self.Qtable[self.s,self.a] = (1-self.alpha) * self.Qtable[self.s,self.a] + self.alpha * (r + self.gamma * self.Qtable[s_prime,next_action] ) 

        # update dyna model
        if self.dyna > 0:
            
            # update Tc table - sourced from CS7646 lecture 3-07 on Q learning with Dyna
            self.Tctable[self.s,self.a,s_prime] += 1
            # update T table - sourced from CS7646 lecture 3-07 on Q learning with Dyna
            self.Ttable[self.s,self.a,s_prime] = self.Tctable[self.s,self.a,s_prime] / np.sum(self.Tctable[self.s,self.a,:])
            # update R table - sourced from CS7646 lecture 3-07 on Q learning with Dyna
            self.Rtable[self.s,self.a] = (1-self.alpha) * self.Rtable[self.s,self.a] + self.alpha * r 
            #log available dyna location
            self.dynaTrack[self.s,self.a] = 1
            # iterate provided number of times from object initialize - sourced from CS7646 lecture 3-07 on Q learning with Dyna
            for i in range(self.dyna):
                # hallucinate location and direction then determine most probable next location and probable reward
                dyna_s = np.where(self.dynaTrack == 1)[0]
                dyna_s = rand.choice(dyna_s)
                dyna_a = rand.choice(np.where(self.dynaTrack[dyna_s] == 1)[0])
                dyna_s_prime = np.argmax(self.Tctable[dyna_s,dyna_a])
                dyna_r = self.Rtable[dyna_s,dyna_a]

                # find the best next action for dyna hallucination
                dyna_next_action = np.argmax(self.Qtable[dyna_s_prime])
                self.Qtable[dyna_s,dyna_a] = (1-self.alpha) * self.Qtable[dyna_s,dyna_a] + self.alpha * (dyna_r + self.gamma * self.Qtable[dyna_s_prime,dyna_next_action] ) 

        # save state for next iteration
        self.s = s_prime
        self.a = next_action

        # from testqlearner.py
        # decide if we're going to ignore the action and  		  	   		  	  		  		  		    	 		 		   		 		  
        # choose a random one instead  	
        if rand.uniform(0.0, 1.0) <= self.rar:  # going rogue  		  	   		  	  		  		  		    	 		 		   		 		  
            action = rand.randint(0, self.num_actions)  # choose the random direction  
            self.rar = self.rar * self.radr # randomness decays
            
            if self.verbose: print("went random - new random rate is ", self.rar)

        if self.verbose:	  	   		  	  		  		  		    	 		 		   		 		  
            print(f"s = {s_prime}, a = {action}, r={r}")  	

        # redundant for API purposes
        action = next_action
        return action  		  	   		  	  		  		  		    	 		 		   		 		  
    
    def query_no_update(self, s_prime):
        return np.argmax(self.Qtable[s_prime])

if __name__ == "__main__":  		  	   		  	  		  		  		    	 		 		   		 		  
    print("Remember Q from Star Trek? Well, this isn't him")  		  	   		  	  		  		  		    	 		 		   		 		  
