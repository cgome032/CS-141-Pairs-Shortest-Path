import sys
import re
import time

import math

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")

vertices=[]
edges=[]

def BellmanFord(G):
    pathPairs=[]
    #for u in G[0]:
    for source in vertices:
        vertexPairs = []
        for sink in vertices:
            vertexPairs.append([(source,sink), math.inf])
        pathPairs.append(vertexPairs);
        pathPairs[source][source][1] = 0
        #print("Debugging for vertex:",source)
        #for x in pathPairs[source]:
        #    print(x)
        #for i in range(1,len(vertices)-1):
        #    print("Printing i",i)
        for j in range(len(edges)):
            # Debugging purposes
            #print("Printing j",j)
            for k in range(len(edges)):
                #Debugging purposes
                #print("Printing k",k)
                if pathPairs[source][k][1] > pathPairs[source][j][1] + float(edges[j][k]):
                    pathPairs[source][k][1] = pathPairs[source][j][1] + float(edges[j][k])
        #print("Printing PathPairs:")
        #for i in pathPairs[source]:
        #    print (i)

        # Check for negative cycle
        for u in range(len(edges)):
            for v in range(len(edges)):
                if pathPairs[source][v][1] > pathPairs[source][u][1] + float(edges[u][v]):
                    print("There is a negative cycle")
                    return False

    # Fill in your Bellman-Ford algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    for i in pathPairs:
        print(i)
    return (pathPairs)

def FloydWarshall(G):
    pathPairs=[]
    Distance = 0
    Distance =(edges)
    for x in Distance:
        print(x)
    # Fill in your Floyd-Warshall algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            for k in range(len(vertices)):
                if j == k:
                    Distance[j][k] = 0
                else:
                    Distance[j][k] = min(float(Distance[j][k]),float(Distance[j][i]) + float(Distance[i][k]))

    for i in Distance:
        print(i)

    return pathPairs

def readFile(filename):
    global vertices
    global edges
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
    #Debugging
    print("Printing vertices")
    for i in vertices:
        print(i)
    print("Printing edges")
    for i in edges:
        print(i)
    return (vertices,edges)

def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    if algorithm == 'b' or algorithm == 'B':
        BellmanFord(G)
    if algorithm == 'f' or algorithm == 'F':
        FloydWarshall(G)
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
        FloydWarshall(G)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
