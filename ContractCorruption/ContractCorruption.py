forestM = []
forestD = []
edgesM = []
edgesD = []
allEdges = []

class ForestSet:
  def __init__(self, p, rank):
    self.p = p
    self.rank = rank
    
def main(N, C):
    initForest(N)
    countM, countD = calcContracts(C)
    printResult(countM, countD)
    # Uncomment the following line to print out the spanning tree
    #findSpanningTree(countM, countD, N)

def initForest(N):
    for n in range(N):
        m = ForestSet(n, 0)
        k = ForestSet(n, 0)
        forestM.append(m)
        forestD.append(k)

def findSet(forest, x): 
    if forest[x].p != x:
        forest[x].p= findSet(forest, forest[x].p)
    return forest[x].p

def union(forest, v, u):
    s1 = findSet(forest, v)
    s2 = findSet(forest, u)
    if forest[s1].rank < forest[s2].rank:
        forest[s1].p = s2
    else:
        if forest[s1].rank == forest[s2].rank:
            forest[s1].rank += 1
        forest[s2].p = s1

def calcContracts(C):
    countM = 0
    countD = 0
    for i in range(C):
        line = raw_input().split()
        u = int(line[0]) - 1
        v = int(line[1]) - 1
        allEdges.append((u, v, line[2]))
        if line[2] == 'MAVERICK' and countM < N/2:
            setU = findSet(forestM, u)
            setV = findSet(forestM, v)
            if setU != setV:
                edgesM.append((u, v, 'MAVERICK'))
                union(forestM, setV, setU)
                countM += 1
        elif line[2] == 'DESPERADO' and countD < N/2:
            setU = findSet(forestD, u)
            setV = findSet(forestD, v)
            if setU != setV:
                edgesD.append((u, v, 'DESPERADO'))
                union(forestD, setV, setU)
                countD += 1
    return countM, countD

def printResult(countM, countD):
    if countD < int(N)/2 or countM < int(N)/2:
        print int(N)-1-2*min(countD,countM)
    else:    
        if (int(N)-1)%2 ==0:
            print 0
        else:
            print 1

def addEdgesFromLargerForest(companyName, smallForest, sol, N):
    for (u, v, company) in allEdges:
        if company == companyName:
            # Check if adding (u, v) will form a cycle
            setU = findSet(smallForest, u)
            setV = findSet(smallForest, v)
            if setU != setV:
                union(smallForest, setV, setU)
                sol.append((u, v, company))
                if len(sol) == N -1:
                    return sol

def findSpanningTree(countM, countD, N):
    sol = []
    # 1) Add all the edges of the smaller forest into the spanning tree
    # 2) From all edges, if it's from the company of the bigger forest
    # check if adding it will form a cycle, if not, keep adding until
    # the total edge number = N - 1
    if countM <= countD:
        sol.extend(edgesM)
        addEdgesFromLargerForest("DESPERADO", forestM, sol, N)
        sol = map(lambda x: (x[0]+1, x[1]+1, x[2]), sol)
        for (u, v, company) in sol:
            print u, v, company
    else:
        sol.extend(edgesD)
        addEdgesFromLargerForest("MAVERICK", forestD, sol, N)
        sol = map(lambda x: (x[0]+1, x[1]+1, x[2]), sol)
        for (u, v, company) in sol:
            print u, v, company

if __name__ == '__main__':
    [N, C] = map(int, raw_input().split())
    main(N, C)
