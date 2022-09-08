def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Total Cholesterol")
    print("9 - Quit:")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()

def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)
        
def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif HDL_value < 40:
        return "Low"
    else:
        return "Borderline Low"

def output_HDL_result(hdl_value,charac):
    print("The results for a HDL value of {} is: {}".format(hdl_value, charac))

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)
        
## LDL

def input_LDL ():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)
    
def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130<= LDL_value < 159:
        return "Borderline High"
    elif 160<= LDL_value < 189:
        return "High"
    elif LDL_value >= 190:
        return "Very High"
        
def output_LDL_result(ldl_value, charac):
    print("The result for a LDL value of {} is: {}".format(ldl_value,charac))
        
def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value,answer)
    
def Total_Cholesterol():
    total = int(input_HDL()) + int(input_LDL())
    return int(total)
    
def Total_check(total):
    if total < 200:
        return "Normal"
    elif 200<= total < 239:
        return "Borderline high"
    elif total >= 240:
        return "High"
        
   
def output_Total(total, charac):
    print("The total cholesterol is {} is: {}".format(total, charac))
    
def total_driver():
    value = Total_Cholesterol()
    answer = Total_check(value)
    output_Total(value,answer)
    

interface()
