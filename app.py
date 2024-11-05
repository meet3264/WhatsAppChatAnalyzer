import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)


    user_list = df['user'].unique().tolist()
    user_list.remove('group notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt ",user_list)

    if st.sidebar.button("Show analysis"):
        num_messages, words_count, num_media_msg, num_links = helper.fetchstats(selected_user,df)
        st.title("Top Statistics : ")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words_count)

        with col3:
            st.header("Shared Media")
            st.title(num_media_msg)

        with col4:
            st.header("Shared Links")
            st.title(num_links)

        #monthly timeline Analysis

        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='violet')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline analysis

        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #finding the busiest person in the group(group level)

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, df1 = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(df1)

        #wordcloud
        st.title("WordCloud")
        df_wc = helper.create_wordcloud(selected_user,df )
        fig, ax =plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        #most common words

        most_common_df = helper.most_common_words(selected_user,df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #emoji analysis
        emoji_df = helper.emoji_helper(selected_user,df)
        st.title("Emojis Analysis")
        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig,ax = plt.subplots()
            ax.pie(emoji_df[1].head(),labels = emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)