import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib.ticker import PercentFormatter
import squarify


def app():
    st.markdown("""
         ### Segmentation Dashboard
    """)
    data_df = pd.read_pickle('Demo_Project_multi_page_dashboard_Benbhk/data/segmentation_all_df.pkl')
    seg_df = pd.read_pickle('Demo_Project_multi_page_dashboard_Benbhk/data/segmentation.pkl')
    data_df_cust = data_df.drop_duplicates(subset=['customer_ID'], keep='last')
    table_final_price = pd.pivot_table(data_df, values='final_price', index=['customer_ID'], aggfunc=np.sum)
    spend_per_purchase = pd.read_pickle('Demo_Project_multi_page_dashboard_Benbhk/data/spend_per_purchase.pkl')
    nb_of_itm_per_purchase = pd.read_pickle('Demo_Project_multi_page_dashboard_Benbhk/data/nb_of_itm.pkl')

    seg = -1

    #added
    col1, col2, col3 = st.columns((0.07,1,0.07))

    with col2:
        seg_count_df = data_df.groupby('segmentation')[['final_price']].agg('sum').reset_index()
        sizes = seg_count_df['final_price']
        labels = [f"Segment 1:\n online, young group, accessories",f"Segment 2:\n online, 96% women, cosmetics",f"Segment 3:\n 90% offline, men, clothes/shoes/accessories", f"Segment 4:\n 70% offline, premium, clothes, highest frequency", f"Segment 5:\n online, young, clothes", f"Segment 6:\n 30% offline, kitchen, high fidelity", f"Segment 7:\n online, young, clothes", f"Segment 8:\n online, young, shoes", f"Segment 9:\n 50% offline, men, high fidelity",f"Segment 10:\n online,\n midd-aged women,\n cosmetics"]
        fig, ax = plt.subplots(figsize=(15,5))
        color = ['peachpuff', 'salmon', 'palegreen', 'gold','paleturquoise', 'plum','lightgrey', 'rosybrown', 'lightseagreen', 'pink']
        ax = squarify.plot(sizes,color=color, label = labels)
        ax.axis('off')
        st.pyplot(fig)

    col0, col1, col2, col3, col4= st.columns((1,1,1,1,1))
    with col0:
        if st.button('Segment 1'):
            seg = 0
    with col1:
        if st.button('Segment 2'):
            seg = 1
    with col2:
        if st.button('Segment 3'):
            seg = 2
    with col3:
        if st.button('Segment 4'):
            seg = 3
    with col4:
        if st.button('Segment 5'):
            seg = 4

    col5, col6, col7, col8, col9 = st.columns((1,1,1,1,1))
    with col5:
        if st.button('Segment 6'):
            seg = 5
    with col6:
        if st.button('Segment 7'):
            seg = 6
    with col7:
        if st.button('Segment 8'):
            seg = 7
    with col8:
        if st.button('Segment 9'):
            seg = 8
    with col9:
        if st.button('Segment 10'):
            seg = 9


    if seg != -1:

        st.markdown("""
                ### Customer Information
            """)

        seg_0_df = seg_df[seg_df['customer_segmentation'] == seg]
        seg_0_list = seg_0_df['customer_ID'].unique().tolist()
        data_0_df = data_df[data_df['customer_ID'].isin(seg_0_list)]
        data_0_df_cust = data_0_df.drop_duplicates(subset=['customer_ID'], keep='last')
        table_final_price_0 = pd.pivot_table(data_0_df, values='final_price', index=['customer_ID'], aggfunc=np.sum)


        col1, col2, col3, col4, col5, col6 = st.columns((1,1,1,1,1,1))
        col1.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4jqDkl_5KVJ6cDu1D1ETfjDYFAkyJFgU-uA&usqp=CAU", width=50)
        col2.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuoQFSXIwwl2QDsopgs9uZG-K9trW4E8D4mA&usqp=CAU", width=25)
        col3.image("https://svgsilh.com/svg_v2/2024650.svg", width=30)
        col4.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDtJiOILri07AikNsRYouOM8wzSpGwyeAP1w&usqp=CAU", width=50)
        col5.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZJuWdgcnjUVVps2ptDXTWXZlox9doqvd4fphu4RN9b44hEba_6q8IJPyQ5qXabLagIk4&usqp=CAU",width=50)
        col6.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYI9Wis30IUMQAuF8MS9F0WqAAZAH6KbIX5TbOFWy_97Tbdo5l46lCcBNWIftNFiulduY&usqp=CAU", width=85)

        col1, col2, col3, col4, col5, col6 = st.columns((1,1,1,1,1,1))
        col1.metric("No. of Customers", len(data_0_df['customer_ID'].unique().tolist()), f"{round(data_0_df_cust['segmentation'].count()/data_df_cust['segmentation'].count(),2)*100}% of total",delta_color="off")
        col2.metric("Men",f"{round(data_0_df_cust[data_0_df_cust['gender']=='male']['gender'].count()*100/data_0_df_cust['gender'].count(),0)}%", f"{round((data_0_df_cust[data_0_df_cust['gender']=='male']['gender'].count()*100/data_0_df_cust['gender'].count())-(data_df_cust[data_df_cust['gender']=='male']['gender'].count()*100/data_df_cust['gender'].count()),1)} pp.")
        col3.metric("Women",f"{round(data_0_df_cust[data_0_df_cust['gender']=='female']['gender'].count()*100/data_0_df_cust['gender'].count(),0)}%", f"{round((data_0_df_cust[data_0_df_cust['gender']=='female']['gender'].count()*100/data_0_df_cust['gender'].count())-(data_df_cust[data_df_cust['gender']=='female']['gender'].count()*100/data_df_cust['gender'].count()),1)} pp.")
        col4.metric("Ø Age", round(data_0_df_cust['age'].mean(),1), f"{round(data_0_df_cust['age'].mean()- data_df_cust['age'].mean(),1)} years")
        col5.metric("Premium Customers", f"{round(data_0_df_cust[data_0_df_cust['premium_status']=='y']['premium_status'].count()*100/data_0_df_cust['premium_status'].count(),1)}%", f"{round((data_0_df_cust[data_0_df_cust['premium_status']=='y']['premium_status'].count()*100/data_0_df_cust['premium_status'].count()) -(data_df_cust[data_df_cust['premium_status']=='y']['premium_status'].count()*100/data_df_cust['premium_status'].count()),1)} pp.")
        col6.metric("Online Customers", f"{round(data_0_df_cust[data_0_df_cust['on_off']=='online']['on_off'].count()*100/data_0_df_cust['on_off'].count(),1)}%", f"{round((data_0_df_cust[data_0_df_cust['on_off']=='online']['on_off'].count()*100/data_0_df_cust['on_off'].count())-(data_df_cust[data_df_cust['on_off']=='online']['on_off'].count()*100/data_df_cust['on_off'].count()),1)} pp.")


        col1, col2, col3, col4 = st.columns((1,1,1,1))
        with col1:
            st.metric("Segment Fidelity", f"{round(data_0_df[data_0_df['segmentation'] == seg]['segmentation'].count()/data_0_df['segmentation'].count()*100,1)}%")
        with col2:
            st.metric("Weighted Purchase ", f"{round(data_0_df['segmentation'].count()/data_df['segmentation'].count()*100,1)}%")
        with col3:
            st.metric("Weighted Spending", f"{round(data_0_df['final_price'].sum()/data_df['final_price'].sum()*100,1)}%")
        with col4:
            st.metric("Spending Ratio", round((data_0_df['final_price'].sum()/data_df['final_price'].sum()*100)/(data_0_df_cust['segmentation'].count()/data_df_cust['segmentation'].count()*100),1))


        st.write("")
        st.write("")

        st.markdown("""
            ### Customer Behavior
        """)
        col1, col2, col3, col4, col5 = st.columns((1,1,1,1,1))
        col1.metric("Ø No. of Purchases",round(data_0_df.drop_duplicates(subset=['date','customer_ID'], keep='last').groupby('customer_ID')[['date']].agg('count').reset_index()['date'].mean(),1),round((data_0_df.drop_duplicates(subset=['date','customer_ID'], keep='last').groupby('customer_ID')[['date']].agg('count').reset_index()['date'].mean())-(data_df.drop_duplicates(subset=['date','customer_ID'], keep='last').groupby('customer_ID')[['date']].agg('count').reset_index()['date'].mean()),1))
        col2.metric("Ø Item Spend", f"{round(data_0_df['final_price'].mean(),1)} HKD",f"{round(data_0_df['final_price'].mean()-data_df['final_price'].mean(),1)} HKD")
        col3.metric("Ø Basket Size", round(nb_of_itm_per_purchase[nb_of_itm_per_purchase['customer_ID'].isin(seg_0_list)]['money_spend'].mean(),1),f"{round(nb_of_itm_per_purchase[nb_of_itm_per_purchase['customer_ID'].isin(seg_0_list)]['money_spend'].mean()-nb_of_itm_per_purchase['money_spend'].mean(),1)}")
        col4.metric("Ø Basket Spend", f"{round(spend_per_purchase[spend_per_purchase['customer_ID'].isin(seg_0_list)]['money_spend'].mean(),1)} HKD", f"{round(spend_per_purchase[spend_per_purchase['customer_ID'].isin(seg_0_list)]['money_spend'].mean()-spend_per_purchase['money_spend'].mean(),1)} HKD")
        col5.metric("Median Customer Spend", f"{table_final_price_0['final_price'].quantile(.5)} HKD", f"{round(table_final_price_0['final_price'].quantile(.5)-table_final_price['final_price'].quantile(.5),1)} HKD")

        st.write("")
        st.write("")

        st.markdown("""
            ### About Product
        """)

        col1,col2= st.columns((1,1))
        with col1:
            data = data_0_df.groupby('product_cat')[['final_price']].agg('count').reset_index()
            data = data.sort_values(by='final_price', ascending=False)
            data['percentage'] = data['final_price']/ data['final_price'].sum()
            data = data[0:5]
            fig, ax = plt.subplots(figsize=(5,3))
            palette = sns.color_palette("Blues_d")
            palette.reverse()
            ax = sns.barplot(palette=palette,data=data, y='product_cat', x='percentage', ax=ax, order=data['product_cat'])
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.set_title('Top5 Purchases by Product Category', fontweight="bold", fontsize=16)
            plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
            sns.despine(left=True, bottom=True)
            st.pyplot(fig)

        with col2:
            data = data_0_df.groupby('product_cat')[['final_price']].agg('sum').reset_index()
            data = data.sort_values(by='final_price', ascending=False)
            data['final_price'] = data['final_price']/1000
            data['percentage'] = data['final_price']/ data['final_price'].sum()
            data = data[0:5]
            fig, ax = plt.subplots(figsize=(5,3))
            palette = sns.color_palette("Blues_d")
            palette.reverse()
            ax = sns.barplot(palette=palette,data=data, y='product_cat', x='percentage', ax=ax, order=data['product_cat'])
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.set_title('Top5 Revenue by Product Category', fontweight="bold", fontsize=16)
            plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
            sns.despine(left=True, bottom=True)
            st.pyplot(fig)


        st.write("")
        st.write("")

        st.markdown("""
            ### About Vendor
        """)

        col1,col2= st.columns((1,1))
        with col1:
            data = data_0_df.groupby('vendor_cat')[['final_price']].agg('count').reset_index()
            data = data.sort_values(by='final_price', ascending=False)
            data['percentage'] = data['final_price']/ data['final_price'].sum()
            data = data[0:5]
            fig, ax = plt.subplots(figsize=(5,3))
            palette = sns.color_palette("Blues_d")
            palette.reverse()
            ax = sns.barplot(palette=palette,data=data, y='vendor_cat', x='percentage', ax=ax, order=data['vendor_cat'])
            ax.set_ylabel('')
            ax.set_xlabel('')
            ax.set_title('Top5 Purchases by Vendor Category', fontweight="bold", fontsize=16)
            plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
            sns.despine(left=True, bottom=True)
            st.pyplot(fig)

        with col2:
            data = data_0_df.groupby('vendor_cat')[['final_price']].agg('sum').reset_index()
            data = data.sort_values(by='final_price', ascending=False)
            data['final_price'] = data['final_price']/1000
            data['percentage'] = data['final_price']/ data['final_price'].sum()
            data = data[0:5]
            fig, ax = plt.subplots(figsize=(5,3))
            palette = sns.color_palette("Blues_d")
            palette.reverse()
            ax = sns.barplot(palette=palette,data=data, y='vendor_cat', x='percentage', ax=ax, order=data['vendor_cat'])
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.set_title('Top5 Revenue by Vendor Category', fontweight="bold", fontsize=16)
            plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
            sns.despine(left=True, bottom=True)
            st.pyplot(fig)
