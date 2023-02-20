  def apna (N):
        AB,O=0,0
        for i in range(2,N+1):
            total=3**(i-1)
            AB=total -O
            O=AB
        return(AB%1000000007)
