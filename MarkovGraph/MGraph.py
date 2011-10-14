from MNode import MNode
import re

class MGraph:
    """
    Takes in data and adds it to a graph representing the state to state
    chain of possible sequences.

    'states' is a dictionary  of MNodes representing the graph of states.
    It is initialized with a single MNode with a state of None.
    """

    def __init__(self):
        #create the initial state
        self.states = {'': MNode(None)}

    def addData(self, data, sep  = None, 
            end = re.compile('[^.]*(\.|!|\?)')):
        """
        Consumes the data constructing the node and adding them to the graph.

        Has optional paramters:
            'sep' - The characters that separate the data.
            'end' - A regular expression that represents the end of a 
                sentence.
        
        Preconditions:
            'data' is a string of space separated by delimiting characters. 
        Postconditions:
            The graph has been extended to include the data.
        """
        current = self.states['']
        tokens = data.split(sep)
        for token in tokens:
            if token not in self.states:
                self.states[token] = MNode(token)

            node = self.states[token]
            current.addoption(node)

            if end.match(token) is None:
               current = node
            else:
                current = self.states['']

    def generateSentence(self, max = 50):
        """
        Generates a sentence which is represented by starting at the
        initial state and going next to other states until an ending
        state is encountered. Currently that is anything that returns
        a MNode with zero options.

        Has optional parameters:
            'max' - The limit to the length of words to grab
                This is important since technically paths through the
                graph can be circular.

        Preconditions:
            None.
        Postconditions:
            A generated string of text is returned. This includes empty string.
        """
        words = ''
        current = self.states['']

        counter = max
        while counter > 0:
            current = current.next()
            words += str(current)

            if len(current.options) == 0:
                break

            if counter <> 1:
                words += ' '
                
            counter -= 1

        return words
