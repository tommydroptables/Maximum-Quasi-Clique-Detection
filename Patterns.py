__author__ = 'Tom'
level1 = []


class Pattern():

    def __init__(self, tempNodes, tempCanidate):
        self.nodes = tempNodes
        self.candidate = tempCanidate

    #accessors for nodes and canidate
    def getNode(self):
        return self.nodes

    def getCandidate(self):
        return self.candidate
    def getLevel1(self):
        return level1
    def appendNode(self, node):
        self.nodes.append(node)
    def appendCandidate(self, canid):
        self.canidate.append(canid)



    #check if each node in the maximal clique is up to our standards in percentage
    def isQuasi(maximalClique):

        print("You are in the maximal Method")
        level1.append(maximalClique)


    #p is a object of the Pattern class
    def findMaximized(p):
        for i in range(0, len(p.getCanidate())):
            if(len(Pattern.findIntersection(p.getCanidate(), level1[p.getCanidate()[i]].candidate)) == 0):
                p.isQuasi(p.getNode())
            #here we may need to check if the pattern above this node is a quasi.  Which would be removing the last element from the array
            else:
                pat = Pattern.pattern(p.nodes.append(p.getCanidate()[i]), Pattern.findIntersection(p.candidate, level1[p.candidate[i]].candidate))
                Pattern.findMaximized(pat)


    def findIntersection(a, b):
        return set(a).intersection(b)