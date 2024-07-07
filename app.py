import os
import re
import requests
from bs4 import BeautifulSoup

def get_code_scanning_alerts(github_token, repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/code-scanning/alerts"
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        alerts = [alert for alert in response_data if alert['rule']['security_severity_level'] in ['low', 'medium', 'high', 'critical']]
        return alerts
    else:
        print(f"Failed to fetch alerts: {response.status_code}")
        return []

def get_exploitability_likelihood(cwe_id):
    url = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
    try:
        response = requests.get(url, verify=True) 
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')
        likelihood_section = soup.find('div', id='oc_200_Likelihood_Of_Exploit') 

        if likelihood_section:
            likelihood_value = likelihood_section.find_next('div', class_='indent').text.strip()
            return likelihood_value
        else:
            return 'Likelihood of Exploit not found'

    except requests.exceptions.RequestException as e:
        return f'Error accessing CWE page: {e}'

def main():
    github_token = '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'  # Set this in your environment variables
    repo_owner = 'Vinothini-dev'
    repo_name = 'netskope_task'
    
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return
    
    alerts = get_code_scanning_alerts(github_token, repo_owner, repo_name)
    for alert in alerts:
        cwe_ids = [tag.split('/')[-1].split('-')[-1] for tag in alert['rule']['tags'] if tag.startswith('external/cwe/cwe-')]
        print(f'Alert: {alert["rule"]["id"]} - {alert["rule"]["description"]}')
        print(f'Severity: {alert["rule"]["security_severity_level"]}')
        
        if cwe_ids:
            for cwe_id in cwe_ids:
                likelihood = get_exploitability_likelihood(cwe_id)
                print(f'Likelihood of Exploit for CWE-{cwe_id}: {likelihood}')
        else:
            print('No CWE ID found')

if __name__ == '__main__':
    main()

