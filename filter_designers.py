from linkedin_scraper import Company
from selenium import webdriver
import json

# Use this script only when lines 64-80 of company.py have been commented out

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

def companies_decoder(obj):
    if "about_us" in obj:
        company =  Company(linkedin_url=obj["linkedin_url"], name = obj["name"], about_us = obj["about_us"], website = obj["website "], headquarters=obj["headquarters"], founded = obj["founded"], industry = obj["industry"], company_type = obj["company_type"], company_size = obj["company_size"], specialties = obj["specialties"], showcase_pages = obj["showcase_pages"], affiliated_companies = obj["affiliated_companies"])
        company.employees = obj["employees"]
        return company
    return obj

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
with open('companies.json', "r") as f:
    json_data = f.read()

companies = json.loads(json_data, object_hook = companies_decoder)

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