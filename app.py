import re
import subprocess

# Guardrails-style policy: block secrets
BLOCK_PAT = re.compile(r"\b(api key|password|credential)\b", re.IGNORECASE)

# Regex to extract NAT workflow result: ['...']
RESULT_PAT = re.compile(r"\[\s*'([^']+)'\s*\]")
ANSI_PAT = re.compile(r"\x1b\[[0-9;]*m")  # strip ANSI colors if present

def nat_run(question: str) -> str:
    out = subprocess.check_output(
        ["nat", "run", "--config_file", "nat_config.yml", "--input", question],
        text=True,
        stderr=subprocess.STDOUT,
    )

    # Clean ANSI escape codes
    out = ANSI_PAT.sub("", out)

    # Extract workflow result
    match = RESULT_PAT.search(out)
    if match:
        return match.group(1).strip()

    # Fallback
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    return lines[-1] if lines else ""

print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").strip()
    if not user or user.lower() in {"exit", "quit"}:
        break

    # Guardrails policy gate
    if BLOCK_PAT.search(user):
        print("Bot: I can’t help with secrets or credentials.")
        continue

    # Allowed → NAT agent + tool
    answer = nat_run(user)
    print("Bot (agent):", answer)
O

