import requests
import mechanize
from bs4 import BeautifulSoup


class Attack:

	def __init__(self, url):
		self.url = url
		self.request = requests.get(url)

	def form(self):
		parseHTML = BeautifulSoup(self.request.text, 'html.parser')
		html_form = parseHTML.form
		return html_form

	def input_field_names(self, html_form):
		inputs = html_form.find_all('textarea')
		inputFieldNames = []
		for items in inputs:
		    if items.has_attr('name'):
		        inputFieldNames.append(items['name'])

		return inputFieldNames

	def run(self, payload):
		form = self.form()
		print('Your form is', form)
		field_names = self.input_field_names(form)
		form_submit = mechanize.Browser()
		form_submit.open(self.url)
		form_submit.select_form(form.get('name'))

		form_submit.form[field_names[0]] = payload
		for i in range(1,len(field_names)):
		    form_submit.form[field_names[i]] = "Test from server"

		form_submit.submit()

		final_result = form_submit.response().read().decode()

		is_vulnerable = bool(final_result.find('&lt;script&gt;') > 0)
		return is_vulnerable