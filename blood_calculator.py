def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit:")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return 

def input_HDL():
    HDL_input = input("Enter the HDL value:)
    return int(HDL_input)
        
def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal":
    elif HDL_value < 40:
        return "Low"
    else:
        return "Borderline Low"

interface()
