#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:44:08 2019

@author: adamsiegel
"""

import requests
from bs4 import BeautifulSoup

def roster_grabber(team_name):
    #team_name format ought to be the three letter abbreviation for the team's home city, e.g. SAC, ATL, LAL
    request_string = "https://www.basketball-reference.com/teams/" + team_name + "/2019.html"
    page = requests.get(request_string).content

    soup = BeautifulSoup(page, 'html.parser')

    for tag in soup.find_all(True):
        if tag.has_attr('csk') and tag.has_attr('data-stat') and tag['data-stat'] == "player":
            tag_string = str(tag.string)
            #currently the tag_string conditional removes two-way players, will amend at some point going forward
            if (tag_string != "None"):
                print(tag_string)
            
roster_grabber("SAC")