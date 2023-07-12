from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)

CREATE DATABASE web_service;

USE web_service;

CREATE TABLE user (
    id            int(10),
    email         varchar(32),
    name          varchar(64),
    password      varchar(256)
);
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/result', methods=['POST'])
# def result():
#     input_text = st.text_input('Masukkan teks:')
#     result_text = input_text.upper()
#     return render_template('result.html', result=result_text)

# if __name__ == '__main__':
#     app.run()
