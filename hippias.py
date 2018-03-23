import json


class Hippias:
    def __init__(self, config_file="config.json"):
        configs = json.load(open(config_file))
        self.reddit_configs = configs['reddit']
        self.tumblr_configs = configs['tumblr']


if __name__ == "__main__":
    h = Hippias()

