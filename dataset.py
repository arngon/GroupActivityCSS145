
import pandas as pd
import numpy as np
import os
import squarify
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from wordcloud import WordCloud
from io import StringIO
from mpl_toolkits.mplot3d import Axes3D

# Mount Google Drive
# drive.mount('/content/drive')

# Read file
df = pd.read_csv("laptop_price - dataset.csv")

# Create a Streamlit app
st.title("Laptop Market Analysis")



st.markdown("""

 Group 8 - BM4:
            
     Gonzales, Arnold
     Oalican, Maria Junella May
     Paz, Cedric Anthony
     San Miguel, Ian Rafael
     Zuniga, Danilo Raqui
            
    Original file is located at
    https://colab.research.google.com/drive/13_qN4ypZnJt61F-fbgDKfVn-hAcp4IqG

""")



# Data Table
st.subheader("Data Table")
st.write(df.head())

# Info
buffer = StringIO()
df.info(buf=buffer)
df_info_as_string = buffer.getvalue()
st.subheader("Data Info")
st.text(df_info_as_string)

# Describe
st.subheader("Data Description")
st.write(df.describe())

# Sum
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Total company
st.subheader("Total Companies")
st.write("The number of brands in Company column is", df['Company'].nunique())
brand_counts = df['Company'].value_counts()
st.write("There are {} unique brands in the dataset, including:".format(len(brand_counts)))
st.write(brand_counts)

# Scatter
st.subheader("Scatter Plot")
st.markdown("""
 The Scatter plot here shows the average purchase price and weight of Laptops that are being sold in the market, The average price of a laptop is around 700-2000 euros, and weight around 1.15-2.5KG.
 """)
fig, ax = plt.subplots()
ax.scatter(df['Weight (kg)'], df['Price (Euro)'], s=32, alpha=.8)
ax.spines[['top', 'right',]].set_visible(False)
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('Price (Euro)')
ax.set_title('Weight and Price')
st.pyplot(fig)

# Pie Chart
 
st.subheader("Pie Chart")

st.markdown("The Pie Chart here shows the Product and Product Count, the average product count is about 12 with the Aspire 3, EliteBook 840, and the Lattitude 5580. The best selling laptop here is the Dell XPS 13 with about 30 sales.")


 
Product = df.Product.value_counts().reset_index(name='Product_count').iloc[:20]
fig = px.pie(
    data_frame=Product,
    names='Product', values='Product_count',
    hole=.1,
    color_discrete_sequence=px.colors.sequential.RdBu,
    height=500, width=1000,
)
fig.update_traces(textposition='inside', textinfo='label+value')
st.plotly_chart(fig)

# Bar
 
st.subheader("Bar Graph")


st.markdown("The Bar Graph shows the TypeName of Laptops, Ultrabooks and Gaming Laptops has the average of 200, while Notenook laptops has the highest, which has 700.")

 
fig, ax = plt.subplots()
df.groupby('TypeName').size().plot(kind='barh', ax=ax, color=sns.palettes.mpl_palette('Dark2'))
ax.spines[['top', 'right',]].set_visible(False)
ax.set_xlabel('Frequency')
st.pyplot(fig)

# Histogram
 
st.subheader("Histogram")


st.markdown("The Histogram here shows the average weight of 250 laptops is 2.1 to 2.3KG.")

fig, ax = plt.subplots()
df['Weight (kg)'].plot(kind='hist', bins=20, edgecolor='black', ax=ax)
ax.spines[['top', 'right',]].set_visible(False)
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('Frequency')
ax.set_title('Weight (kg)')
st.pyplot(fig)

# Line

st.subheader("Line Graph")

st.markdown("The Line chart here shows the average RAM(GB) of each laptop that are available in the market, about 17-35 laptops has about 8-16GB of RAM.")


fig, ax = plt.subplots()
df['RAM (GB)'].plot(kind='line', ax=ax)
ax.spines[['top', 'right']].set_visible(False)
ax.set_ylabel('RAM (GB)')
ax.set_xlabel('Frequency')
ax.set_title('RAM (GB)')
st.pyplot(fig)

# Candle Stick

st.subheader("Candle Stick")


st.markdown("The Candle Stick here shows the average price of laptops from each of the 19 companies that are listed in this graph, 13 companies has a average listed price of 700-2100 euros.")


fig, ax = plt.subplots()
df.boxplot(column='Price (Euro)', by='Company', ax=ax, figsize=(12, 6), rot=45)
ax.set_xlabel('Company')
ax.set_ylabel('Price (Euro)')
ax.set_title('Distribution of Laptop Prices by Company')
st.pyplot(fig)

# Bubble Chart
 
st.subheader("Bubble Chart")


