import sys

class IDS:
    time = 0
    length = 0
    N = int()
    M = int()
    maze = list()
    visited = list()


    def __init__(self):
        with open(sys.argv[1], 'r') as f:
            inputStrings = f.readlines()
        arraySize = inputStrings.pop(0)
        self.N, self.M = map(int,arraySize.split())
        self.visited = [[0 for i in range(self.M)] for j in range(self.N)]
        for row in inputStrings:
            localList1 = row.split()
            localList2 = list()
            for i in localList1:
                localList2.append(int(i))
            self.maze.append(localList2)

    def findStartingPoint(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.maze[i][j] == 3:
                    return i, j

    def run(self):
        exited = False
        maxDepth = 1
        s1, s2 = self.findStartingPoint()

        def dfs(s1, s2, depth):
            self.time += 1
            if self.visited[s1][s2] == 1 or self.maze[s1][s2] == 1 or depth > maxDepth:
                return False
            self.visited[s1][s2] = 1
            if self.maze[s1][s2] == 4:
                return True
            exited = False
            if s1+1 < self.N and exited == False:
                exited = dfs(s1+1, s2, depth+1)
            if s2 > 0 and exited == False:
                exited = dfs(s1, s2-1, depth+1)
            if s1 > 0 and exited == False:
                exited = dfs(s1-1, s2, depth+1)
            if s2+1 < self.M and exited == False:
                exited = dfs(s1, s2+1, depth+1)
            if exited == True:
                self.maze[s1][s2] = 5
            return exited

        while exited == False:
            self.time = 0
            exited = dfs(s1,s2,1)
            self.visited = [[0 for i in range(self.M)] for j in range(self.N)]
            maxDepth += 1

        self.maze[s1][s2] = 3
        for i in range(self.N):
            for j in range(self.M):
                if self.maze[i][j] == 5:
                    self.length += 1

        output=str()
        for row in self.maze:
            for point in row:
                output = output + str(point)+' '
            output += '\n'
        output += '---\nlength='+str(self.length)+'\ntime='+str(self.time)+'\n'

        with open(sys.argv[2], 'w') as f:
            f.writelines(output)



if __name__ == "__main__":
    ids=IDS()
    ids.run()