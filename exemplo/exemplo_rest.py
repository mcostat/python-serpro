import requests


# pegar posts por ID
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(response)
#print(response.json())


# pegar todos os posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')

print(response)
#print(response.json())


# pegar todos os users
response = requests.get('https://jsonplaceholder.typicode.com/users')

print(response)
#print(response.json())
