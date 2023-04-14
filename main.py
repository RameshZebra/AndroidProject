import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

page_id = "269322097"
api_token = "Mjk0MTkzMzA4MjQ0Oj1IhhKalaA1ay1qYxIm0plR79fG"
url = f"https://confluence.zebra.com//rest/api/content/{page_id}?expand=body.view"
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.get(url, headers=headers)
head = ["Key", "Summary", "Due"]
result = []
final = []

if response.status_code == 200:
    page_data = response.json()
    d= page_data["body"]["view"]["value"]
    soup = BeautifulSoup(d, "html.parser")
    table = soup.find("table", {"class": "aui"})
    i = ""
    for link in table.find_all("td"):
        i = (link.text).replace('\n','')
        result.append(i.replace(" ",""))

    for j in range(0,len(result), 3):
        inter = []
        for k in range(0,3):
            inter.append(result[j+k])
        final.append(inter)

    print(tabulate(final, headers=head, tablefmt="simple"))

else:
    print("Error retrieving page:", response.status_code)
