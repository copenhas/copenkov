from random import random
import pdb

class MNode:
    """
    MarkovNode is to store a single state with weighted options to
    be used while generating a Markov chain. After costructing a graph
    of nodes the generator could walk the graph of states to generate
    the chain.

    This is a simple storage class with basic chain generation abilities.
    It's the responsibility of the graph builder and graph walker to make
    sense of it all.

    'state' - The state this node represents. The str() value of this
        object is used as keys in the dictionary members.
    'options' - A dictionary of possible next states from te current one.
    'weights' - A dictionary of weights for the possible next states.
    'counts' - A dictionary of the number of times an options was added.
    """

    def __init__(self, state):
        self.state = state
        self.options = {}
        self.weights = {}
        self.counts = {}
        self.totalcount = 0

    #TODO: Could add support to allowing the programmer to supply their
    # own function to generate the weighted values.
    def addoption(self, option):
        """
        Accept an 'option', another MarkovNode, which will be weighted and 
        added to the possible options. If it already exists then the 
        weights will be recalculated.

        Preconditions:
            'option' is not None
        Postconditions:
            'option' is added and weighted to 'options'
        """
        if option == None:
            return

        key = str(option)
        if str(option) in self.options:
            self.counts[key] += 1
        else:
            self.options[key] = option
            self.counts[key] = 1

        self.totalcount += 1

        #TODO: could optimize this by not updating all the weights
        # until next is called and just keep track of if we need to do it.
        #have to update all weights
        for key in self.options.keys():
            self.weights[key] = float(self.counts[key]) / self.totalcount

    #TODO: Could allow the programming to supply their own function
    # to generate the next state in the chain.
    def next(self):
        """
        Generates the next state in the Markov chain from the current node.

        Preconditions:
            None.
        Postconditions:
            A MNode is return representing the next state.
                If the next state does not exists MNode will have a None
                valued state with zero options to represent the end.
        """

        #TODO: needs sanity check
        #lets get a random number from 0.0 to 1.0 representing a percentage
        choice = random()
        for key, value in self.weights.items():
            #weights should also be in a 0.0 to 1.0 range
            if choice <= value:
                return self.options[key]
            else:
                #if we don't subtract then we could never select lower weights
                choice -= value

        return MNode(None)
        
#************* Python Special Functions **********************
    def __str__(self):
        if self.state is not None:
            return str(self.state) 
        else:
            return '' 

