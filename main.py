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

# def isPR():
#     pull_request = context.payload.get("pull_request")
#     if pull_request is None or pull_request.get("title") is None :
#         print("This action should only be run with Pull Request Events")
#         exit(1)


if __name__ == "__main__":
    print(vars(context))
    print(context.payload.get("pull_request").get("head"))
    print(context.payload.get("pull_request").get("head").get("ref"))
    print(context.payload.get("pull_request").get("base"))
    print(context.payload.get("pull_request").get("base").get("ref"))
    # pull_request = context.payload.get("pull_request")
    # if pull_request is None or pull_request.get("title") is None :
    #     print("This action should only be run with Pull Request Events")
    #     exit(1)
    # print("Starting PR Title check for Jira Issue Key")
    # title = pull_request.get("title")
    # checkTitle(title)
