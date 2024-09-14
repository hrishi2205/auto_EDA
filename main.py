import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    activities = ["EDA", "Adding soon"]   
    choice = st.sidebar.selectbox("Select Activities", activities)

    all_columns = None

    if choice == 'EDA':
        st.title("Exploratory Data Analysis By Hrishi 22BCS15070")

        data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data, encoding='unicode_escape')

            df.dropna(axis=1, how='all', inplace=True)
            df.dropna(inplace=True)
            st.dataframe(df.head())
            
            if st.checkbox("Show Shape"):
                st.write(df.shape)

            if st.checkbox("Show Columns"):
                all_columns = df.columns.to_list()
                st.write(all_columns)

            if st.checkbox("Summary"):
                st.write(df.describe())

            if st.checkbox("Show Selected Columns"):
                selected_columns = st.multiselect("Select Columns", all_columns)
                new_df = df[selected_columns]
                st.dataframe(new_df.head())


            if st.checkbox("Pie Plot"):
                if all_columns is not None:  
                    column_to_plot = st.selectbox("Select 1 Column", all_columns)
                    pie_plot = df[column_to_plot].value_counts().head(10).plot.pie(autopct="%1.1f%%")
                    st.write(pie_plot)
                    st.pyplot()

            if st.checkbox("Bar Plot"):
                if all_columns is not None: 
                    x_column = st.selectbox("Select X-axis Column", all_columns)
                    y_column = st.selectbox("Select Y-axis Column", all_columns)
                    if x_column != y_column:
                        top_categories = df[x_column].value_counts().head(10).sort_values(ascending=False).index.tolist()
                        filtered_df = df[df[x_column].isin(top_categories)]
                        bar_plot = filtered_df.groupby(x_column)[y_column].sum().plot(kind='bar')
                        st.write(bar_plot)
                        st.pyplot()
                    else:
                        st.write("Please select different columns for X and Y axes.")

    elif choice == 'Adding soon':
        st.info('More Features will be added soon. Thanks for using - From Hrishi Yadav')

if __name__ == '__main__':
    main()
