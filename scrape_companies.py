from linkedin_scraper import actions, Company
from selenium import webdriver
import time
import json

class RelevantCompany:
    name = None
    designers = []
    about_us = None
    size = None

    def __init__(self, name = None, about_us = None, size = None, designers = []):
        self.name = name
        self.designers = designers
        self.about_us = about_us
        self.size = size

class Designer:
    name = None
    designation = None
    linkedin_url = None
    company = None
    about_us = None
    size = None
    def __init__(self, name = None, designation = None, linkedin_url = None, size = None, about_us = None, company = None):
        self.name = name
        self.designation = designation
        self.about_us = about_us
        self.company = company
        self.linkedin_url = linkedin_url
        self.size = size

def dumper(obj):
    if isinstance(obj, Company):
        return { "linkedin_url": obj.linkedin_url, "name" : obj.name,"about_us" : obj.about_us,"website": obj.website,"headquarters" : obj.headquarters,"founded" : obj.founded,"industry" : obj.industry,"company_type" : obj.company_type,"company_size" : obj.company_size,"specialties" : obj.specialties,"showcase_pages" : obj.showcase_pages,"affiliated_companies" : obj.affiliated_companies, "employees": obj.employees}
    if isinstance(obj, Designer):
        return {"name": obj.name, "linkedin_url": obj.linkedin_url, "designation": obj.designation, "company": obj.company, "size": obj.size, "about_us": obj.about_us}
    try:
        return obj.toJSON()
    except:
        try:
            return obj.__dict__
        except:
            return "unnecessary"

driver = webdriver.Chrome("./chromedriver")

email = "aryaman_khandelwal@yahoo.com"
password = "dhinkachika2000"
actions.login(driver, email, password)
time.sleep(0.5)


company_urls = [
"https://www.linkedin.com/company/pytorch-lightning/",
"https://www.linkedin.com/company/paytrix/",
"https://www.linkedin.com/company/lithoscarbon/",
"https://www.linkedin.com/company/gomomento/",
"https://www.linkedin.com/company/mintlify/",
"https://www.linkedin.com/company/collectableapp/",
"https://www.linkedin.com/company/miferia/",
"https://www.linkedin.com/company/marriagepact/",
"https://www.linkedin.com/company/reserv-ai/",
"https://www.linkedin.com/company/arc-tech-inc/",
"https://www.linkedin.com/company/pleo-company/",
"https://www.linkedin.com/company/decodable/",
"https://www.linkedin.com/company/column-tax/",
"https://www.linkedin.com/company/tryaqueduct/",
"https://www.linkedin.com/company/cofactr/",
"https://www.linkedin.com/company/disclo/",
"https://www.linkedin.com/company/palettehq/",
"https://www.linkedin.com/company/zenlytic/about/",
"https://www.linkedin.com/company/feathery-forms/",
"https://www.linkedin.com/company/cogsyapp/",
"https://www.linkedin.com/company/smallstep/",
"https://www.linkedin.com/company/bankwithrelay/",
"https://www.linkedin.com/company/therightfoot/",
"https://www.linkedin.com/company/paraficapital/",
"https://www.linkedin.com/company/akkio/",
"https://www.linkedin.com/company/parative-hq/",
"https://www.linkedin.com/company/usevesta/",
"https://www.linkedin.com/company/truvideo/",
"https://www.linkedin.com/company/topographyhealth/",
"https://www.linkedin.com/company/argylesystems/"
]

companies = []
for url in company_urls:
    try:
        current = Company(url, driver = driver, close_on_complete = False)
        companies.append(current)
    except: 
        continue


json_data = json.dumps(companies, default = dumper)

with open("companies.json", "w") as outfile:
    outfile.write(json_data)

relevant_companies = []
all_designers = []
for company in companies:
    designers = []
    for employee in company.employees:
        if employee:
            if "design".casefold() in employee["designation"].casefold():
                designers.append(employee)
                designer = Designer(name = employee["name"], designation=employee["designation"], linkedin_url=employee["linkedin_url"], size = company.company_size, about_us = company.about_us, company = company.name)
                all_designers.append(designer)
    if len(designers) > 0:
        relevant_companies.append(RelevantCompany(company.name, company.about_us, company.company_size, designers))
            
relevant_json_data = json.dumps(relevant_companies, default = dumper)
designers_json_data = json.dumps(all_designers, default = dumper)

with open("relevant_companies.json", "w") as outfile:
    outfile.write(relevant_json_data)

with open("designers.json", "w") as outfile:
    outfile.write(designers_json_data)