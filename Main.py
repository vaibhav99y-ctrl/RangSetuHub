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
    print("नमस्ते! RangSetuHub ऐप में आपका स्वागत है।")
    choice = input("1. रजिस्टर 2. लॉगिन : ")
    
    if choice == '1':
        register()
    elif choice == '2':
        login()

import json

# डेटाबेस लोड करना
def load_data():
    try:
        with open('artist_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# रिल्स लिंक के साथ प्रोफाइल अपडेट करना
def add_reel(username):
    reel_url = input("अपने काम की रील लिंक (Instagram/Drive link) पेस्ट करें: ")
    data = load_data()
    for artist in data:
        if artist['username'] == username:
            artist['reel_url'] = reel_url
            break
    
    with open('artist_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("आपकी रील सफलतापूर्वक अपलोड हो गई है!")

# प्रगत फिल्टर (Advanced Search)
def advanced_search():
    data = load_data()
    print("\n--- कलाकार खोजें (Search Artists) ---")
    city_filter = input("शहर का नाम (उदा. Jamner): ")
    cat_filter = input("कला का प्रकार (उदा. Painter/Artist): ")

    results = [a for a in data if a['city'].lower() == city_filter.lower() and a['category'].lower() == cat_filter.lower()]

    if results:
        print(f"\n{len(results)} कलाकार मिले:")
        for r in results:
            reel = r.get('reel_url', 'रील उपलब्ध नहीं है')
            print(f"- {r['name']} | अनुभव: {r['experience']} साल | रील लिंक: {reel}")
    else:
        print("माफ करें, इस शहर में इस प्रकार के कलाकार अभी उपलब्ध नहीं हैं।")
