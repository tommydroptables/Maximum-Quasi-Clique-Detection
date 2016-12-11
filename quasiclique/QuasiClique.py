__author__ = 'Tom'

import re, string, sys, igraph, numpy, random, threading
from Patterns import Pattern
from RowF import RowFound
from threading import Semaphore
import cairocffi as cairo
import copy

lock = Semaphore()

class QuasiClique():
    # Global so we can share it between processes
    percent = 0


    def __init__(self):
        global percent

        self.maximizedArray = []
        self.pattyArray2Hop = []
        self.colors = ["blue", "green", "yellow", "purple", "orange", "white", "gray", "cyan", "sienna", "coral", "plum"]

        self.num_threads = 5 # int (input("Enter the number of threads\n"))
        percent = 99.0 #float (input("Enter the quasi percentage\n"))


    def main(self):
        """main

        Returns:
            TYPE: none
        """
        global percent

        with open('data/sample.txt', 'r') as file1:
            g = igraph.Graph.Read_Ncol(file1, names=True, directed=False, weights=False)

        one_hop = g.get_adjacency().data

        width_one_hop = len(numpy.array(one_hop)[0])

        two_hop = numpy.zeros((width_one_hop, width_one_hop))

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
        #WE MIGHT NOT NEED TO SORT THE CANIDATES WHEN WE ADD THEM ###########################################
        for i in range(0, len(two_hop[0])):
            for j in range(0, len(two_hop[0])):
                if two_hop[i][j] > 0:
                    if j > i:
                        if j not in self.pattyArray2Hop[i].candidate:
                            self.pattyArray2Hop[i].candidate.append(j)
                            self.pattyArray2Hop[i].candidate.sort()



        thread = []

        local_n =  int(len(one_hop) / self.num_threads)

        for index in range(0, self.num_threads):
            local_start = local_n * index
            local_stop = (local_n * index) + local_n
            if(index == self.num_threads - 1):
                local_stop = len(one_hop) - 1
            t = threading.Thread(target= self.thread_maximized, args=(local_start, local_stop, one_hop))
            thread.append(t)
            t.start()

        for j in thread:
            j.join()

        for pattty in self.maximizedArray:
            nodes = []
            for node in pattty.nodes:
                nodes.append(str(node))
            print '++ Nodes: %s\n' % ' '.join(nodes)

        #display graph with iGraph
        layout = g.layout("kk")
        #create labels
        label = []
        myColours = []

        #set the default color to red
        for i in range(0, (len(one_hop[0]))): str(myColours.append("red"))

        for i in range(0, (len(one_hop[0]))): str(label.append(i))

        #the bellow for loop applies the colors the the quasi cliques
        for pattty in self.maximizedArray:

            #get a new color that is not used
            rand_color = random.choice(self.colors)
            self.colors.remove(rand_color)

            #apply that color to those nodes in that clique
            for node in pattty.nodes:
                myColours[node] = rand_color

        #set colors of graph from colors set in the above for loop

        g.vs['color'] = myColours
        igraph.plot(g, layout=layout, vertex_label=label)


    def thread_maximized(self, start, stop, one_hoppy_hop):
        for i in range(start, stop):
            print("index: ", i, " Start: ", start, " Stop: ", stop)
            self.findMaximized( self.pattyArray2Hop[i], one_hoppy_hop)


    #Finds the Clustering Coefficient of the nodes that are passed to it
    def coieficOf(self, adjacency_mat, nodes):
        TOTAL = 0
        top = 0
        # this takes each node and finds the correlation coefficient and adds it to the total
        for i in nodes:
            row = RowFound(i, [])
            #finds all the index that have 1's
            for index in range(0, len(adjacency_mat[0])):
                if adjacency_mat[i][index] == 1 and index in nodes:
                    row.candidate.append(index)
            top = 0
            length_of_row = 0
            #calculates how many neighbors are friends
            #calculates the top of the correlation coefficient equation
            for can in row.candidate:
                for index, rowAdj in enumerate(adjacency_mat[can]):
                    #each node has nodes in common but they are not the ones we are looking for ************************************
                    if rowAdj == 1 and adjacency_mat[row.row][index] == 1 and index in nodes:
                        top += 1
                if can in nodes:
                    length_of_row += 1

            #calculates the bottom of the correlation coefficient equation
            bottom = ( length_of_row * (length_of_row - 1))

            if bottom < 2:
                tots = top / 2
            else:
                tots = ((top/2) / (bottom / 2))

            #calculates the correlation coefficient for the node and saves it to TOTAL
            TOTAL = (TOTAL + tots)
        length = len(nodes)

        #once it is all calculated TOTAL is the correlation coefficient of the nodes that are passed to this function
        TOTAL = TOTAL / length

        return TOTAL > (percent / 100)


    #check if each node in the maximal clique is up to our standards in percentage
    def isQuasi(self, tempPattern):
        notfound = True
        for index, maximalPattern in enumerate(self.maximizedArray):
            if set (tempPattern.nodes).issuperset(maximalPattern.nodes):
                self.maximizedArray.pop(index)
                self.maximizedArray.append(tempPattern)
                notfound = False
                return
            elif set (maximalPattern.nodes).issuperset(tempPattern.nodes):
                return

        if notfound:
            self.maximizedArray.append(tempPattern)


    # Finds the maximized nodes
    def findMaximized(self, p, one_hop_local):
        #THE PROBLEM IS THAT WE ARE REMOVING ELEMENTS FROM THE LIST CANDIDATES AND LOOPING THROUGH THE SAME LIST
        temp_canid_list = copy.deepcopy(p.candidate)
        for candidate_of_p in temp_canid_list:
            #get the candidates of i from the 2 hop array
            level1twoHopCandidates = self.pattyArray2Hop[candidate_of_p]
            test1 = level1twoHopCandidates.candidate[:]

            #here we may need to check if the pattern above this node is a quasi.  Which would be removing the last element from the array
            level1twoHopCandidatesNew = self.pattyArray2Hop[candidate_of_p]
            candidate_of_candidate = level1twoHopCandidatesNew.candidate[:]
            pnodes_recursive = p.nodes[:]
            pnodes_recursive.append(candidate_of_p)

            pat = Pattern(pnodes_recursive, list(self.findIntersection(p.candidate, candidate_of_candidate)))
            self.findMaximized(pat, one_hop_local)
            #print("length: ", len(p.candidate))
            if(len(self.findIntersection(p.candidate, test1)) == 0):
            #if self.coieficOf( one_hop_local, p.nodes):
                if(self.coieficOf(one_hop_local, p.nodes)):
                    self.isQuasi(p)
                if len(p.candidate) > 0:
                    tempNodes = p.nodes[:]
                    tempNodes.extend(p.candidate)
                    pat1 = Pattern(tempNodes, [])
                    if(self.coieficOf(one_hop_local, pat1.nodes)):
                        self.isQuasi(pat1)


    def findIntersection(self, a, b):
        return set(a).intersection(b)

# run main
if  __name__ =='__main__':
    q = QuasiClique().main()
