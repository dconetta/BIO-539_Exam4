#!/usr/bin/env python3
import argparse
import pandas as pd


# function to calculate k and possible kmers given a string of characters [ATCG] 
def  poss_kmer(k, string):
    ''' 
    This is a function to caluclate k and possible kmers given a string of characters
    for exmaple: ATTGGCATT
    
    k: kmer length
    string: string of characters 
    
    return: possible number of characters to the k or number of substrings that
    would fit in the string
     
    '''
    string_l = len(string)
    poss_a = string_l + 1 - k
    poss_b = 4 ** k
    if poss_a < poss_b:
        return poss_a
    else:
        return poss_b

# function to calculate k and observed kmers given a string of characters [ATCG] - also known as the actual kmers       
def obs_kmer(k, string): 
    ''' 
    This is a function to caluclate k and observed kmers given a string of characters
    for exmaple: ATTGGCATT
    
    k: kmer length
    string: string of characters 
    
    return: possible combinations of substrings (given k)
     
    '''
    full_list = [] # create empty data frame with duplicates
    unique_list = [] # create empty data frame for unique combinations
    count = 0 # create empty counter 
    string_l = len(string) # calculate length of the string as done above 
    for i in range(1,string_l+1): # indexing with i across all kmer values
        single_k = string[(i-1):(i-1+k)] # defining the range of k values [1:length(string)] 
        if len(single_k) == k: # only include kmers of the length we're looking at 
            full_list.append(single_k) # add all kmers to a df 
    for item in full_list:
        if item not in unique_list: # select unique combinations
            count += 1 # add 1 to running count every time there is a new combination
            unique_list.append(item)
    return(count) # this is the total number of unquie combinations of k (1:9) letters

# function to create a data frame that includes columns for k, possible, and observed kmers given a string of characters [ATCG]        
def make_df(string): 
    ''' 
    This is a function to create table of possible, and observed kmers given a string of characters
    for exmaple: ATTGGCATT
    
    string: string of characters 
    
    return: table with totals that equal linguistic complexity 
     
    '''
    df_empty = [] # create empty data frame
    string_l = len(string)
    for k in range(1,string_l+1):
        df_output.append([obs_kmer(k, string), poss_kmer(k, string)])
    df_output = pd.DataFrame(df_output, index = range(1, string_l+1), columns =  ["observed kmers", "possible kmers"])
    df_output.loc['Total'] = df_output.sum()
    return(df_output)

# function to caluclate linguistic complexity (ratio of total observed and total possible - basically how close is the observed to all potential outcomes)
def linguistic_complexity(df_output):
    ''' 
    This calculates the linguistic complexity (total obs/ total poss)
    ''' 
    ling_complex = df_output.loc['Total', 'Observed kmers'] / df_output.loc['Total', 'Possible kmers']
    return(ling_complex)



# function to output file
def main(args):
    '''
    This takes a file (.csv) of strings and outputs
    a new file with the table of k, possible, observed and linguistic complexity

    '''
# Establish errors
    assert args.k > 0
    if (args.k > 0): # making sure that k values have to all be greater than zero for functions to run/pass test
        print(args.k)
    else: print("NA")
    
    assert args.k <= args.string_l
    if (args.k <= args.string_l): #making sure that k values that exceed the length of the string do not keep creating outputs since it is not possible
        print(args.k)
    else: print("NA")
    
    assert string == char_list["A", "C", "T", "G"]
    assert matched_list = [characters in char_list for characters in string])
    if (string_contains_chars = all(matched_list)): #making sure that only characters A, C, T, and G are recognized as valid string characters
        print(string)
    else: print("NA")
    
#test that we can read in file

#this is where functions will go 
    seq_test = open("seq_test.txt") # read in sequence example text file
    print(seq_test.read()) #output at command line to see that it is working
    data = seq_test #defining new data frame with sequence data that is provided
    m_df = make_df(data) # generate data.frame with k, obs_kmer, and poss_kmer values (df_output)
    ling = linguistic_complexity(data) # calculate ling complexity of each string in sequence file
    m_df.to_csv('output') #write output to csv


# this is for test script (this reference main function)
if __name__ == '__main__':    #for all function called main do the following
   parser = argparse.ArgumentParser() #use the argparse function to separate out strings
   parser.add_argument(seq_test, type=argparse.FileType('r')) #specifying what files to parse into separate strings
   args = parser.parse_args() #defining args as separated string file
   main(args) #running args through the main function



    '''
    full_list = [] # create empty data frame with duplicates
    unique_list = [] # create empty data frame for unique combinations
    count = 0 # create empty counter 
    string_l = len(string) # calculate length of the string as done above 
    for i in range(1,string_l+1): # indexing with i across all kmer values
        single_k = string[(i-1):(i-1+k)] # select k value [1:length(string)] 
        if len(single_k) == k: # only include kmers of the length we're looking at 
            full_list.append(single_k) # add all kmers to a df 
    for item in full_list:
        if item not in unique_list: # select unique combinations
            count += 1 # add 1 to running count every time there is a new combination
            unique_list.append(item)
    return(count) # this is the total number of unquie combinations of k (1:9) letters

# function to create table of k, possible, and observed kmers given a string of characters [ATCG]        
def make_df(string): 
    ''' 
    This is a function to create table of possible, and observed kmers given a string of characters
    for exmaple: ATTGGCATT
    
    string: string of characters 
    
    return: table with totals that equal linguistic complexity 
     
    '''
    df_empty = [] # create empty data frame
    string_l = len(string)
    for k in range(1,string_l+1):
        df_output.append([obs_kmer(k, string), poss_kmer(k, string)])
    df_output = pd.DataFrame(df_output, index = range(1, string_l+1), columns =  ["observed kmers", "possible kmers"])
    df_output.loc['Total'] = df_output.sum()
    return(df_output)

# function to caluclate linguistic complexity
def linguistic_complexity(df_output):
    ''' 
    This calculates the linguistic complexity (total obs/ total poss)
    ''' 
    ling_complex = df_output.loc['Total', 'Observed kmers'] / df_output.loc['Total', 'Possible kmers']
    return(ling_complex)

# function to output file 
def main(args): 
    ''' 
    This takes a file (.csv) of strings and outputs
    a new file with the table of k, possible, observed and linguistic complexity
    
    ''' 
    complx = [] #create empty df 
    #also defining limitations here (min/max k, letters, etc)
    
#this is where functions will go 
    seq_test = open("seq_test.txt", "r") # read in text file
    #print(seq_test.read())
    m_df = make_df(seq_test) # generate data.frame (df_output)
    complx = linguistic_complexity(seq_test) # calculate ling complx - use function
    # df = pd.DataFrame.to_csv("C:/Users/Kim Rivera/Documents/Spring 2021/BIO539")
    # df.to_csv(index=False)
    # print("Linguistic Complexity", test)
    # 
    # df = pd.DataFrame({})
    # df.to_csv(index = False)


# output to .csv (data frame & complex)


#be careful with tabs (throughout)



# this is for test script (this reference main function)
if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('seq_test.txt', type=argparse.FileType('r'))
    args = parser.parse_args()
    main(args)

#make .txt
