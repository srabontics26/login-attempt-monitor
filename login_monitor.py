from collections import Counter

logins = [
    ("192.168.1.10", "failed"),
    ("192.168.1.15", "success"),
    ("192.168.1.10", "failed"),
    ("192.168.1.20", "success"),
    ("192.168.1.10", "failed"),
    ("192.168.1.25", "failed"),
    ("192.168.1.15", "success"),
]

failed_attempts = Counter()

for ip, status in logins:
    if status == "failed":
        failed_attempts[ip] += 1

print("Login Attempt Monitor")
print("---------------------")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed attempt(s)")

print("\nSuspicious IP addresses:")

found = False

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"- {ip} ({count} failed attempts)")
        found = True

if not found:
    print("No repeated failed login attempts found.")
