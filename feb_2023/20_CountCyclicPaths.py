#   Given a triangular pyramid with its vertices marked as O, A, B and C and a number N,
#   the task is to find the number of ways such that a person starting from the origin O initially, 
#   reaches back to the origin in N steps. In a single step, a person can go to any of its adjacent vertices.
  def countpaths(N):
        AB,O=0,0
        for i in range(2,N+1):
            total=3**(i-1)
            AB=total -O
            O=AB
        return(AB%1000000007)
