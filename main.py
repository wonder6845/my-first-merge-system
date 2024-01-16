#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt", "r") as start:
    letters = start.read()


with open("Input/Names/invited_names.txt", "r") as send:
    send_list = send.readlines()

for name in send_list:
    remove_space_name = name.strip()
    fixed_letter = letters.replace("[name]", remove_space_name)
    fixed_letter = fixed_letter.replace("Angela", "Hong")

    file_name = f"Output/ReadyToSend/To_{remove_space_name}.txt"

    with open(file_name, "w") as mail:
        mail.write(fixed_letter)