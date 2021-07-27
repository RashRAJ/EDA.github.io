import streamlit as st
import sweetviz as sv
import numpy as np
import pandas as pd
import codecs


from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components
from PIL import Image

#side bar
with st.sidebar.header("MENU"):
    menu = ["Home","Pandas Profile","Sweetviz","About"]
    choice = st.sidebar.selectbox(" ",menu)

with st.sidebar.subheader("Upload File"):
    uploaded_file = st.sidebar.file_uploader(" ", type=["csv", "xlxs"])

with st.sidebar.subheader("File Type"):
    with st.sidebar.beta_container():
        file_type = st.radio(' ', ['CSV File', 'Excel File'])


def st_display_sweetviz(report_html, width=1100, height=1000):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, width=width, height=height, scrolling=True)



def main():

    if choice == "Home":
        st.header('**Welcome !**')
        video_file = open("Octo.mp4", 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif choice == 'Pandas Profile':
        st.header('**Automated EDA with pandas profile**')
        st.write("---")
        if uploaded_file is not None:
            @st.cache
            def load_data():
                if file_type == "CSV File":
                    data = pd.read_csv(uploaded_file, encoding='cp1252')
                else:
                    data = pd.read_excel(uploaded_file)
                return data

            df = load_data()
            report = ProfileReport(df, explorative=True)
            st.header("**input data**")
            st.table(df.head())
            st.write("---")
            st.header("**Generated Report**")
            st_profile_report(report)
            

        else:
            #st.markdown('**APP DEMO**')
            
            st.subheader('No data?')
            st.subheader('Generate report using synthetic data')
            if st.button('Demo app'):
                @st.cache
                def load_syn_data():
                    a = pd.DataFrame(np.random.rand(100, 5),columns=['a', 'b', 'c', 'd', 'e'])
                    return a
                df = load_syn_data()
                report = ProfileReport(df, explorative=True)
                st.header('**Input Data**')
                st.write('---')
                st.table(df.head())
                st.header('**Generated Report**')
                st.write('---')
                st_profile_report(report)

    elif choice == "Sweetviz":
        st.header("**Automated EDA with Sweetviz**")
        st.write('---')
        if uploaded_file is not None:
            @st.cache
            def load_data():
                if file_type == "CSV File":
                    data = pd.read_csv(uploaded_file, encoding='cp1252')
                else:
                    data = pd.read_excel(uploaded_file)
                return data
            df = load_data()
            st.table(df.head())
            if st.button('Generate sweetviz report '):
                st.subheader('Sweetviz Report')
                st.write('---')
                report = sv.analyze(df)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")

        else:
            st.subheader('No data?')
            st.subheader('Generate report using synthetic data')
            if st.button('Demo app'):
                @st.cache
                def load_syn_data():
                    a = pd.DataFrame(np.random.rand(100, 5),columns=['a', 'b', 'c', 'd', 'e'])
                    return a
                df = load_syn_data()
                st.write(df)
                st.write('')
                #if st.button('Generate sweetviz report '):
                st.subheader('Sweetviz Report')
                st.write('---')
                report = sv.analyze(df)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")

        






if __name__ == '__main__':
	main()