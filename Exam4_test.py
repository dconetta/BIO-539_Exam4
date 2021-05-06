# python3 string_script.py py.test
# setting tests for Exam4 python script to purposefully pass and fail to make sure functions are legitimate

from Exam4 import *

import pandas as pd 

# Observed Kmer Function Test 1
# test when K value is 1 for given string 'ATTTGGATT'
def test_obs_kmers_1():
  k = 1
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = 3 #calculated from obs_kmer function
  assert actual_result == expected_result
  
# Observed Kmer Function Test 2
# test when K value is 0 for given string 'ATTTGGATT'
  # k should not run because in script told that all k values should be greater than 0 (NA should be output)
def test_obs_kmers_1():
  k = 0
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = NA
  assert actual_result == expected_result
  
# Observed Kmer Function Test 3
# test when K value is 100 for given string 'ATTTGGATT'
  # k should not run because in script it was set that that k values cannot exceed the length of the string
def test_obs_kmers_1():
  k = 100
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = NA
  assert actual_result == expected_result

# Observed Kmer Function Test 4
# test when K value is 1 for given string 'ATTTGGAKX'
  # k should not run because in script made it so that characters outside of A, C, T, and G were not to be included
def test_obs_kmers_1():
  k = 1
  string = 'ATTTGGAKX'
  actual_result = obs_kmers(k, string)
  expected_result = NA
  assert actual_result == expected_result
  
#Possible Kmer Function Test 1 
# when K value is 1 for given string 'ATTTGGATT'
def test_poss_kmer():
  k = 1
  string = 'ATTTGGATT'
  actual_result = poss_kmers(k, string)
  expected_result = 4
  assert actual_result == expected_result


# Making Data Frame Function Test 1 
# when K value is for given string 'ATT'
  #brackets indicate the list of observed and possible kmer values and including the total row
def test_df_output1():
  string = 'ATT'
  df_output_exp = {'observed kmers': [2,2,1,5], 
            'possible kmers': [3,2,1,6]
            }
  df_actual = make_df(string)
  test = pd.DataFrame(df_output)
  final =  df_output_exp.equals(df_actual) #also try compare (this is an output, its a dataframe)
  assert final == True


# Linguistic Complexity Function Test 1 
# when K value is for given string 'ATT'

def test_ling_complex1():
  df_output_exp = {'observed kmers': [2,2,1,5], 
            'possible kmers': [3,2,1,6],
            index = [1,2,3, 'total]}
  actual_result = linguistic_complexity(df_output_exp)
  expected_result = 0.83
  assert == actual_result == expected_result