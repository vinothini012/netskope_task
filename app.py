import requests

def get_repo_owner(github_token, repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}"
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()
        repo_owner = repo_data['owner']['login']
        return repo_owner
    else:
        print(f"Failed to fetch repository details: {response.status_code}")
        return None

# Example usage
github_token = 'your_github_token'
repo_full_name = 'owner/repository'  # Replace with actual owner/repository
repo_owner = get_repo_owner(github_token, repo_full_name)
if repo_owner:
    print(f"Repository owner: {repo_owner}")
