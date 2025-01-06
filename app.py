import streamlit as st
import pickle

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Email/SMS Spam Classifier')

# title = st.text_input("Movie title", "Life of Brian")
# st.write("The current movie title is", title)