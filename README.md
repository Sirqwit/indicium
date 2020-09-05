# python solution for Indicium
This solution use python backtracking and python laziness.
I suggest you look [Laziness in Python - Computerphile](https://www.youtube.com/watch?v=5jwV3zxXc8E&t=318s) and [Python Sudoku Solver - Computerphile](https://www.youtube.com/watch?v=G_UYXzGuqvM)

## Problem
 
> Indicium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.
>
> A Latin square is an N-by-N square matrix in which each cell contains one of N different values, such that no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.
>
> The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).
>
> Given values N and K, produce any N-by-N "natural Latin square" with trace K, or say it is impossible. For example, here are two possible answers for N = 3, K = 6. In each case, the values that contribute to the trace are underlined.
>
>- 2 1 3 - 3 1 2
>- 3 2 1 - 1 2 3
>- 1 3 2 - 2 3 1
> 
> Input
>
> The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line containing two integers N and K: the desired size of the matrix and the desired trace.
> Output
>
> For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no answer for the given parameters or POSSIBLE otherwise. In the latter case, output N more lines of N integers each, representing a valid "natural Latin square" with a trace of K, as described above. 
 
## Solution

The idea is to first find possibles diagonal throught backtracking, and save this maybe long list. 
This is the code:
```python
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
```

The function dpos checks if the value can actually be in the diagonal position.

In a similar way we check if the grid can be filled:
```python
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
```

In conclusion the idea is: 
- find possible diagonal matrix. 
- try to fill it.
- if is true print POSSIBLE and the matrix solution.
- else try another diagonal.

The problem of this program, besides the fact that the code can be written better, is that is very slow if the diagonal exist but it can not be filled.
A solution to improve the performance is to create a better diagonal solver and add condition.
The good thing about this program is that it can easly print all possibles solution (I commented out that part in the code). Keep in mind that the grid must be small otherwise it will take very long time :)
