import unittest
from agentui.linter import UILinter

class TestLinter(unittest.TestCase):
    def test_flat_gray_detection(self):
        bad_html = '<div class="bg-[#111111] text-white">Hello</div>'
        report = UILinter.audit_code(bad_html)
        self.assertFalse(report["passed"])
        self.assertTrue(any("NO_FLAT_GRAYS" in issue["rule"] for issue in report["issues"]))

    def test_god_level_passing(self):
        god_level_html = """
        <div class="bg-slate-950/80 backdrop-blur-xl border border-white/10 p-6 rounded-2xl">
          <span class="font-mono text-xs text-cyan-400">STATUS</span>
          <h1 class="font-sans text-2xl font-bold">Title</h1>
          <button class="bg-cyan-500 hover:scale-[1.02] active:scale-95 transition-all">Click</button>
        </div>
        """
        report = UILinter.audit_code(god_level_html)
        self.assertTrue(report["passed"])
        self.assertGreaterEqual(report["score"], 80)

if __name__ == "__main__":
    unittest.main()
