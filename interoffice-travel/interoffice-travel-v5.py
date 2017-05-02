#!/bin/python

import sys
import array

sys.stdin = open('./2-input', 'r')
# sys.stdin = open('./1-input', 'r')

n = int(raw_input().strip())
# Each index 'i' contains the energy necessary to travel 'i' units.
w = map(int, raw_input().strip().split(' '))

# connections as list pointing to list of connected nodes
con = [[] for _ in range(n+1)]

for a0 in xrange(n-1):
    # A hallway connects offices 'u' and 'v'
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    # Write Your Code Here
    con[u].append(v)
    con[v].append(u)

# shortest path, matrix of shortest path between nodes
# -1      => shortest path not determined
# x == y => distance = 0
sp = [-1 for _ in xrange(0, n+1)]

def printMatrix(matrix):
    for i in xrange(1, n+1):
        sys.stdout.write(str(matrix[i]) + " ")
    print

LOG = False

def printLog(*message):
    #print "nrargs", len(message)
    #print message
    if not LOG:
        return
    for i in message:
        sys.stdout.write(str(i) + " ")
    print

def shortestPath (start, endpoints, length, sp):
    #compute shortest path
    # length: int = pathlength, nr of steps made upto now
    # endpoints: []   = all points reachable from original start in equal nr of steps

    # shortest path already found somewhere else?
    # print("  CALLED  ", "( ", start, endpoints, length, " )")
    # minPathLength = sys.maxint
    newEndpoints = [0 for _ in xrange(n+1)]
    global pr
    def incend(ne, i, e):
        ne[i] = e
        return i + 1

    while len(endpoints) != 0:
        newEndpoints = [] # don't touch original path
        newEndpointsExtend = newEndpoints.extend
        # nrNewEndpoints = 0

        for e in endpoints:
            if sp[e] >= 0:
                # path from start to e already computed
                # printLog( "  MIN  ", "FOR ", start, "->", e, " | LEN ", length, " COMPUTED ", sp[e])
                continue
            # path length to e not yet computed
            sp[e] = length
            # compute path length for points connected to e
            newEndpointsExtend(con[e])

        endpoints = newEndpoints
        length += 1
    return  # minPathLength

def computeShortestPathForAllNodes():
    for i in xrange(1, n+1):
        # print i
        printLog("COMPUTE ==> ", i, "N")
        # only compute sp if not computed yet
        shortestPath(i, [i], [], 0)

def computeEnergy():
    global sp
    output = ""
    for meetingRoom in xrange(1, n+1):
        energy = 0
        sp = [-1 for _ in xrange(0, n+1)]
        endpoints = [0 for _ in xrange(0, n+1)]
        shortestPath(meetingRoom, [meetingRoom], 0, sp)
        for office in xrange(1, n+1):
            energy += w[sp[office]]
        output += str(energy) + " "
        # printMatrix(sp)
    return output


print computeEnergy()
