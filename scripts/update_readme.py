import json
import urllib.request
import re
from datetime import datetime

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events/public"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching activity: {e}")
        return []
    return []

def format_event(event):
    created_at = event.get("created_at")
    dt = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    time_str = dt.strftime("%b %d, %Y")
    
    event_type = event.get("type")
    repo_name = event.get("repo", {}).get("name", "")
    # Clean repo name (remove username prefix if desired, or keep it)
    repo_short = repo_name.replace("vansh917917/", "")
    
    payload = event.get("payload", {})
    
    if event_type == "PushEvent":
        ref = payload.get("ref", "refs/heads/main")
        branch = ref.split("/")[-1]
        return f"⚡ `{time_str}` - Pushed commits to `{branch}` branch on **[{repo_short}](https://github.com/{repo_name})**"
            
    elif event_type == "PullRequestEvent":
        action = payload.get("action", "")
        pr_title = payload.get("pull_request", {}).get("title", "")
        pr_url = payload.get("pull_request", {}).get("html_url", "")
        return f"🔀 `{time_str}` - {action.capitalize()} PR **[{pr_title}]({pr_url})** on **{repo_short}**"
        
    elif event_type == "IssuesEvent":
        action = payload.get("action", "")
        issue_title = payload.get("issue", {}).get("title", "")
        issue_url = payload.get("issue", {}).get("html_url", "")
        return f"❗ `{time_str}` - {action.capitalize()} issue **[{issue_title}]({issue_url})** on **{repo_short}**"
        
    elif event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "")
        return f"✨ `{time_str}` - Created {ref_type} on **[{repo_short}](https://github.com/{repo_name})**"
        
    elif event_type == "WatchEvent":
        return f"⭐️ `{time_str}` - Starred **[{repo_short}](https://github.com/{repo_name})**"
        
    return None

def update_readme():
    username = "vansh917917"
    events = fetch_activity(username)
    
    activity_lines = []
    seen_messages = set() # Avoid duplicate entries
    
    for event in events:
        formatted = format_event(event)
        if formatted and formatted not in seen_messages:
            activity_lines.append(formatted)
            seen_messages.add(formatted)
            if len(activity_lines) >= 5:
                break
                
    if not activity_lines:
        activity_text = "No recent public activity recorded."
    else:
        activity_text = "\n".join(f"* {line}" for line in activity_lines)
        
    # Read README
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("README.md not found!")
        return

    # Replace content between comments
    pattern = r"(<!-- START_SECTION:activity -->)(.*?)(<!-- END_SECTION:activity -->)"
    replacement = f"\\1\n{activity_text}\n\\3"
    
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    
    if count > 0:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated README.md with latest activity!")
    else:
        print("Could not find start/end section markers in README.md!")

if __name__ == "__main__":
    update_readme()
