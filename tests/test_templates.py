import unittest
from agentui.templates import TEMPLATES, get_template

class TestTemplates(unittest.TestCase):
    def test_template_keys(self):
        self.assertIn("bento-card", TEMPLATES)
        self.assertIn("command-palette", TEMPLATES)
        self.assertIn("status-pill", TEMPLATES)

    def test_get_template(self):
        tpl = get_template("bento-card")
        self.assertIn("backdrop-blur-xl", tpl)
        self.assertIn("font-mono", tpl)

if __name__ == "__main__":
    unittest.main()
