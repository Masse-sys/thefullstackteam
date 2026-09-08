"""Temporary negative control: must be removed after GitHub blocks this PR."""
import unittest


class PilotGate(unittest.TestCase):
    def test_intentional_failure_blocks_merge(self):
        self.fail("Intentional pilot: verify GitHub blocks a failing required check.")
