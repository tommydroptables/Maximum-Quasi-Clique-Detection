__author__ = 'Tom'


import re, string, sys, igraph, numpy
from Patterns import Pattern
from RowF import RowFound
class QuasiClick():
    def __init__(self, tempMax, temp2Hop):
        self.maximizedArray = tempMax
        self.pattyArray2Hop = temp2Hop

    percent = 0
    def main(self):
        global percent 
        percent = float (input("Enter the quasi percentage"))
        file1 = open('C:\\Users\\Tom\\PycharmProjects\\Quasi\\poop.txt', 'r')
        g = igraph.Graph.Read_Ncol(file1,names=True,directed=False,weights=False)
        file1.close()
        one_hop = g.get_adjacency().data
        one_h = numpy.array(one_hop)
        two_hop = numpy.zeros((len(one_h[0]), len(one_h[0])))

        for i in one_hop:
            for j in i:
                print(j, " ", end="")
            print("\n")

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
            self.findMaximized(patt, one_hop)


        #display candidates for each node in maximized
        for patttt in self.maximizedArray:
            print("\nNodes: ", end="")
            for nod in patttt.nodes:
                print(nod, " ", end="")
            print("\nCandidates: ", end="")
            for can in patttt.candidate:
                print(can, " ", end="")

        #display graph with iGraph
        layout = g.layout("kk")
        #create labels
        label = []
        for i in range(0, (len(one_hop[0]))): str(label.append(i))
        igraph.plot(g, layout=layout, vertex_label=label)


    def coieficOf(self, adjacency_mat, nodes):
        TOTAL = 0
        top = 0
        #TOTAL = start
        # this takes each node and finds the correlation coefficient and adds it to the total
        for i in nodes:
            row = RowFound(i, [])
            #finds all the index that have 1's
            for index in range(0, len(adjacency_mat[0])):
                if adjacency_mat[i][index] == 1:
                    row.candidate.append(index)
            top = 0.0
            #calculates how many neighbors are friends
            for can in row.candidate:
                for index, rowAdj in enumerate(adjacency_mat[can]):
                    if rowAdj == 1 and adjacency_mat[row.row][index] == 1:
                        top += 1
            #keep
            bottom = ( len(row.candidate) * (len(row.candidate) - 1))
            if bottom < 1:
                bottom = 1

            tots =  ((top/2) / (bottom / 2))

            #calculates the correlation coefficient for the node

            TOTAL = (TOTAL + tots)
        TOTAL= TOTAL / len(adjacency_mat[0])
        print(TOTAL, " HERERERERER")
        if TOTAL > percent:
            return True
        else:
            return False


    #check if each node in the maximal clique is up to our standards in percentage
    def isQuasi(self, tempPattern):
        notfound = True
        for maximalPattern in self.maximizedArray:
            if set (tempPattern.nodes).issuperset(maximalPattern.nodes):
                self.maximizedArray.replace(maximalPattern, tempPattern)
                notfound = False
            elif set (maximalPattern.nodes).issuperset(tempPattern.nodes):
                return 0
        if notfound:
            self.maximizedArray.append(tempPattern)




    #p is a object of the Pattern class


    #re-write sudo code for this section!!!!!!!!!!!


    def findMaximized(self, p, one_hop_local):
        #THE PROBLEM IS THAT WE ARE REMOVING ELEMENTS FROM THE LIST CANDIDATES AND LOOPING THROUGH THE SAME LIST
        stay = True
        print("Node", end="")
        for n in p.nodes:
            print(n, end="")
        print("\n")
        for candidate_of_p in p.candidate.copy():
            #get the candidates of i from the 2 hop array
            level1twoHopCandidates = self.pattyArray2Hop[candidate_of_p]
            test1 = level1twoHopCandidates.candidate[:]

            #here we may need to check if the pattern above this node is a quasi.  Which would be removing the last element from the array
            level1twoHopCandidatesNew = self.pattyArray2Hop[candidate_of_p]
            candidate_of_candidate = level1twoHopCandidatesNew.candidate[:]
            pnodes_recursive = p.nodes[:]
            pnodes_recursive.append(candidate_of_p)

            pat = Pattern(pnodes_recursive, self.findIntersection(p.candidate, candidate_of_candidate))
            self.findMaximized(pat, one_hop_local)

            #if(len(self.findIntersection(p.candidate, test1)) == 0):
            if self.coieficOf( one_hop_local, p.nodes):
                self.isQuasi(p)
                stay = False
                break

    def findIntersection(self, a, b):
        return set(a).intersection(b)

# run main~
if  __name__ =='__main__':
    q = QuasiClick([], [])
    q.main()