import pandas as pd
import streamlit as st
import mainfile

df=pd.read_csv("trialdb.csv")       #movie dataset(containing all details of movies)
poster=pd.read_csv("posterdb.csv")  #posters dataset(containing movie name,poster image urls)
posterdict={}
for i in range(21):     #creating a dictionary, mapping movie names to their poster image urls
    posterdict[poster.loc[i].at['name']]=poster.loc[i].at['link']

#setting background image
page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://d35hnlqsfbl0b5.cloudfront.net/j-media/751f57d37560524e6c31013.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

titletxt= '<p style="font-family:Aleo; color:White; font-size: 42px;">Movie Recommendation System</p>'
st.markdown(titletxt,unsafe_allow_html=True)

movie_list = df['title'].values
prev_search=[" ",]
input_txt='<p style="font-family:Aleo; color:White; font-size: 22px;">Type a movie</p>'
selected_movie = st.text_input(
    "Type a movie"
)
prev_search.append(selected_movie)

#condition when button to show recommendations is clicked
if st.button('Show Recommendation'):

    new_page_bg_img = '''
    <style>
      .stApp {
    background-image: url("https://cdn.wallpaperdirect.com/asset/img/product/136996/tiled/sketchtwenty-3-melton-silk-beige-wallpaper-tiled-136996.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(new_page_bg_img, unsafe_allow_html=True)
    chosen_index=mainfile.search_movie(selected_movie)      #using the backend search algorithm(from mainfile.py) to find the movie in the dataset
    chosen_movie=mainfile.get_title_from_index(chosen_index)
    str="showing results for: "+chosen_movie
    st.markdown(str,unsafe_allow_html=False)
    recommended_movie_names = mainfile.recommend(chosen_index)  #calling the recommend function from backend to suggest
    
    col1, col2, col3 = st.columns(3)
    i=0
    count=0
    #printing the movie recommendations with their posters
    while(count<3):
        with col1:
            st.image(posterdict[recommended_movie_names[i]])
            st.text(recommended_movie_names[i])
            st.header(" ")
        i+=1
        with col2:
            st.image(posterdict[recommended_movie_names[i]])
            st.text(recommended_movie_names[i])
            st.header(" ")
        i+=1
        with col3:
            st.image(posterdict[recommended_movie_names[i]])
            st.text(recommended_movie_names[i])
            st.header(" ")
        i+=1
        count+=1