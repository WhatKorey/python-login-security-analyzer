
login_attempts = [
    {"username": "admin", "ip_address": "192.0.2.10", "status": "failed"},
    {"username": "admin", "ip_address": "192.0.2.10", "status": "failed"},
    {"username": "admin", "ip_address": "192.0.2.10", "status": "failed"},
    {"username": "korey", "ip_address": "198.51.100.4", "status": "success"},
    {"username": "guest", "ip_address": "203.0.113.7", "status": "failed"},
    {"username": "guest", "ip_address": "203.0.113.7", "status": "failed"},
    {"username": "admin", "ip_address": "203.0.113.50", "status": "failed"},
    {"username": "guest", "ip_address": "203.0.113.50", "status": "failed"},
    {"username": "testuser", "ip_address": "203.0.113.50", "status": "failed"},

]
failed_usernames = {}

failed_count = {}

usernames_by_ip = {}

for login in login_attempts:
    if login["status"] == "failed":
        ip = login["ip_address"]
        username = login["username"]

        if ip not in failed_count:
            failed_count[ip] = 0

        failed_count[ip] += 1

        if username not in failed_usernames:
            failed_usernames[username] = 0

        failed_usernames[username] += 1

        if ip not in usernames_by_ip:
            usernames_by_ip[ip] = set()

        usernames_by_ip[ip].add(username)



print("== Login Security Report ==")
print("Total login attempts:", len(login_attempts))

for ip, count in failed_count.items():
    print(f"IP Address: {ip} - Failed Attempts: {count}")


    if count >= 3:
        print(f"Warning: IP Address {ip} has exceeded the threshold of failed login attempts.")


print("\n=== Username Security Report ===")

for username, count in failed_usernames.items():
    print(f"Username: {username} - Failed Attempts: {count}")

    if count >= 3:
        print(f"Warning: Username '{username}' has exceeded the threshold of failed login attempts.")


print("\n=== Mutiple Account Dection ===")

for ip, usernames in usernames_by_ip.items():
    print(f"IP Address: {ip} | Unique Usernames: {len(usernames)}")

    if len(usernames) >= 3:
        print(f"Warning: IP Address {ip} has attempted logins with multiple usernames.")