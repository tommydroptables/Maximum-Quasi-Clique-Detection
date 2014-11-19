__author__ = 'Tom'


import re, string, sys, igraph, numpy
from Patterns import Pattern

class QuasiClick():
    def __init__(self, tempMax, temp2Hop):
        self.maximizedArray = tempMax
        self.pattyArray2Hop = temp2Hop

    def main(self):

        file1 = open('C:\\Users\\Tom\\PycharmProjects\\Quasi\\poop.txt', 'r')
        g = igraph.Graph.Read_Ncol(file1,names=True,directed=False,weights=False)
        file1.close()
        one_hop = g.get_adjacency().data
        one_h = numpy.array(one_hop)
        two_hop = numpy.zeros((len(one_h[0]), len(one_h[0])))



        #this multiplies two arrays
        for row in range(0, len(one_hop[0])):
            for row2 in range(0, len(one_hop[0])):
                for col in range(0, len(one_hop[0])):
                    two_hop[row][row2] += one_hop[row][col] * one_hop[col][row2]

        #add candidates from one_hop array
        for i in range(0, len(one_hop[0])):
            patty = Pattern([], [])
            patty.nodes.append(i)
            for j in range(0, len(one_hop[0])):
                if j > i:
                    if(one_hop[i][j] == 1):
                        patty.candidate.append(j)
            self.pattyArray2Hop.append(patty)




        #add candidates from two_hop array while sorting them while you add them
        #WE MIGHT NOT NEED TO SORT THE CANIDATES WHEN WE ADD THEM###########################################
        for i in range(0, len(two_hop[0])):
            for j in range(0, len(two_hop[0])):
                if two_hop[i][j] > 0:
                    if j > i:
                        if j not in self.pattyArray2Hop[i].candidate:
                            self.pattyArray2Hop[i].candidate.append(j)
                            self.pattyArray2Hop[i].candidate.sort()


        '''
        #display candidates for each node in graph that are 2 hop
        for i in self.pattyArray2Hop:
            for n in i.nodes:
                print("Node: ", n)
            for j in i.candidate:
                print(j , " ", end="")
            print("\n")
        '''

        for patt in self.pattyArray2Hop:
            self.findMaximized(patt)


        #display graph with iGraph
        layout = g.layout("kk")
        #create labels
        label = []
        for i in range(0, (len(one_hop[0]))): str(label.append(i))
        igraph.plot(g, layout=layout, vertex_label=label)




    #check if each node in the maximal clique is up to our standards in percentage
    def isQuasi(self, maximalClique):
        print("You are in the maximal Method")
        self.maximizedArray.append(maximalClique)


    #p is a object of the Pattern class
    def findMaximized(self, p):
        for candidate_of_p in p.candidate:
            #get the candidates of i from the 2 hop array
            pCandidate = candidate_of_p
            level1twoHopCandidates = self.pattyArray2Hop[pCandidate]
            test1 = level1twoHopCandidates.candidate

            if(len(self.findIntersection(p.candidate, test1)) == 0):
                p.isQuasi(p.nodes)
            #here we may need to check if the pattern above this node is a quasi.  Which would be removing the last element from the array
            else:
                pat = Pattern(p.nodes.append(candidate_of_p), self.findIntersection(p.candidate, self.pattyArray2Hop[candidate_of_p].candidate))
                p.candidate.pop(candidate_of_p)
                self.findMaximized(pat)

    def findIntersection(self, a, b):
        return set(a).intersection(b)

# run main
if  __name__ =='__main__':
    q = QuasiClick([], [])
    q.main()