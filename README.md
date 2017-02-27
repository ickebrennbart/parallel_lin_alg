# parallel_lin_alg
Python script that distributes large matrix operations across multiple cores

This function takes two vectors/matrices as input arguments along with a linear algebra operation (by default the dot product). The parallel flag indicates if the operation should be carried out on a single core or multiple ones. The cores parameter determines the number of cores to use or the number of parallel operations to run.

During initialization of your code, an example operation could be run on a single core and in parallel to determine the possible speed up of distributing the  computation.

Below is an example graph showing results of computing the dot product of increasing matrix sizes on a single and 4 cores.
