
import requests
from requests import auth

r = requests.get("https://xkcd.com/353/")
print(r)
print(dir(r))
print(r.text)
print(r.status_code)
print(r.headers)
payload = {
    'count':25
}
r = requests.get("https://www.apirequest.in/api/user",params=payload)
print(r.json())
payload = {

    "brand": "LogiTech",
    "category": "Electronics",
    "created_at": "2025-03-01T12:00:00Z",
    "currency": "INR",
    "id": "P1001",
    "name": "Wireless Mouse",
    "price": 799.99,
    "rating": 4.5,
    "stock": 120

}
r = requests.post("https://www.apirequest.in/api/product",data=payload)
print(r.status_code)
print(r.json())

r = requests.get("https://www.apirequest.in/api/user",auth=('vivek','vivek123'))
print(r)