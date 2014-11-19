__author__ = 'Tom'


class Pattern():
    level1 = []
    twoHopArray = []
    def __init__(self, tempNodes, tempCanidate):
        self.nodes = tempNodes
        self.candidate = tempCanidate

    #accessors for nodes and canidate
    def getNode(self):
        return self.nodes
    def set2Hop(self, hoptwo):
        self.twoHopArray = hoptwo
    def getCandidate(self):
        return self.candidate
    def appendNode(self, node):
        self.nodes.append(node)
    def appendCandidate(self, canid):
        self.candidate.append(canid)



    #check if each node in the maximal clique is up to our standards in percentage
    def isQuasi(self, maximalClique):
        print("You are in the maximal Method")
        self.level1.append(maximalClique)


    #p is a object of the Pattern class
    def findMaximized(self, p):
        for i in range(0, len(p.candidate)):
            if(len(Pattern.findIntersection(p.candidate, self.level1[p.candidate[i]].candidate)) == 0):
                p.isQuasi(p.nodes)
            #here we may need to check if the pattern above this node is a quasi.  Which would be removing the last element from the array
            else:
                pat = Pattern(p.nodes.append(p.candidate[i]), Pattern.findIntersection(p.candidate, self.level1[p.candidate[i]].candidate))
                p.candidate.pop(p.candidate[i])
                Pattern.findMaximized(pat)


    def findIntersection(a, b):
        return set(a).intersection(b)