import argparse
import logging

from dvc.command.base import append_doc_link
from dvc.command.base import CmdBase


logger = logging.getLogger(__name__)


class CmdInstall(CmdBase):
    def run(self):
        try:
            self.repo.install()
        except Exception:
            logger.exception("failed to install dvc hooks")
            return 1
        return 0


def add_parser(subparsers, parent_parser):
    INSTALL_HELP = "Install DVC git hooks into the repository."
    install_parser = subparsers.add_parser(
        "install",
        parents=[parent_parser],
        description=append_doc_link(INSTALL_HELP, "install"),
        help=INSTALL_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    install_parser.set_defaults(func=CmdInstall)
