from pacal import *
from pylab import figure, show

from pacal.depvars.models import Model
from pacal.depvars.nddistr import NDProductDistr, Factor1DDistr

#X = BetaDistr(3, 3, sym = "X")
#Y = BetaDistr(4, 2, sym = "Y")
#Z = X + Y
#Z.setSym("Z")
#
#for c in [0.1, 0.5, 0.9, 1.5, 1.9]:
#    print "X + Y =", c
#    print "==================="
#    P = NDProductDistr([Factor1DDistr(X), Factor1DDistr(Y)])
#    M = Model(P, [Z])
#    figure()
#    
#    print M
#    M.varschange(Y, Z)
#    print M
#    M.condition(Z, c)
#    print M
#    M.summary()
#    M.plot()
#    M.varschange(X, Y)
#    print M
#    M.plot()
#    M.summary()
#    print


X1 = BetaDistr(3, 3, sym = "X1")
X2 = BetaDistr(2, 2, sym = "X2")
X3 = BetaDistr(3, 5, sym = "X3")
X4 = BetaDistr(3, 3, sym = "X4")
S2 = X1 + X2
S2.setSym("S2")
S3 = S2 + X3
S3.setSym("S3")

P = NDProductDistr([Factor1DDistr(X1), Factor1DDistr(X2), Factor1DDistr(X3)])
M = Model(P, [S2, S3])
#M.eliminate_other([S3])
print M
M.varschange(X1, S2)
print M
M.varschange(X3, S3)
print M
M.condition(S3, 0.8)
M.varschange(S2, X3)
M.varschange(X3, X1)

print M
M.plot()
M.condition(X1, 0.4)
print M
figure()
M.plot()


M = Model(P, [S2, S3])
M.eliminate_other([S3])
M.varschange(X1,S3)
print M
M.condition(S3, 0.8)
M.plot()
figure()
M.condition(X3, 0.4)
M.plot()

#print M
#M.varschange(X1, S2)
#M.eliminate(X1)
#print M
#M.eliminate(X2)
#print M
#M.varschange(X3, S3)
#M.eliminate(X3)
#print M
#M.plot()
#show()

show()