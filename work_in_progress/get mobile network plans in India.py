    # This script fetches all the mobile network plans of all the operators in all the states in India. You can compare rates offered by operators across different states from one single csv file.
    
    import requests
    from bs4 import BeautifulSoup
    import os
    from selenium import webdriver
    driver = webdriver.Chrome()
    url='https://www.mobikwik.com/'
    driver.get(url)
    el = driver.find_element_by_css_selector(".check-plans.ng-scope") 
    el.click() #Click on browse plans on home page
     
     
    # In[ ]:
     
    # Fetch the html
    html = driver.page_source
     
    # Create a parser using beautifulSoup library
    soup = BeautifulSoup(html)
     
     
    # In[ ]:
     
    # Fetch the required element
     
    browse_plans = soup.findAll('dl', class_ = ' extraDefault customDropDown')
    operators = browse_plans[0].findAll('li')
    operator_list = [] #List of operators
    for o in operators:
        operator_list.append(o.span.text)
     
    del operator_list[0]
     
     
    state_list = browse_plans[2].findAll('li')
    states = [] #List of states
    for s in state_list:
        states.append(s.span.text)
        
    plans_types = browse_plans[3].findAll('li')
    plan_types = [] #List of all the plans
    for pt in plans_types:
        plan_types.append(pt.span.text)
     
     
    # In[ ]:
     
    # Create a csv file with the header
     
    import csv
    import re
    csvfile = open('network_operators.csv', 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['Operator'] + ['Circle'] + ['Plan'] + ['Denomination'] + ['Description'] + ['Validity'] + ['Talktime'])
     
     
    # In[ ]:
     
    #Iterate over all the operators, states and plans.
    # Click on each dropdown menu
    #Fetch the source html
    #Parse the html
    #Write the data in csv file
    for op in operator_list:
        for state in states:
            for plan in plan_types:
                arrow = driver.find_element_by_xpath('/html/body/div[3]/div[3]/section/div/div[1]/dl[1][@class=" extraDefault customDropDown" and @selected-value="view.operator"]')
                arrow.click()
                driver.find_element_by_xpath("/html/body/div[3]/div[3]/section/div/div[1]/dl[1]/dd/ul/li/span[contains(text(), '"+op+"')]").click()
                arrow = driver.find_element_by_xpath('/html/body/div[3]/div[3]/section/div/div[1]/dl[3][@class=" extraDefault customDropDown" and @selected-value="view.circle"]')
                arrow.click()
                driver.find_element_by_xpath("/html/body/div[3]/div[3]/section/div/div[1]/dl[3]/dd/ul/li/span[contains(text(), '"+state+"')]").click()
                arrow = driver.find_element_by_xpath('/html/body/div[3]/div[3]/section/div/div[1]/dl[4][@class=" extraDefault customDropDown" and @selected-value="view.planType"]')
                arrow.click()
                driver.find_element_by_xpath("/html/body/div[3]/div[3]/section/div/div[1]/dl[4]/dd/ul/li/span[contains(text(), '"+plan+"')]").click()
                html = driver.page_source
                soup = BeautifulSoup(html)
                allplans = soup.findAll('div', class_ = 'wrpr')
                allplan_amount = soup.find_all(attrs={"data-ng-repeat": "plan in plans | orderBy:'amount'"})
                if(len(allplan_amount) >=1):
                    denomination = allplan_amount[0].span.text
                    denomination = re.findall(r'\d+', denomination)[0]
                    validity = allplan_amount[0].i.text
                    description = allplan_amount[0].find(attrs={"data-ng-bind": "plan.planDescription"}).text
                    talktime = allplan_amount[0].em.text.replace("₹ ", "")
                    talktime = re.findall(r'\d+', talktime)[0]
                    writer.writerow([op, state, plan, denomination, description, validity, talktime])
                else:
                    writer.writerow([op, state, plan, 'nil', 'nil', 'nil', 'nil'])
     
     
    # In[ ]:
     
    driver.close # Close the driver
    csvfile.close() # Close the file
