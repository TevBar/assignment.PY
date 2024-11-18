service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer,issue):
    if ticket_id in service_tickets:
        print(f"ticket id {ticket_id} already exists")
    else: 
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": open}
        print(f"ticket {ticket_id} has been successfully created.")

def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        if new_status.lower() in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = new_status.lower()
            print(f"{ticket_id} status changed to {new_status}.")
        else: 
            print(f"Must have open ticket as open or closed")


def display_tickets(status_filter = None):
    if status_filter and status_filter.lower() not in ["open", "closed"]:
        print("Error: Status filter must be set to 'open' or 'closed'.")
        return

    print("\nCustomer Service Tickets")
    for ticket_id, details in service_tickets.items():
        if not status_filter or details["Status"] == status_filter.lower():
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
        print()


print("Welcome to the Customer Service Ticket Tracker!")

# Display initial tickets
display_tickets()

# Add a new ticket
open_ticket("Ticket003", "Charlie", "Password reset issue")

# Update the status of a ticket
update_ticket_status("Ticket001", "closed")

# Display tickets filtered by status
print("\nDisplaying only 'open' tickets:")
display_tickets(status_filter="open")

print("\nDisplaying all tickets:")
display_tickets()