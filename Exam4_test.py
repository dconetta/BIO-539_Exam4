# python3 string_script.py py.test

#test multiple inputs (e.g. large k or small k)

from string_script import *

import pandas as pd 

# test obs kmer function 1
def test_obs_kmers_1():
  k = 1
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = 3
  assert actual_result == expected_result
  
  # test obs kmer function 2
def test_obs_kmers_1():
  k = 0
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = 
  assert actual_result == expected_result

# test poss kmer function
def test_poss_kmer():
  k = 1
  actual_result = poss_kmers(k, string)
  expected_result = 4
  assert actual_result == expected_result

# look at obs/poss for letters 
# test the making of the dataframe (df_output)
# cant ref variables from not function 
def test_df_output1():
  string = 'ATT'
  df_output_exp = [[2,3], [2,2], [1,1],[5,6]] # this is lst of list, make data.frame (check for functions)
  df_actual = make_df(string)
  result =  df_exp.equals(df_actual) #also try compare (this is an output, its a dataframe)
  assert result == True


# next make test for linguistic function







13

