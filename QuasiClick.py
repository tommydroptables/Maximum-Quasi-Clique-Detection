__author__ = 'Tom'

import re, string, sys, igraph, numpy
from Patterns import Pattern


def main():

    file1 = open('C:\\Users\\Tom\\PycharmProjects\\Quasi\\poop.txt', 'r')
    g = igraph.Graph.Read_Ncol(file1,names=True,directed=False,weights=False)
    file1.close()
    one_hop = g.get_adjacency().data
    one_h = numpy.array(one_hop)
    two_hop = numpy.zeros((len(one_h[0]), len(one_h[0])))
    pattyArray = []



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
        pattyArray.append(patty)

    '''
    #display candidates for each node in graph that are 2 hop
    for i in two_hop:
        for j in i:
            print(j, " ", end="")
        print("\n")
    '''

    #add candidates from two_hop array while sorting them while you add them
    #WE MIGHT NOT NEED TO SORT THE CANIDATES WHEN WE ADD THEM###########################################
    for i in range(0, len(two_hop[0])):
        for j in range(0, len(two_hop[0])):
            if two_hop[i][j] > 0:
                if j > i:
                    if j not in pattyArray[i].candidate:
                        pattyArray[i].candidate.append(j)
                        pattyArray[i].candidate.sort()


    # display nodes and their canidates that are two hops away
    for p in pattyArray:
        for n in p.getNode():
            print("Node ", n, ":")
        for c in p.getCandidate():
            print(c, " ", end="")
        print("\n")




    #find the maximized
    #for patt in Pattern.level1:
    #   Pattern.findMaximized(patt)


   # two_hop = numpy.zeros((8, 8))

    '''
    #this multiplies two arrays
    for row in range(0, len(one_hop[0])):
        for row2 in range(0, len(one_hop[0])):
            for col in range(0, len(one_hop[0])):
                two_hop[row][row2] += one_hop[row][col] * one_hop[col][row2]
    '''
    #add all the candidates for each node in level one to level on array
    #by making pattern objects then adding them to the level1 array


    #display adjacency matrix
    '''
    for i in one_hop:
        for j in i:
            print(j, " ", end="")
        print("\n")

    #Display two_hops matrix
    #http://puu.sh/cUyrj/c5909616bd.png
    #http://puu.sh/cUyrj/c5909616bd.png
    for i in two_hop:
        for j in i:
            print(j, " ", end="")
        print("\n")
    '''

    #display graph with iGraph
    layout = g.layout("kk")
    #create labels
    label = []
    for i in range(0, (len(one_hop[0]))): str(label.append(i))
    igraph.plot(g, layout=layout, vertex_label=label)

# run main
if  __name__ =='__main__':
    main()




