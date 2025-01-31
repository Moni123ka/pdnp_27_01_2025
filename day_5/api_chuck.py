import requests

# pip install requests
url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>

print(response.text)

data = response.json()

# wypisze klucze
for k in data:
    print(k)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(data['value'])
# Chuck Norris' idea of fast food is chasing down a Cheetah and cooking to up on his BBQ.
print(data['icon_url'])  # https://api.chucknorris.io/img/avatar/chuck-norris.png
response_img = requests.get(data['icon_url'])
with open('icona.jpg', "wb") as f:
    f.write(response_img.content)
print("Zdjęcie zapisane")
