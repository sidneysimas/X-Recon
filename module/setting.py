from module.banner import custom_input
import json
from colorama import Fore

def change_setting(json_file, new_max_depth,status):

    with open(json_file, 'r') as file:
        data = json.load(file)
        
    if status == "MXDH":

        data['max_depth'] = int(new_max_depth)

        with open(json_file, 'w') as file:
            json.dump(data, file,indent=4)


    
def Change_MaxDepth():
     
    max_depth_val = json.loads(open("setting.json").read())['max_depth']
    print(f"{Fore.GREEN} Ok, Your Max Depth is {Fore.RED}{max_depth_val}{Fore.GREEN} if You Want change this. give me a number(2-5)\n")
    mxdt = int(custom_input("SETTING"))
    if mxdt < 2 or mxdt > 6:
        exit("Please enter a number in the range of 2 to 6")
    change_setting("setting.json",mxdt,"MXDH")