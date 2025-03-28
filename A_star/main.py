import heapq  
import sys

def findPath(map , start , end):
    if(map[start[0]][start[1]] == 1 or map[end[0]][end[1]] == 1):
        return 
    
    dir = [[-1,0],[1,0],[0,-1],[0,1]]

    heap = []
    heapq.heappush(heap , (0, start))

    p = {}

    cost_g = [[sys.maxsize for n in range(len(map[0]))] for m in range(len(map))]
    cost_g[start[0]][start[1]] = 0

    cost_f = [[sys.maxsize for n in range(len(map[0]))] for m in range(len(map))]
    cost_f[start[0]][start[1]] = h_manhattan(start,end)

    while len(heap) != 0:
        current = heapq.heappop(heap)[1]
        
        if(current == end):
            return p 

        for move in dir :
            next = [current[0] + move[0],current[1] + move[1]]
            
            if(next[0] < 0 or next[0] >= len(map)):
                continue
            if(next[1] < 0 or next[1] >= len(map[0])):
                continue
            if(map[next[0]][next[1]] == 1):
                continue

            cost = cost_g[current[0]][current[1]] + 1
            
            if(cost < cost_g[next[0]][next[1]]):
                p[(next[0],next[1])] = current
                cost_g[next[0]][next[1]] = cost
                cost_f[next[0]][next[1]] = cost + h_manhattan(next , end)
                heapq.heappush(heap , (cost_f[next[0]][next[1]] , next))
    return 



def h_manhattan(pos1,pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def printPath(map , path , start , end):
    print("Path : ")
    for i in range(len(map)):
        for j in range(len(map[0])):
            if([i,j] == start):
                print(" S ",end=" ")
                continue
            if([i,j] == end):
                print(" E ",end=" ")
                continue
            if(map[i][j] == 2):
                print(" X ",end=" ")
                continue
            print(" " + str(map[i][j]) + " ",end=" ")
        print("\n")


if __name__ == "__main__":
    map = [[0,0,0,0,0,0],
           [0,1,1,1,1,1],
           [0,0,0,0,0,0],
           [0,1,1,1,1,0],
           [0,0,0,0,0,0]]
    
    start = [0,0]
    end = [4,5]

    path = findPath(map,start,end)

    current = end

    while current != start:
        map[current[0]][current[1]] = 2
        current = path[(current[0],current[1])]
    map[start[0]][start[1]] = 2

    printPath(map,path,start , end)