import requests

# http://rahulshettyacademy.com
# 'visit-month'
cookie = {'visit-month': 'February'}  # common cookies/authentication/headers can be declared here.
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie,
                        timeout=1)  # timeouts to wait for response.
# print(response.history)  # 301,200 (redirects check)
print(response.status_code)

se = requests.session()  # we use session manager to manage auth/cookies...etc
se.cookies.update({'visit-month': 'February'})

res = se.get("https://httpbin.org/cookies",
             cookies={'visit-year': '2023'})  # we can pass cookies parameter as key:value dict format here as well.
print(res.text)

# Attachments sending.
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Govind\\Downloads\\testerimage.jpeg', 'rb')}
r = requests.post(url, files=files)
print(r)
print(r.text)
