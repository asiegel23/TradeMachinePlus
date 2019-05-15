import requests
from bs4 import BeautifulSoup

def get_team_salary_info(team_name):
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

    team_salary = 0
    
    for key in player_salary_dict:
        salary = player_salary_dict[key]
        salary_string = str(salary)[1:].replace(',', '')
        salary_number = int(salary_string)
        
        team_salary += salary_number

    salary_cap = 101869000
    luxury_tax_cap = 123733000

    cap_space = salary_cap - team_salary
    practical_space = luxury_tax_cap - team_salary
    
    team_salary_string = "$" + "{:,}".format(team_salary)
    cap_space_string = "$" + "{:,}".format(cap_space)
    practical_space_string = "$" + "{:,}".format(practical_space)

    print(team_name + "'s Salary is: " + team_salary_string)
    print(team_name + "'s Cap Space is: " + cap_space_string)
    print(team_name + "'s Practical Cap Space is: " + practical_space_string)

get_team_salary_info("DAL")
get_team_salary_info("DET")
