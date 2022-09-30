# movie-recommender
This project demonstrates the use of basic algorithms in movie recommendation systems.

## Requirements
Python 3.9.13

### Steps to execute:
Run the following commands on command prompt terminal<br>
(after python is installed)<br>
Make sure to enter into the movie-recommender-master directory on command prompt(using cd) for the following steps
- **Creating and entering into virtual environment**
    - ```pip install virtualenv```
    - ```python -m virtualenv myvenv```
    - ```myvenv\Scripts\activate.bat```<br>
- **Installing streamlit**
    - ```pip install streamlit```<br>
    **IMP: close the text editor and open it again (for streamlit installation to be effective)**
- **Execution**<br>
    On a new cmd terminal run
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


