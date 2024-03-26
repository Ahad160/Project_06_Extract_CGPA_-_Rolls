# Open file 1 containing board rolls
My_Class_Rolls=r'E:\Codeing\Python Language\Projects\Project_6_Extract_CGPA_&_Rolls\Main.Files\ALL_Roll.txt'
with open(My_Class_Rolls,"r") as f1:
    board_rolls = f1.readlines()


gai_CGPA=r'E:\Codeing\Python Language\Projects\Project_6_Extract_CGPA_&_Rolls\Main.Files\GAI_CGPA.txt'
# Open file 2 containing board rolls and CGPA
with open(gai_CGPA, "r") as f2:
    board_cgpa = f2.readlines()

# Extract board rolls from file 1
board_rolls = [roll.strip() for roll in board_rolls]

# Open file 3 to write matching rolls and CGPA
with open("file3.txt", "w") as f3:
    # Iterate over board rolls and CGPA in file 2
    for line in board_cgpa:
        # Extract roll and CGPA (if available)
        values = line.strip().split()
        if len(values) > 0:
            roll = values[0]
            cgpa = values[1] if len(values) > 1 else None
            # If roll is in file 1, write it to file 3
            if roll in board_rolls:
                f3.write(f"{roll} {cgpa}\n")
                print(f"Copied {roll} {cgpa}")