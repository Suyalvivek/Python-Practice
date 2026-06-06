import json
book = {}
book['vivek'] = {
    'name':'vivek',
    'age':21,
    'phone':909900990,
    'address':'delhi'
}
book['yogesh'] = {
    'name':'yogesh',
    'age':25,
    'phone':90990099,
    'address':'delhi'
}
print(book)
js = json.dumps(book)
with open("./book.txt","w+") as f:
    f.write(js)
    print(type(js))
with open("./book.txt","r") as f:
    s=f.read()
    book=json.loads(s)
    print(book)
    print(type(book))
