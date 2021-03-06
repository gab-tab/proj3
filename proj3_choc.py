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

try:
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
except Error as e:
    print(e)
cur.execute('DROP TABLE IF EXISTS "Countries"')

statement = """
    CREATE TABLE 'Countries' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'Alpha2' TEXT,
        'Alpha3' TEXT,
        'EnglishName' TEXT,
        'Region' TEXT,
        'Subregion' TEXT,
        'Population' INTEGER,
        'Area' REAL
        );
    """
cur.execute(statement)
conn.commit()

user_input = input('Countries table exsits. Delete? yes/no ')
if user_input == 'yes':
    'DROP TABLE IF EXISTS "Countries"'


f=open(COUNTRIESJSON, "r")
f_contents  = f.read()
lst = json.loads(f_contents)
f.close()
for item in lst:
    insertion = ((None, item['alpha2Code'], item['alpha3Code'], item['name'], item['region'], item['subregion'], item['population'], item['area']))
    statement = 'INSERT INTO "Countries"'
    statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(statement, insertion)
    conn.commit()

cur.execute('DROP TABLE IF EXISTS "Bars"')

statement = """
    CREATE TABLE 'Bars' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'Company' TEXT,
        'SpecificBeanBarName' TEXT,
        'REF' TEXT,
        'ReviewDate' TEXT,
        'CocoaPercent' REAL,
        'CompanyLocation' REAL,
        'CompanyLocationId' INTEGER,
        'Rating' REAL,
        'BeanType' TEXT,
        'BroadBeanOrigin' TEXT,
        'BroadBeanOriginId' INTEGER
    );
    """
cur.execute(statement)
conn.commit()

input2 = input('Bars table exists. Delete? yes/no. ')
if input2 == 'yes':
    'DROP TABLE "Bars"'

query = '''
    SELECT *
    FROM Countries
'''
cur.execute(query)
locationdict = {}
for x in cur:
    locationdict[x[3]] = x[0]


with open(BARSCSV, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        company = row[0]
        specific_bean = row[1]
        ref = row[2]
        review_date = row[3]
        cocoa_percent = row[4]
        location = row[5]
        if location in locationdict:
            location_id = locationdict[location]
        rating = row[6]
        bean_type = row[7]
        origin = row[8]
        if origin in locationdict:
            origin_id = locationdict[origin]
        insert_statement = (None, company, specific_bean, ref, review_date, cocoa_percent, location, location_id, rating, bean_type, origin, origin_id)
        statement = 'INSERT INTO "Bars"'
        statement += 'Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(statement, insert_statement)
    conn.commit()

# Part 2: Implement logic to process user commands
# def process_command(command):
#     if command.split()[0] == 'bars':
#         sellCountry = None
#         sourceCountry = None
#         sellregion = None
#         sourceregion = None
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

def load_help_text():
    with open('help.txt') as f:
        return f.read()

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
