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

    current = f"origin/{current_branch}"
    target = f"origin/{target_branch}"

    # Get the diff between the two branches
    diff = repo.git.diff("--name-only", current, target)

    # Split to file names
    files = diff.splitlines()

    return files


def isImmutable(file_name):
    for regex in files:
        print(file_name)
        if re.search(f"^{regex}", file_name):
            return True

    return False


if __name__ == "__main__":
    # Check that this runs only in PR
    isPR()

    current_branch = context.payload.get("pull_request").get("head").get("ref")
    target_branch = context.payload.get("pull_request").get("base").get("ref")

    print(f"Corrent branch {current_branch}")
    print(f"Target branch {target_branch}")

    diffFiles = write_branch_diff(current_branch, target_branch)

    print(f"Changed files are: {diffFiles}")

    print(files)
    files = list(filter(lambda x: x != "", files.split(' ')))
    print(files)

    immutable = []

    for file in diffFiles:
        if isImmutable(file):
            immutable.append(file)

    if immutable == []:
        exit(0)
    else:
        for file in immutable:
            print(f"Immutable file changed: {file}")
        exit(1)
