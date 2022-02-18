import requests
import sys

sys.path.insert(0, "C:\\Users\\PK\\PycharmProjects\\APIAutomation\\config")

from configurations import *
from jsonfiles import *
from resources import *

sess = requests.session()
sess.auth = ("gocalvin", getPassword())

url = "https://api.github.com/user"
git_resp = sess.get(url)


print(git_resp.status_code)

url2 = "https://api.github.com/user/repos"

git_repos_resp = sess.get(url)