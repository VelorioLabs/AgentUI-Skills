import unittest
from agentui.tokens import THEMES, get_theme

class TestTokens(unittest.TestCase):
    def test_theme_keys(self):
        self.assertIn("cyberpunk", THEMES)
        self.assertIn("linear", THEMES)
        self.assertIn("glassmorphism", THEMES)
        self.assertIn("cosmic", THEMES)

    def test_theme_properties(self):
        theme = get_theme("cyberpunk")
        self.assertEqual(theme["bg_base"], "#07090e")
        self.assertEqual(theme["accent_primary"], "#00f0ff")

if __name__ == "__main__":
    unittest.main()
