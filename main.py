import json
import os
import re
import git
from actions_toolkit.github import Context

context = Context()

files = os.environ.get("INPUT_FILES")


# Check that this runs only in PR
def isPR():
    pull_request = context.payload.get("pull_request")
    if pull_request is None or pull_request.get("title") is None :
        print("This action should only be run with Pull Request Events")
        exit(1)


def write_branch_diff(current_branch, target_branch):
    # Open the repository
    repo = git.Repo(".")

    # Fetch the origin
    repo.remotes.origin.fetch()

    # Get the diff between the two branches
    diff = repo.git.diff("--name-only", f"origin/{current_branch}", f"origin/{target_branch}")

    # Split to file names
    files = diff.splitlines()

    return files

def isMatch(file_name):
    for regex in files:
        txt = "The rain in Spain"
        if re.search(f"^{regex}", file_name):
            return False
    
    return True


if __name__ == "__main__":
    # Check that this runs only in PR
    isPR()

    current_branch = context.payload.get("pull_request").get("head").get("ref")
    target_branch = context.payload.get("pull_request").get("base").get("ref")

    print(f"Corrent branch {current_branch}")
    print(f"Target branch {target_branch}")

    diffFiles = write_branch_diff(current_branch, target_branch)

    print(diffFiles)

    immutable = []

    for file in diffFiles:
        if isMatch(file):
            immutable.append(file)
    
    if immutable == []:
        exit(0)
    else:
        for file in immutable:
            print(f"Immutable file changed: {file}")


    # pull_request = context.payload.get("pull_request")
    # if pull_request is None or pull_request.get("title") is None :
    #     print("This action should only be run with Pull Request Events")
    #     exit(1)
    # print("Starting PR Title check for Jira Issue Key")
    # title = pull_request.get("title")
    # checkTitle(title)
