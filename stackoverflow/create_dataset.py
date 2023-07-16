import requests
import csv
from bs4 import BeautifulSoup
import re

def scrape_questions(tag):
    # Define the API endpoint URL for questions
    questions_url = 'https://api.stackexchange.com/2.3/questions'

    # Set the parameters for the questions API request
    questions_params = {
        'site': 'stackoverflow',
        'tagged': tag,
        'filter': 'withbody',
        'pagesize': 100,  # Number of questions per page
        'page': 1,        # Page number
    }

    # Send a GET request to the questions API endpoint
    questions_response = requests.get(questions_url, params=questions_params)

    # Check if the request for questions was successful
    if questions_response.status_code == 200:
        # Extract the questions data from the response
        questions_data = questions_response.json()

        return questions_data['items']
    else:
        # Handle the case when the request for questions was not successful
        print('Error:', questions_response.status_code)
        return []

def scrape_answers(question_id):
    # Define the API endpoint URL for answers
    answers_url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'

    # Set the parameters for the answers API request
    answers_params = {
        'site': 'stackoverflow',
        'filter': 'withbody',
    }

    # Send a GET request to the answers API endpoint
    answers_response = requests.get(answers_url, params=answers_params)

    # Check if the request for answers was successful
    if answers_response.status_code == 200:
        # Extract the answers data from the response
        answers_data = answers_response.json()

        return answers_data['items']
    else:
        # Handle the case when the request for answers was not successful
        print('Error:', answers_response.status_code)
        return []

def clean_text(html_text):
    # Remove HTML tags from the text
    cleaned_text = BeautifulSoup(html_text, 'html.parser').get_text()

    # Remove extra whitespaces and newline characters
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question Title', 'Question Votes', 'Answer Body'])

        for question in data:
            # Extract the question title and vote count
            question_title = clean_text(question['title'])
            question_votes = question['score']

            # Scrape answers for the question
            answers = scrape_answers(question['question_id'])

            for answer in answers:
                # Extract the answer body
                answer_body = clean_text(answer['body'])

                # Write the cleaned data to the CSV file
                writer.writerow([question_title, question_votes, answer_body])

# Define the tag you want to scrape
tag = 'python'

# Scrape the questions
questions = scrape_questions(tag)
print(questions)
# Save the data to a CSV file
# save_to_csv(questions, 'stackoverflow_data.csv')
