import requests

cookie = {'visit-month':'February'}

sess = requests.session()

sess.cookies.update(cookie)

#cookie_resp = requests.get("https://httpbin.org/cookies",cookies=cookie)

cookie_resp = sess.get("https://httpbin.org/cookies")  # Using session to get cookies

print(cookie_resp.status_code)

print (cookie_resp.history) #checks for redirections   //allow_redirects = False to be used in request