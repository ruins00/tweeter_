# Tweeter
A Twitter post scheduler made with Python, Flask, CSS and HTML that posts Tweets on specified times by interacting with the Twitter API.

## Setup & Installation

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```
## Setting up Twitter Developer Credentials

1. Visit the Twitter Developer Portal at https://developer.twitter.com/ and sign in or create an account.

2. Create a Twitter Developer Account by clicking on your profile icon, selecting "Apps," and clicking "Create an app."

3. Provide app details, including the name, description, and website, and complete the necessary agreement and verification steps.

4. Set up a project by navigating to the app's dashboard, clicking on the "Project settings" tab, and selecting "Set up a new project."

5. Generate API keys by going to the "Keys and tokens" tab, noting down the "API key," "API secret key," and generating the "Access token" and "Access token secret."

6. Store all the keys as environment variables in your system according to variable names in `tweet.py` file.

## Setting up Google Sheets Credentials

1. Create a Google Cloud Platform (GCP) project and enable the Google Sheets API.

2. Create a service account and download the JSON credentials file, rename the file as `cred.json`.

3. Share the target Google Sheet with the service account email from the credentials file, granting appropriate permissions.

4. Save the key as an environment variable in your system according to the variable name in `main.py` file.


## Running The App

```bash
python main.py
```

## Running The Background Script

```bash
python tweet.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
