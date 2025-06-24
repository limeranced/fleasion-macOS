from colorama import Fore, Style, init
init()
import importlib.util
import os

# user guide for making your own
# addon/addon2 will set replacee/replacement to a string. addon can be a list (optional), addon2 cant
# start_key/start_key2 will start the user in a json from a set position (make sure the set position doesnt share a name or ill go to the first one)
# return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names finishes an area and returns all the data back and finishes this codes use
# add a line push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names) for doing multiple changes of seperate things in the same case
# if you want to skip then set skip to True
# leaving empty and only returning will make the user enter 2 from the json starting from the top

def get_valid_input(prompt, valid_values=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return 'back'
        try:
            if valid_values is None or int(user_input) in valid_values:
                return int(user_input)
            else:
                print(f"{Fore.RED}\nInvalid option. Please choose from {valid_values}.\n{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\nInvalid input. Please enter a valid number.\n{Style.RESET_ALL}")


def push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):
    spec = importlib.util.spec_from_file_location("backbone_module", "main.py")
    backbone_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(backbone_module)

    if hasattr(backbone_module, "backbone"):
        json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names = backbone_module.backbone(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
    else:
        print(f"Error: The file {backbone_module} does not contain a `backbone` function.")

def bloxstrap():
    base_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Bloxstrap', 'Modifications')
    nested_folders = ["PlatformContent", "pc", "textures", "sky"]

    if not os.path.exists(base_path):
        print(f"{Fore.RED}bloxstrap not found{Style.RESET_ALL}")
    else:
        path = base_path
        for folder in nested_folders:
            path = os.path.join(path, folder)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created folder: {path}")
            else:
                print(f"Folder already exists: {path}")

        print("All folders created successfully! Import your skyboxes into the opened folder.")
        os.startfile(path)

def run(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):

    while True:
        options = get_valid_input(f"Asset replacements:\n"
                        f"0:  {Fore.GREEN}Custom{Style.RESET_ALL}\n"
                        f"1:  {Fore.GREEN}Custom Skyboxes{Style.RESET_ALL}\n"
                        f"2:  {Fore.GREEN}Hitmarker Tweaks{Style.RESET_ALL}\n"
                        f"3:  {Fore.GREEN}Gun Sounds{Style.RESET_ALL}\n"
                        f"4:  {Fore.GREEN}CLIENT avatar tweaks{Style.RESET_ALL}\n"
                        f"Type 'back' to return to the previous menu.\n: ",
                        valid_values=[0, 1, 2, 3, 4]
        )
        if options == 'back':
            print(f"{Fore.CYAN}\nReturning to main menu.{Style.RESET_ALL}")
            skip = True
            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        
        try:
            match options:
                case 0:
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 1:
                    while True:
                        sky_option = get_valid_input(
                            f"\nIs Bloxstrap sky folder setup?\n"
                            f"1: {Fore.GREEN}yes{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}no{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2]
                        )

                        if sky_option == 'back':
                            print(f"\n{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                            break

                        match sky_option:
                            case 1:
                                start_key = "skyboxes"
                                addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                bloxstrap()
                                start_key = "skyboxes"
                                addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 2:
                    while True:
                        sky_option = get_valid_input(
                            f"\nSound or Hitmarker\n"
                            f"1: {Fore.GREEN}Sound{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}Hitmarker{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2]
                        )

                        if sky_option == 'back':
                            print(f"\n{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                            break

                        match sky_option:
                            case 1:
                                start_key = "dahood hit sound"
                                start_key2 = "replacement sounds"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                start_key = "shield icon"
                                start_key2 = "hitmarker"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 3:
                    start_key = "guns"
                    start_key2 = "replacement sounds"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 4:
                    while True:
                        sky_option = get_valid_input(
                            f"\nPick which item you want to change\n"
                            f"1: {Fore.GREEN}Stevie Standard > Headless{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}International Netherlands Fedora > SKOTN{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2]
                        )

                        if sky_option == 'back':
                            print(f"\n{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                            break

                        match sky_option:
                            case 1:
                                addon = ["0111487c7d3044bec56587c86740c9ce", "aa50829c76ec2756b28883af05342ca6"]
                                addon2 = "912c8cc21a2bfff5a882e91a8695da9a"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                addon = "7ce2ac6c1ed6d340767e00fe02f529f6"
                                addon2 = "b96f172467aa810b20bc5a99eba858e5"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = ["59cccb6d405a32f9a1d48ac20ec23fd2", "06ad51e8624af959dc7b5994b8453f29"]
                                addon2 = "9d5876394f908ec23b2d54dfb424059b"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names                    
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
