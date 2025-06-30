from datetime import datetime
import requests

# =============================
# 🚨 Fill in your own credentials before running
# =============================
GRAPH_ID = ""      # e.g., "graph1"
USERNAME = ""      # e.g., "yourusername"
TOKEN = ""         # e.g., "yourtoken"

HEADER = {
    "X-USER-TOKEN": TOKEN
}

# ========== Create a Pixela user (run only once) ==========
# pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ========== Create a graph (run only once) ==========
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADER)
# print(response.text)

# ========== Post a pixel ==========
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
TODAY = datetime.now().strftime("%Y%m%d")

post_request_body = {
    "date": TODAY,
    "quantity": "7.8",  # Change this to log a different value
}

response = requests.post(url=post_pixel_endpoint, json=post_request_body, headers=HEADER)
print(response.text)