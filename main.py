import tkinter as tk
from tkinter import scrolledtext, Label, Frame, Entry, Button

window = tk.Tk()
window.title('Eve - Booking System ChatBot')
window.geometry('600x600')
window.configure(bg='#191919')

guest_name = None
guest_email = None
checkin_date = None
checkout_date = None
reserved_room = None

def clear_message():
    chat_area.delete('1.0', tk.END)

def send_message(event):
    global guest_name, guest_email, checkin_date, checkout_date, reserved_room
    
    user_input_text = user_input.get()
    chat_area.insert(tk.END, f'{user_input_text} <You \n', 'user')
    
    if any(keyword in user_input_text.lower() for keyword in ["Hi", "hi", "Hi!", "Hello", "hello", "Hello!"]):
        chat_area.insert(tk.END, f' Eve> {introduce()} {details()}\n', 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["clear", "clear chat", "Clear chat", "Clear chat."]):
        clear_message()
        chat_area.insert(tk.END, ' Eve> Chat cleared.\n', 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["how are you", "How are you", "How are you?"]):
        chat_area.insert(tk.END, f" Eve> I'm doing good. Thank you for asking! How can I assist you today? {details()}\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["I am interested about something", "Can I ask something", "Can I ask something?", "options"]):
        chat_area.insert(tk.END, f" Eve> Thank you for taking interest in our hotel! What do you want to ask? {details()}\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["amenities", "facilities", "amenity", "facility", "service", "services", "what can you offer", "what are your features?", "What does your hotel offer?"]):
        chat_area.insert(tk.END, f" Eve> {describe_amenities()}\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["describe rooms", "room description", "describe the rooms", "Can you describe the rooms"]):
        chat_area.insert(tk.END, f" Eve> {describe_rooms()}\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["location", "hotel locations", "locations", "Where are you located?", "What are your locations?", "Where are your locations?"]):
        chat_area.insert(tk.END, f" Eve> {locations()}\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["Can we check in early", "early check in", "check-in early", "early check-in", "extend stay", "can we extend our stay", "stay extension", "extend", "extension", "Can we check-in early?", "can we check-in early"]):
        chat_area.insert(tk.END, f" Eve> Early check-in / late check-out depends on room availability and is not guaranteed. An extension of stay has an additional fee of P500 when there is a confirmation from the guest.\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["available", "available rooms", "is there any available rooms", "Is there any available rooms?"]):
        chat_area.insert(tk.END, f" Eve> Thank you for choosing our hotel. Fortunately, we currently have available rooms. To learn more about the rooms that we offer, you can type 'room description'.\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["thank you", "thanks", "thank", "Thank you!", "Thank you"]):
        chat_area.insert(tk.END, " Eve> You're welcome! I'm happy to serve you.\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["contact", "how to contact", "talk to you", "how can I talk to you", "how can I call you", "how do i call you", "how to contact you", "How do I contact you?"]):
        chat_area.insert(tk.END, f" Eve> You can talk to us here! \n{contacts()}\n", 'bot')
    elif any(keyword in user_input_text.lower() for keyword in ["book", "booking", "reservation", "reservations"]):
        chat_area.insert(tk.END, " Eve> To book a reservation, first, please provide your name: \n", 'bot')
    elif guest_name is None:
        guest_name = user_input_text
        chat_area.insert(tk.END, " Eve> Nice! Next, please provide your email address: \n", 'bot')
    elif guest_email is None:
        guest_email = user_input_text
        chat_area.insert(tk.END, " Eve> Great! This time please provide your check-in date in this format MM-DD-YYYY: \n", 'bot')
    elif checkin_date is None:
        checkin_date = user_input_text
        chat_area.insert(tk.END, " Eve> Thank you! Now please provide your check-out date in this format MM-DD-YYYY: \n", 'bot')
    elif checkout_date is None:
        checkout_date = user_input_text
        chat_area.insert(tk.END, f" Eve> Thanks! These are our available rooms: {describe_rooms()} \nPlease type in your desired room: \n", 'bot')
    elif reserved_room is None:
        reserved_room = user_input_text
        chat_area.insert(tk.END, f" Eve> Thank you for providing your details! Here is their summary {guest_reservations()} "
                         f"\n\nWe will send a confirmation email through {guest_email} so we can talk about more details of your reservations." 
                         f"For more information, you can either ask me or contact the following details: {contacts()}\n", 'bot')
    else:
        chat_area.insert(tk.END, " Eve> Sorry. I do not understand. Please type your message with words I can understand.\n", 'bot')
    user_input.delete(0, 'end')

def introduce():
    return (
        "Hello! Welcome to SunCity Hotel and Resort! \n" 
        "\nI'm your virtual assistant, Eve, and I'm here to help you with any questions you have regarding your booking at SunCity Hotel and Resort." 
        "How can I assist you today?\n"
    )
    
def details():
    return (
        "\nYou can type 'contacts' to know our contact details."
        "\nYou can type 'amenity' to know the facilities and amenities that we offer."
        "\nYou can type 'room description' to know the types of rooms that we offer."
        "\nYou can type 'location' to know the locations that we currently have."
        "\nYou can type 'book' to book a reservation.\n"
    )

def contacts():
    return "\nContact Us: +63 912 345 6789 \nEmail Address: suncity@email.com\n"

def describe_amenities():
    return (
        "\nOur hotel and resort offer a wide variety of amenities and facilities."
        "\n \nHere, you can find a poolside bar, swimming pool and jacuzzi, a semi-open & outdoor restaurant, and a gift shop for your souvenirs. There is a fitness center so you can keep your body fit and healthy while enjoying your stay, and conference rooms and banquet facilities for celebrations and important meetings and events."
        "\n \nThere is also outside catering service, laundry service, free Wi-Fi internet access, car parking, and 24-hour security and room service, and disabled room to provide you the best vacation and stay experience, and to cater to different kinds of guests."
        "\n \nOur rooms are air-conditioned, and there are windows that will provide you the perfect sunset view and a fresh sea breeze.\n"
    )

def describe_rooms():
    return (
        "\nOur hotel and resort offer different types of rooms to cater to different kinds of customers and guests."
        "\n \nThe following rooms contain essential amenities and facilities such as toilets, a television, a telephone, tables and chairs, a wardrobe closet, a mini fridge, hotel slippers, and hairdryers. They also contain windows with a perfect sunset and sea view."
        "\n \n   SINGLE ROOM - Contains one single bed; Capacity: 1 person; Room size: 45m^2 \n     PRICE: P800"
        "\n   DOUBLE ROOM - Contains one double bed; Capacity: 2 persons; Room size: 45m^2 \n     PRICE: P1200"
        "\n   TRIPLE ROOM - Contains three single beds; Capacity: 3 persons; Room size: 65m^2 \n      PRICE: P2000"
        "\n   QUAD ROOM - May contain 4 separate single beds, 2 single beds and 1 double bed, or 2 double beds; Capacity: 4 persons; Room size: 85m^2 \n      PRICE: P3000"
        "\n   DELUXE ROOM - Has 1 king-size bed; Apart from the essential amenities, it also contains toiletries, bathrobes and towels, wardrobe closet, is soundproof, a jacuzzi and has a balcony with a perfect sunset and sea view; Capacity: 2 persons; Room size: 85 m^2 \n     PRICE: P5000"
        "\n   SUITE - Has a living room, mini-bar, and two bedrooms; Apart from the essential amenities, it also contains toiletries, bathrobes and towels, wardrobe closet, and is soundproof; Capacity: 4 persons; Room size: 100 m^2 \n     PRICE: P10000\n"
    )
    
def locations():
    return (
        "\nOur hotels and resorts are placed in the following locations:"
        "\nWe have our branch in Batangas, Cavite, Olongapo, and Leyte, strategically positioned to offer you an unforgettable experience."
    )
    
def guest_reservations():
    return (
        "\n\nName: " + str(guest_name) +
        "\nEmail address: " + str(guest_email) +
        "\nCheck-in date: " + str(checkin_date) +
        "\nCheck-out date: " + str(checkout_date) +
        "\nReserved room type: " + str(reserved_room) 
    )
    
logo_text = Label(height=2, width=30, bg='#191919', text='SunCity Hotel and Resort', font=('Gabriola',30), fg='#fdf5a6')
logo_text.place(x=300, y=-30, anchor='n')

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=62, height=22, bg='#282a2d', fg='#ffffff', insertbackground='#ffffff', font=('Candara', 12))
chat_area.place(x=10, y=80)
chat_area.tag_configure('user', foreground='#ffffff', background='#09606a', justify='right')
chat_area.tag_configure('bot', foreground='#ffffff')

input_bg = Frame(height=55, width=500, bg='#43464b')
input_bg.place(x=10, y=520)

sendbtn_bg = Frame(height=55, width=65, bg='#43464b')
sendbtn_bg.place(x=525, y=520)

def on_enter(e):
    user_input.delete(0, 'end')
    user_input.config(fg='#ffffff')

def on_leave(e):
    n = user_input.get()
    user_input.config(fg='#ffffff')
    if n == '' or n == ' ':
        user_input.insert(0, 'Enter message')
        user_input.config(fg='#ffffff')

user_input = Entry(input_bg, width=50, bg='#43464b', font=('Candara', 13), relief=tk.FLAT, border=0)
user_input.place(x=10, y=17)
user_input.insert(0, 'Enter message')
user_input.config(fg='#ffffff')
user_input.bind("<FocusIn>", on_enter)
user_input.bind("<FocusOut>", on_leave)
user_input.bind("<Return>", send_message)

send_btn = Button(sendbtn_bg, height=1, width=3, bg='#43464b', text='➤', font=('Helvetica', 20),
                  activeforeground='#ffffff', fg='#ffffff', relief=tk.FLAT, border=0,
                  activebackground='#43464b', command=send_message)
send_btn.place(x=5, y=4)

window.mainloop()