st.markdown("Based on the graph, most laptops are set to have around 2.0 - 3.0 GHz CPUs. While it is known that the higher the price, the better the product, it is also important to take note of every detail before purchase. Such as the laptop with the price of around 6000EU, it is the most expensive one in the list but it cannot be said that it is the best laptop there is in the list. There are laptops around 2000EU - 4000EU who can beat the $6000 laptop in some other aspects.")


fig, ax = plt.subplots()
ax.scatter(df['CPU_Frequency (GHz)'], df['Price (Euro)'], s=df['RAM (GB)'] * 20, alpha=0.5, c='blue')
ax.set_xlabel('CPU Frequency (GHz)')
ax.set_ylabel('Price (Euro)')
ax.set_title('Bubble Chart: CPU Frequency vs Price (Bubble Size = RAM)')
st.pyplot(fig)


# Tree Map
 
st.subheader("Treemap")


st.markdown("This chart determines which brands or companies are the most in-demand based on the total price of laptops manufactured by the company. To dig deeper, the ones which are occupying the most space in the graph are the companies that have manufactured various laptop models, and the overall prices of those models are what make up their sizes in the graph. The leading brands based on the graph are Lenovo, HP, Asus, and Dell as the biggest one among the selection.")


company_prices = df.groupby('Company')['Price (Euro)'].sum().reset_index()
fig, ax = plt.subplots()

squarify.plot(sizes=company_prices['Price (Euro)'], label=company_prices['Company'],alpha=0.8)

st.pyplot(plt)
plt.clf()

# Violin Plot
 
st.subheader("Violin Plot")

st.markdown("This graph the prices of laptop models within a certain brand or manufacturer. The graph shows that most laptop prices are around 1000EU - 2000EU. Among the selection of laptop brands, the manufacturer that has the most amount of manufactured models is Razer given it's significantly larger size compared to others. Razer also has the most expensive laptop model worth around 8000EU, while other manufacturers often top it off at around 6000EU.")


fig, ax = plt.subplots(figsize=(12, 6))
sns.violinplot(x='Company', y='Price (Euro)', data=df, hue='Company', palette='Set2', inner='quartile')
ax.set_xlabel('Company')
ax.set_ylabel('Price (Euro)')
ax.set_title('Violin Plot: Laptop Prices by Company')
ax.tick_params(axis='x', labelrotation=45)
st.pyplot(fig)

# Word Cloud
 
st.subheader("Word Cloud")


st.markdown("Word Cloud here shows the most common laptops and specs that are bought in the market, Inspiron, Lattitude, ThinkPad, ProBook and EliteBook are the most common laptops while, 4GB, 8GB and 1TB are the common configurations of the laptops.")


text_data = ' '.join(df['Product'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text_data)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')  # Turn off the axis
ax.set_title('Word Cloud: Laptop Products')
st.pyplot(fig)

 
st.subheader("Conclusion")

st.markdown(""""

The analysis of the laptop market reveals some interesting trends and consumer preferences. The scatter plot shows that most laptops are priced between €700 and €2000, which indicates that buyers are willing to spend on quality devices. People also seem to prefer lightweight laptops, with weights ranging from 1.15 kg to 2.5 kg, making them easy to carry around. The pie chart highlights that popular models like the Aspire 3, EliteBook 840, and Latitude 5580 sell about 12 units on average, while the Dell XPS 13 is a standout, racking up around 30 sales. The bar graph shows that Ultrabooks and Gaming Laptops average around 200 units sold, but Notebook laptops are the clear favorites, with about 700 sales, suggesting consumers are leaning toward versatile and budget-friendly options. Looking at the data further, the histogram indicates that most laptops weigh between 1.25 kg and 2.75 kg, which balances portability and performance well. The line chart reveals that many laptops come with 8 GB to 16 GB of RAM, showing that people are prioritizing performance for tasks like multitasking. The candlestick chart shows that 13 out of 19 brands offer laptops priced between €700 and €2100, pointing to a competitive market. The bubble chart graph shows that most laptops are set to have around 2.0 - 3.0 GHz CPUs, and can cost as much as €6000, But €2000- €4000 can be beat the €6000 one in someaspects. The tree map illustrates which brands are in demand, with Lenovo, HP, Asus, and Dell taking up the most space, likely because of their wide range of models. The Violin plot depicts that most laptops are priced around €1000-€2000, and tops out at around €8000 from Razer. Finally, the word cloud highlights popular models and specifications, like Inspiron, Latitude, and common configurations of 4GB, 8GB, and 1TB. Overall, the data suggests that both budget-friendly and high-performance laptops have a strong market presence, with brands that focus on quality and value likely to do well.

""")

 
