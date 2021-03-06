from github import Github
from config.github import Github as Config


class Authenticate:

    # Authenticate constructor
    def __init__(self):
        self.config = Config()
        self.github = Github(self.config.tokens())

    # Get the authenticate object
    def get(self):
        return self.github

