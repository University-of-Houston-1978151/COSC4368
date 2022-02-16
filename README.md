# COSC4368-HW1
Implement Randomized Hill Climbing, called RHC in the following, and conduct a set of experiments, minimizing the folowing function f:

f(x,y) = -(y+47) * sin( sqrt( abs( (x/2) + (y+47) ) ) ) - x * sin( abs(x - (y + 47)) )
With -512 <= x,y <= 512

Your procedure should be called RHC and have the following parameters:
- sp: starting point of the RHC run
- p: number of neighbors of the current solution that will be generated (amount of times the function will be looped)
- z: neighborhood size (x,y minus a randomly generated number depending on the range of z; for example, if z is 0.5, the range will be [-0.5, 0.5]. Algorithm will randomly pick a number between [-0.5, 0.5] and subtract it from x then do the same for y)
- seed: the seed for generating random numbers