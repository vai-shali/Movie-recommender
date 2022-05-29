import pandas as pd
from difflib import SequenceMatcher

df=pd.read_csv("trialdb.csv")
features=['keywords','cast','genres','director']    #field used for calculating similarity
for feature in features:
    df[feature]=df[feature].fillna('')              #assining empty string to null values

def get_title_from_index(index):
    return df[df.index==index]["title"].values[0]   #function to obtain movie title name using the index

def combine_features(row):                          #function to combine the necessary features into 1 files
	try:
		return row['keywords'] +"_"+row['cast']+"_"+row["genres"]+"_"+row["director"]
	except:
		print("Error:", row)

df['combined_features']=df.apply(combine_features,axis=1)

rows,cols=(21,21)
count_matrix=[[0.0]*cols]*rows      #creating count matrix to store the similarity index values 

#knn algorithm
def euclidean_dist(m1,m2):      #algorithm to find similarity value between 2 movies/movie titles
    distance=0.0
    m1=m1.lower()
    m2=m2.lower()
    if '_' in m1:               #Similarity calculated from cast,genre,director and keyword fields
        m1=m1.split('_')
        m2=m2.split('_')
        l=min(len(m1),len(m2))
        for i in range(l):
            distance+=SequenceMatcher(a=m1[i],b=m2[i]).ratio()
    else:                       #used for finding the searched movie title from the database of movies
        if m1 in m2:
            distance=1.0
        else:
            distance=SequenceMatcher(a=m1,b=m2).ratio()
    return round(distance,4)


#sorting algorithm
def partition(l, r, nums):      #used With quicksort() function, helper function for sorting
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] >= pivot:
            # Swapping values larger than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swappping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
def quicksort(l, r, nums):          #sorting algorithm used to sort the similarity values in descending order
    if len(nums) == 1:              # Terminating Condition for recursion
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)   # Recursively sorting the left values
        quicksort(pi+1, r, nums)   # Recursively sorting the right values
    return nums

#search algorithm
def search_movie(movie):           #searching algorithm to find the movie from the database
    search_list=[]
    movies_index={}
    for i in range(21):
        dist=euclidean_dist(movie,get_title_from_index(i))
        search_list.append(dist)
        movies_index[dist]=i
    quicksort(0,20,search_list)
    return movies_index[search_list[0]]

#creating the matrix
def recommend(chosen):
    for j in range(21):    #creating the count matrix that contains similarity between chosen movie and all other movies in the dataset
        count_matrix[chosen][j]=euclidean_dist(df.loc[chosen].at['combined_features'],df.loc[j].at['combined_features'])

    recs={}
    for i in range(21):     #creating a dictionary that maps index to movie names
        recs[count_matrix[chosen][i]]=get_title_from_index(i)

    quicksort(0,20,count_matrix[chosen])    #sorting the count matrix in descending order to find out most similar movies(first few movies)
    count=0
    result=[]
    for i in count_matrix[chosen]:      #making a list of top matched movies & returning it to app.py
        result.append(recs[i])
        count+=1
        if count==9:
            break
    return result
