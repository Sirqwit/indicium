import numpy as np

def create(k):
    return np.zeros([k,k], dtype = int)

def dpos(v, pos, k, s):
    s -= v
    if(s<0):
        return False
    if(pos==k-1):
        if(s!=0):
            return False
    return True

def diag(k, s):
    global grid
    for pos in range (k):
        if(grid[pos][pos]==0):
            for n in range (1,k+1):
                if dpos(n, pos, k, s):
                    s -= n
                    grid[pos][pos] = n
                    yield from diag(k, s)
                    grid[pos][pos] = 0
                    s += n
            return    
    yield (grid)

def pos(x,y,n,k):
    global grid
    for i in range(0,k):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    return True

def solve(k):
    global grid
    for y in range (k):
        for x in range (k):
            if grid[y][x] == 0:
                for n in range (1, k+1):
                    if pos(x,y,n,k):
                        grid[y][x] = n
                        yield from solve(k)
                        grid[y][x] = 0
                return
    yield (grid)

def pr(sol, k):
    for y in range (k):
        for x in range (k):
            print(sol[x][y], '', end = '')
        print()

def main():
    global grid
    N = int(input()) 
    for i in range (1, N+1):
        found = False
        k, s = input().split()
        k = int(k)
        s = int(s)
        grid = create(k)
        d = diag(k, s)        
        print('Case #{}: '.format(i), end = '')
        
        for possible in d:
            #print(possible)
            grid = possible
            s = solve(k)
            #solution = next(s)
            
            for t in s:
                solution = t
                found = True
                break
            
            if(found):
                break
        
        if(found):
            print("POSSIBLE")
            pr(solution,k)
        else:
            print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
