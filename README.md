# movie-recommender
This project demonstrates the use of basic algorithms in movie recommendation systems.

## Requirements
Python 3.9.13

### Steps to execute:
Run the following commands on command prompt terminal<br>
(after python is installed)
- **Creating and entering into virtual environment**
    - ```pip install virtualenv```
    - ```python -m virtualenv myvenv```
    - ```myvenv\Scripts\activate.bat```<br>
- **Installing streamlit**
    - ```pip install streamlit```<br>
- **Execution**
    - ```streamlit run app.py```

## How it works
- A movie is typed into the input box as shown in the output screenshot.
- On clicking Show Recommendation button, the selected movie and other suggested movies are displayed.
- Even if the typed movie does not exist/not in database, top matched movies are displayed
- Similarity index between movies is calculated (using KNN algorithm) based on cast, genre, director and keyword fields from the dataset


### Algorithms used:
1. KNN algorithm
2. Quick sort algorithm
3. Search algorithm

### Tech stack: 
1. Python 3 for algorithms backend
2. Streamlit for frontend

### Datasets:
1. trialdb- movie dataset containing various fields such as Title, genre, cast, release date etc.
2. posterdb- dataset containing movies titles and their poster image urls


## Output

### Starting window(before input)

![MSimg1](https://user-images.githubusercontent.com/79700331/170872022-498e7ee5-a472-4658-83ef-ee23b24b5270.jpg)

### After show recommendations button clicked

![MSimg2](https://user-images.githubusercontent.com/79700331/170872159-b58bbfd3-44d2-4ff2-99dd-43626a9f35c5.jpg)

![MSimg3](https://user-images.githubusercontent.com/79700331/170872177-103618c5-dadd-4d79-8790-d48dacbb51c1.jpg)


