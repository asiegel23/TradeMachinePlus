import requests
from bs4 import BeautifulSoup

def get_player_salaries(team_name):
    player_salary_dict = {}
    salaries = []
    player_tags = []
    request_string = "https://www.basketball-reference.com/contracts/" + team_name + ".html"
    page = requests.get(request_string).content

    soup = BeautifulSoup(page, 'html.parser')

    for tag in soup.find_all(True):
        if tag.has_attr('csk') and tag.has_attr('data-stat') and tag['data-stat'] == "player":
            a = tag.find('a')
            a_str = str(a['href'])
            player_tag = a_str[9:-5]
            player_tags.append(player_tag)
        if tag.has_attr('csk') and tag['data-stat'] == "y1":
            salary = tag.string
            salaries.append(salary)

    count = 0

    while count < len(salaries):
        player_salary_dict[str(player_tags[count])] = salaries[count]
        count += 1

    for key, val in player_salary_dict.items():
        print(key + "---" + val)


get_player_salaries("SAC")
