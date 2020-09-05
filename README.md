*  python solution for Indicium
This solution use python backtracking and python laziness

** Problem
 *
 Indicium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

 A Latin square is an N-by-N square matrix in which each cell contains one of N different values, such that no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

 The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

 Given values N and K, produce any N-by-N "natural Latin square" with trace K, or say it is impossible. For example, here are two possible answers for N = 3, K = 6. In each case, the values that contribute to the trace are underlined.

 2 1 3   3 1 2
 3 2 1   1 2 3
 1 3 2   2 3 1
 Input

 The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line containing two integers N and K: the desired size of the matrix and the desired trace.
 Output

 For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no answer for the given parameters or POSSIBLE otherwise. In the latter case, output N more lines of N integers each, representing a valid "natural Latin square" with a trace of K, as described above. 
 *
