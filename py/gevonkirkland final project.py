import requests
first_name = input("First Name: ") 
last_name = input("Last Name: ") 
url = "https://api.chucknorris.io/jokes/random"
params = {"limitTo" : "[nerdy]", 
          "firstName" : first_name,
          "lastname" : last_name}  
response = requests.get(url)
joke = response.json() ["value"]
print(joke) 
