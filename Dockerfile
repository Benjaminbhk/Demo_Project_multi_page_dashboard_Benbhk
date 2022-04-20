FROM python:3.8.6-buster

COPY . /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD streamlit run Demo_Project_multi_page_dashboard_Benbhk/app.py
