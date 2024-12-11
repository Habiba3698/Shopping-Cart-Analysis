
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


df=pd.read_csv('shopping_full.csv')


# how did the sales change over the months

temp= df.groupby('order_month').agg({'total_price': 'sum'}).reset_index().sort_values(by='order_month')
fig1 = px.line(temp , x="order_month", y='total_price',color_discrete_sequence=px.colors.qualitative.G10, title='how did sales change over the months')


# is age tied to favorite color

fig2 = px.scatter(df, x='age', y='colour', title='is age tied to favorite color')

# is gender tied to favorite color

fig3 = px.scatter(df, x='gender', y='colour', title='is gender tied to favorite color')

# what is the percentage of sales per gender

fig4 = px.pie(df, values='total_price', names='gender', hole=.2, title='the percentage of sales per gender ',color_discrete_sequence=px.colors.qualitative.G10)

# what is the percentage of denims sold per state

temp= df[df['product_name']== 'Denim']

fig5 = px.pie(temp, values='total_price', names='state', hole=.2, title='the percentage of denims sold per state',color_discrete_sequence=px.colors.qualitative.G10)

# the percentage of sales per state 

fig6 = px.pie(df, values='total_price', names='state', hole=.2,title='the percentage of sales per state ', color_discrete_sequence=px.colors.qualitative.G10)

# what is the count of each product name sold?

fig7= px.histogram(df, x='product_name', hover_data= df.columns, title='Number of pieces sold for each product')

#is there a relation between size and gender?

fig8 = px.scatter(df, x='gender', y='size', title='is there a relation between size and gender?')


tab1, tab2 = st.tabs(['📈 Stats','📊 Charts'])
n = df.describe()
c = df.describe(include = 'O')

with tab1:
    col1, col2, col3 = st.columns([7,1,7])
    with col1:
        st.subheader('Numerical Statistics')
        st.dataframe(n.T, 700, 700)
    with col3:
        st.subheader('Categorical Statistics')
        st.dataframe(c, 700, 500)
        

with tab2:

    st.header("How how did the sales change over the months?")
    st.plotly_chart(fig1)


    st.header("Is age tied to favorite color?")
    st.plotly_chart(fig2)

    st.header("Is gender tied to favorite color?")
    st.plotly_chart(fig3)

    st.header("What is the percentage of sales per gender?")
    st.plotly_chart(fig4)

    st.header("What is the percentage of denims sold per state?")
    st.plotly_chart(fig5)

    st.header("What is the percentage of sales per state ?")
    st.plotly_chart(fig6)

    st.header("What is the count of each product name sold?")
    st.plotly_chart(fig7)

    st.header("Is there a relation between size and gender?")
    st.plotly_chart(fig8)

