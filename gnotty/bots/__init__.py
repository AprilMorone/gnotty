
from gnotty.bots.base import BaseBot
from gnotty.bots.chat import ChatMixin
from gnotty.bots.commits import BitBucketMixin, GitHubMixin
from gnotty.bots.commands import CommandMixin
from gnotty.bots.events import on


##########################
#  Concrete bot classes  #
##########################

class ChatBot(ChatMixin, BaseBot):
    pass

class BitBucketBot(BitBucketMixin, BaseBot):
    pass

class GitHubBot(GitHubMixin, BaseBot):
    pass

class CommitBot(GitHubMixin, BitBucketMixin, BaseBot):
    pass

class CommandBot(CommandMixin, BaseBot):
    pass

class Voltron(ChatMixin, CommandMixin, BitBucketMixin, GitHubMixin, BaseBot):
    pass
