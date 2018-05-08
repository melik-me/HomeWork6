# Задание 1.
# Тесторое приложение с REST API http://pulse-rest-testing.herokuapp.com/

import requests

base_url = "http://pulse-rest-testing.herokuapp.com/"
book_dict = {
    "title": "The Dark Tower",
    "author": "Stephen King"
}

resp = requests.post(base_url + "books/", data=book_dict)
req_dict = resp.json()
id = req_dict["id"]
resp = requests.get(base_url + "books/" + str(id))
if resp.status_code == 200:
    print("Book was created and now is available here:\n" + base_url + "books/" + str(id) + "\n")
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.get(base_url + "books/")
book_list = resp.json()
if resp.status_code == 200:
    for book in book_list:
        if book["title"] == "The Dark Tower":
            print("Book is present in a list of books by address:\n" + base_url + "books/" + "\n")
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.put(base_url + "books/" + str(id), data={"author": "King of Horror"})

resp = requests.get(base_url + "books/" + str(id))
req_dict = resp.json()
if resp.status_code == 200:
    print("Book was created and now is available here:\n" + base_url + "books/" + str(id))
    print("It's author was changed to {}.\n".format(req_dict["author"]))
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.get(base_url + "books/")
book_list = resp.json()
if resp.status_code == 200:
    for book in book_list:
        if book["title"] == "The Dark Tower" and book["author"] == "King of Horror":
            print("Book is present in a list of books by address:\n" + base_url + "books/")
            print("It's new author is {}.\n".format(book["author"]))
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.delete(base_url + "books/" + str(id))
if resp.status_code == 204:
    print("Book was deleted.")
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))