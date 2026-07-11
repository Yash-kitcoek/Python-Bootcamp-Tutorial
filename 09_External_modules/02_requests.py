import requests

r = requests.get('https://api.github.com/users/yash-kitcoek')

print(r.text)


with open("write.txt", "w") as f:
    f.write(r.text)