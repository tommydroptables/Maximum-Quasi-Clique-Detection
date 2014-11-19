__author__ = 'Tom'


class Pattern():
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






