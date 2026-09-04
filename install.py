import os
import shutil
import argparse

def install():
    parser = argparse.ArgumentParser(description="Install AgentUI-Skills for Antigravity, Claude, or Cursor")
    parser.add_argument("--agent", choices=["antigravity", "cursor", "claude", "all"], default="all")
    parser.add_argument("--target", default=".", help="Target project root directory")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.abspath(args.target)

    if args.agent in ["antigravity", "all"]:
        dest = os.path.join(target_dir, ".agents", "skills", "vibe-ui-designer")
        os.makedirs(dest, exist_ok=True)
        shutil.copytree(os.path.join(base_dir, "skills", "vibe-ui-designer"), dest, dirs_exist_ok=True)
        print(f"[✔] Installed Antigravity skill to: {dest}")

    if args.agent in ["cursor", "all"]:
        rules_dir = os.path.join(target_dir, ".cursor", "rules")
        os.makedirs(rules_dir, exist_ok=True)
        shutil.copy(os.path.join(base_dir, "cursor", ".cursor", "rules", "ui-designer.mdc"), rules_dir)
        shutil.copy(os.path.join(base_dir, "cursor", ".cursorrules"), target_dir)
        print(f"[✔] Installed Cursor rules to: {target_dir}")

    if args.agent in ["claude", "all"]:
        claude_dir = os.path.join(target_dir, ".claude")
        os.makedirs(claude_dir, exist_ok=True)
        shutil.copy(os.path.join(base_dir, "claude", ".claude", "ui-designer.md"), claude_dir)
        shutil.copy(os.path.join(base_dir, "claude", "CLAUDE.md"), target_dir)
        print(f"[✔] Installed Claude Code rules to: {target_dir}")

if __name__ == "__main__":
    install()
