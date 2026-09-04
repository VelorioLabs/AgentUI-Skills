"""Command-Line Interface for AgentUI."""
import sys
import argparse
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from agentui.tokens import THEMES, get_theme
from agentui.templates import TEMPLATES, get_template
from agentui.linter import UILinter

def main():
    parser = argparse.ArgumentParser(
        description="AgentUI - God-Level UI/UX Design Engine & Linter for AI Agents",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Operational mode")

    # audit command
    audit_parser = subparsers.add_parser("audit", help="Audit code against VibeUI 25-point design standards")
    audit_parser.add_argument("target", help="File or directory to audit")
    audit_parser.add_argument("--json", action="store_true", help="Output audit in JSON format")

    # list command
    subparsers.add_parser("list", help="List available themes and component recipes")

    # add command
    add_parser = subparsers.add_parser("add", help="Print or inject a component template")
    add_parser.add_argument("component", choices=list(TEMPLATES.keys()), help="Component name")

    # theme command
    theme_parser = subparsers.add_parser("theme", help="Export design tokens for a theme")
    theme_parser.add_argument("name", choices=list(THEMES.keys()), help="Theme name")

    args = parser.parse_args()

    if args.command == "audit":
        reports = UILinter.audit_path(args.target)
        if args.json:
            print(json.dumps(reports, indent=2))
        else:
            print(f"\n🔍 AgentUI Design Linter Results:")
            for r in reports:
                print(f"\n[{r['grade']}] Score: {r['score']}/100 - {r['filename']}")
                for issue in r['issues']:
                    print(f"  ✖ {issue['rule']}: {issue['message']}")
                if not r['issues']:
                    print("  ✔ 100% God-Level Design Compliance!")
    elif args.command == "list":
        print("\n🎨 Available Design Themes:")
        for k, v in THEMES.items():
            print(f"  - {k:15}: {v['name']}")
        print("\n🧩 Available Component Recipes:")
        for k in TEMPLATES.keys():
            print(f"  - {k}")
    elif args.command == "add":
        print(get_template(args.component))
    elif args.command == "theme":
        print(json.dumps(get_theme(args.name), indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
