# This script generates our PythonLoopsBlocks.yml rule file.
#
# usage: python gen_python.py > PythonLoopsBlocks.yml && git commit -a -m "updated PythonLoopsBlocks.yml"

CONSTRUCTS = {
    'loop': ('for', 'while'),
    'block': ('for', 'while', 'if', 'else', 'try', 'except', 'with')
}

# Top-level rule file template
TEMPLATE = """# DO NOT EDIT: See gen_python.py
extends: substitution
message: "Prefer '%s' over '%s'"
level: warning
description: "Standardize spelling of Python programming constructs."
nonword: true
code: true
swap:
  {rules}"""

RULE_TEMPLATES = ("'{name} {type}': {name}-{type}",
                  "'`{name}`(?: |-){type}': {name}-{type}")

rules = "\n  ".join(template.format(name=name, type=type)
                    for (type, names) in CONSTRUCTS.items()
                    for name in names
                    for template in RULE_TEMPLATES)

print(TEMPLATE.format(rules=rules))
