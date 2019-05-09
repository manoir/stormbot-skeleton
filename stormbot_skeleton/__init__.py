"""Skeleton plugin for Stormbot"""
from stormbot.bot import Plugin


class Skeleton(Plugin):
    def __init__(self, bot, args):
        self._bot = bot
        self.config = args.skeleton_config

    @classmethod
    def argparser(cls, parser):
        parser.add_argument("--skeleton-config", type=str, default="config", help="Skeleton runtime option (default: %(default)s)")

    def cmdparser(self, parser):
        subparser = parser.add_parser('skeleton', bot=self._bot)
        subparser.set_defaults(command=self.run)
        subparser.add_argument("text", type=str, help="Some dummy argument")

    def run(self, msg, parser, args, peer):
        self._bot.write(args.text)

if __name__ == "__main__":
    from stormbot.bot import main
    main(Skeleton)
