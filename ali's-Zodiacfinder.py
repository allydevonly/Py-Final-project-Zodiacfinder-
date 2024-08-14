import tkinter as tk
from tkinter import ttk

# Function to determine zodiac sign
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Invalid Date"

# Function to handle button click
def show_zodiac_sign():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        zodiac_sign = get_zodiac_sign(day, month)
        result_label.config(text=f"Your Zodiac Sign is: {zodiac_sign}")
    except ValueError:
        result_label.config(text="Please enter valid numbers for day and month.")

# Function to show the zodiac sign finder frame
def show_finder_frame():
    welcome_frame.pack_forget()
    finder_frame.pack(fill="both", expand=True)

# Set up the main window
root = tk.Tk()
root.title("Zodiac Sign Finder")
root.geometry("400x300")
root.config(bg="#F0F0F0")

# Style configuration
style = ttk.Style()
style.configure("TLabel",
                font=("Helvetica", 12),
                background="#F0F0F0",
                foreground="#333333")  # Text color for labels
style.configure("TButton",
                font=("Helvetica", 12),
                padding=10,
                background="#007BFF",
                foreground="#000000")  # Text color for button set to black
style.configure("TEntry",
                font=("Helvetica", 12),
                padding=5)

# Create frames
welcome_frame = tk.Frame(root, bg="#F0F0F0")
finder_frame = tk.Frame(root, bg="#F0F0F0")

# Welcome frame content
welcome_label = ttk.Label(welcome_frame, text="Welcome to Ali's Zodiac Sign Finder", font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=50)

start_button = ttk.Button(welcome_frame, text="Start", command=show_finder_frame)
start_button.pack(pady=10)

# Zodiac sign finder frame content
label1 = ttk.Label(finder_frame, text="Enter your birth day (1-31):")
label1.pack(pady=10)

day_entry = ttk.Entry(finder_frame, width=10)
day_entry.pack(pady=5)

label2 = ttk.Label(finder_frame, text="Enter your birth month (1-12):")
label2.pack(pady=10)

month_entry = ttk.Entry(finder_frame, width=10)
month_entry.pack(pady=5)

button = ttk.Button(finder_frame, text="Find Zodiac Sign", command=show_zodiac_sign)
button.pack(pady=15)

result_label = ttk.Label(finder_frame, text="", font=("Helvetica", 14), background="#F0F0F0")
result_label.pack(pady=10)

# Initially show the welcome frame
welcome_frame.pack(fill="both", expand=True)

# Run the application
root.mainloop()
