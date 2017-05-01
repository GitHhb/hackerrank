#!/bin/python

import sys

n = int(raw_input().strip())
# Each index 'i' contains the energy necessary to travel 'i' units.
w = map(int, raw_input().strip().split(' '))

# connections as list pointing to list of connected nodes
con = [[] for _ in range(n+1)]
# shortest path, matrix of shortest path between nodes
# -1 	 => shortest path not determined
# x == y => distance = 0
sp = [ [-1 if x != y else 0 for x in range(0, n+1)] for y in range(0, n+1) ]
sp 

for a0 in xrange(n-1):
	# A hallway connects offices 'u' and 'v'
	u, v = raw_input().strip().split(' ')
	u, v = [int(u), int(v)]
	# Write Your Code Here
	con[u].append(v);
	con[v].append(u);

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

def shortestPath (start, end, curShortestLength, path):
	# sp already computed?
	if sp[start][end] >= 0:
		printLog( "  RTRN = COMPUTED", sp[start][end], "  TRY  ", start, "-", end, " PATH ", path)
		return sp[start][end]

	#compute shortest path f
	path.append(start)
	minPathLen = sys.maxint
	cycleFound = False
	for i in con[start]:
		# prevent cyclical graphs, if i already in path then skip i
		if i in path:
			printLog( "      DECYCLE", start, i, end)
			cycleFound = True
			continue
		printLog( "    TRY  ", start, i, end, " LEN", minPathLen, " PATH ", path)
		minPathLen = min(minPathLen, shortestPath(i, end, minPathLen, path))
	# store length of shortest path
	printLog( "  RESL ", start, "-", end, " LEN", minPathLen, " PATH ", path)
	minPathLen += 1
	# if cycle found we could not compute the shortest path for node start
	if not cycleFound:
		sp[start][end] = minPathLen
		sp[end][start] = minPathLen
	path.pop()
	printLog( "  STORE ", start, "-", end, minPathLen)
	return minPathLen

#shortestPath(3, 4, 0, [])
#printMatrix(sp)
#sys.exit()

def computeShortestPathForAllNodes():
	for i in range(1, n+1):
		for j in range(1, n+1):
			# only compute sp if not computed yet
			printLog( "COMPUTE ==> ", i, j)
			if sp[i][j] <= 0:
				shortestPath(i, j, 0, [])
				print i, j, sp[i][j]
		
def computeEnergy():
	output = ""
	for meetingRoom in range(1, n+1):
		energy = 0
		for office in range(1, n+1):
			energy += w[sp[office][meetingRoom]]
		output += str(energy) + " "
	return output


computeShortestPathForAllNodes()
#printMatrix(sp)

print computeEnergy()
