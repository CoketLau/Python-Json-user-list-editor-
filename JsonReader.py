import json
import pathlib

Folder = pathlib.Path(__file__).parent
JsonPath = Folder / "Chat.Json"

def Read():
    with open(JsonPath, "r") as JsonFile:
        return json.load(JsonFile)

def AddUser(Name):
    Data = Read()
    Data["Users"].append({"Name": Name, "Online": True, "LastActive": 0})
    Data["ServerStatus"] = "Online"

    with open ("Chat.Json", "w") as JsonFile:
        json.dump(Data, JsonFile, indent=4)

def DeleteUser(Name):
    Data = Read()

    for i in Data["Users"]:
        if i["Name"] == Name:
            Data["Users"].remove(i)
    
    with open ("Chat.Json", "w") as JsonFile:
        json.dump(Data, JsonFile, indent=4)

def ListUsers():
    Data = Read()
    
    for i in Data["Users"]:
        print(i["Name"])



def CallFunctionForTesting():
    while True:
        Data = Read()
        Choice = input("Enter: Add / Delete / List users: ").lower()

        if Choice == "delete":
            WhatUser = input("What user: ")
            
            for i in Data["Users"]:
                if i["Name"] == WhatUser:
                    DeleteUser(WhatUser)
                    print("User removed")
                    break
            else:
                print("User was NOT found")

        if Choice == "add":
            NameNewUser = input("Username: ")

            for i in Data["Users"]:
                if i["Name"] == NameNewUser:
                    print("Username is already being used")
                    break
            else:
                AddUser(NameNewUser)
        
        if Choice == "list":
            ListUsers()


CallFunctionForTesting()