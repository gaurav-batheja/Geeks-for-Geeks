  Given a rectangle of dimensions L x B find the minimum number (N) of identical squares 
  of maximum side that can be cut out from that rectangle 
  so that no residue remains in the rectangle. 
  Also find the dimension K of that square.
  import math  
  def minimumSquares(self, L, B):
        dim = math.gcd(L, B)
        return ((L * B) // (dim ** 2), dim)
