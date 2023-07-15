import requests
import os
import colorama
from colorama import Fore,Back

colorama.init(autoreset=True)
logo = f"{Fore.LIGHTRED_EX} Git-Profile-Grabber"
print(f"""{Fore.LIGHTRED_EX}
                                        ````:         --            :          --        :````
                                            #############################################
                                            &                                           %
                                            &            {logo}           %
                                            &                                           %
                                            &                                           %
                                            &                                           %
                                            &                    By                     %
                                            &                                           %
                                            &                @hackSavior                %
                                            &                                           %
                                            #############################################
""")

number = input("Enter Number Of Profile To Grab: ")
print("\n")
try:
    number = int(number)  # Attempt to convert the input to an integer
    current_directory = os.getcwd()
    profiles_directory = os.path.join(current_directory, "profiles")

    # Create the "profiles" directory if it doesn't exist
    if not os.path.exists(profiles_directory):
        os.makedirs(profiles_directory)

    for i in range(number):
        url = f"https://avatars.githubusercontent.com/u/{i}?v=9"
        filename = f"profile{i}.jpg"  # Generate a unique filename for each image
        filepath = os.path.join(profiles_directory, filename)
        response = requests.get(url)
        response.raise_for_status()

        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"{Fore.LIGHTBLACK_EX}[+] profile{i+1} saved successfully to "+f"{Fore.LIGHTMAGENTA_EX} Profiles")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except OSError:
    print("Not Valid Response")
