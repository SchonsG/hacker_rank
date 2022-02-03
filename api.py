#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

import requests


def request_api(url, params, page=1):
    params = {**params, "page": page}
    header = {"Content-type": "application/json"}

    result = requests.get(url, headers=header, params=params)
    return result.json()


def sum_goals(data, team):
    goals = 0
    for keys in data:
        goals += int(keys.get(team, 0))

    return goals


def get_goals(competition, year, team):
    parameter = {"competition": competition, "year": year}
    url_match = "https://jsonmock.hackerrank.com/api/football_matches"
    tot_goals = 0

    for team_group in ["team1", "team2"]:
        params = {**parameter, team_group: team}

        response = request_api(url_match, params)
        res_data = response["data"]

        tot_goals += sum_goals(res_data, f"{team_group}goals")

        while response["total_pages"] >= response["page"]+1:
            response = request_api(url_match, params, response["page"]+1)
            tot_goals += sum_goals(response["data"], f"{team_group}goals")

    return tot_goals


def get_winner(competition, year):
    url = "https://jsonmock.hackerrank.com/api/football_competitions"
    params = {"name": competition, "year": year}

    result = request_api(url, params)

    return result["data"][0]["winner"]


def getWinnerTotalGoals(competition, year):
    winner = get_winner(competition, year)
    result = get_goals(competition, year, winner)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
