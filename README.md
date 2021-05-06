# BIO-539_Exam4

May 2021
Professor: Dr. Rachel Schwartz

The purpose of this repository is to create functions in python that will allow the
user to read in a sequence file and obtain the linguistic complexity for each line
of that sequence file (reads each line as a string). Then given the python script
the user should be able to test each of the functions created in the test script
to double check that all functions pass robust testing.

The linguistic complexity is the ratio of observed to possible kmers in a given 
sequence provided the amount of 'k' characters in a given sequence.

observed kmers are all the unique combinations of the string and substrings for
each value of 'k'. The possible kmers are all the potential combinations of 
characters of a sequence that is possible for that value of 'k'. 

For example for the string sequence 'ATTGGATT' for k = 1, the observed kmer
value is 3 (since only A, T, G are unique characters in this string) while
the possible kmer would be 4 because in a sequence there are four unique 
characters possible (A, T, G, and C). So if we took the linguistic complexity
of this example k = 1, for 'ATTGGATT' would be observed / possible or 
(3 / 4) = 0.75.

In this repository there are three files:

	- Exam4.py (the python script that calculates linguistic complexity)
	
	- Exam4_test.py (the python script that tests each function in Exam4)
	
	- seq_test.txt (text file of example sequence strings to use to output LC)

In the Exam4.py file five major functions are created in defined;
	- obs_kmer: calculates the observed kmers given the value k and string

	- poss_kmer: calculates the possible kmers given the value k and string

	- make_df: creates a data frame with all these values for given string
	
	- linguistic_complexity: calculates LC from data frame of given string
	
	- main: generalized to run any string to calculate LC

In Exam4_test the first four functions are tested to pass certain qualifications
to make sure the functions are robust enough to run any sequence string and the 
outcomes are trustworthy.

Lastly, seq_test is a text file of random sequence strings that the user can use
to run the created python scripts on to get csv file outputs of LC. 
