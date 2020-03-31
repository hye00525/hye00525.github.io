#!flask/bin/python
import sys
import nltk # is not in JavaScript
import requests
import random, json
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, Response


app = Flask(__name__)


@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Joe')

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	word = request.form['name']
	result=''
	if word:
		url_e = "http://endic.naver.com/search.nhn?query=" + word
		response = requests.get(url_e)
		soup = BeautifulSoup(response.content, "lxml")
		try:
			result += soup.find('dl', {'class':'list_e2'}).find('dd').find('span', {'class':'fnt_k05'}).get_text()
		except:
			result="It is not registered in Naver dictionary."
	else:
		result="It is not registered in Naver dictionary."

	return result


if __name__ == '__main__':
	# run!
	app.run()