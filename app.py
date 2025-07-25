import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# st.write("Hello, Streamlit!")
st.sidebar.title("WhatsApp chat Analyzer")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:

    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert into string
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # st.dataframe(df)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('Group Notification')
    user_list.sort()
    user_list.insert(0, 'Overall')  # Add 'Overall' at the beginning of the list
    
    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    st.title('Top Statistics')

    if st.sidebar.button("Show Analysis"):
        
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        # Display the statistics in columns
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        
        with col2:
            st.header("Total Words")
            st.title(words)
        
        with col3: 
            st.header("Media Shared")
            st.title(num_media_messages)
        
        with col4: 
            st.header("Links Shared")
            st.title(num_links)

        # Monthly Timeline
        st.title('Monthly Timeline')
        timeline =  helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color = 'blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Daily Timeline
        st.title('Daily Timeline')
        daily_timeline =  helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['Only_date'], daily_timeline['message'], color = 'blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Weekly Activity
        st.title('Activity Stats')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.weekly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation = 90)
            st.pyplot(fig)
        
        with col2:
            st.header("Most Busy Month")
            busy_month = helper.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values)
            plt.xticks(rotation = 90)
            st.pyplot(fig)
        

        # Heatmap
        st.title("Weekly Activity HeatMap")
        activity_table = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(activity_table, cmap = 'magma')
        st.pyplot(fig)


        # Finding the busiest users in the group(Only Group Level)
        if selected_user == 'Overall':
            st.title("Most Busy Users")
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            
            col1, col2 = st.columns(2)

            with col1:
                # x.index is the user names(x axis)
                # x.values is the number of messages sent by each user(y axis)
                ax.bar(x.index, x.values, color = 'blue')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            
            with col2:
                new_df.index.name = 'S.No'
                new_df.index = new_df.index.astype(str)
                st.dataframe(new_df, height = 350, width=400)
                

                
        # Word Cloud
        st.title("Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most common words
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df['Word'], most_common_df['Count'], color='blue')
        st.title("Most Common Words")
        st.pyplot(fig)
        # st.dataframe(most_common_df)
        # styled_common = most_common_df.style.set_properties(**{'text-align': 'right'})
        # st.dataframe(styled_common, use_container_width=True)

        # Emoji Analysis
        emoji_df = helper.emoji_analysis(selected_user, df)
        emoji_df.index.name = 'S.No'
        emoji_df.index = emoji_df.index.astype(str)
        st.title("Emoji Analysis")
        st.dataframe(emoji_df, width=400)
        
