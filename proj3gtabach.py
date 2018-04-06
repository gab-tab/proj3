import sqlite3
import csv
import json



# proj3_choc.py
# You can change anything in this file you want as long as you pass the tests
# and meet the project requirements! You will need to implement several new
# functions.

# Part 1: Read data from CSV and JSON into a new database called choc.db
DBNAME = 'choc.db'
BARSCSV = 'flavors_of_cacao_cleaned.csv'
COUNTRIESJSON = 'countries.json'

conn = sqlite3.connect(DBNAME)
cur = conn.cursor()
cur.execute('Create table if not exists Countries(Id integer primary key, Alpha2 text, Alpha3 text, EnglishName text, Region text, Subregion text, Population integer, Area real)')
cur.execute('Create table if not exists Bars("Id" integer primary key, "Company" text, "SpecificBeanBarName" text, REF text, ReviewDate text, CocoaPercent real, CompanyLocation text, CompanyLocationId integer, Rating real, BeanType text, BroadBeanOrigin text, BroadBeanOriginId integer)')
conn.commit()

f=open(COUNTRIESJSON, "r")
f_contents  = f.read()
lst = json.loads(f_contents)
for item in lst:
    temp_query = "Insert into Countries (Alpha2, Alpha3, EnglishName, Region, Subregion, Population, Area) values ('" + str(item['alpha2Code']) + "', '" + str(item['alpha3Code']) + "', '" + str(item['name']) + "', '" + str(item['region']) + "', '" + str(item['subregion']) + "', '" + str(item['population']) + "', '" + str(item['area']) +"');"
    print (temp_query)
    cur.execute(temp_query)
conn.commit()
f.close()

query = '''
    SELECT *
    FROM Countries
'''
cur.execute(query)
locationdict = {}
for x in cur:
    locationdict[x[3]] = x[0]


with open(BARSCSV, "r") as csvfile:

    # If you are using sqlite3, you can take advantage of the import function which lets you import directly from the csv

    reader = csv.reader(csvfile, delimiter = ",")
    count = 0
    for dict in reader:
        if count == 0:
            count += 1
            continue
        company = row[0]
        specific_bean = row[1]
        ref = rew[2]
        review_date = row[3]
        cocoa_percent = row[4]
        location = row[5]
        if location in locationdict:
            location_id = locationdict[location]
        rating = row[6]
        bean_type = row[7]
        origin = row[8]
        if origin in locationdict:
            oritin_id = locationdict[origin]
        insert = (None, company, specific_bean, ref, review_date, cocoa_percent, location)
        statement = 'INSERT INTO "Bars"'
        statement += 'Values (?,?,?,?,?,?,?,?)'
        cur.execute(statement, inset)


# Part 2: Implement logic to process user commands
# def process_command(command):
#     if command.split()[0] == 'bars':
#         sellCountryNone
#         sourceCountryNone
#         sellregionNone
#         sourceregionNone
#         sort_by = 'Bars.Rating'
#         slicedirection = "DESC"
#         slicenumber = 20
#
#         for detail in command.split()(1:):
#             if "sellcountry" in detail:
#                 sellCountry = detail.split("-")[1]
#             elif "sourcecountry" in detail:
#                 sellRegion = detail.split("-")[1]
#             elif "sellregion" in detail:
#                 sourceregion = detail.split("-")[1]
#             elif "sourceregion" in detail:
#                 sourceregino = detail.split("-")[1]
#             elif detail = "ratings":
#                 sort_by = "Bars.Rating"
#             elif detail = "cocoa":
#                 sort_by = "Bars.CocoaPercent"
#             elif "tags" in detail:
#                 sliceDirection = "DESC"
#                 sliceNumber = detail.split("-")[1]
#
# def load_help_text():
#     with open('help.txt') as f:
#         return f.read()

# Part 3: Implement interactive prompt. We've started for you!
def interactive_prompt():
    help_text = load_help_text()
    response = ''
    while response != 'exit':
        response = input('Enter a command: ')

        if response == 'help':
            print(help_text)
            continue

# Make sure nothing runs or prints out when this file is run as a module
if __name__=="__main__":
    interactive_prompt()
