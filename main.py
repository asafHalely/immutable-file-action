import git
from actions_toolkit.github import Context

context = Context()

# PK = os.environ.get("INPUT_PROJECT_KEY")


# def getRegex():
#     if PK is not None:
#         return rf'^{PK}-\d+:? +\S'
#     return r'^[A-Z]+-\d+:? +\S'


# def checkTitle(title):
#     regex = getRegex()
#     print(regex)
#     if re.search(regex, title) is None :
#         print("Bad Title")
#         exit(1)

#     print("Title is Ok")

# Check that this runs only in PR
def isPR():
    pull_request = context.payload.get("pull_request")
    if pull_request is None or pull_request.get("title") is None :
        print("This action should only be run with Pull Request Events")
        exit(1)


def write_branch_diff(current_branch, target_branch):
    # Open the repository
    repo = git.Repo(".")
    repo.remotes.origin.fetch()

    # Get the diff between the two branches
    diff = repo.git.diff(f"origin/{current_branch}", f"origin/{target_branch}")

    # Write the diff to a file
    print(diff)


if __name__ == "__main__":
    # Check that this runs only in PR
    isPR()

    current_branch = context.payload.get("pull_request").get("head").get("ref")
    target_branch = context.payload.get("pull_request").get("base").get("ref")

    print(f"Corrent branch {current_branch}")
    print(f"Target branch {target_branch}")

    write_branch_diff(current_branch, target_branch)

    # pull_request = context.payload.get("pull_request")
    # if pull_request is None or pull_request.get("title") is None :
    #     print("This action should only be run with Pull Request Events")
    #     exit(1)
    # print("Starting PR Title check for Jira Issue Key")
    # title = pull_request.get("title")
    # checkTitle(title)
