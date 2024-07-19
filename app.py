import streamlit as st
import requests

st.set_page_config(
    page_title="Word Wise",
    page_icon="icon.png",
    menu_items={
        "About":"Unlock the power of words with Word Wise! Whether you're crafting the perfect sentence or exploring new vocabulary, our tool helps you find the perfect synonyms and antonyms for any word. Enhance your writing and expand your lexicon effortlessly. Try it now and see words in a whole new light!"
    }   
)

st.write("<h2 style='color:#FF6F61;'>Master Synonyms & Antonyms Effortlessly!</h2>",unsafe_allow_html=True)

word=st.text_input("Enter your word")
btn=st.button("Find")

if btn:
    word = f"{word}"
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
    if response.status_code == requests.codes.ok:
        data=response.json()
        st.write(f"<h3 style='color:#FFD700;'>Synonyms of {word}:</h3>",unsafe_allow_html=True)
        synonyms=[]
        antonyms=[]
        # API Fetching
        def Fetch_Data():
            global synonyms,antonyms
            for i in data["synonyms"]:
                if i not in synonyms:
                    synonyms.append(i)
            for j in data["antonyms"]:
                if j not in antonyms:
                    antonyms.append(j)
        Fetch_Data()

        # Synonyms
        syn=""
        for synonym in synonyms:
            if(synonyms[-1]==synonym):
                syn=syn+synonym+"."
            else:
                syn=syn+synonym+", "
        st.write(f"<li style=font-size:22px>{syn}</li>",unsafe_allow_html=True)

        # Antonyms
        ant=""
        for antonym in antonyms:
            if(antonym==''):
                pass
            elif(antonyms[-1]==antonym):
                ant=ant+antonym+"."
            else:
                ant=ant+antonym+", "
        # If antonyms has data then show this
        if(len(ant)>=1):
            st.write(f"<h3 style='color:#FFD700;'>Antonyms of {word}:</h3>",unsafe_allow_html=True)
            st.write(f"<li style=font-size:22px>{ant}</li>",unsafe_allow_html=True)