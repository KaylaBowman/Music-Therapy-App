import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.figure_factory as ff

#dropdown menu
categories = ["Data Overview", "Investigate The Data", "Clean The Data", "Explore The Data", "Get Recommendations"]
selected_category = st.selectbox("Choose a section of this project to explore:", categories)

#title of the app
st.title("Welcome To My Music Therapy App")
st.markdown("Please be advised that all recommendations are based on self-reported mental health scores of listeners. Since these recommendations are based on the correlations between listening preferences and mental health, they are not proven to *cause* changes in mood, but rather are *associated* with changes in mood.")

if selected_category == "Data Overview":
    
    #display the selected category
    st.write(f"You selected: {selected_category}")
    
    #markdown section
    st.subheader("What does the first [dataset](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results) look like?")
    st.markdown("* Purpose: this dataset will build our recommendation system by providing info on the relationships between listening habits and mental health")
    st.markdown("* Mixture of data types (ex: Primary streaming service: Nominal, Hours per day: Ratio, Anxiety: Ordinal, Composer: Binary")
    st.markdown("Feature description:")
    st.write("* All observations are self-reported")
    st.write("* 16 unique genres are considered")
    st.write("* BMP = Beats per minute of favorite genre")
    st.write("* All feature descriptions are on the link above")
    
    #load the Data
    mxmh_survey_results = pd.read_csv("mxmh_survey_results.csv")
        
    #display the data
    st.write(mxmh_survey_results.head())  

    #markdown section
    st.subheader("What does the second [dataset](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019) look like?")
    st.markdown("* Purpose: this dataset will provide a libary to pull songs from based on user input")
    st.markdown("* Mixture of data types (ex: Artist: Nominal, Duration_ms: Ratio, Popularity: Ordinal, Explicit: Binary")
    st.markdown("Feature description:")
    st.write("* Valence: positivity of the track, 0 to 1")
    st.write("* Danceability: considers tempo, beat strength, and rhythm stability")
    st.write("* Energy: intensity of song, 0 to 1")
    st.write("* All feature descriptions are on the link above")

    
    #load the Data
    songs = pd.read_csv("songs_normalize.csv")
        
    #display the data
    st.write(songs.head())  

if selected_category == "Investigate The Data":

    #load the Data
    mxmh_survey_results = pd.read_csv("mxmh_survey_results.csv")
    
    #missing vals
    st.subheader("Any missing vals?")
    #make a heatmap of the missing data
    nan_mask = mxmh_survey_results.isna()
    nan_array = nan_mask.astype(int).to_numpy()
    
    plt.figure(figsize=(12, 6))
    plt.imshow(nan_array.T, interpolation='nearest', aspect='auto', cmap='viridis')
    plt.xlabel('mxmh_survey_results Index')
    plt.ylabel('Features')
    plt.title('Visualizing Missing Values in mxmh_survey_results Dataset')
    plt.yticks(range(len(mxmh_survey_results.columns)), mxmh_survey_results.columns)
    num_participants = nan_array.shape[0]
    plt.xticks(np.linspace(0, num_participants-1, min(10, num_participants)).astype(int))
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)
    
    #distribution 
    st.header("Distribution of Features")
    
    st.subheader("Age")
    #age 
    fig = px.histogram(mxmh_survey_results, x="Age", title="Age Distribution")
    st.plotly_chart(fig)
    
    st.subheader("Streaming Service")
    #streaming service
    platforms = ['Spotify', 'Pandora', 'YouTube Music', 
                 'I do not use a streaming service.', 
                 'Apple Music', 'Other streaming service']
    popularity = [458, 11, 94, 71, 51, 0]
    
    #create a horizontal bar plot
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.barh(platforms, popularity, color='skyblue')
    plt.title('Distribution of Primary Streaming Service')
    plt.xlabel('Popularity')
    plt.ylabel('Streaming Service')
    
    st.pyplot(plt)
    
    st.subheader("Favorite Genre")
    #fav genre
    plt.figure(figsize=(10, 6))  
    plt.hist(mxmh_survey_results["Fav genre"], bins=16, edgecolor='black')
    
    #set the title of the plot
    plt.title('Distribution of Fav Genre', fontsize=16)
    
    #set the x-axis title
    plt.xlabel('Fav Genre', fontsize=12)
    plt.xticks(rotation=45) 
    
    st.pyplot(plt)
    
    st.subheader("Mental Health Stats")
    #anxiety 
    fig = px.histogram(mxmh_survey_results, x="Anxiety", title="Anxiety Distribution")
    st.plotly_chart(fig)
    
    #depression
    fig = px.histogram(mxmh_survey_results, x="Depression", title="Depression Distribution")
    st.plotly_chart(fig)
    
    #insomnia
    fig = px.histogram(mxmh_survey_results, x="Insomnia", title="Insomnia Distribution")
    st.plotly_chart(fig)
    
    #OCD
    fig = px.histogram(mxmh_survey_results, x="OCD", title="OCD Distribution")
    st.plotly_chart(fig)
    
    
    #frequency
    st.markdown("Genre Frequency")
    
    fig = px.histogram(mxmh_survey_results, x=('Frequency [Latin]'), title="Frequency of Latin Listeners")
    st.plotly_chart(fig)
    
    fig = px.histogram(mxmh_survey_results, x=('Frequency [Rock]'), title="Frequency of Rock Listeners")
    st.plotly_chart(fig)
    
    fig = px.histogram(mxmh_survey_results, x=('Frequency [Classical]'), title="Frequency of Latin Listeners")
    st.plotly_chart(fig)
    
    fig = px.histogram(mxmh_survey_results, x=('Frequency [Latin]'), title="Frequency of Pop Listeners")
    st.plotly_chart(fig)
    
    #Experts
    st.subheader("Experts")
    
    fig, ax = plt.subplots()
    sns.histplot(data=mxmh_survey_results, x="Composer", bins=2, label="Composers", multiple="stack", ax=ax)
    sns.histplot(data=mxmh_survey_results, x="Instrumentalist", bins=2, label="Instrumentalists", ax=ax)
    
    ax.legend()
    
    ax.set_title("Distribution of Composers and Instrumentalists")
    
    st.pyplot(fig)
    
    #Music Effects
    st.subheader("Music Effects")
    fig, ax = plt.subplots()
    sns.histplot(data=mxmh_survey_results, x='Music effects', hue='Music effects', palette=['red', 'blue', 'green'])
    ax.legend()
    ax.set_title("Distribution of Perceived Music Effects")
    st.pyplot(fig)
    
    #look at outliers
    st.subheader("Any Outliers?")
    
    fig, ax = plt.subplots()
    sns.histplot(data=mxmh_survey_results, x='Hours per day')
    ax.legend()
    ax.set_title("Hours Per Day")
    st.pyplot(fig)
    
    #hour outliers
    num_24_hours = sum(mxmh_survey_results['Hours per day'] == 24)
    st.write(f"Number of participants reporting 24 hours per day: {num_24_hours}")
    
    #age outliers:
    age_outliers = sum((mxmh_survey_results['Age'] > 70) | (mxmh_survey_results['Age'] < 18))
    st.write(f"Number of participants younger than 18 or older than 70: {age_outliers}")

if selected_category == "Clean The Data":

    #load the Data
    mxmh_survey_results = pd.read_csv("mxmh_survey_results.csv")
    
    #handle missing vals 
    st.subheader("Handle BPM Missing Values")
    st.markdown("Group by genre, then replace with median of genre")

    #get pop median so we can test our replacement worked
    pop_median = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Pop"]["BPM"].median()
    st.write(f"The median BPM of Pop: {pop_median}")

    #group and replace
    for i, val in enumerate(mxmh_survey_results["BPM"].isna()):
        genre = mxmh_survey_results.loc[i, "Fav genre"]  # Get the genre for the current row
        if genre == "Latin":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Latin"]["BPM"].median()
        if genre == "Rock":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Rock"]["BPM"].median()
        if genre == "Video game music":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Video game music"]["BPM"].median()
        if genre == "Jazz":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Jazz"]["BPM"].median()
        if genre == "R&B":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "R&B"]["BPM"].median()
        if genre == "K pop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "K pop"]["BPM"].median()
        if genre == "Country":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Country"]["BPM"].median()
        if genre == "EDM":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "EDM"]["BPM"].median()
        if genre == "Hip hop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Hip hop"]["BPM"].median()
        if genre == "Pop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Pop"]["BPM"].median()
        if genre == "Rap":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Rap"]["BPM"].median()
        if genre == "Classical":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Classical"]["BPM"].median()
        if genre == "Metal":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Metal"]["BPM"].median()
        if genre == "Folk":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Folk"]["BPM"].median()
        if genre == "Lofi":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Lofi"]["BPM"].median()
        if genre == "Gospel":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Gospel"]["BPM"].median()

    #see that the values were replaced
    filtered_data = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Pop"]
    st.write(filtered_data.head())  

    #see that BPM has no missing values
    #missing vals
    st.subheader("No More Missing BPM Vals")
    #make a heatmap of the missing data
    nan_mask = mxmh_survey_results.isna()
    nan_array = nan_mask.astype(int).to_numpy()
    
    plt.figure(figsize=(12, 6))
    plt.imshow(nan_array.T, interpolation='nearest', aspect='auto', cmap='viridis')
    plt.xlabel('mxmh_survey_results Index')
    plt.ylabel('Features')
    plt.title('Visualizing Missing Values in mxmh_survey_results Dataset')
    plt.yticks(range(len(mxmh_survey_results.columns)), mxmh_survey_results.columns)
    num_participants = nan_array.shape[0]
    plt.xticks(np.linspace(0, num_participants-1, min(10, num_participants)).astype(int))
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

    st.subheader("Handle Outliers")
    #I don't trust the participants who say they listen to music 24hrs/day
    cleaned_data = mxmh_survey_results.copy()
    #I will say the max they could realistically listen to is 16 hrs
    cleaned_data = cleaned_data[(cleaned_data["Hours per day"] < 16)]
    #deleted 6 rows
    st.markdown("Deleted all instances of Hours Per Day above 16")
    cleaned_data.shape

    #take away age outliers 
    cleaned_data = cleaned_data[(cleaned_data["Age"] > 18) & (cleaned_data["Age"] < 64)]
    st.markdown("Deleted all instances of Age < 18 and Age > 64 (3 SDs from the 75% percentile)")
    cleaned_data.shape
    
    #recode frequency genre
    st.subheader("Recode Categorical Data")
    st.markdown("Genre Frequencies")

    frequency_mapping = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Very frequently": 4 }

    # Replace the values in the "Frequency [Country]" column
    cleaned_data["Frequency [Latin]"] = cleaned_data["Frequency [Latin]"].replace(frequency_mapping)
    cleaned_data["Frequency [Rock]"] = cleaned_data["Frequency [Rock]"].replace(frequency_mapping)
    cleaned_data["Frequency [Video game music]"] = cleaned_data["Frequency [Video game music]"].replace(frequency_mapping)
    cleaned_data["Frequency [Jazz]"] = cleaned_data["Frequency [Jazz]"].replace(frequency_mapping)
    cleaned_data["Frequency [R&B]"] = cleaned_data["Frequency [R&B]"].replace(frequency_mapping)
    cleaned_data["Frequency [K pop]"] = cleaned_data["Frequency [K pop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Country]"] = cleaned_data["Frequency [Country]"].replace(frequency_mapping)
    cleaned_data["Frequency [EDM]"] = cleaned_data["Frequency [EDM]"].replace(frequency_mapping)
    cleaned_data["Frequency [Hip hop]"] = cleaned_data["Frequency [Hip hop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Pop]"] = cleaned_data["Frequency [Pop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Rap]"] = cleaned_data["Frequency [Rap]"].replace(frequency_mapping)
    cleaned_data["Frequency [Classical]"] = cleaned_data["Frequency [Classical]"].replace(frequency_mapping)
    cleaned_data["Frequency [Metal]"] = cleaned_data["Frequency [Metal]"].replace(frequency_mapping)
    cleaned_data["Frequency [Folk]"] = cleaned_data["Frequency [Folk]"].replace(frequency_mapping)
    cleaned_data["Frequency [Lofi]"] = cleaned_data["Frequency [Lofi]"].replace(frequency_mapping)
    cleaned_data["Frequency [Gospel]"] = cleaned_data["Frequency [Gospel]"].replace(frequency_mapping)

    #see the changes
    st.write(cleaned_data.head())  

