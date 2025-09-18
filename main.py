import requests

# Replace with your GitHub username and repo
username = "beingralph"
repo = "vistaar"

url = f"https://api.github.com/repos/{username}/{repo}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Repository: {data['name']}")
    print(f"Stars: {data['stargazers_count']}")
    print(f"Forks: {data['forks_count']}")
    print(f"Last Updated: {data['updated_at']}")
else:
    print("Error fetching data:", response.status_code)
