# Задание 1.
# Тесторое приложение с REST API http://pulse-rest-testing.herokuapp.com/

import requests

base_url = "http://pulse-rest-testing.herokuapp.com/"
role_dict = {
    "name": "Roland Deschain",
    "type": "The Gunslinger",
    "level": "80",
    "book": "26"
}

resp = requests.post(base_url + "roles/", data=role_dict)
req_dict = resp.json()
id = req_dict["id"]
resp = requests.get(base_url + "roles/" + str(id))
if resp.status_code == 200:
    print("Character was created and now is available here:\n" + base_url + "roles/" + str(id) + "\n")
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.get(base_url + "roles/")
character_list = resp.json()
if resp.status_code == 200:
    for character in character_list:
        if character["name"] == "Roland Deschain":
            print("Character is present in a list of characters by address:\n" + base_url + "roles/" + "\n")
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.put(base_url + "roles/" + str(id), data={"level": 88})

resp = requests.get(base_url + "roles/" + str(id))
req_dict = resp.json()
if resp.status_code == 200:
    print("Character was created and now is available here:\n" + base_url + "roles/" + str(id))
    print("It's level was changed to {}.\n".format(req_dict["level"]))
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.get(base_url + "roles/")
character_list = resp.json()
if resp.status_code == 200:
    for character in character_list:
        if character["name"] == "Roland Deschain" and character["level"] == 88:
            print("Character is present in a list of characters by address:\n" + base_url + "roles/")
            print("It's new level is {}.\n".format(character["level"]))
else:
    raise Exception("Something is wrong. Response code is:{}".format(resp.status_code))

resp = requests.delete(base_url + "roles/" + str(id))
if resp.status_code == 204:
    print("Character was deleted.")
else:
    raise Exception("Something is wrong. Response code is:{}.".format(resp.status_code))