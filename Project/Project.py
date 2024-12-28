import os
import multiprocessing
import subprocess
import signal
import shutil

class Backup:
    @staticmethod
    def backup_file(source_file, destination):
        clear_terminal()
        try:
            if not os.path.isfile(source_file):
                print(f"Error: {source_file} is not a valid file.")
                return

            if not os.path.exists(destination):
                os.makedirs(destination)

            with open(source_file, 'rb') as src, open(os.path.join(destination, os.path.basename(source_file)), 'wb') as dest:
                dest.write(src.read())

            print(f"File '{source_file}' has been backed up to '{destination}'.")
        except Exception as e:
            print(f"Error during file backup: {e}")

    @staticmethod
    def backup_dir(source_dir, destination):
        try:
            if not os.path.isdir(source_dir):
                print(f"Error: {source_dir} is not a valid directory.")
                return

            destination_path = os.path.join(destination, os.path.basename(source_dir))

            if os.path.exists(destination_path):
                print(f"Error: Destination directory '{destination_path}' already exists.")
                return

            # Copy the entire directory and its contents
            shutil.copytree(source_dir, destination_path)
            print(f"Directory '{source_dir}' has been backed up to '{destination_path}'.")

        except Exception as e:
            print(f"Error during directory backup: {e}")


    def back_menu():
        destination = '/home/oslab'  # Set the backup destination path

        while True:
            clear_terminal()     
            print("Backup System")
            print("1. Backup a file")
            print("2. Backup a directory")
            print("3. Exit")

            choice = input("Enter your choice [1-3]: ")

            if choice == "1":
                source_file = input("Enter the path of the file to back up: ")
                clear_terminal()
                Backup.backup_file(source_file, destination)
            elif choice == "2":
                source_dir = input("Enter the path of the directory to back up: ")
                Backup.backup_dir(source_dir, destination)
            elif choice == "3":
                print("We out")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

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
        input("\nPress Enter to return to the menu...")

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
            print("User Management Script")
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
                print("4. Delete Process")
                print("5. Back to Main Menu")
                print()
                choice = input("Enter your choice [1-5]: ")
        
                if choice == '1':
                    Process_Management.create_process_and_thread()
                elif choice == '2':
                    Process_Management.show_process_list()
                elif choice == '3':
                    Process_Management.share_data_between_processes()
                elif choice == '4':
                    pid = int(input("Enter PID to delete: "))
                    Process_Management.del_process(pid)
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
            subprocess.run(["sudo","ps", "-ef"])  # Lists all processes (Linux-specific)
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
        def del_process(pid):
            try:
                # Try to terminate gracefully first
                os.kill(pid, signal.SIGTERM)  # Graceful termination
                print(f"Process with PID {pid} terminated successfully using SIGTERM.")
            except ProcessLookupError:
                print(f"No process found with PID {pid}.")
            except PermissionError:
                print(f"Permission denied to terminate process with PID {pid}. Try running as superuser.")
            except Exception as e:
                print(f"An error occurred while attempting to terminate the process: {e}")

            # If process doesn't terminate, force it using SIGKILL (last resort)
            try:
                os.kill(pid, signal.SIGKILL)  # Forceful termination
                print(f"Process with PID {pid} terminated successfully using SIGKILL.")
            except Exception as e:
                print(f"Failed to forcefully terminate the process: {e}")

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
            Backup.back_menu()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main_menu()
