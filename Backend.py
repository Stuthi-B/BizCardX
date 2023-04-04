# importing required libraries
import easyocr as ocr
import re
import cv2
import Db as db
import os


details = {}
states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
          "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", " Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "West Bengal"]
cities = ["Port Blair", "Adoni", "Amaravati", "Anantapur", "Chandragiri", "Chittoor", "Dowlaiswaram", "Eluru", "Guntur", "Kadapa", "Kakinada", "Kurnool", "Machilipatnam", "Nagarjunakoṇḍa", "Rajahmundry", "Srikakulam", "Tirupati", "Vijayawada", "Visakhapatnam", "Vizianagaram", "Yemmiganur", "Itanagar", "Dhuburi", "Dibrugarh", "Dispur", "Guwahati", "Jorhat", "Nagaon", "Sivasagar", "Silchar", "Tezpur", "Tinsukia", "Ara", "Barauni", "Begusarai", "Bettiah", "Bhagalpur", "Bihar Sharif", "Bodh Gaya", "Buxar", "Chapra", "Darbhanga", "Dehri", "Dinapur Nizamat", "Gaya", "Hajipur", "Jamalpur", "Katihar", "Madhubani", "Motihari", "Munger", "Muzaffarpur", "Patna", "Purnia", "Pusa", "Saharsa", "Samastipur", "Sasaram", "Sitamarhi", "Siwan", "Chandigarh", "Ambikapur", "Bhilai", "Bilaspur", "Dhamtari", "Durg", "Jagdalpur", "Raipur", "Rajnandgaon", "Daman", "Diu", "Silvassa", "Delhi", "New Delhi", "Madgaon", "Panaji", "Ahmadabad", "Amreli", "Bharuch", "Bhavnagar", "Bhuj", "Dwarka", "Gandhinagar", "Godhra", "Jamnagar", "Junagadh", "Kandla", "Khambhat", "Kheda", "Mahesana", "Morbi", "Nadiad", "Navsari", "Okha", "Palanpur", "Patan", "Porbandar", "Rajkot", "Surat", "Surendranagar", "Valsad", "Veraval", "Ambala", "Bhiwani", "Chandigarh", "Faridabad", "Firozpur Jhirka", "Gurugram", "Hansi", "Hisar", "Jind", "Kaithal", "Karnal", "Kurukshetra", "Panipat", "Pehowa", "Rewari", "Rohtak", "Sirsa", "Sonipat", "Bilaspur", "Chamba", "Dalhousie", "Dharmshala", "Hamirpur", "Kangra", "Kullu", "Mandi", "Nahan", "Shimla", "Una", "Anantnag", "Baramula", "Doda", "Gulmarg", "Jammu", "Kathua", "Punch", "Rajouri", "Srinagar", "Udhampur", "Bokaro", "Chaibasa", "Deoghar", "Dhanbad", "Dumka", "Giridih", "Hazaribag", "Jamshedpur", "Jharia", "Rajmahal", "Ranchi", "Saraikela", "Badami", "Ballari", "Bengaluru", "Belagavi", "Bhadravati", "Bidar", "Chikkamagaluru", "Chitradurga", "Davangere", "Halebid", "Hassan", "Hubballi-Dharwad", "Kalaburagi", "Kolar", "Madikeri", "Mandya", "Mangaluru", "Mysuru", "Raichur", "Shivamogga", "Shravanabelagola", "Shrirangapattana", "Tumakuru", "Vijayapura", "Alappuzha", "Vatakara", "Idukki", "Kannur", "Kochi", "Kollam", "Kottayam", "Kozhikode", "Mattancheri", "Palakkad", "Thalassery", "Thiruvananthapuram", "Thrissur", "Kargil", "Leh", "Balaghat", "Barwani", "Betul", "Bharhut", "Bhind", "Bhojpur", "Bhopal", "Burhanpur", "Chhatarpur", "Chhindwara", "Damoh", "Datia", "Dewas", "Dhar",
          "Dr. Ambedkar Nagar (Mhow)", "Guna", "Gwalior", "Hoshangabad", "Indore", "Itarsi", "Jabalpur", "Jhabua", "Khajuraho", "Khandwa", "Khargone", "Maheshwar", "Mandla", "Mandsaur", "Morena", "Murwara", "Narsimhapur", "Narsinghgarh", "Narwar", "Neemuch", "Nowgong", "Orchha", "Panna", "Raisen", "Rajgarh", "Ratlam", "Rewa", "Sagar", "Sarangpur", "Satna", "Sehore", "Seoni", "Shahdol", "Shajapur", "Sheopur", "Shivpuri", "Ujjain", "Vidisha", "Ahmadnagar", "Akola", "Amravati", "Aurangabad", "Bhandara", "Bhusawal", "Bid", "Buldhana", "Chandrapur", "Daulatabad", "Dhule", "Jalgaon", "Kalyan", "Karli", "Kolhapur", "Mahabaleshwar", "Malegaon", "Matheran", "Mumbai", "Nagpur", "Nanded", "Nashik", "Osmanabad", "Pandharpur", "Parbhani", "Pune", "Ratnagiri", "Sangli", "Satara", "Sevagram", "Solapur", "Thane", "Ulhasnagar", "Vasai-Virar", "Wardha", "Yavatmal", "Imphal", "Cherrapunji", "Shillong", "Aizawl", "Lunglei", "Kohima", "Mon", "Phek", "Wokha", "Zunheboto", "Balangir", "Baleshwar", "Baripada", "Bhubaneshwar", "Brahmapur", "Cuttack", "Dhenkanal", "Kendujhar", "Konark", "Koraput", "Paradip", "Phulabani", "Puri", "Sambalpur", "Udayagiri", "Karaikal", "Mahe", "Puducherry", "Yanam", "Amritsar", "Batala", "Chandigarh", "Faridkot", "Firozpur", "Gurdaspur", "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana", "Nabha", "Patiala", "Rupnagar", "Sangrur", "Abu", "Ajmer", "Alwar", "Amer", "Barmer", "Beawar", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittaurgarh", "Churu", "Dhaulpur", "Dungarpur", "Ganganagar", "Hanumangarh", "Jaipur", "Jaisalmer", "Jalor", "Jhalawar", "Jhunjhunu", "Jodhpur", "Kishangarh", "Kota", "Merta", "Nagaur", "Nathdwara", "Pali", "Phalodi", "Pushkar", "Sawai Madhopur", "Shahpura", "Sikar", "Sirohi", "Tonk", "Udaipur", "Gangtok", "Gyalshing", "Lachung", "Mangan", "Arcot", "Chengalpattu", "Chennai", "Chidambaram", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kanchipuram", "Kanniyakumari", "Kodaikanal", "Kumbakonam", "Madurai", "Mamallapuram", "Nagappattinam", "Nagercoil", "Palayamkottai", "Pudukkottai", "Rajapalayam", "Ramanathapuram", "Salem", "Thanjavur", "Tiruchchirappalli", "Tirunelveli", "Tiruppur", "Thoothukudi", "Udhagamandalam", "Vellore", "Hyderabad", "Karimnagar", "Khammam", "Mahbubnagar", "Nizamabad", "Sangareddi", "Warangal", "Agartala", "Agra", "Aligarh", "Amroha", "Ayodhya", "Azamgarh", "Bahraich", "Ballia", "Banda", "Bara Banki", "Bareilly", "Basti", "Bijnor", "Bithur", "Budaun", "Bulandshahr", "Deoria", "Etah", "Etawah", "Faizabad", "Farrukhabad-cum-Fatehgarh", "Fatehpur", "Fatehpur Sikri", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj", "Kanpur", "Lakhimpur", "Lalitpur", "Lucknow", "Mainpuri", "Mathura", "Meerut", "Mirzapur-Vindhyachal", "Moradabad", "Muzaffarnagar", "Partapgarh", "Pilibhit", "Prayagraj", "Rae Bareli", "Rampur", "Saharanpur", "Sambhal", "Shahjahanpur", "Sitapur", "Sultanpur", "Tehri", "Varanasi", "Almora", "Dehra Dun", "Haridwar", "Mussoorie", "Nainital", "Pithoragarh", "Alipore", "Alipur Duar", "Asansol", "Baharampur", "Bally", "Balurghat", "Bankura", "Baranagar", "Barasat", "Barrackpore", "Basirhat", "Bhatpara", "Bishnupur", "Budge Budge", "Burdwan", "Chandernagore", "Darjeeling", "Diamond Harbour", "Dum Dum", "Durgapur", "Halisahar", "Haora", "Hugli", "Ingraj Bazar", "Jalpaiguri", "Kalimpong", "Kamarhati", "Kanchrapara", "Kharagpur", "Cooch Behar", "Kolkata", "Krishnanagar", "Malda", "Midnapore", "Murshidabad", "Nabadwip", "Palashi", "Panihati", "Purulia", "Raiganj", "Santipur", "Shantiniketan", "Shrirampur", "Siliguri", "Siuri", "Tamluk", "Titagarh"]

# creating function to fetch each data from the card
def mobile(data):
    for i in data:
        if re.search(r"(\+?\d{1,3}[- ]?\d{3}[- ]?\d{4})", i) != None:
            details["mobno"] = details["mobno"] + " " + i
            data = data.remove(i)
            return data


def pin(data):
    for i in data:
        if re.findall(r"(\d{6})", i):
            details["pincode"] = i
            data = data.remove(i)
            return data


def mail(data):
    for i in data:
        if re.search(r'[\w\.-]+@[\w\.-]+(\.\s?[\w]+)+', i) != None:
            details["email"] = str(i)
            data = data.remove(i)
            return data


def url(data):
    for i in data:
        if re.search(r'^((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?\/?$', i) != None:
            details["url"] = str(i)
            data = data.remove(i)
            return data


def name(data):
    for i in data:
        if re.search(r'^[A-Za-z]+((\s)?([A-Za-z])+)*$', i):
            details["name"] = str(i)
            data = data.remove(i)
            # print(data)
            return data


def Address(data):
    for i in data:
        if re.search(r"^(\d{0,6})(?:\w)\s([A-Z][\w]+[ -]+){1,3}(Street|St|Road|Rd)", i):
            print("address", i)
            # print(i.split(","))
            for j in i.split(","):
                if j in states:
                    print(j)
                elif j in cities:
                    print("city", j)
            details["address"] = str(i.strip(', '))
            data = data.remove(i)
            # print(data)
            return data


def company_name(data):
    for i in data:
        if re.search ("\b[A-Z]\w+(?:\.com?)?(?:[ -]+(?:&[ -]+)?[A-Z]\w+(?:\.com?)?){0,2}[,\s]+(?i:ltd|llc|inc|plc|co(?:rp)?|group|holding|gmbh)\b", i):
            details["company"]=i
            data=data.remove(i)
            # print (data)
            return data
        else:
             details["company"] = None


def designation(data):
    for i in data:
        if re.search(r"[^\t\w\t]+,(?P<jobtitle>\w+)", i):
            details["desig"]=i
            data =data.remove(i)
            print (data)
            return data
        else:
            details["desig"] = None


def state(data):
    for i in data:
        if i in states:
            details["state"]=i
            data=data.remove(i)
            return data
        else:
            details["state"] = None


def city(data):
    for i in data:
        if i in cities:
            details["city"]=i
            data=data.remove(i)
            return data
        else:
            details["city"] = None


def fetch_all(file):
    file_path = os.path.join("./data/uploadedImages/", file.name)
    if file is not None:
        with open(file_path, "wb") as user_file:
            user_file.write(file.getbuffer())
    img = cv2.imread(file_path, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    details["mobno"] = ""
    reader = ocr.Reader(['en', 'en'], gpu=True)
    data = reader.readtext(gray, detail=0)
    name(data)
    mobile(data)
    mail(data)
    url(data)
    Address(data)
    city(data)
    state(data)
    pin(data)
    company_name(data)
    designation(data)
    db.insert_data(details)



# fetch_all()
print(details)