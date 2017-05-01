#!/bin/python

import sys
sys.stdin = open('./2-input', 'r')

n = int(raw_input().strip())
# Each index 'i' contains the energy necessary to travel 'i' units.
w = map(int, raw_input().strip().split(' '))

# connections as list pointing to list of connected nodes
con = [[] for _ in range(n+1)]
# shortest path, matrix of shortest path between nodes
# -1      => shortest path not determined
# x == y => distance = 0
# sp = [[-1 if x != y else 0 for x in range(0, n+1)] for y in range(0, n+1)]
sp = []

for a0 in xrange(n-1):
    # A hallway connects offices 'u' and 'v'
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    # Write Your Code Here
    con[u].append(v)
    con[v].append(u)

def printMatrix(matrix):
    for i in range(1, n+1):
        print i, matrix[i][1:]

LOG = False

def printLog(*message):
    #print "nrargs", len(message)
    #print message
    if not LOG:
        return
    for i in message:
        sys.stdout.write(str(i) + " ")
    print

def shortestPath (start, endpoints, beenhere, length):
    #compute shortest path
    # length: int = pathlength, nr of steps made upto now
    # endpoints: []   = all points reachable from original start in equal nr of steps

    # shortest path already found somewhere else?
    # print("  CALLED  ", "( ", start, endpoints, beenhere, length, " )")
    print length
    newEndpoints = [] # don't touch original path
    # minPathLength = sys.maxint
    global sp

    if len(endpoints) == 0:
        return # 0

    for e in endpoints:
        if e in beenhere: 
            # every next path passing s will be longer, so skip
            printLog("    BEENHERE ")
            continue
        if sp[e] > 0:
            # path from start to e already computed
            printLog( "  MIN  ", "FOR ", start, "->", e, " | LEN ", length, " COMPUTED ", sp[start][e])
            continue
        # path length to e not yet computed
        sp[e] = length
        # compute path length for points connected to e
        newEndpoints.extend(con[e])
        # print "2--> ", start, e, newEndpoints

    beenhere.extend(endpoints)
    shortestPath(start, set(newEndpoints), beenhere, length + 1)

    printLog("  NEXT ", "STARTSET ", " LEN", length+1)
    # for i in range(len(endpoints)):
        # beenhere.pop()
    printLog("  RETURNED ", "( ", start, ", ", beenhere, length, " )", " MINPATHLENGHT ")
    return  # minPathLength

#shortestPath(3, 4, 0, [])
#printMatrix(sp)
#sys.exit()

def computeShortestPathForAllNodes():
    for i in range(1, n+1):
        # print i
        printLog("COMPUTE ==> ", i, "N")
        # only compute sp if not computed yet
        shortestPath(i, [i], [], 0)

def computeEnergy():
    global sp
    output = ""
    for meetingRoom in range(1, 3):
        energy = 0
        print "Start INIT meetingroom ", meetingRoom
        sp = [0 for _ in range(0, n+1)]
        print "Done  INIT meetingroom ", meetingRoom
        shortestPath(meetingRoom, [meetingRoom], [], 0)
        for office in range(1, n+1):
            energy += w[sp[office]]
        output += str(energy) + " "
        print energy
    return output


# computeShortestPathForAllNodes()
# printMatrix(sp)

print computeEnergy()
