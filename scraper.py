from google_play_scraper import search
import pandas as pd
import time
import re

def keywords():
    keywords_first_alternative = [
    "conversational agent",
    "conversational system",
    "dialog system",
    "assistance technology",
    "relational agent",
    "chatbot",
    "virtual human",
    "virtual agent",
    "virtual coach",
    "virtual therapist",
    "virtual therapy",
    "avatar",
    "artificial Intelligence"
    ]

    keywords_second_alternative = [
        "depression",
        "anxiety",
        #"agoraphobia",
        #"phobia",
        "panic",
        "mental health",
        "mental illness",
        "mental disorder",
        #"psychology",
        #"affective disorder",
        #"bipolar",
        "mood disorder",
        #"psychosis",
        #"psychotic",
        #"schizophrenia",
        "well-being",
        #"quality of life",
        "self-harm",
        "self-injury",
        #"stress",
        #"distress",
        "mood",
        "loneliness",
        #"social isolation",
        #"autism",
        #"suicide",
        "insomnia",
        #"emotion",
        #"affect"
    ]

    combined_keywords = []

    # Create combinations of keywords from the first and second alternatives
    for keyword_first in keywords_first_alternative:
        for keyword_second in keywords_second_alternative:
            combined_keywords.append(keyword_first + " " + keyword_second)
    return combined_keywords

def scrape():
    apps = pd.DataFrame()
    combined_keywords = keywords()
    for keyword in combined_keywords:
    #['therapy', 'therapeutic chatbot', 'mental health', 'therapy chatbot','depression','self-harm','anxiety','schizophrenia','substance abuse','addiction']:
        print(keyword)
        result = search(
            keyword,
            lang="en",  # defaults to 'en'
            country="us",  # defaults to 'us'
            n_hits=20  # defaults to 30 (= Google's maximum)

        )
        result = pd.DataFrame(result)
        result['keyword'] = keyword
        apps = pd.concat([apps, result],axis=0)
        time.sleep(3)
    return apps

def main():
    apps = scrape()
    df = pd.DataFrame(apps)
    df = df.drop_duplicates('appId')
    df['installs'] = df['installs'].apply(lambda x: int(re.sub("[^0-9]", "", x)))
    apps.to_csv("apps.csv",index=False)


if __name__ == "__main__":
    main()