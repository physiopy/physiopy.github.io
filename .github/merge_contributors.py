# Code to combine all-contributors files from multiple repositories into a single file
# With help from GitHub Copilot

import requests
import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List all physiopy repos (manually inputted for now)
repo_list = {'name': [
    'prep4phys',
    'physioqc',
    'physiopy.github.io',
    'phys2denoise',
    'peakdet',
    'peakdet2',
    'physutils',
    'physiopy-repository-template',
    'physiopy-community-guidelines',
    'phys2bids',
    'physiopy',
    'physiopy-test-workflows',
    'brainhack-physiopy-2023',
    'physiopy_tutorial',
    '.github',
    'physiopy-codesprint-spring2023',
    'brainhack-physiopy-2022',
    'outreach'
]}

# Initialize DataFrame with additional columns
repo_list_df = pd.DataFrame(data=repo_list)
repo_list_df['cont_json'] = False
repo_list_df['cont_txt'] = False

# Create a directory to save the JSON files
os.makedirs('contributors_files', exist_ok=True)

# Loop through repos and save contributor file if it exists
for repo in repo_list_df['name']:
    url = f'https://github.com/physiopy/{repo}/raw/master/.all-contributorsrc'
    try:
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        if r.headers.get('Content-Type') == 'application/json':
            content = r.json()
            with open(f'contributors_files/{repo}_all-contributorsrc.json', 'w') as f:
                json.dump(content, f, indent=2)
            repo_list_df.loc[repo_list_df['name'] == repo, ['cont_json', 'cont_txt']] = [True, False]
            logging.info(f'Successfully saved JSON for {repo}')
        else:
            with open(f'contributors_files/{repo}_all-contributorsrc.txt', 'w') as f:
                f.write(r.text)
            repo_list_df.loc[repo_list_df['name'] == repo, ['cont_json', 'cont_txt']] = [False, True]
            logging.warning(f'Saved as text for {repo} due to non-JSON content')
    except requests.exceptions.RequestException as e:
        repo_list_df.loc[repo_list_df['name'] == repo, ['cont_json', 'cont_txt']] = [False, False]
        logging.error(f'Failed to fetch {repo}: {e}')

# Display the updated DataFrame
display(repo_list_df)

# Function to merge contributors
def merge_contributors(contributors_list):
    merged_contributors = {}
    for contributor in contributors_list:
        login = contributor['login']
        if login in merged_contributors:
            merged_contributors[login]['contributions'] = list(set(
                merged_contributors[login]['contributions'] + contributor['contributions']
            ))
        else:
            merged_contributors[login] = contributor
    return list(merged_contributors.values())

# Initialize an empty list to hold all contributors
all_contributors = []

# Read all JSON files from the contributors_files directory
json_files = glob.glob('contributors_files/*.json')

for json_file in json_files:
    with open(json_file, 'r') as f:
        content = json.load(f)
        all_contributors.extend(content['contributors'])

# Merge all contributors
merged_contributors = merge_contributors(all_contributors)

# Create the final .all-contributorsrc content
merged_file = {
    "contributors": merged_contributors
}

# Write the merged contributors to a new .all-contributorsrc file
with open('merged_all-contributorsrc.json', 'w') as f:
    json.dump(merged_file, f, indent=2)

logging.info('Successfully merged all contributors into merged_all-contributorsrc.json')