class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}
        self.customers = {}
        self.admin_password = "admin 123"
        self.load_data()

    def save_data(self):
        # Save rooms
        with open("rooms.txt", "w") as file:
            for room_number, details in self.rooms.items():
                file.write(f"{room_number},{details['type']},{details['price']},{details['occupied']}\n")

        # Save customers
        with open("customers.txt", "w") as file:
            for customer, room_number in self.customers.items():
                file.write(f"{customer},{room_number}\n")

    def load_data(self):
        try:
            with open("rooms.txt", "r") as file:
                for line in file:
                    room_number, room_type, price, occupied = line.strip().split(",")
                    self.rooms[room_number] = {
                        'type': room_type,
                        'price': float(price),
                        'occupied': occupied == 'True'
                    }
        except FileNotFoundError:
            pass

        try:
            with open("customers.txt", "r") as file:
                for line in file:
                    customer, room_number = line.strip().split(",")
                    self.customers[customer] = room_number
        except FileNotFoundError:
            pass

    def add_room(self, room_number, room_type, price):
        self.rooms[room_number] = {'type': room_type, 'price': price, 'occupied': False}
        self.save_data()
        print(f"Room {room_number} added successfully-")

    def book_room(self, customer_name, room_number):
        if room_number in self.rooms and not self.rooms[room_number]['occupied']:
            self.rooms[room_number]['occupied'] = True
            self.customers[customer_name] = room_number
            self.save_data()
            print(f"Room {room_number} booked for {customer_name}.")
        else:
            print("Room is either not available or already occupied.")

    def checkout(self, customer_name):
        if customer_name in self.customers:
            room_number = self.customers[customer_name]
            self.rooms[room_number]['occupied'] = False
            del self.customers[customer_name]
            self.save_data()
            print(f"{customer_name} has checked out from room {room_number} . ")
        else:
            print("Customer not found.")

    def view_rooms(self):
        for room_number, details in self.rooms.items():
            status = "Occupied" if details['occupied'] else "Available"
            print(f"Room {room_number}: Type: {details['type']}, Price: {details['price']}, Status:{status}")

    def admin_login(self):
        password = input("Enter admin password: ")
        if password == self.admin_password:
            return True
        else:
            print("Invalid password.")
            return False

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Room")
            print("2. View Rooms")
            print("3. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                room_number = input("Enter room number: ")
                room_type = input("Enter room type: ")
                price = float(input("Enter room price: "))
                self.add_room(room_number, room_type, price)
            elif choice == '2':
                self.view_rooms()
            elif choice == '3':
                break
            else:
                print("Invalid choice.")

    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. Book Room")
            print("2. Checkout")
            print("3. View Rooms")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                customer_name = input("Enter your name: ")
                room_number = input("Enter room number to book: ")
                self.book_room(customer_name, room_number)
            elif choice == '2':
                customer_name = input("Enter your name: ")
                self.checkout(customer_name)
            elif choice == '3':
                self.view_rooms()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def run(self):
        while True:
            print("******************************************")
            print("* Welcome to the Hotel Management System *")
            print("******************************************")
            print("1. Admin Login")
            print("2. Customer Menu")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                if self.admin_login():
                    self.admin_menu()
            elif choice == '2':
                self.customer_menu()
            elif choice == '3':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    hms = HotelManagementSystem()
    hms.run()
