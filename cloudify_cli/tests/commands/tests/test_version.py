from ..test_base import CliCommandTest


class VersionTest(CliCommandTest):

    def test_version(self):
        self.invoke('cfy --version')