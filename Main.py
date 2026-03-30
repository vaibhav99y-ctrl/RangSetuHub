import json

# डेटाबेस फाइल्स के नाम
USER_FILE = 'users.json'

def register():
    print("\n--- नया अकाउंट बनाएं ---")
    username = input("अपना यूजरनेम डालें: ")
    password = input("अपना पासवर्ड डालें: ")
    
    user_data = {"username": username, "password": password}
    
    try:
        with open(USER_FILE, 'r+') as f:
            users = json.load(f)
            # चेक करना कि यूजरनेम पहले से तो नहीं है
            for u in users:
                if u['username'] == username:
                    print("यह नाम पहले से मौजूद है! दूसरा चुनें।")
                    return
            users.append(user_data)
            f.seek(0)
            json.dump(users, f, indent=4)
    except FileNotFoundError:
        with open(USER_FILE, 'w') as f:
            json.dump([user_data], f, indent=4)
    
    print(f"बधाई हो {username}! आपका अकाउंट बन गया है।")

def login():
    print("\n--- लॉगिन करें ---")
    username = input("यूजरनेम: ")
    password = input("पासवर्ड: ")
    
    try:
        with open(USER_FILE, 'r') as f:
            users = json.load(f)
            for user in users:
                if user['username'] == username and user['password'] == password:
                    print(f"स्वागत है {username}! आप लॉगिन हो चुके हैं।")
                    return True
    except FileNotFoundError:
        print("अभी तक कोई अकाउंट नहीं बना है। पहले रजिस्टर करें।")
    
    print("गलत यूजरनेम या पासवर्ड!")
    return False

# मुख्य प्रोग्राम (Main Logic)
if __name__ == "__main__":
    print("नमस्ते! विकासकलरआर्ट कम्युनिटी ऐप में आपका स्वागत है।")
    choice = input("1. रजिस्टर 2. लॉगिन : ")
    
    if choice == '1':
        register()
    elif choice == '2':
        login()
