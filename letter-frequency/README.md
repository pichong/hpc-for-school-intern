Letter Frequency
----------------

First, have a look at Wikipedia article on letter frequency: https://en.wikipedia.org/wiki/Letter_frequency
Then develop the different versions of the program and guess the language of each file: file\*.txt.

### Version 1
First version of the program that counts number of 'e' characters in a text file
and compute its apparition frequency

### Version 2
Second version of the program that compute frequency of characters from 'a' to 'z'.
It uses the ord() and chr() functions to get int associated value of a character so that it
can store the number of occurences of the characters in an array.

### Version 3
Third version of the program that perform parallel computing of the frequency of characters.
The file is divided into 'nranks' portions, and each rank works on its portion.
Results are aggregated at the end with an MPI reduce operation.

Using the "time" command, evaluate execution time in function of number of tasks working in parallel.
