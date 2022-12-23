import datetime
import requests
USER_NAME = "jarngalrahul"
TOKEN = "lkTLO409Yelko9ijl2390ejTJfk0"
url_endpoint = "https://pixe.la/v1/users"
users_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# ----------------- Setting up a new account------------------#

# response = requests.post(url=url_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{url_endpoint}/{USER_NAME}/graphs"
graph_name = "graph1"
graph_config = {
    "id": graph_name,
    "name": "Commits-per-day",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# ------------------------Creating a pixel graph---------------------#

# post_response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)

# ------------------------Adding a pixel data---------------------#
cur_date = "".join(str(datetime.date.today()).split("-"))
graph_edit_endpoint = f"{url_endpoint}/{USER_NAME}/graphs/{graph_name}"
pixel_data = {
    "date": cur_date,
    "quantity": input("How many commits you made today?"),
}
post_response = requests.post(
    url=graph_edit_endpoint, json=pixel_data, headers=headers)
print(post_response.text)
# --------------Update a pixel------------------#

# update_endpoint = f"{url_endpoint}/{USER_NAME}/graphs/{graph_name}/{cur_date}"
# updated_pixel_data = {
#     "quantity": "10"
# }
# put_response = requests.put(
#     url=update_endpoint, json=updated_pixel_data, headers=headers)
# print(put_response.text)


# --------------Deleting a pixel------------------#

# deleting_endpoint = f"{url_endpoint}/{USER_NAME}/graphs/{graph_name}/{cur_date}"
# delete_reponse = requests.delete(url=deleting_endpoint, headers=headers)
# print(delete_reponse.text)
