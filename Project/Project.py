import os
import multiprocessing
import subprocess

class UserManagement:
    @staticmethod
    def clear_terminal():
        os.system("clear" if os.name == "posix" else "cls")

    @staticmethod
    def create_user():
        UserManagement.clear_terminal()
        username = input("Enter the username to create: ")
        try:
            subprocess.run(["sudo", "adduser", username], check=True)
            print(f"User '{username}' created successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to create user '{username}'.")

    @staticmethod
    def change_password():
        UserManagement.clear_terminal()
        username = input("Enter the username to change the password for: ")
        try:
            subprocess.run(["sudo", "passwd", username], check=True)
            print(f"Password for user '{username}' changed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to change password for user '{username}'.")

    @staticmethod
    def list_users():
        UserManagement.clear_terminal()
        try:
            with open("/etc/passwd", "r") as f:
                users = [line.split(":")[0] for line in f.readlines()]
            print("\nExisting users:")
            for user in users:
                print(user)
        except Exception as e:
            print(f"Failed to list users: {e}")

    @staticmethod
    def delete_user():
        UserManagement.clear_terminal()
        username = input("Enter the username to delete: ")
        confirm = input(f"Are you sure you want to delete the user '{username}'? This action cannot be undone (yes/no): ")
        if confirm.lower() == 'yes':
            try:
                subprocess.run(["sudo", "deluser", username], check=True)
                print(f"User '{username}' deleted successfully.")
            except subprocess.CalledProcessError:
                print(f"Failed to delete user '{username}'.")
        else:
            print("Deletion cancelled.")

    @staticmethod
    def user_mgmt():
        while True:
            UserManagement.clear_terminal()
            print("\nLinux User Management Script")
            print("1. Create a user")
            print("2. Change password of a user")
            print("3. List all users")
            print("4. Delete a user")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                UserManagement.create_user()
            elif choice == '2':
                UserManagement.change_password()
            elif choice == '3':
                UserManagement.list_users()
            elif choice == '4':
                UserManagement.delete_user()
            elif choice == '5':
                print("Exiting the script.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
# Function to clear the terminal
def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

class Process_Management:
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
            UserManagement.user_mgmt() 
        elif choice == '2':
            print("Service Management is not implemented yet.")
            input("\nPress Enter to return to the menu...")
        elif choice == '3':
            Process_Management.process_management_menu()
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
