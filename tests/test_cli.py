import unittest
import subprocess
import sys

class TestCLI(unittest.TestCase):
    def test_cli_list(self):
        cmd = [sys.executable, "-m", "agentui.cli", "list"]
        res = subprocess.run(cmd, capture_output=True, text=True, cwd=r"c:\Users\varshan\.gemini\antigravity\scratch\VelorioLabs\AgentUI-Skills")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Cyberpunk Dark Ops HUD", res.stdout)

if __name__ == "__main__":
    unittest.main()
