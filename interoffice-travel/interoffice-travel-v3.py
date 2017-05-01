#!/bin/python

import sys
sys.stdin= open('\\\\ubus\public\downloads\source\\2-input.txt', 'r')

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
def shortestPath (orgstart, start, end, beenhere, length, depth):
	#compute shortest path
	# length: int = shortest pathlength from start set to end point found up to now
	# start: []   = all points reachable from original start in equal nr of steps

	# shortest path already found somewhere else?
	printLog("  CALLED  ", "( ", start, ", ", end, beenhere, length, " )"  )
	# print "DEPTH ", depth
	if length <= 0:
		return sys.maxint

	newStart = [] # don't touch original path
	minPathLength = sys.maxint

	for s in start:
		if s in beenhere: # every next path passing s will be longer, so skip
			printLog("    BEENHERE ", s)
			continue
		if sp[s][end] == 0:
			depth -= 1
			return 0
		if sp[s][end] > 0:
			# sp already computed
			printLog( "  MIN  ",  "FOR ", start, "from s: ", s, "->", end, " | LEN ", length, " COMPUTED ", sp[s][end] )
			minPathLength = min(minPathLength, sp[s][end])
		else:
			# depth = min length from initial start point to point s
			sp[orgstart][s] = depth
			# points for which length still has to be computed
			newStart.extend(con[s])

	if newStart == []:
		depth -= 1
		return minPathLength
	# minPathLength should be length of shortest path found anywhere
	minPathLength = min( minPathLength, length)

	beenhere.extend(start)
	minPathLength = min(minPathLength, shortestPath(orgstart, set(newStart), end, beenhere, minPathLength - 1, depth + 1) + 1)

	printLog( "  NEXT ", "STARTSET ", newStart, " LEN", length+1)
	for i in range(len(start)):
		beenhere.pop()
	printLog("  RETURNED ", "( ", start, ", ", end, beenhere, length, " )", " MINPATHLENGHT ", minPathLength  )
	depth -= 1
	return  minPathLength

#shortestPath(3, 4, 0, [])
#printMatrix(sp)
#sys.exit()

def computeShortestPathForAllNodes():
	for i in range(1, n+1):
		for j in range(1, n+1):
			# only compute sp if not computed yet
			printLog( "COMPUTE ==> ", i, j)
			if sp[i][j] <= 0 or sp[j][i] <= 0:
				sp[i][j] = sp[j][i] = shortestPath(i, [i], j, [], sys.maxint, 0)
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
# printMatrix(sp)

print computeEnergy()