if selected_category == "Explore The Data":

    ##########repeating the filtering so I can use the filtered_dataset here
    
    #load the Data
    mxmh_survey_results = pd.read_csv("mxmh_survey_results.csv")

    #group and replace
    for i, val in enumerate(mxmh_survey_results["BPM"].isna()):
        genre = mxmh_survey_results.loc[i, "Fav genre"]  # Get the genre for the current row
        if genre == "Latin":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Latin"]["BPM"].median()
        if genre == "Rock":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Rock"]["BPM"].median()
        if genre == "Video game music":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Video game music"]["BPM"].median()
        if genre == "Jazz":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Jazz"]["BPM"].median()
        if genre == "R&B":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "R&B"]["BPM"].median()
        if genre == "K pop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "K pop"]["BPM"].median()
        if genre == "Country":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Country"]["BPM"].median()
        if genre == "EDM":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "EDM"]["BPM"].median()
        if genre == "Hip hop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Hip hop"]["BPM"].median()
        if genre == "Pop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Pop"]["BPM"].median()
        if genre == "Rap":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Rap"]["BPM"].median()
        if genre == "Classical":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Classical"]["BPM"].median()
        if genre == "Metal":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Metal"]["BPM"].median()
        if genre == "Folk":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Folk"]["BPM"].median()
        if genre == "Lofi":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Lofi"]["BPM"].median()
        if genre == "Gospel":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Gospel"]["BPM"].median()

  
    cleaned_data = mxmh_survey_results.copy()
    #I will say the max they could realistically listen to is 16 hrs
    cleaned_data = cleaned_data[(cleaned_data["Hours per day"] < 16)]
    #deleted 6 rows

    #take away age outliers 
    cleaned_data = cleaned_data[(cleaned_data["Age"] > 18) & (cleaned_data["Age"] < 64)]
    
    #recode frequency genre

    frequency_mapping = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Very frequently": 4 }

    # Replace the values in the "Frequency [Country]" column
    cleaned_data["Frequency [Latin]"] = cleaned_data["Frequency [Latin]"].replace(frequency_mapping)
    cleaned_data["Frequency [Rock]"] = cleaned_data["Frequency [Rock]"].replace(frequency_mapping)
    cleaned_data["Frequency [Video game music]"] = cleaned_data["Frequency [Video game music]"].replace(frequency_mapping)
    cleaned_data["Frequency [Jazz]"] = cleaned_data["Frequency [Jazz]"].replace(frequency_mapping)
    cleaned_data["Frequency [R&B]"] = cleaned_data["Frequency [R&B]"].replace(frequency_mapping)
    cleaned_data["Frequency [K pop]"] = cleaned_data["Frequency [K pop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Country]"] = cleaned_data["Frequency [Country]"].replace(frequency_mapping)
    cleaned_data["Frequency [EDM]"] = cleaned_data["Frequency [EDM]"].replace(frequency_mapping)
    cleaned_data["Frequency [Hip hop]"] = cleaned_data["Frequency [Hip hop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Pop]"] = cleaned_data["Frequency [Pop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Rap]"] = cleaned_data["Frequency [Rap]"].replace(frequency_mapping)
    cleaned_data["Frequency [Classical]"] = cleaned_data["Frequency [Classical]"].replace(frequency_mapping)
    cleaned_data["Frequency [Metal]"] = cleaned_data["Frequency [Metal]"].replace(frequency_mapping)
    cleaned_data["Frequency [Folk]"] = cleaned_data["Frequency [Folk]"].replace(frequency_mapping)
    cleaned_data["Frequency [Lofi]"] = cleaned_data["Frequency [Lofi]"].replace(frequency_mapping)
    cleaned_data["Frequency [Gospel]"] = cleaned_data["Frequency [Gospel]"].replace(frequency_mapping)

    ############ done repeating the filtering
    
    st.subheader("Any correlations between frequency and mental health?")

    selected_features = ['Frequency [Classical]', "Frequency [Country]", "Frequency [EDM]", "Frequency [Folk]", 
                     "Frequency [Gospel]", "Frequency [Hip hop]", "Frequency [Jazz]", "Frequency [K pop]", "Frequency [Latin]", "Frequency [Lofi]",
                     "Frequency [Metal]", "Frequency [Pop]", "Frequency [R&B]", "Frequency [Rap]", "Frequency [Rock]",  "Anxiety", "Depression", "Insomnia", "OCD"] # Focus on these variables

    # Correlation Heatmap (Interactive)
    correlation_matrix = cleaned_data[selected_features].corr().values
    fig_heatmap = ff.create_annotated_heatmap(
         z=correlation_matrix,
         x=selected_features,
         y=selected_features,
         colorscale='Viridis'
     )
    fig_heatmap.update_layout(
        title="Correlation Heatmap (Interactive)",
        xaxis_title="Features",
        yaxis_title="Features"
    )
    st.plotly_chart(fig_heatmap)
    

    #hours and mh
    st.subheader("Is hours spent listening per day correlated with reported MH scores? Not strongly.")
    selected_features = ['Hours per day', "Anxiety", "Depression", "Insomnia", "OCD"] # Focus on these variables

    # Correlation Heatmap (Interactive)
    correlation_matrix = cleaned_data[selected_features].corr().values
    fig_heatmap = ff.create_annotated_heatmap(
         z=correlation_matrix,
         x=selected_features,
         y=selected_features,
         colorscale='Viridis'
     )
    fig_heatmap.update_layout(
        title="Correlation Heatmap (Interactive)",
        xaxis_title="Features",
        yaxis_title="Features"
    )
    st.plotly_chart(fig_heatmap)
    

    st.subheader("How does mental health vary across age?")

    bins = [18, 25, 31, 36, 41, 46, 51, 58, 64]  
    labels = ['18-24', '25-30', '31-35', '36-40', '41-45', '46-50', '51-57', '58-64']  # Labels for the bins

    # Create the binned column
    cleaned_data['age_binned'] = pd.cut(cleaned_data['Age'], bins=bins, labels=labels, right=False)


    #now plot it 
    fig_violin = px.violin(cleaned_data, x='age_binned', y='Anxiety', box=True, points='all',
                           labels={'Age':'Age', 'Anxiety':'Anxiety'},
                           title="Interactive Violin Plot of Age vs Anxiety")

    st.plotly_chart(fig_violin)

    #fav genre and MH
    st.subheader("Is fav genre associated with MH scores?")
    fig_violin = px.violin(cleaned_data, x='Fav genre', y='Anxiety', box=True, points='all',
                           labels={'Fav genre':'Favorite Genre', 'Anxiety':'Anxiety'},
                           title="Interactive Violin Plot of Fav Genre vs Anxiety")
    
    st.plotly_chart(fig_violin)

    fig_violin = px.violin(cleaned_data, x='Fav genre', y='Depression', box=True, points='all',
                           labels={'Fav genre':'Favorite Genre', 'Depression':'Depression'},
                           title="Interactive Violin Plot of Fav Genre vs Depression ")

    st.plotly_chart(fig_violin)

    fig_violin = px.violin(cleaned_data, x='Fav genre', y='OCD', box=True, points='all',
                           labels={'Fav genre':'Favorite Genre', 'OCD':'OCD'},
                           title="Interactive Violin Plot of Fav Genre vs OCD")
    st.plotly_chart(fig_violin)

    fig_violin = px.violin(cleaned_data, x='Fav genre', y='Insomnia', box=True, points='all',
                           labels={'Fav genre':'Favorite Genre', 'Insomnia':'Insomnia'},
                           title="Interactive Violin Plot of Fav Genre vs Insomnia")
    st.plotly_chart(fig_violin)

    
    #look at mental health stat by genre
    st.subheader("Anxiety Score by Genre")
    #sns.boxplot(data=cleaned_data, x="Frequency [Latin]", y = "Anxiety")
    #plt.title('Anxiety Scores of Latin Listeners')

    #function to create and display a box plot for a specific genre
    def plot_boxplot(genre, score):
        plt.figure(figsize=(10, 6))  
        sns.boxplot(data=cleaned_data, x=genre, y=score)
        #make it so user can choose MH stat and genre
        plt.title(f'{score} Scores of {genre} Listeners')
        plt.xlabel(genre)  
        plt.ylabel(score)  
        st.pyplot(plt)  
        plt.clf()  


    #dropdown menu for selecting a mental health score
    score_options = ["Anxiety", "Depression"]
    selected_score = st.selectbox("Choose a mental health category to consider:", score_options)
    
    #dropdown menu for selecting a genre
    genre_options = ["Frequency [Latin]", "Frequency [Rock]", "Frequency [Classical]", 
                     "Frequency [Pop]", "Frequency [Jazz]", "Frequency [Hip-Hop]", 
                     "Frequency [Electronic]", "Frequency [Reggae]", 
                     "Frequency [Country]", "Frequency [R&B]", 
                     "Frequency [Indie]", "Frequency [Folk]", 
                     "Frequency [Punk]", "Frequency [Blues]", 
                     "Frequency [Metal]", "Frequency [Soul]"]
    
    selected_genre = st.selectbox("Choose a genre to consider:", genre_options)
    

    #call the plot function with the selected genre and score
    plot_boxplot(selected_genre, selected_score)

    #feature engineering
    st.subheader("Feature Engineering:")
    st.markdown("Create a dataset with final mental health scores based on frequency of genre consumption")

    #group average MH scores by highest frequency genre
    st.markdown("Group average MH scores by all Very Frequent genre responses")

    #making latin subsets based on frequency
    cleaned_data_latin1 = cleaned_data[cleaned_data["Frequency [Latin]"] == 1]
    cleaned_data_latin2 = cleaned_data[cleaned_data["Frequency [Latin]"] == 2]
    cleaned_data_latin3 = cleaned_data[cleaned_data["Frequency [Latin]"] == 3]
    cleaned_data_latin4 = cleaned_data[cleaned_data["Frequency [Latin]"] == 4]
    
    
    #now get the average MH scores for each frequency
    ave_anxiety_latin1 = cleaned_data_latin1["Anxiety"].mean()
    ave_dep_latin1 = cleaned_data_latin1["Depression"].mean()
    ave_insom_latin1 = cleaned_data_latin1["Insomnia"].mean()
    ave_ocd_latin1 = cleaned_data_latin1["OCD"].mean()
    
    ave_anxiety_latin2 = cleaned_data_latin2["Anxiety"].mean()
    ave_dep_latin2 = cleaned_data_latin2["Depression"].mean()
    ave_insom_latin2 = cleaned_data_latin2["Insomnia"].mean()
    ave_ocd_latin2 = cleaned_data_latin2["OCD"].mean()
    
    ave_anxiety_latin3 = cleaned_data_latin3["Anxiety"].mean()
    ave_dep_latin3 = cleaned_data_latin3["Depression"].mean()
    ave_insom_latin3 = cleaned_data_latin3["Insomnia"].mean()
    ave_ocd_latin3 = cleaned_data_latin3["OCD"].mean()
    
    ave_anxiety_latin4 = cleaned_data_latin4["Anxiety"].mean()
    ave_dep_latin4 = cleaned_data_latin4["Depression"].mean()
    ave_insom_latin4 = cleaned_data_latin4["Insomnia"].mean()
    ave_ocd_latin4 = cleaned_data_latin4["OCD"].mean()
    
    
    
    #making rock subsets based on frequency
    cleaned_data_rock1 = cleaned_data[cleaned_data["Frequency [Rock]"] == 1]
    cleaned_data_rock2 = cleaned_data[cleaned_data["Frequency [Rock]"] == 2]
    cleaned_data_rock3 = cleaned_data[cleaned_data["Frequency [Rock]"] == 3]
    cleaned_data_rock4 = cleaned_data[cleaned_data["Frequency [Rock]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_rock1 = cleaned_data_rock1["Anxiety"].mean()
    ave_dep_rock1 = cleaned_data_rock1["Depression"].mean()
    ave_insom_rock1 = cleaned_data_rock1["Insomnia"].mean()
    ave_ocd_rock1 = cleaned_data_rock1["OCD"].mean()
    
    ave_anxiety_rock2 = cleaned_data_rock2["Anxiety"].mean()
    ave_dep_rock2 = cleaned_data_rock2["Depression"].mean()
    ave_insom_rock2 = cleaned_data_rock2["Insomnia"].mean()
    ave_ocd_rock2 = cleaned_data_rock2["OCD"].mean()
    
    ave_anxiety_rock3 = cleaned_data_rock3["Anxiety"].mean()
    ave_dep_rock3 = cleaned_data_rock3["Depression"].mean()
    ave_insom_rock3 = cleaned_data_rock3["Insomnia"].mean()
    ave_ocd_rock3 = cleaned_data_rock3["OCD"].mean()
    
    ave_anxiety_rock4 = cleaned_data_rock4["Anxiety"].mean()
    ave_dep_rock4 = cleaned_data_rock4["Depression"].mean()
    ave_insom_rock4 = cleaned_data_rock4["Insomnia"].mean()
    ave_ocd_rock4 = cleaned_data_rock4["OCD"].mean()
    
    
    
    
    #making Video game music subsets based on frequency
    cleaned_data_vgm1 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 1]
    cleaned_data_vgm2 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 2]
    cleaned_data_vgm3 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 3]
    cleaned_data_vgm4 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_vgm1 = cleaned_data_vgm1["Anxiety"].mean()
    ave_dep_vgm1 = cleaned_data_vgm1["Depression"].mean()
    ave_insom_vgm1 = cleaned_data_vgm1["Insomnia"].mean()
    ave_ocd_vgm1 = cleaned_data_vgm1["OCD"].mean()
    
    ave_anxiety_vgm2 = cleaned_data_vgm2["Anxiety"].mean()
    ave_dep_vgm2 = cleaned_data_vgm2["Depression"].mean()
    ave_insom_vgm2 = cleaned_data_vgm2["Insomnia"].mean()
    ave_ocd_vgm2 = cleaned_data_vgm2["OCD"].mean()
    
    ave_anxiety_vgm3 = cleaned_data_vgm3["Anxiety"].mean()
    ave_dep_vgm3 = cleaned_data_vgm3["Depression"].mean()
    ave_insom_vgm3 = cleaned_data_vgm3["Insomnia"].mean()
    ave_ocd_vgm3 = cleaned_data_vgm3["OCD"].mean()
    
    ave_anxiety_vgm4 = cleaned_data_vgm4["Anxiety"].mean()
    ave_dep_vgm4 = cleaned_data_vgm4["Depression"].mean()
    ave_insom_vgm4 = cleaned_data_vgm4["Insomnia"].mean()
    ave_ocd_vgm4 = cleaned_data_vgm4["OCD"].mean()
    
    
    
    #making Jazz subsets based on frequency
    cleaned_data_jazz1 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 1]
    cleaned_data_jazz2 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 2]
    cleaned_data_jazz3 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 3]
    cleaned_data_jazz4 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_jazz1 = cleaned_data_jazz1["Anxiety"].mean()
    ave_dep_jazz1 = cleaned_data_jazz1["Depression"].mean()
    ave_insom_jazz1 = cleaned_data_jazz1["Insomnia"].mean()
    ave_ocd_jazz1 = cleaned_data_jazz1["OCD"].mean()
    
    ave_anxiety_jazz2 = cleaned_data_jazz2["Anxiety"].mean()
    ave_dep_jazz2 = cleaned_data_jazz2["Depression"].mean()
    ave_insom_jazz2 = cleaned_data_jazz2["Insomnia"].mean()
    ave_ocd_jazz2 = cleaned_data_jazz2["OCD"].mean()
    
    ave_anxiety_jazz3 = cleaned_data_jazz3["Anxiety"].mean()
    ave_dep_jazz3 = cleaned_data_jazz3["Depression"].mean()
    ave_insom_jazz3 = cleaned_data_jazz3["Insomnia"].mean()
    ave_ocd_jazz3 = cleaned_data_jazz3["OCD"].mean()
    
    ave_anxiety_jazz4 = cleaned_data_jazz4["Anxiety"].mean()
    ave_dep_jazz4 = cleaned_data_jazz4["Depression"].mean()
    ave_insom_jazz4 = cleaned_data_jazz4["Insomnia"].mean()
    ave_ocd_jazz4 = cleaned_data_jazz4["OCD"].mean()
    
    
    
    #making R&B subsets based on frequency
    cleaned_data_rnb1 = cleaned_data[cleaned_data["Frequency [R&B]"] == 1]
    cleaned_data_rnb2 = cleaned_data[cleaned_data["Frequency [R&B]"] == 2]
    cleaned_data_rnb3 = cleaned_data[cleaned_data["Frequency [R&B]"] == 3]
    cleaned_data_rnb4 = cleaned_data[cleaned_data["Frequency [R&B]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_rnb1 = cleaned_data_rnb1["Anxiety"].mean()
    ave_dep_rnb1 = cleaned_data_rnb1["Depression"].mean()
    ave_insom_rnb1 = cleaned_data_rnb1["Insomnia"].mean()
    ave_ocd_rnb1 = cleaned_data_rnb1["OCD"].mean()
    
    ave_anxiety_rnb2 = cleaned_data_rnb2["Anxiety"].mean()
    ave_dep_rnb2 = cleaned_data_rnb2["Depression"].mean()
    ave_insom_rnb2 = cleaned_data_rnb2["Insomnia"].mean()
    ave_ocd_rnb2 = cleaned_data_rnb2["OCD"].mean()
    
    ave_anxiety_rnb3 = cleaned_data_rnb3["Anxiety"].mean()
    ave_dep_rnb3 = cleaned_data_rnb3["Depression"].mean()
    ave_insom_rnb3 = cleaned_data_rnb3["Insomnia"].mean()
    ave_ocd_rnb3 = cleaned_data_rnb3["OCD"].mean()
    
    ave_anxiety_rnb4 = cleaned_data_rnb4["Anxiety"].mean()
    ave_dep_rnb4 = cleaned_data_rnb4["Depression"].mean()
    ave_insom_rnb4 = cleaned_data_rnb4["Insomnia"].mean()
    ave_ocd_rnb4 = cleaned_data_rnb4["OCD"].mean()
    
    
    
    #making K pop subsets based on frequency
    cleaned_data_kpop1 = cleaned_data[cleaned_data["Frequency [K pop]"] == 1]
    cleaned_data_kpop2 = cleaned_data[cleaned_data["Frequency [K pop]"] == 2]
    cleaned_data_kpop3 = cleaned_data[cleaned_data["Frequency [K pop]"] == 3]
    cleaned_data_kpop4 = cleaned_data[cleaned_data["Frequency [K pop]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_kpop1 = cleaned_data_kpop1["Anxiety"].mean()
    ave_dep_kpop1 = cleaned_data_kpop1["Depression"].mean()
    ave_insom_kpop1 = cleaned_data_kpop1["Insomnia"].mean()
    ave_ocd_kpop1 = cleaned_data_kpop1["OCD"].mean()
    
    ave_anxiety_kpop2 = cleaned_data_kpop2["Anxiety"].mean()
    ave_dep_kpop2 = cleaned_data_kpop2["Depression"].mean()
    ave_insom_kpop2 = cleaned_data_kpop2["Insomnia"].mean()
    ave_ocd_kpop2 = cleaned_data_kpop2["OCD"].mean()
    
    ave_anxiety_kpop3 = cleaned_data_kpop3["Anxiety"].mean()
    ave_dep_kpop3 = cleaned_data_kpop3["Depression"].mean()
    ave_insom_kpop3 = cleaned_data_kpop3["Insomnia"].mean()
    ave_ocd_kpop3 = cleaned_data_kpop3["OCD"].mean()
    
    ave_anxiety_kpop4 = cleaned_data_kpop4["Anxiety"].mean()
    ave_dep_kpop4 = cleaned_data_kpop4["Depression"].mean()
    ave_insom_kpop4 = cleaned_data_kpop4["Insomnia"].mean()
    ave_ocd_kpop4 = cleaned_data_kpop4["OCD"].mean()
    
    
    
    #making Country subsets based on frequency
    cleaned_data_country1 = cleaned_data[cleaned_data["Frequency [Country]"] == 1]
    cleaned_data_country2 = cleaned_data[cleaned_data["Frequency [Country]"] == 2]
    cleaned_data_country3 = cleaned_data[cleaned_data["Frequency [Country]"] == 3]
    cleaned_data_country4 = cleaned_data[cleaned_data["Frequency [Country]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_country1 = cleaned_data_country1["Anxiety"].mean()
    ave_dep_country1 = cleaned_data_country1["Depression"].mean()
    ave_insom_country1 = cleaned_data_country1["Insomnia"].mean()
    ave_ocd_country1 = cleaned_data_country1["OCD"].mean()
    
    ave_anxiety_country2 = cleaned_data_country2["Anxiety"].mean()
    ave_dep_country2 = cleaned_data_country2["Depression"].mean()
    ave_insom_country2 = cleaned_data_country2["Insomnia"].mean()
    ave_ocd_country2 = cleaned_data_country2["OCD"].mean()
    
    ave_anxiety_country3 = cleaned_data_country3["Anxiety"].mean()
    ave_dep_country3 = cleaned_data_country3["Depression"].mean()
    ave_insom_country3 = cleaned_data_country3["Insomnia"].mean()
    ave_ocd_country3 = cleaned_data_country3["OCD"].mean()
    
    ave_anxiety_country4 = cleaned_data_country4["Anxiety"].mean()
    ave_dep_country4 = cleaned_data_country4["Depression"].mean()
    ave_insom_country4 = cleaned_data_country4["Insomnia"].mean()
    ave_ocd_country4 = cleaned_data_country4["OCD"].mean()
    
    
    
    #making EDM subsets based on frequency
    cleaned_data_edm1 = cleaned_data[cleaned_data["Frequency [EDM]"] == 1]
    cleaned_data_edm2 = cleaned_data[cleaned_data["Frequency [EDM]"] == 2]
    cleaned_data_edm3 = cleaned_data[cleaned_data["Frequency [EDM]"] == 3]
    cleaned_data_edm4 = cleaned_data[cleaned_data["Frequency [EDM]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_edm1 = cleaned_data_edm1["Anxiety"].mean()
    ave_dep_edm1 = cleaned_data_edm1["Depression"].mean()
    ave_insom_edm1 = cleaned_data_edm1["Insomnia"].mean()
    ave_ocd_edm1 = cleaned_data_edm1["OCD"].mean()
    
    ave_anxiety_edm2 = cleaned_data_edm2["Anxiety"].mean()
    ave_dep_edm2 = cleaned_data_edm2["Depression"].mean()
    ave_insom_edm2 = cleaned_data_edm2["Insomnia"].mean()
    ave_ocd_edm2 = cleaned_data_edm2["OCD"].mean()
    
    ave_anxiety_edm3 = cleaned_data_edm3["Anxiety"].mean()
    ave_dep_edm3 = cleaned_data_edm3["Depression"].mean()
    ave_insom_edm3 = cleaned_data_edm3["Insomnia"].mean()
    ave_ocd_edm3 = cleaned_data_edm3["OCD"].mean()
    
    ave_anxiety_edm4 = cleaned_data_edm4["Anxiety"].mean()
    ave_dep_edm4 = cleaned_data_edm4["Depression"].mean()
    ave_insom_edm4 = cleaned_data_edm4["Insomnia"].mean()
    ave_ocd_edm4 = cleaned_data_edm4["OCD"].mean()
    
    
    
    #making Hip hop subsets based on frequency
    cleaned_data_hiphop1 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 1]
    cleaned_data_hiphop2 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 2]
    cleaned_data_hiphop3 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 3]
    cleaned_data_hiphop4 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_hiphop1 = cleaned_data_hiphop1["Anxiety"].mean()
    ave_dep_hiphop1 = cleaned_data_hiphop1["Depression"].mean()
    ave_insom_hiphop1 = cleaned_data_hiphop1["Insomnia"].mean()
    ave_ocd_hiphop1 = cleaned_data_hiphop1["OCD"].mean()
    
    ave_anxiety_hiphop2 = cleaned_data_hiphop2["Anxiety"].mean()
    ave_dep_hiphop2 = cleaned_data_hiphop2["Depression"].mean()
    ave_insom_hiphop2 = cleaned_data_hiphop2["Insomnia"].mean()
    ave_ocd_hiphop2 = cleaned_data_hiphop2["OCD"].mean()
    
    ave_anxiety_hiphop3 = cleaned_data_hiphop3["Anxiety"].mean()
    ave_dep_hiphop3 = cleaned_data_hiphop3["Depression"].mean()
    ave_insom_hiphop3 = cleaned_data_hiphop3["Insomnia"].mean()
    ave_ocd_hiphop3 = cleaned_data_hiphop3["OCD"].mean()
    
    ave_anxiety_hiphop4 = cleaned_data_hiphop4["Anxiety"].mean()
    ave_dep_hiphop4 = cleaned_data_hiphop4["Depression"].mean()
    ave_insom_hiphop4 = cleaned_data_hiphop4["Insomnia"].mean()
    ave_ocd_hiphop4 = cleaned_data_hiphop4["OCD"].mean()
    
    
    
    
    #making Pop subsets based on frequency
    cleaned_data_pop1 = cleaned_data[cleaned_data["Frequency [Pop]"] == 1]
    cleaned_data_pop2 = cleaned_data[cleaned_data["Frequency [Pop]"] == 2]
    cleaned_data_pop3 = cleaned_data[cleaned_data["Frequency [Pop]"] == 3]
    cleaned_data_pop4 = cleaned_data[cleaned_data["Frequency [Pop]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_pop1 = cleaned_data_pop1["Anxiety"].mean()
    ave_dep_pop1 = cleaned_data_pop1["Depression"].mean()
    ave_insom_pop1 = cleaned_data_pop1["Insomnia"].mean()
    ave_ocd_pop1 = cleaned_data_pop1["OCD"].mean()
    
    ave_anxiety_pop2 = cleaned_data_pop2["Anxiety"].mean()
    ave_dep_pop2 = cleaned_data_pop2["Depression"].mean()
    ave_insom_pop2 = cleaned_data_pop2["Insomnia"].mean()
    ave_ocd_pop2 = cleaned_data_pop2["OCD"].mean()
    
    ave_anxiety_pop3 = cleaned_data_pop3["Anxiety"].mean()
    ave_dep_pop3 = cleaned_data_pop3["Depression"].mean()
    ave_insom_pop3 = cleaned_data_pop3["Insomnia"].mean()
    ave_ocd_pop3 = cleaned_data_pop3["OCD"].mean()
    
    ave_anxiety_pop4 = cleaned_data_pop4["Anxiety"].mean()
    ave_dep_pop4 = cleaned_data_pop4["Depression"].mean()
    ave_insom_pop4 = cleaned_data_pop4["Insomnia"].mean()
    ave_ocd_pop4 = cleaned_data_pop4["OCD"].mean()
    
    
    
    
    #making Rap subsets based on frequency
    cleaned_data_rap1 = cleaned_data[cleaned_data["Frequency [Rap]"] == 1]
    cleaned_data_rap2 = cleaned_data[cleaned_data["Frequency [Rap]"] == 2]
    cleaned_data_rap3 = cleaned_data[cleaned_data["Frequency [Rap]"] == 3]
    cleaned_data_rap4 = cleaned_data[cleaned_data["Frequency [Rap]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_rap1 = cleaned_data_rap1["Anxiety"].mean()
    ave_dep_rap1 = cleaned_data_rap1["Depression"].mean()
    ave_insom_rap1 = cleaned_data_rap1["Insomnia"].mean()
    ave_ocd_rap1 = cleaned_data_rap1["OCD"].mean()
    
    ave_anxiety_rap2 = cleaned_data_rap2["Anxiety"].mean()
    ave_dep_rap2 = cleaned_data_rap2["Depression"].mean()
    ave_insom_rap2 = cleaned_data_rap2["Insomnia"].mean()
    ave_ocd_rap2 = cleaned_data_rap2["OCD"].mean()
    
    ave_anxiety_rap3 = cleaned_data_rap3["Anxiety"].mean()
    ave_dep_rap3 = cleaned_data_rap3["Depression"].mean()
    ave_insom_rap3 = cleaned_data_rap3["Insomnia"].mean()
    ave_ocd_rap3 = cleaned_data_rap3["OCD"].mean()
    
    ave_anxiety_rap4 = cleaned_data_rap4["Anxiety"].mean()
    ave_dep_rap4 = cleaned_data_rap4["Depression"].mean()
    ave_insom_rap4 = cleaned_data_rap4["Insomnia"].mean()
    ave_ocd_rap4 = cleaned_data_rap4["OCD"].mean()
    
    
    
    #making Classical subsets based on frequency
    cleaned_data_classical1 = cleaned_data[cleaned_data["Frequency [Classical]"] == 1]
    cleaned_data_classical2 = cleaned_data[cleaned_data["Frequency [Classical]"] == 2]
    cleaned_data_classical3 = cleaned_data[cleaned_data["Frequency [Classical]"] == 3]
    cleaned_data_classical4 = cleaned_data[cleaned_data["Frequency [Classical]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_classical1 = cleaned_data_classical1["Anxiety"].mean()
    ave_dep_classical1 = cleaned_data_classical1["Depression"].mean()
    ave_insom_classical1 = cleaned_data_classical1["Insomnia"].mean()
    ave_ocd_classical1 = cleaned_data_classical1["OCD"].mean()
    
    ave_anxiety_classical2 = cleaned_data_classical2["Anxiety"].mean()
    ave_dep_classical2 = cleaned_data_classical2["Depression"].mean()
    ave_insom_classical2 = cleaned_data_classical2["Insomnia"].mean()
    ave_ocd_classical2 = cleaned_data_classical2["OCD"].mean()
    
    ave_anxiety_classical3 = cleaned_data_classical3["Anxiety"].mean()
    ave_dep_classical3 = cleaned_data_classical3["Depression"].mean()
    ave_insom_classical3 = cleaned_data_classical3["Insomnia"].mean()
    ave_ocd_classical3 = cleaned_data_classical3["OCD"].mean()
    
    ave_anxiety_classical4 = cleaned_data_classical4["Anxiety"].mean()
    ave_dep_classical4 = cleaned_data_classical4["Depression"].mean()
    ave_insom_classical4 = cleaned_data_classical4["Insomnia"].mean()
    ave_ocd_classical4 = cleaned_data_classical4["OCD"].mean()
    
    
    
    #making Metal subsets based on frequency
    cleaned_data_metal1 = cleaned_data[cleaned_data["Frequency [Metal]"] == 1]
    cleaned_data_metal2 = cleaned_data[cleaned_data["Frequency [Metal]"] == 2]
    cleaned_data_metal3 = cleaned_data[cleaned_data["Frequency [Metal]"] == 3]
    cleaned_data_metal4 = cleaned_data[cleaned_data["Frequency [Metal]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_metal1 = cleaned_data_metal1["Anxiety"].mean()
    ave_dep_metal1 = cleaned_data_metal1["Depression"].mean()
    ave_insom_metal1 = cleaned_data_metal1["Insomnia"].mean()
    ave_ocd_metal1 = cleaned_data_metal1["OCD"].mean()
    
    ave_anxiety_metal2 = cleaned_data_metal2["Anxiety"].mean()
    ave_dep_metal2 = cleaned_data_metal2["Depression"].mean()
    ave_insom_metal2 = cleaned_data_metal2["Insomnia"].mean()
    ave_ocd_metal2 = cleaned_data_metal2["OCD"].mean()
    
    ave_anxiety_metal3 = cleaned_data_metal3["Anxiety"].mean()
    ave_dep_metal3 = cleaned_data_metal3["Depression"].mean()
    ave_insom_metal3 = cleaned_data_metal3["Insomnia"].mean()
    ave_ocd_metal3 = cleaned_data_metal3["OCD"].mean()
    
    ave_anxiety_metal4 = cleaned_data_metal4["Anxiety"].mean()
    ave_dep_metal4 = cleaned_data_metal4["Depression"].mean()
    ave_insom_metal4 = cleaned_data_metal4["Insomnia"].mean()
    ave_ocd_metal4 = cleaned_data_metal4["OCD"].mean()
    
    
    
    
    #making Folk subsets based on frequency
    cleaned_data_folk1 = cleaned_data[cleaned_data["Frequency [Folk]"] == 1]
    cleaned_data_folk2 = cleaned_data[cleaned_data["Frequency [Folk]"] == 2]
    cleaned_data_folk3 = cleaned_data[cleaned_data["Frequency [Folk]"] == 3]
    cleaned_data_folk4 = cleaned_data[cleaned_data["Frequency [Folk]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_folk1 = cleaned_data_folk1["Anxiety"].mean()
    ave_dep_folk1 = cleaned_data_folk1["Depression"].mean()
    ave_insom_folk1 = cleaned_data_folk1["Insomnia"].mean()
    ave_ocd_folk1 = cleaned_data_folk1["OCD"].mean()
    
    ave_anxiety_folk2 = cleaned_data_folk2["Anxiety"].mean()
    ave_dep_folk2 = cleaned_data_folk2["Depression"].mean()
    ave_insom_folk2 = cleaned_data_folk2["Insomnia"].mean()
    ave_ocd_folk2 = cleaned_data_folk2["OCD"].mean()
    
    ave_anxiety_folk3 = cleaned_data_folk3["Anxiety"].mean()
    ave_dep_folk3 = cleaned_data_folk3["Depression"].mean()
    ave_insom_folk3 = cleaned_data_folk3["Insomnia"].mean()
    ave_ocd_folk3 = cleaned_data_folk3["OCD"].mean()
    
    ave_anxiety_folk4 = cleaned_data_folk4["Anxiety"].mean()
    ave_dep_folk4 = cleaned_data_folk4["Depression"].mean()
    ave_insom_folk4 = cleaned_data_folk4["Insomnia"].mean()
    ave_ocd_folk4 = cleaned_data_folk4["OCD"].mean()
    
    
    
    
    
    #making Lofi subsets based on frequency
    cleaned_data_lofi1 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 1]
    cleaned_data_lofi2 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 2]
    cleaned_data_lofi3 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 3]
    cleaned_data_lofi4 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 4]
    
    #Now get the average MH scores for each frequency
    ave_anxiety_lofi1 = cleaned_data_lofi1["Anxiety"].mean()
    ave_dep_lofi1 = cleaned_data_lofi1["Depression"].mean()
    ave_insom_lofi1 = cleaned_data_lofi1["Insomnia"].mean()
    ave_ocd_lofi1 = cleaned_data_lofi1["OCD"].mean()
    
    ave_anxiety_lofi2 = cleaned_data_lofi2["Anxiety"].mean()
    ave_dep_lofi2 = cleaned_data_lofi2["Depression"].mean()
    ave_insom_lofi2 = cleaned_data_lofi2["Insomnia"].mean()
    ave_ocd_lofi2 = cleaned_data_lofi2["OCD"].mean()
    
    ave_anxiety_lofi3 = cleaned_data_lofi3["Anxiety"].mean()
    ave_dep_lofi3 = cleaned_data_lofi3["Depression"].mean()
    ave_insom_lofi3 = cleaned_data_lofi3["Insomnia"].mean()
    ave_ocd_lofi3 = cleaned_data_lofi3["OCD"].mean()
    
    ave_anxiety_lofi4 = cleaned_data_lofi4["Anxiety"].mean()
    ave_dep_lofi4 = cleaned_data_lofi4["Depression"].mean()
    ave_insom_lofi4 = cleaned_data_lofi4["Insomnia"].mean()
    ave_ocd_lofi4 = cleaned_data_lofi4["OCD"].mean()
    
    
    
    
    #making Gospel subsets based on frequency
    cleaned_data_gospel1 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 1]
    cleaned_data_gospel2 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 2]
    cleaned_data_gospel3 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 3]
    cleaned_data_gospel4 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_gospel1 = cleaned_data_gospel1["Anxiety"].mean()
    ave_dep_gospel1 = cleaned_data_gospel1["Depression"].mean()
    ave_insom_gospel1 = cleaned_data_gospel1["Insomnia"].mean()
    ave_ocd_gospel1 = cleaned_data_gospel1["OCD"].mean()
    
    ave_anxiety_gospel2 = cleaned_data_gospel2["Anxiety"].mean()
    ave_dep_gospel2 = cleaned_data_gospel2["Depression"].mean()
    ave_insom_gospel2 = cleaned_data_gospel2["Insomnia"].mean()
    ave_ocd_gospel2 = cleaned_data_gospel2["OCD"].mean()
    
    ave_anxiety_gospel3 = cleaned_data_gospel3["Anxiety"].mean()
    ave_dep_gospel3 = cleaned_data_gospel3["Depression"].mean()
    ave_insom_gospel3 = cleaned_data_gospel3["Insomnia"].mean()
    ave_ocd_gospel3 = cleaned_data_gospel3["OCD"].mean()
    
    ave_anxiety_gospel4 = cleaned_data_gospel4["Anxiety"].mean()
    ave_dep_gospel4 = cleaned_data_gospel4["Depression"].mean()
    ave_insom_gospel4 = cleaned_data_gospel4["Insomnia"].mean()
    ave_ocd_gospel4 = cleaned_data_gospel4["OCD"].mean()
    
    #create a dataframe for these values
    index = ["Classical", "Country", "EDM", "Folk", "Gospel", "Hip hop", "Jazz", "K pop", "Latin", "Lofi", 
             "Metal", "Pop", "R&B", "Rap", "Rock", "Video game music"]
    columns = ["Anxiety", "Depression", "Insomnia", "OCD"]
    
    mh_by_genre = pd.DataFrame(index=index, columns=columns)
    

    #add values
    average_anxiety = [ave_anxiety_classical4, ave_anxiety_country4, ave_anxiety_edm4,  ave_anxiety_folk4, ave_anxiety_gospel4, ave_anxiety_hiphop4, 
        ave_anxiety_jazz4, ave_anxiety_kpop4, ave_anxiety_latin4, ave_anxiety_lofi4, ave_anxiety_metal4, ave_anxiety_pop4, ave_anxiety_rnb4, 
        ave_anxiety_rap4, ave_anxiety_rock4, ave_anxiety_vgm4]
    
    average_depression = [ave_dep_classical4, ave_dep_country4, ave_dep_edm4, ave_dep_folk4, ave_dep_gospel4, ave_dep_hiphop4, ave_dep_jazz4, 
            ave_dep_kpop4, ave_dep_latin4, ave_dep_lofi4, ave_dep_metal4, ave_dep_pop4, ave_dep_rnb4, ave_dep_rap4, ave_dep_rock4, ave_dep_vgm4]
    
    average_ocd = [ave_ocd_classical4, ave_ocd_country4, ave_ocd_edm4, ave_ocd_folk4, ave_ocd_gospel4, ave_ocd_hiphop4, ave_ocd_jazz4, ave_ocd_kpop4, 
        ave_ocd_latin4, ave_ocd_lofi4, ave_ocd_metal4, ave_ocd_pop4, ave_ocd_rnb4, ave_ocd_rap4, ave_ocd_rock4, ave_ocd_vgm4]
    
    average_insomnia = [ave_insom_classical4, ave_insom_country4, ave_insom_edm4, ave_insom_folk4, ave_insom_gospel4, ave_insom_hiphop4, ave_insom_jazz4, 
            ave_insom_kpop4, ave_insom_latin4, ave_insom_lofi4, ave_insom_metal4, ave_insom_pop4, ave_insom_rnb4, ave_insom_rap4, ave_insom_rock4, 
            ave_insom_vgm4]
    
    mh_by_genre["Anxiety"] = average_anxiety
    mh_by_genre["Depression"] = average_depression
    mh_by_genre["Insomnia"] = average_insomnia
    mh_by_genre["OCD"] = average_ocd
    
    st.write(mh_by_genre)  


    st.subheader("Heatmap of Genre and Average Mental Health Stat (based only on Very Frequent responses)")
    fig = px.imshow(mh_by_genre.T, labels=dict(x="MH Score", y="Genre", color="Score"), color_continuous_scale="Viridis", 
    title="Interactive Heatmap of Mental Health Scores by Genre",)
    # Show the heatmap
    st.plotly_chart(fig)


    st.markdown("I used mh_by_genre.describe() to identify the MH category with the highest variability (SD) so I could capture more unique responses. This came out to be Depression (sd = 0.517690; Anxiety SD = 0.502129, Insomnia SD = 0.328233, OCD SD = 0.240497)")
    st.markdown("I then created a binary feature that expressed whether the avergae depression score for a given genre was above or below 5. This is how I will recommend genres to users.")

    mh_by_genre["Effect"] = np.where(mh_by_genre["Depression"] >= 5, 1, 0)

    mh_by_genre


if selected_category == "Get Recommendations":


    ########################repeating so this dropdown option can use the same updated data

    
    #load the Data
    mxmh_survey_results = pd.read_csv("mxmh_survey_results.csv")

    #group and replace
    for i, val in enumerate(mxmh_survey_results["BPM"].isna()):
        genre = mxmh_survey_results.loc[i, "Fav genre"]  # Get the genre for the current row
        if genre == "Latin":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Latin"]["BPM"].median()
        if genre == "Rock":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Rock"]["BPM"].median()
        if genre == "Video game music":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Video game music"]["BPM"].median()
        if genre == "Jazz":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Jazz"]["BPM"].median()
        if genre == "R&B":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "R&B"]["BPM"].median()
        if genre == "K pop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "K pop"]["BPM"].median()
        if genre == "Country":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Country"]["BPM"].median()
        if genre == "EDM":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "EDM"]["BPM"].median()
        if genre == "Hip hop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Hip hop"]["BPM"].median()
        if genre == "Pop":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Pop"]["BPM"].median()
        if genre == "Rap":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Rap"]["BPM"].median()
        if genre == "Classical":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Classical"]["BPM"].median()
        if genre == "Metal":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Metal"]["BPM"].median()
        if genre == "Folk":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Folk"]["BPM"].median()
        if genre == "Lofi":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Lofi"]["BPM"].median()
        if genre == "Gospel":
            mxmh_survey_results.loc[i, "BPM"] = mxmh_survey_results[mxmh_survey_results["Fav genre"] == "Gospel"]["BPM"].median()

  
    cleaned_data = mxmh_survey_results.copy()
    #I will say the max they could realistically listen to is 16 hrs
    cleaned_data = cleaned_data[(cleaned_data["Hours per day"] < 16)]
    #deleted 6 rows

    #take away age outliers 
    cleaned_data = cleaned_data[(cleaned_data["Age"] > 18) & (cleaned_data["Age"] < 64)]
    
    #recode frequency genre

    frequency_mapping = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Very frequently": 4 }

    # Replace the values in the "Frequency [Country]" column
    cleaned_data["Frequency [Latin]"] = cleaned_data["Frequency [Latin]"].replace(frequency_mapping)
    cleaned_data["Frequency [Rock]"] = cleaned_data["Frequency [Rock]"].replace(frequency_mapping)
    cleaned_data["Frequency [Video game music]"] = cleaned_data["Frequency [Video game music]"].replace(frequency_mapping)
    cleaned_data["Frequency [Jazz]"] = cleaned_data["Frequency [Jazz]"].replace(frequency_mapping)
    cleaned_data["Frequency [R&B]"] = cleaned_data["Frequency [R&B]"].replace(frequency_mapping)
    cleaned_data["Frequency [K pop]"] = cleaned_data["Frequency [K pop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Country]"] = cleaned_data["Frequency [Country]"].replace(frequency_mapping)
    cleaned_data["Frequency [EDM]"] = cleaned_data["Frequency [EDM]"].replace(frequency_mapping)
    cleaned_data["Frequency [Hip hop]"] = cleaned_data["Frequency [Hip hop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Pop]"] = cleaned_data["Frequency [Pop]"].replace(frequency_mapping)
    cleaned_data["Frequency [Rap]"] = cleaned_data["Frequency [Rap]"].replace(frequency_mapping)
    cleaned_data["Frequency [Classical]"] = cleaned_data["Frequency [Classical]"].replace(frequency_mapping)
    cleaned_data["Frequency [Metal]"] = cleaned_data["Frequency [Metal]"].replace(frequency_mapping)
    cleaned_data["Frequency [Folk]"] = cleaned_data["Frequency [Folk]"].replace(frequency_mapping)
    cleaned_data["Frequency [Lofi]"] = cleaned_data["Frequency [Lofi]"].replace(frequency_mapping)
    cleaned_data["Frequency [Gospel]"] = cleaned_data["Frequency [Gospel]"].replace(frequency_mapping)

   
    #make aged binned

    bins = [18, 25, 31, 36, 41, 46, 51, 58, 64]  
    labels = ['18-24', '25-30', '31-35', '36-40', '41-45', '46-50', '51-57', '58-64']  # Labels for the bins

    # Create the binned column
    cleaned_data['age_binned'] = pd.cut(cleaned_data['Age'], bins=bins, labels=labels, right=False)


    

    #feature engineering
    
    #making latin subsets based on frequency
    cleaned_data_latin1 = cleaned_data[cleaned_data["Frequency [Latin]"] == 1]
    cleaned_data_latin2 = cleaned_data[cleaned_data["Frequency [Latin]"] == 2]
    cleaned_data_latin3 = cleaned_data[cleaned_data["Frequency [Latin]"] == 3]
    cleaned_data_latin4 = cleaned_data[cleaned_data["Frequency [Latin]"] == 4]
    
    
    #now get the average MH scores for each frequency
    ave_anxiety_latin1 = cleaned_data_latin1["Anxiety"].mean()
    ave_dep_latin1 = cleaned_data_latin1["Depression"].mean()
    ave_insom_latin1 = cleaned_data_latin1["Insomnia"].mean()
    ave_ocd_latin1 = cleaned_data_latin1["OCD"].mean()
    
    ave_anxiety_latin2 = cleaned_data_latin2["Anxiety"].mean()
    ave_dep_latin2 = cleaned_data_latin2["Depression"].mean()
    ave_insom_latin2 = cleaned_data_latin2["Insomnia"].mean()
    ave_ocd_latin2 = cleaned_data_latin2["OCD"].mean()
    
    ave_anxiety_latin3 = cleaned_data_latin3["Anxiety"].mean()
    ave_dep_latin3 = cleaned_data_latin3["Depression"].mean()
    ave_insom_latin3 = cleaned_data_latin3["Insomnia"].mean()
    ave_ocd_latin3 = cleaned_data_latin3["OCD"].mean()
    
    ave_anxiety_latin4 = cleaned_data_latin4["Anxiety"].mean()
    ave_dep_latin4 = cleaned_data_latin4["Depression"].mean()
    ave_insom_latin4 = cleaned_data_latin4["Insomnia"].mean()
    ave_ocd_latin4 = cleaned_data_latin4["OCD"].mean()
    
    
    
    #making rock subsets based on frequency
    cleaned_data_rock1 = cleaned_data[cleaned_data["Frequency [Rock]"] == 1]
    cleaned_data_rock2 = cleaned_data[cleaned_data["Frequency [Rock]"] == 2]
    cleaned_data_rock3 = cleaned_data[cleaned_data["Frequency [Rock]"] == 3]
    cleaned_data_rock4 = cleaned_data[cleaned_data["Frequency [Rock]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_rock1 = cleaned_data_rock1["Anxiety"].mean()
    ave_dep_rock1 = cleaned_data_rock1["Depression"].mean()
    ave_insom_rock1 = cleaned_data_rock1["Insomnia"].mean()
    ave_ocd_rock1 = cleaned_data_rock1["OCD"].mean()
    
    ave_anxiety_rock2 = cleaned_data_rock2["Anxiety"].mean()
    ave_dep_rock2 = cleaned_data_rock2["Depression"].mean()
    ave_insom_rock2 = cleaned_data_rock2["Insomnia"].mean()
    ave_ocd_rock2 = cleaned_data_rock2["OCD"].mean()
    
    ave_anxiety_rock3 = cleaned_data_rock3["Anxiety"].mean()
    ave_dep_rock3 = cleaned_data_rock3["Depression"].mean()
    ave_insom_rock3 = cleaned_data_rock3["Insomnia"].mean()
    ave_ocd_rock3 = cleaned_data_rock3["OCD"].mean()
    
    ave_anxiety_rock4 = cleaned_data_rock4["Anxiety"].mean()
    ave_dep_rock4 = cleaned_data_rock4["Depression"].mean()
    ave_insom_rock4 = cleaned_data_rock4["Insomnia"].mean()
    ave_ocd_rock4 = cleaned_data_rock4["OCD"].mean()
    
    
    
    
    #making Video game music subsets based on frequency
    cleaned_data_vgm1 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 1]
    cleaned_data_vgm2 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 2]
    cleaned_data_vgm3 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 3]
    cleaned_data_vgm4 = cleaned_data[cleaned_data["Frequency [Video game music]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_vgm1 = cleaned_data_vgm1["Anxiety"].mean()
    ave_dep_vgm1 = cleaned_data_vgm1["Depression"].mean()
    ave_insom_vgm1 = cleaned_data_vgm1["Insomnia"].mean()
    ave_ocd_vgm1 = cleaned_data_vgm1["OCD"].mean()
    
    ave_anxiety_vgm2 = cleaned_data_vgm2["Anxiety"].mean()
    ave_dep_vgm2 = cleaned_data_vgm2["Depression"].mean()
    ave_insom_vgm2 = cleaned_data_vgm2["Insomnia"].mean()
    ave_ocd_vgm2 = cleaned_data_vgm2["OCD"].mean()
    
    ave_anxiety_vgm3 = cleaned_data_vgm3["Anxiety"].mean()
    ave_dep_vgm3 = cleaned_data_vgm3["Depression"].mean()
    ave_insom_vgm3 = cleaned_data_vgm3["Insomnia"].mean()
    ave_ocd_vgm3 = cleaned_data_vgm3["OCD"].mean()
    
    ave_anxiety_vgm4 = cleaned_data_vgm4["Anxiety"].mean()
    ave_dep_vgm4 = cleaned_data_vgm4["Depression"].mean()
    ave_insom_vgm4 = cleaned_data_vgm4["Insomnia"].mean()
    ave_ocd_vgm4 = cleaned_data_vgm4["OCD"].mean()
    
    
    
    #making Jazz subsets based on frequency
    cleaned_data_jazz1 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 1]
    cleaned_data_jazz2 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 2]
    cleaned_data_jazz3 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 3]
    cleaned_data_jazz4 = cleaned_data[cleaned_data["Frequency [Jazz]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_jazz1 = cleaned_data_jazz1["Anxiety"].mean()
    ave_dep_jazz1 = cleaned_data_jazz1["Depression"].mean()
    ave_insom_jazz1 = cleaned_data_jazz1["Insomnia"].mean()
    ave_ocd_jazz1 = cleaned_data_jazz1["OCD"].mean()
    
    ave_anxiety_jazz2 = cleaned_data_jazz2["Anxiety"].mean()
    ave_dep_jazz2 = cleaned_data_jazz2["Depression"].mean()
    ave_insom_jazz2 = cleaned_data_jazz2["Insomnia"].mean()
    ave_ocd_jazz2 = cleaned_data_jazz2["OCD"].mean()
    
    ave_anxiety_jazz3 = cleaned_data_jazz3["Anxiety"].mean()
    ave_dep_jazz3 = cleaned_data_jazz3["Depression"].mean()
    ave_insom_jazz3 = cleaned_data_jazz3["Insomnia"].mean()
    ave_ocd_jazz3 = cleaned_data_jazz3["OCD"].mean()
    
    ave_anxiety_jazz4 = cleaned_data_jazz4["Anxiety"].mean()
    ave_dep_jazz4 = cleaned_data_jazz4["Depression"].mean()
    ave_insom_jazz4 = cleaned_data_jazz4["Insomnia"].mean()
    ave_ocd_jazz4 = cleaned_data_jazz4["OCD"].mean()
    
    
    
    #making R&B subsets based on frequency
    cleaned_data_rnb1 = cleaned_data[cleaned_data["Frequency [R&B]"] == 1]
    cleaned_data_rnb2 = cleaned_data[cleaned_data["Frequency [R&B]"] == 2]
    cleaned_data_rnb3 = cleaned_data[cleaned_data["Frequency [R&B]"] == 3]
    cleaned_data_rnb4 = cleaned_data[cleaned_data["Frequency [R&B]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_rnb1 = cleaned_data_rnb1["Anxiety"].mean()
    ave_dep_rnb1 = cleaned_data_rnb1["Depression"].mean()
    ave_insom_rnb1 = cleaned_data_rnb1["Insomnia"].mean()
    ave_ocd_rnb1 = cleaned_data_rnb1["OCD"].mean()
    
    ave_anxiety_rnb2 = cleaned_data_rnb2["Anxiety"].mean()
    ave_dep_rnb2 = cleaned_data_rnb2["Depression"].mean()
    ave_insom_rnb2 = cleaned_data_rnb2["Insomnia"].mean()
    ave_ocd_rnb2 = cleaned_data_rnb2["OCD"].mean()
    
    ave_anxiety_rnb3 = cleaned_data_rnb3["Anxiety"].mean()
    ave_dep_rnb3 = cleaned_data_rnb3["Depression"].mean()
    ave_insom_rnb3 = cleaned_data_rnb3["Insomnia"].mean()
    ave_ocd_rnb3 = cleaned_data_rnb3["OCD"].mean()
    
    ave_anxiety_rnb4 = cleaned_data_rnb4["Anxiety"].mean()
    ave_dep_rnb4 = cleaned_data_rnb4["Depression"].mean()
    ave_insom_rnb4 = cleaned_data_rnb4["Insomnia"].mean()
    ave_ocd_rnb4 = cleaned_data_rnb4["OCD"].mean()
    
    
    
    #making K pop subsets based on frequency
    cleaned_data_kpop1 = cleaned_data[cleaned_data["Frequency [K pop]"] == 1]
    cleaned_data_kpop2 = cleaned_data[cleaned_data["Frequency [K pop]"] == 2]
    cleaned_data_kpop3 = cleaned_data[cleaned_data["Frequency [K pop]"] == 3]
    cleaned_data_kpop4 = cleaned_data[cleaned_data["Frequency [K pop]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_kpop1 = cleaned_data_kpop1["Anxiety"].mean()
    ave_dep_kpop1 = cleaned_data_kpop1["Depression"].mean()
    ave_insom_kpop1 = cleaned_data_kpop1["Insomnia"].mean()
    ave_ocd_kpop1 = cleaned_data_kpop1["OCD"].mean()
    
    ave_anxiety_kpop2 = cleaned_data_kpop2["Anxiety"].mean()
    ave_dep_kpop2 = cleaned_data_kpop2["Depression"].mean()
    ave_insom_kpop2 = cleaned_data_kpop2["Insomnia"].mean()
    ave_ocd_kpop2 = cleaned_data_kpop2["OCD"].mean()
    
    ave_anxiety_kpop3 = cleaned_data_kpop3["Anxiety"].mean()
    ave_dep_kpop3 = cleaned_data_kpop3["Depression"].mean()
    ave_insom_kpop3 = cleaned_data_kpop3["Insomnia"].mean()
    ave_ocd_kpop3 = cleaned_data_kpop3["OCD"].mean()
    
    ave_anxiety_kpop4 = cleaned_data_kpop4["Anxiety"].mean()
    ave_dep_kpop4 = cleaned_data_kpop4["Depression"].mean()
    ave_insom_kpop4 = cleaned_data_kpop4["Insomnia"].mean()
    ave_ocd_kpop4 = cleaned_data_kpop4["OCD"].mean()
    
    
    
    #making Country subsets based on frequency
    cleaned_data_country1 = cleaned_data[cleaned_data["Frequency [Country]"] == 1]
    cleaned_data_country2 = cleaned_data[cleaned_data["Frequency [Country]"] == 2]
    cleaned_data_country3 = cleaned_data[cleaned_data["Frequency [Country]"] == 3]
    cleaned_data_country4 = cleaned_data[cleaned_data["Frequency [Country]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_country1 = cleaned_data_country1["Anxiety"].mean()
    ave_dep_country1 = cleaned_data_country1["Depression"].mean()
    ave_insom_country1 = cleaned_data_country1["Insomnia"].mean()
    ave_ocd_country1 = cleaned_data_country1["OCD"].mean()
    
    ave_anxiety_country2 = cleaned_data_country2["Anxiety"].mean()
    ave_dep_country2 = cleaned_data_country2["Depression"].mean()
    ave_insom_country2 = cleaned_data_country2["Insomnia"].mean()
    ave_ocd_country2 = cleaned_data_country2["OCD"].mean()
    
    ave_anxiety_country3 = cleaned_data_country3["Anxiety"].mean()
    ave_dep_country3 = cleaned_data_country3["Depression"].mean()
    ave_insom_country3 = cleaned_data_country3["Insomnia"].mean()
    ave_ocd_country3 = cleaned_data_country3["OCD"].mean()
    
    ave_anxiety_country4 = cleaned_data_country4["Anxiety"].mean()
    ave_dep_country4 = cleaned_data_country4["Depression"].mean()
    ave_insom_country4 = cleaned_data_country4["Insomnia"].mean()
    ave_ocd_country4 = cleaned_data_country4["OCD"].mean()
    
    
    
    #making EDM subsets based on frequency
    cleaned_data_edm1 = cleaned_data[cleaned_data["Frequency [EDM]"] == 1]
    cleaned_data_edm2 = cleaned_data[cleaned_data["Frequency [EDM]"] == 2]
    cleaned_data_edm3 = cleaned_data[cleaned_data["Frequency [EDM]"] == 3]
    cleaned_data_edm4 = cleaned_data[cleaned_data["Frequency [EDM]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_edm1 = cleaned_data_edm1["Anxiety"].mean()
    ave_dep_edm1 = cleaned_data_edm1["Depression"].mean()
    ave_insom_edm1 = cleaned_data_edm1["Insomnia"].mean()
    ave_ocd_edm1 = cleaned_data_edm1["OCD"].mean()
    
    ave_anxiety_edm2 = cleaned_data_edm2["Anxiety"].mean()
    ave_dep_edm2 = cleaned_data_edm2["Depression"].mean()
    ave_insom_edm2 = cleaned_data_edm2["Insomnia"].mean()
    ave_ocd_edm2 = cleaned_data_edm2["OCD"].mean()
    
    ave_anxiety_edm3 = cleaned_data_edm3["Anxiety"].mean()
    ave_dep_edm3 = cleaned_data_edm3["Depression"].mean()
    ave_insom_edm3 = cleaned_data_edm3["Insomnia"].mean()
    ave_ocd_edm3 = cleaned_data_edm3["OCD"].mean()
    
    ave_anxiety_edm4 = cleaned_data_edm4["Anxiety"].mean()
    ave_dep_edm4 = cleaned_data_edm4["Depression"].mean()
    ave_insom_edm4 = cleaned_data_edm4["Insomnia"].mean()
    ave_ocd_edm4 = cleaned_data_edm4["OCD"].mean()
    
    
    
    #making Hip hop subsets based on frequency
    cleaned_data_hiphop1 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 1]
    cleaned_data_hiphop2 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 2]
    cleaned_data_hiphop3 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 3]
    cleaned_data_hiphop4 = cleaned_data[cleaned_data["Frequency [Hip hop]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_hiphop1 = cleaned_data_hiphop1["Anxiety"].mean()
    ave_dep_hiphop1 = cleaned_data_hiphop1["Depression"].mean()
    ave_insom_hiphop1 = cleaned_data_hiphop1["Insomnia"].mean()
    ave_ocd_hiphop1 = cleaned_data_hiphop1["OCD"].mean()
    
    ave_anxiety_hiphop2 = cleaned_data_hiphop2["Anxiety"].mean()
    ave_dep_hiphop2 = cleaned_data_hiphop2["Depression"].mean()
    ave_insom_hiphop2 = cleaned_data_hiphop2["Insomnia"].mean()
    ave_ocd_hiphop2 = cleaned_data_hiphop2["OCD"].mean()
    
    ave_anxiety_hiphop3 = cleaned_data_hiphop3["Anxiety"].mean()
    ave_dep_hiphop3 = cleaned_data_hiphop3["Depression"].mean()
    ave_insom_hiphop3 = cleaned_data_hiphop3["Insomnia"].mean()
    ave_ocd_hiphop3 = cleaned_data_hiphop3["OCD"].mean()
    
    ave_anxiety_hiphop4 = cleaned_data_hiphop4["Anxiety"].mean()
    ave_dep_hiphop4 = cleaned_data_hiphop4["Depression"].mean()
    ave_insom_hiphop4 = cleaned_data_hiphop4["Insomnia"].mean()
    ave_ocd_hiphop4 = cleaned_data_hiphop4["OCD"].mean()
    
    
    
    
    #making Pop subsets based on frequency
    cleaned_data_pop1 = cleaned_data[cleaned_data["Frequency [Pop]"] == 1]
    cleaned_data_pop2 = cleaned_data[cleaned_data["Frequency [Pop]"] == 2]
    cleaned_data_pop3 = cleaned_data[cleaned_data["Frequency [Pop]"] == 3]
    cleaned_data_pop4 = cleaned_data[cleaned_data["Frequency [Pop]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_pop1 = cleaned_data_pop1["Anxiety"].mean()
    ave_dep_pop1 = cleaned_data_pop1["Depression"].mean()
    ave_insom_pop1 = cleaned_data_pop1["Insomnia"].mean()
    ave_ocd_pop1 = cleaned_data_pop1["OCD"].mean()
    
    ave_anxiety_pop2 = cleaned_data_pop2["Anxiety"].mean()
    ave_dep_pop2 = cleaned_data_pop2["Depression"].mean()
    ave_insom_pop2 = cleaned_data_pop2["Insomnia"].mean()
    ave_ocd_pop2 = cleaned_data_pop2["OCD"].mean()
    
    ave_anxiety_pop3 = cleaned_data_pop3["Anxiety"].mean()
    ave_dep_pop3 = cleaned_data_pop3["Depression"].mean()
    ave_insom_pop3 = cleaned_data_pop3["Insomnia"].mean()
    ave_ocd_pop3 = cleaned_data_pop3["OCD"].mean()
    
    ave_anxiety_pop4 = cleaned_data_pop4["Anxiety"].mean()
    ave_dep_pop4 = cleaned_data_pop4["Depression"].mean()
    ave_insom_pop4 = cleaned_data_pop4["Insomnia"].mean()
    ave_ocd_pop4 = cleaned_data_pop4["OCD"].mean()
    
    
    
    
    #making Rap subsets based on frequency
    cleaned_data_rap1 = cleaned_data[cleaned_data["Frequency [Rap]"] == 1]
    cleaned_data_rap2 = cleaned_data[cleaned_data["Frequency [Rap]"] == 2]
    cleaned_data_rap3 = cleaned_data[cleaned_data["Frequency [Rap]"] == 3]
    cleaned_data_rap4 = cleaned_data[cleaned_data["Frequency [Rap]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_rap1 = cleaned_data_rap1["Anxiety"].mean()
    ave_dep_rap1 = cleaned_data_rap1["Depression"].mean()
    ave_insom_rap1 = cleaned_data_rap1["Insomnia"].mean()
    ave_ocd_rap1 = cleaned_data_rap1["OCD"].mean()
    
    ave_anxiety_rap2 = cleaned_data_rap2["Anxiety"].mean()
    ave_dep_rap2 = cleaned_data_rap2["Depression"].mean()
    ave_insom_rap2 = cleaned_data_rap2["Insomnia"].mean()
    ave_ocd_rap2 = cleaned_data_rap2["OCD"].mean()
    
    ave_anxiety_rap3 = cleaned_data_rap3["Anxiety"].mean()
    ave_dep_rap3 = cleaned_data_rap3["Depression"].mean()
    ave_insom_rap3 = cleaned_data_rap3["Insomnia"].mean()
    ave_ocd_rap3 = cleaned_data_rap3["OCD"].mean()
    
    ave_anxiety_rap4 = cleaned_data_rap4["Anxiety"].mean()
    ave_dep_rap4 = cleaned_data_rap4["Depression"].mean()
    ave_insom_rap4 = cleaned_data_rap4["Insomnia"].mean()
    ave_ocd_rap4 = cleaned_data_rap4["OCD"].mean()
    
    
    
    #making Classical subsets based on frequency
    cleaned_data_classical1 = cleaned_data[cleaned_data["Frequency [Classical]"] == 1]
    cleaned_data_classical2 = cleaned_data[cleaned_data["Frequency [Classical]"] == 2]
    cleaned_data_classical3 = cleaned_data[cleaned_data["Frequency [Classical]"] == 3]
    cleaned_data_classical4 = cleaned_data[cleaned_data["Frequency [Classical]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_classical1 = cleaned_data_classical1["Anxiety"].mean()
    ave_dep_classical1 = cleaned_data_classical1["Depression"].mean()
    ave_insom_classical1 = cleaned_data_classical1["Insomnia"].mean()
    ave_ocd_classical1 = cleaned_data_classical1["OCD"].mean()
    
    ave_anxiety_classical2 = cleaned_data_classical2["Anxiety"].mean()
    ave_dep_classical2 = cleaned_data_classical2["Depression"].mean()
    ave_insom_classical2 = cleaned_data_classical2["Insomnia"].mean()
    ave_ocd_classical2 = cleaned_data_classical2["OCD"].mean()
    
    ave_anxiety_classical3 = cleaned_data_classical3["Anxiety"].mean()
    ave_dep_classical3 = cleaned_data_classical3["Depression"].mean()
    ave_insom_classical3 = cleaned_data_classical3["Insomnia"].mean()
    ave_ocd_classical3 = cleaned_data_classical3["OCD"].mean()
    
    ave_anxiety_classical4 = cleaned_data_classical4["Anxiety"].mean()
    ave_dep_classical4 = cleaned_data_classical4["Depression"].mean()
    ave_insom_classical4 = cleaned_data_classical4["Insomnia"].mean()
    ave_ocd_classical4 = cleaned_data_classical4["OCD"].mean()
    
    
    
    #making Metal subsets based on frequency
    cleaned_data_metal1 = cleaned_data[cleaned_data["Frequency [Metal]"] == 1]
    cleaned_data_metal2 = cleaned_data[cleaned_data["Frequency [Metal]"] == 2]
    cleaned_data_metal3 = cleaned_data[cleaned_data["Frequency [Metal]"] == 3]
    cleaned_data_metal4 = cleaned_data[cleaned_data["Frequency [Metal]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_metal1 = cleaned_data_metal1["Anxiety"].mean()
    ave_dep_metal1 = cleaned_data_metal1["Depression"].mean()
    ave_insom_metal1 = cleaned_data_metal1["Insomnia"].mean()
    ave_ocd_metal1 = cleaned_data_metal1["OCD"].mean()
    
    ave_anxiety_metal2 = cleaned_data_metal2["Anxiety"].mean()
    ave_dep_metal2 = cleaned_data_metal2["Depression"].mean()
    ave_insom_metal2 = cleaned_data_metal2["Insomnia"].mean()
    ave_ocd_metal2 = cleaned_data_metal2["OCD"].mean()
    
    ave_anxiety_metal3 = cleaned_data_metal3["Anxiety"].mean()
    ave_dep_metal3 = cleaned_data_metal3["Depression"].mean()
    ave_insom_metal3 = cleaned_data_metal3["Insomnia"].mean()
    ave_ocd_metal3 = cleaned_data_metal3["OCD"].mean()
    
    ave_anxiety_metal4 = cleaned_data_metal4["Anxiety"].mean()
    ave_dep_metal4 = cleaned_data_metal4["Depression"].mean()
    ave_insom_metal4 = cleaned_data_metal4["Insomnia"].mean()
    ave_ocd_metal4 = cleaned_data_metal4["OCD"].mean()
    
    
    
    
    #making Folk subsets based on frequency
    cleaned_data_folk1 = cleaned_data[cleaned_data["Frequency [Folk]"] == 1]
    cleaned_data_folk2 = cleaned_data[cleaned_data["Frequency [Folk]"] == 2]
    cleaned_data_folk3 = cleaned_data[cleaned_data["Frequency [Folk]"] == 3]
    cleaned_data_folk4 = cleaned_data[cleaned_data["Frequency [Folk]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_folk1 = cleaned_data_folk1["Anxiety"].mean()
    ave_dep_folk1 = cleaned_data_folk1["Depression"].mean()
    ave_insom_folk1 = cleaned_data_folk1["Insomnia"].mean()
    ave_ocd_folk1 = cleaned_data_folk1["OCD"].mean()
    
    ave_anxiety_folk2 = cleaned_data_folk2["Anxiety"].mean()
    ave_dep_folk2 = cleaned_data_folk2["Depression"].mean()
    ave_insom_folk2 = cleaned_data_folk2["Insomnia"].mean()
    ave_ocd_folk2 = cleaned_data_folk2["OCD"].mean()
    
    ave_anxiety_folk3 = cleaned_data_folk3["Anxiety"].mean()
    ave_dep_folk3 = cleaned_data_folk3["Depression"].mean()
    ave_insom_folk3 = cleaned_data_folk3["Insomnia"].mean()
    ave_ocd_folk3 = cleaned_data_folk3["OCD"].mean()
    
    ave_anxiety_folk4 = cleaned_data_folk4["Anxiety"].mean()
    ave_dep_folk4 = cleaned_data_folk4["Depression"].mean()
    ave_insom_folk4 = cleaned_data_folk4["Insomnia"].mean()
    ave_ocd_folk4 = cleaned_data_folk4["OCD"].mean()
    
    
    
    
    
    #making Lofi subsets based on frequency
    cleaned_data_lofi1 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 1]
    cleaned_data_lofi2 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 2]
    cleaned_data_lofi3 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 3]
    cleaned_data_lofi4 = cleaned_data[cleaned_data["Frequency [Lofi]"] == 4]
    
    #Now get the average MH scores for each frequency
    ave_anxiety_lofi1 = cleaned_data_lofi1["Anxiety"].mean()
    ave_dep_lofi1 = cleaned_data_lofi1["Depression"].mean()
    ave_insom_lofi1 = cleaned_data_lofi1["Insomnia"].mean()
    ave_ocd_lofi1 = cleaned_data_lofi1["OCD"].mean()
    
    ave_anxiety_lofi2 = cleaned_data_lofi2["Anxiety"].mean()
    ave_dep_lofi2 = cleaned_data_lofi2["Depression"].mean()
    ave_insom_lofi2 = cleaned_data_lofi2["Insomnia"].mean()
    ave_ocd_lofi2 = cleaned_data_lofi2["OCD"].mean()
    
    ave_anxiety_lofi3 = cleaned_data_lofi3["Anxiety"].mean()
    ave_dep_lofi3 = cleaned_data_lofi3["Depression"].mean()
    ave_insom_lofi3 = cleaned_data_lofi3["Insomnia"].mean()
    ave_ocd_lofi3 = cleaned_data_lofi3["OCD"].mean()
    
    ave_anxiety_lofi4 = cleaned_data_lofi4["Anxiety"].mean()
    ave_dep_lofi4 = cleaned_data_lofi4["Depression"].mean()
    ave_insom_lofi4 = cleaned_data_lofi4["Insomnia"].mean()
    ave_ocd_lofi4 = cleaned_data_lofi4["OCD"].mean()
    
    
    
    
    #making Gospel subsets based on frequency
    cleaned_data_gospel1 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 1]
    cleaned_data_gospel2 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 2]
    cleaned_data_gospel3 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 3]
    cleaned_data_gospel4 = cleaned_data[cleaned_data["Frequency [Gospel]"] == 4]
    
    #now get the average MH scores for each frequency
    ave_anxiety_gospel1 = cleaned_data_gospel1["Anxiety"].mean()
    ave_dep_gospel1 = cleaned_data_gospel1["Depression"].mean()
    ave_insom_gospel1 = cleaned_data_gospel1["Insomnia"].mean()
    ave_ocd_gospel1 = cleaned_data_gospel1["OCD"].mean()
    
    ave_anxiety_gospel2 = cleaned_data_gospel2["Anxiety"].mean()
    ave_dep_gospel2 = cleaned_data_gospel2["Depression"].mean()
    ave_insom_gospel2 = cleaned_data_gospel2["Insomnia"].mean()
    ave_ocd_gospel2 = cleaned_data_gospel2["OCD"].mean()
    
    ave_anxiety_gospel3 = cleaned_data_gospel3["Anxiety"].mean()
    ave_dep_gospel3 = cleaned_data_gospel3["Depression"].mean()
    ave_insom_gospel3 = cleaned_data_gospel3["Insomnia"].mean()
    ave_ocd_gospel3 = cleaned_data_gospel3["OCD"].mean()
    
    ave_anxiety_gospel4 = cleaned_data_gospel4["Anxiety"].mean()
    ave_dep_gospel4 = cleaned_data_gospel4["Depression"].mean()
    ave_insom_gospel4 = cleaned_data_gospel4["Insomnia"].mean()
    ave_ocd_gospel4 = cleaned_data_gospel4["OCD"].mean()
    
    #create a dataframe for these values
    index = ["Classical", "Country", "EDM", "Folk", "Gospel", "Hip hop", "Jazz", "K pop", "Latin", "Lofi", 
             "Metal", "Pop", "R&B", "Rap", "Rock", "Video game music"]
    columns = ["Anxiety", "Depression", "Insomnia", "OCD"]
    
    mh_by_genre = pd.DataFrame(index=index, columns=columns)
    

    #add values
    average_anxiety = [ave_anxiety_classical4, ave_anxiety_country4, ave_anxiety_edm4,  ave_anxiety_folk4, ave_anxiety_gospel4, ave_anxiety_hiphop4, 
        ave_anxiety_jazz4, ave_anxiety_kpop4, ave_anxiety_latin4, ave_anxiety_lofi4, ave_anxiety_metal4, ave_anxiety_pop4, ave_anxiety_rnb4, 
        ave_anxiety_rap4, ave_anxiety_rock4, ave_anxiety_vgm4]
    
    average_depression = [ave_dep_classical4, ave_dep_country4, ave_dep_edm4, ave_dep_folk4, ave_dep_gospel4, ave_dep_hiphop4, ave_dep_jazz4, 
            ave_dep_kpop4, ave_dep_latin4, ave_dep_lofi4, ave_dep_metal4, ave_dep_pop4, ave_dep_rnb4, ave_dep_rap4, ave_dep_rock4, ave_dep_vgm4]
    
    average_ocd = [ave_ocd_classical4, ave_ocd_country4, ave_ocd_edm4, ave_ocd_folk4, ave_ocd_gospel4, ave_ocd_hiphop4, ave_ocd_jazz4, ave_ocd_kpop4, 
        ave_ocd_latin4, ave_ocd_lofi4, ave_ocd_metal4, ave_ocd_pop4, ave_ocd_rnb4, ave_ocd_rap4, ave_ocd_rock4, ave_ocd_vgm4]
    
    average_insomnia = [ave_insom_classical4, ave_insom_country4, ave_insom_edm4, ave_insom_folk4, ave_insom_gospel4, ave_insom_hiphop4, ave_insom_jazz4, 
            ave_insom_kpop4, ave_insom_latin4, ave_insom_lofi4, ave_insom_metal4, ave_insom_pop4, ave_insom_rnb4, ave_insom_rap4, ave_insom_rock4, 
            ave_insom_vgm4]
    
    mh_by_genre["Anxiety"] = average_anxiety
    mh_by_genre["Depression"] = average_depression
    mh_by_genre["Insomnia"] = average_insomnia
    mh_by_genre["OCD"] = average_ocd

    mh_by_genre["Effect"] = np.where(mh_by_genre["Depression"] >= 5, 1, 0)



    ####################### done replicating the filtering done above


    mood_increase_genres = mh_by_genre[mh_by_genre["Effect"] == 0]
    mood_decrease_genres = mh_by_genre[mh_by_genre["Effect"] == 1]

    increase_recommendations = mood_increase_genres.index
    decrease_recommendations = mood_decrease_genres.index

    st.markdown("Please choose a listening goal to recieve aligned genre recommendations.")
    #dropdown menu
    categories = ["Mood Increase", "Mood Decrease"]
    selected_category = st.selectbox("Choose a listening goal:", categories)

    if selected_category == "Mood Increase":
    
        #display the selected category
        st.write(f"You selected: {selected_category}")

        st.markdown("Here are your recommended genres:")
        st.write(increase_recommendations)

        #include a visualization
        # Set the plot style
        sns.set(style="whitegrid")

        # Create a figure and axis
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
            
        # Create a bar plot for each mental health measure
        sns.barplot(x=mh_by_genre.index, y='Anxiety', data=mh_by_genre, ax=axes[0, 0], palette='viridis')
        axes[0, 0].set_title('Anxiety Levels by Genre')
        axes[0, 0].set_ylabel('Anxiety Level')
        axes[0, 0].tick_params(axis='x', rotation=45)
            
        sns.barplot(x=mh_by_genre.index, y='Depression', data=mh_by_genre, ax=axes[0, 1], palette='viridis')
        axes[0, 1].set_title('Depression Levels by Genre')
        axes[0, 1].set_ylabel('Depression Level')
        axes[0, 1].tick_params(axis='x', rotation=45)
            
        sns.barplot(x=mh_by_genre.index, y='Insomnia', data=mh_by_genre, ax=axes[1, 0], palette='viridis')
        axes[1, 0].set_title('Insomnia Levels by Genre')
        axes[1, 0].set_ylabel('Insomnia Level')
        axes[1, 0].tick_params(axis='x', rotation=45)
            
        sns.barplot(x=mh_by_genre.index, y='OCD', data=mh_by_genre, ax=axes[1, 1], palette='viridis')
        axes[1, 1].set_title('OCD Levels by Genre')
        axes[1, 1].set_ylabel('OCD Level')
        axes[1, 1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
            
        #show the plot
        st.pyplot(plt)


    if selected_category == "Mood Decrease":
    
        #display the selected category
        st.write(f"You selected: {selected_category}")

        st.markdown("Here are your recommended genres:")
        st.write(decrease_recommendations)

        #include a visualization
        # Set the plot style
        sns.set(style="whitegrid")

        # Create a figure and axis
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
            
        # Create a bar plot for each mental health measure
        sns.barplot(x=mh_by_genre.index, y='Anxiety', data=mh_by_genre, ax=axes[0, 0], palette='viridis')
        axes[0, 0].set_title('Anxiety Levels by Genre')
        axes[0, 0].set_ylabel('Anxiety Level')
        axes[0, 0].tick_params(axis='x', rotation=45)
            
        sns.barplot(x=mh_by_genre.index, y='Depression', data=mh_by_genre, ax=axes[0, 1], palette='viridis')
        axes[0, 1].set_title('Depression Levels by Genre')
        axes[0, 1].set_ylabel('Depression Level')
        axes[0, 1].tick_params(axis='x', rotation=45)
            
        sns.barplot(x=mh_by_genre.index, y='Insomnia', data=mh_by_genre, ax=axes[1, 0], palette='viridis')
        axes[1, 0].set_title('Insomnia Levels by Genre')
        axes[1, 0].set_ylabel('Insomnia Level')
        axes[1, 0].tick_params(axis='x', rotation=45)
            
        sns.barplot(x=mh_by_genre.index, y='OCD', data=mh_by_genre, ax=axes[1, 1], palette='viridis')
        axes[1, 1].set_title('OCD Levels by Genre')
        axes[1, 1].set_ylabel('OCD Level')
        axes[1, 1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
            
        #show the plot
        st.pyplot(plt)
    
        
