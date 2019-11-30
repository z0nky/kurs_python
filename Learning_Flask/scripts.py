import requests
import json


# Get response from API
def getResponseFromApi(description, location):
    global response_result

    basic_url = 'https://jobs.github.com/positions.json'
    params_to_pass = {
        'description': description,
        'location': location
    }

    response_result = requests.get(basic_url, params=params_to_pass)
    return response_result


# Save response data to JSON file
def saveToJson(description, location):
    getResponseFromApi(description, location)
    with open('jobs.json', 'w', encoding="utf-8") as file:
        file.write(response_result.text)


# Read data from JSON file
def readFromJson():
    with open('jobs.json', encoding="utf-8") as jobs_file:
        load_jobs = json.load(jobs_file)
        return load_jobs
