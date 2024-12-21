# Add patients Project
patients = []

def add_patient():
    name = input("Enter patient name: ").strip()
    patient_id = input("Enter patient ID: ").strip()
    
    for patient in patients:
        if patient["name"] == name and patient["id"] == patient_id:
            print(f"Patient '{name}' with ID '{patient_id}' already exists!\n")
            return

    patients.append({"name": name, "id": patient_id})
    print(f"Patient '{name}' added successfully!\n")

def display_patients():
    if not patients:
        print("No patients in the list.\n")
        return

    print("\nPatient List:")
    for index, patient in enumerate(patients, start=1):
        print(f"{index}. {patient['name']} (ID: {patient['id']})")
    print()

while True:
    print("1. Add a patient")
    print("2. Display patients")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print(" Invalid choice. Please enter 1, 2, or 3.\n")
