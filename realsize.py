# 5a: Basic size calculation program
def calculate_real_size():
    try:
        specimen_name = input("Enter the name of the specimen: ")
        microscope_size = float(input("Enter the microscope size (in μm): "))
        magnification = float(input("Enter the magnification used: "))
        
        if magnification <= 0:
            print("Magnification must be greater than 0.")
            return

        actual_size = microscope_size / magnification
        print(f"Real-life size of '{specimen_name}' is approximately {actual_size:.4f} μm.")
    except ValueError:
        print("Please enter valid numeric values.")

calculate_real_size()
