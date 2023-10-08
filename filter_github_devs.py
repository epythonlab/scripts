import requests
import csv


def get_developers_by_region(region, access_token):
    """
    Retrieve a list of developers from a specific region sorted by their number of followers.

    Parameters:
        region (str): The region you want to filter developers by.
        access_token (str): The GitHub personal access token for authentication.

    Returns:
        list: A list of dictionaries containing developer information, sorted by number of followers.
    """
    base_url = "https://api.github.com/search/users"
    params = {
        "q": f"location:{region}",
        "per_page": 100,  # You can adjust the number of results per page as needed
        "sort": "followers",  # Sort by number of followers
        "order": "desc",  # Sort in descending order (highest followers first)
    }
    headers = {
        "Authorization": f"token {access_token}"
    }
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        developers = data.get("items", [])
        return developers
    else:
        print(f"Failed to retrieve data from GitHub API. Status Code: {response.status_code}")
        return []
    

def get_user_followers(username, access_token):
    """
    Retrieve the number of followers for a specific GitHub user.

    Parameters:
        username (str): The GitHub username of the user.
        access_token (str): The GitHub personal access token for authentication.

    Returns:
        int: The number of followers for the specified user.
    """
    base_url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {access_token}"
    }
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        followers = data.get("followers", 0)
        return followers
    else:
        print(f"Failed to retrieve data for user {username}. Status Code: {response.status_code}")
        return 0
    

def save_to_csv(region, developers, access_token):
    csv_filename = f"{region}_developer_data.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['Username', 'Followers', 'GitHub Profile']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dev in developers:
            username = dev["login"]
            followers = get_user_followers(username, access_token)
            github_link = f"https://github.com/{username}"
            writer.writerow({'Username': username, 'Followers': followers, 'GitHub Profile': github_link})
    
    print(f"Developer data saved in '{csv_filename}'.")
    
    
if __name__ == "__main__":
    region = "Ethiopia"  # Replace this with the region you want to filter by
    access_token = "your token"  # Replace this with your GitHub personal access token
    developers = get_developers_by_region(region, access_token)
    
    if developers:
        print(f"Developers in {region}, sorted by rate:")
        for dev in developers:
            username = dev["login"]
            followers = get_user_followers(username, access_token)
            github_link = f"https://github.com/{username}"
            print(f"{username} - Followers: {followers} - GitHub Profile: {github_link}")
        save_to_csv(region, developers, access_token)
    else:
        print("No developers found in the specified region.")





