#!/usr/bin/env python3

"""
Gemini AI Code Review for CSE636 Week 2 Lab
"""

import os
import subprocess
import google.generativeai as genai


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)


def get_python_files():
    result = subprocess.run(
        ["git", "ls-files", "*.py"],
        capture_output=True,
        text=True
    )

    return [
        f for f in result.stdout.splitlines()
        if f.endswith(".py")
    ]


def read_file(path):
    with open(path, "r") as file:
        return file.read()


def review_code(filename, content):

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

    prompt = f"""
You are a senior Python code reviewer.

Review this Python file.

Check:
- bugs
- security issues
- style problems
- possible improvements

Be concise.

File:
{filename}

Code:
```python
{content}

"""

response = model.generate_content(prompt)

return response.text

def main():

files = get_python_files()

report = [
    "# Gemini AI Code Review Report\n"
]

for file in files:

    print("Reviewing:", file)

    code = read_file(file)

    result = review_code(
        file,
        code
    )

    report.append(
        f"\n## {file}\n\n{result}\n"
    )


with open(
    "ai_review_report.txt",
    "w"
) as f:
    f.write(
        "\n".join(report)
    )


print(
    "AI review complete"
)

if name == "main":
main()


Save the file.

---

## Step 3: Commit and push the change

PowerShell:

```powershell
cd C:\sample-python-app