Wherever you have a long list of data and need to perform some mathematical transformation over them, strongly consider
turning those python data structures (list or tuples or dictionaries) into numpy ndarray objects and
using inherent vectorization capabilities.

Why is Python so slow?
* C, Fortran, etc.: **static typing** and **compiled code** leads to fast execution
    * But: lots of development overhead in declaring variables, no interactive prompt, etc.
* Python, R, Matlab, IDL, etc.: **dynamic typing** and **interpreted excecution** leads to fast development
    * But: lots of execution overhead in dynamic type-checking, etc. Each python operation comes with a small
           type-checking overhead(check the count and find the right code).
           With many repeated small operations(e.g in a loop), this overhead becomes significant!


###### Strategies for making Python:
1. Use Numpy ufuncs
2. Use Numpy vectors
3. Use Numpy arrays i.e ndarray
    * Use Numpy aggregates
    * Use Numpy broadcasting
    * Use Numpy slicing, masking and fancy indexing
4. Use Numpy views

Numpy pushes the looped operations in to compiled code so that they can be done quickly because in compiled code the
type check happens only 1 time for the entire loop of a million repetition.

---
X = np.arange(9).reshape(3, 3).astype(np.int16)
