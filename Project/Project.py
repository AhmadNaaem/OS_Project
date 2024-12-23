import os
import multiprocessing
import subprocess

# Function to clear the terminal
def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

def process_management_menu():
    while True:
        clear_terminal()
        print("\n PROCESS MANAGEMENT ".center(50, '-'))
        print("1. Create Process and Thread")
        print("2. Show Process List")
        print("3. Share Data Between Processes")
        print("4. Manage Custom Programs")
        print("5. Back to Main Menu")
        print()
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            create_process_and_thread()
        elif choice == '2':
            show_process_list()
        elif choice == '3':
            share_data_between_processes()
        elif choice == '4':
            manage_custom_programs()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Option 1: Create process and thread
def create_process_and_thread():
    clear_terminal()
    def process_task():
        print(f"Process running with PID: {os.getpid()}")

    def thread_task():
        print("Thread running.")

    # Create and start a process
    process = multiprocessing.Process(target=process_task)
    process.start()
    process.join()

    # Create and start a thread
    thread = multiprocessing.Process(target=thread_task)
    thread.start()
    thread.join()

    input("\nPress Enter to return to the menu...")

# Option 2: Show process list
def show_process_list():
    clear_terminal()
    print("\nCurrent processes running on the system:")
    subprocess.run(["ps", "-aux"])  # Lists all processes (Linux-specific)
    input("\nPress Enter to return to the menu...")

# Option 3: Share data between processes
def share_data_between_processes():
    clear_terminal()
    def process1(queue):
        data = "Output of Process 1"
        queue.put(data)
        print("Process 1: Data sent to queue.")

    def process2(queue):
        data = queue.get()
        print(f"Process 2: Received data from Process 1 -> {data}")

    print("\nSelect Process for Communication")
    print("1. Process 1 gives input to Process 2")
    print("2. Process 2 gives input to Process 1")
    option = input("Enter your choice [1-2]: ")

    queue = multiprocessing.Queue()

    if option == '1':
        p1 = multiprocessing.Process(target=process1, args=(queue,))
        p2 = multiprocessing.Process(target=process2, args=(queue,))
    elif option == '2':
        p1 = multiprocessing.Process(target=process2, args=(queue,))
        p2 = multiprocessing.Process(target=process1, args=(queue,))
    else:
        print("Invalid option.")
        input("\nPress Enter to return to the menu...")
        return

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    input("\nPress Enter to return to the menu...")

# Option 4: Manage custom programs
def manage_custom_programs():
    while True:
        clear_terminal()
        print("\n CUSTOM PROGRAM MANAGEMENT ".center(50, '-'))
        print("1. Create and Execute a Python Program")
        print("2. Delete a Custom Program")
        print("3. Back to Process Management Menu")
        print()
        choice = input("Enter your choice [1-3]: ")

        if choice == '1':
            program_name = input("Enter program name (without extension): ") + ".py"
            with open(program_name, "w") as file:
                file.write("""\
# Sample Python program
print("This is a custom Python program.")
                """)
            print(f"Program {program_name} created.")
            print("Executing the program:")
            subprocess.run(["python3", program_name])
            input("\nPress Enter to return to the menu...")
        elif choice == '2':
            program_name = input("Enter program name to delete (without extension): ") + ".py"
            if os.path.exists(program_name):
                os.remove(program_name)
                print(f"Program {program_name} deleted.")
            else:
                print(f"Program {program_name} does not exist.")
            input("\nPress Enter to return to the menu...")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

# Main Menu
def main_menu():
    while True:
        clear_terminal()
        print("\n MAIN MENU ".center(50, '-'))
        print("1. User Management")
        print("2. Service Management")
        print("3. Process Management")
        print("4. Backup")
        print("5. Exit")
        print()
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            print("User Management is not implemented yet.")
            input("\nPress Enter to return to the menu...")
        elif choice == '2':
            print("Service Management is not implemented yet.")
            input("\nPress Enter to return to the menu...")
        elif choice == '3':
            process_management_menu()
        elif choice == '4':
            print("Backup is not implemented yet.")
            input("\nPress Enter to return to the menu...")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main_menu()
