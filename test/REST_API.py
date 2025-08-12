import requests

url = "https://api.github.com/search/repositories?q=stars:>4&sort=stars&order=desc"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for i in range(10):
        repo = data['items'][i]
        print(f"repo num {i+1} is: {repo['full_name']}")
        print(f"stars: {repo['stargazers_count']}")
        print("--------------------------------")

else:
    print(f"error: {response.status_code}")