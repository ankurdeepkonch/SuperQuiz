import customtkinter as ctk
import random

# 1. LISTS & DICTIONARIES: Full question pool
questions_pool = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Hemingway", "Tolkien", "Dickens"], "answer": "Shakespeare"},
    {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "What is 9 x 9?", "options": ["81", "72", "99", "90"], "answer": "81"},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Gd", "Go"], "answer": "Au"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Thailand", "India"], "answer": "Japan"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Which is the fastest land animal?", "options": ["Lion", "Cheetah", "Tiger", "Horse"], "answer": "Cheetah"},
    {"question": "Largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippo"], "answer": "Blue Whale"},
    {"question": "Which element has symbol O?", "options": ["Oxygen", "Gold", "Silver", "Iron"], "answer": "Oxygen"},
    {"question": "What is 15 + 27?", "options": ["42", "32", "40", "43"], "answer": "42"},
    {"question": "Which planet has rings?", "options": ["Mars", "Saturn", "Earth", "Venus"], "answer": "Saturn"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"], "answer": "Da Vinci"},
    {"question": "Which gas is essential for breathing?", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"], "answer": "Oxygen"},
    {"question": "7 × 8 = ?", "options": ["54", "56", "49", "58"], "answer": "56"},
    {"question": "Who discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Albert Einstein", "Isaac Newton"], "answer": "Alexander Fleming"},
    {"question": "The square root of 144 is?", "options": ["10", "11", "12", "13"], "answer": "12"},
    {"question": "Which is the smallest country in the world?", "options": ["Monaco", "Nauru", "Vatican City", "Malta"], "answer": "Vatican City"},
    {"question": "What is the boiling point of water at sea level?", "options": ["90°C", "95°C", "100°C", "105°C"], "answer": "100°C"},
    {"question": "Which country has the Great Barrier Reef?", "options": ["Australia", "USA", "South Africa", "India"], "answer": "Australia"},
    {"question": "Solve: 50 ÷ 2 × 3 = ?", "options": ["75", "80", "70", "65"], "answer": "75"},
    {"question": "Who is known as the father of modern physics?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "answer": "Albert Einstein"},
    {"question": "Which desert is the largest in the world?", "options": ["Sahara", "Gobi", "Arabian", "Kalahari"], "answer": "Sahara"},
    {"question": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Neptune", "Uranus"], "answer": "Saturn"},
    {"question": "What is the main gas found in the air we breathe?", "options": ["Oxygen", "Hydrogen", "Nitrogen", "Carbon dioxide"], "answer": "Nitrogen"},
    {"question": "How many players are there in a football (soccer) team on the field?", "options": ["9", "10", "11", "12"], "answer": "11"},
    {"question": "The Pythagoras theorem applies to which type of triangle?", "options": ["Equilateral", "Isosceles", "Right-angled", "Scalene"], "answer": "Right-angled"},
    {"question": "Which country is known for the Eiffel Tower?", "options": ["Italy", "Germany", "France", "Spain"], "answer": "France"},
    {"question": "Water freezes at:", "options": ["0°C", "32°C", "100°C", "-1°C"], "answer": "0°C"},
    {"question": "120 ÷ 5 = ?", "options": ["24", "25", "26", "23"], "answer": "24"},
    {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "James Watt"], "answer": "Alexander Graham Bell"},
    {"question": "Which is the largest continent?", "options": ["Africa", "Asia", "Europe", "Antarctica"], "answer": "Asia"},
    {"question": "18 × 6 = ?", "options": ["108", "112", "102", "114"], "answer": "108"},
    {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
    {"question": "Who proposed the theory of relativity?", "options": ["Newton", "Einstein", "Curie", "Darwin"], "answer": "Einstein"},
    {"question": "Which river is the longest in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"question": "100 – 45 × 2 = ?", "options": ["10", "15", "20", "25"], "answer": "10"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Quartz"], "answer": "Diamond"},
    {"question": "Which country is famous for the Taj Mahal?", "options": ["India", "Pakistan", "Bangladesh", "Nepal"], "answer": "India"},
    {"question": "7² + 24² = ?", "options": ["625", "576", "600", "525"], "answer": "625"},
    {"question": "Which vitamin is produced in the skin when exposed to sunlight?", "options": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
    {"question": "The Andes Mountains are located in which continent?", "options": ["Asia", "Africa", "South America", "Europe"], "answer": "South America"},
    {"question": "What is 1/4 of 100?", "options": ["20", "25", "30", "35"], "answer": "25"},
    {"question": "Which element has the atomic number 1?", "options": ["Helium", "Hydrogen", "Oxygen", "Carbon"], "answer": "Hydrogen"},
    {"question": "Which ocean is on the east coast of the United States?", "options": ["Atlantic", "Pacific", "Indian", "Arctic"], "answer": "Atlantic"},
    {"question": "15 + 28 = ?", "options": ["42", "43", "44", "45"], "answer": "43"},
    {"question": "Who is known as the 'Father of Computers'?", "options": ["Charles Babbage", "Alan Turing", "Steve Jobs", "Bill Gates"], "answer": "Charles Babbage"},
    {"question": "Which is the largest land animal?", "options": ["Lion", "Elephant", "Rhino", "Hippo"], "answer": "Elephant"},
    {"question": "11 × 11 = ?", "options": ["111", "121", "112", "122"], "answer": "121"},
    {"question": "Which country has the city of Venice?", "options": ["Spain", "Italy", "Greece", "France"], "answer": "Italy"},
    {"question": "Which organ pumps blood throughout the human body?", "options": ["Lungs", "Liver", "Heart", "Kidney"], "answer": "Heart"},
    {"question": "5 × 5 × 5 = ?", "options": ["100", "125", "150", "115"], "answer": "125"},
    {"question": "Which country is home to the kangaroo?", "options": ["New Zealand", "Australia", "South Africa", "Brazil"], "answer": "Australia"},
    {"question": "The chemical formula of table salt is?", "options": ["NaCl", "KCl", "NaCO3", "CaCl2"], "answer": "NaCl"},
    {"question": "Which gas causes bubbles in soft drinks?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "What is 200 ÷ 4?", "options": ["40", "50", "60", "45"], "answer": "50"},
    {"question": "Which river flows through London?", "options": ["Seine", "Thames", "Danube", "Rhine"], "answer": "Thames"},
    {"question": "Which planet is known as the 'Blue Planet'?", "options": ["Earth", "Neptune", "Uranus", "Saturn"], "answer": "Earth"},
    {"question": "9 + 10 × 2 = ?", "options": ["28", "29", "30", "31"], "answer": "29"},
    {"question": "Which gas is used in electric bulbs?", "options": ["Neon", "Argon", "Oxygen", "Nitrogen"], "answer": "Argon"},
    {"question": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "answer": "Ottawa"},
    {"question": "Which planet is known as the Gas Giant?", "options": ["Earth", "Jupiter", "Mars", "Venus"], "answer": "Jupiter"},
    {"question": "How many colors are there in a rainbow?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Which scientist formulated the laws of motion?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "answer": "Newton"},
    {"question": "What is 36 ÷ 6?", "options": ["5", "6", "7", "8"], "answer": "6"},
    {"question": "Which country is known as the Pearl of Africa?", "options": ["Uganda", "Kenya", "Tanzania", "Ethiopia"], "answer": "Uganda"},
    {"question": "What is the capital of Germany?", "options": ["Berlin", "Munich", "Frankfurt", "Hamburg"], "answer": "Berlin"},
    {"question": "Which planet is famous for its blue color?", "options": ["Earth", "Neptune", "Mars", "Venus"], "answer": "Neptune"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Hemingway", "Dickens", "Tolkien"], "answer": "Shakespeare"},
    {"question": "Which organ in the human body is responsible for detoxification?", "options": ["Liver", "Kidney", "Heart", "Lungs"], "answer": "Liver"},
    {"question": "Which planet is closest to the Earth?", "options": ["Venus", "Mars", "Mercury", "Jupiter"], "answer": "Venus"},
    {"question": "Which country has the city of Sydney?", "options": ["Australia", "USA", "UK", "Canada"], "answer": "Australia"},
    {"question": "Who discovered the law of gravitation?", "options": ["Einstein", "Newton", "Tesla", "Galileo"], "answer": "Newton"},
    {"question": "What is the currency of India?", "options": ["Rupee", "Dollar", "Yen", "Euro"], "answer": "Rupee"},
    {"question": "What is 25 × 4?", "options": ["100", "90", "95", "110"], "answer": "100"},
    {"question": "Which animal is known as the King of Jungle?", "options": ["Tiger", "Lion", "Elephant", "Leopard"], "answer": "Lion"},
    {"question": "Which is the longest river in Africa?", "options": ["Nile", "Congo", "Zambezi", "Niger"], "answer": "Nile"},
    {"question": "What is the capital of Italy?", "options": ["Rome", "Milan", "Venice", "Naples"], "answer": "Rome"},
    {"question": "Which is the smallest continent by area?", "options": ["Europe", "Australia", "Antarctica", "South America"], "answer": "Australia"},
    {"question": "Who is the author of 'Alice in Wonderland'?", "options": ["Lewis Carroll", "J.K. Rowling", "Mark Twain", "Charles Dickens"], "answer": "Lewis Carroll"},
    {"question": "Which gas do humans inhale?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
    {"question": "What is 50 ÷ 5?", "options": ["5", "10", "15", "20"], "answer": "10"},
    {"question": "Which instrument is used to measure atmospheric pressure?", "options": ["Thermometer", "Barometer", "Hygrometer", "Anemometer"], "answer": "Barometer"},
    {"question": "What is the SI unit of electric current?", "options": ["Volt", "Watt", "Ampere", "Ohm"], "answer": "Ampere"},
    {"question": "Which part of a computer is known as its brain?", "options": ["RAM", "CPU", "Hard Disk", "Monitor"], "answer": "CPU"},
    {"question": "Which is the largest internal organ in the human body?", "options": ["Heart", "Lungs", "Liver", "Kidney"], "answer": "Liver"},
    {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": "6"},
    {"question": "Which programming language is primarily used for styling web pages?", "options": ["HTML", "Python", "CSS", "C++"], "answer": "CSS"},
    {"question": "Which layer of the Earth lies directly beneath the crust?", "options": ["Core", "Mantle", "Inner Core", "Outer Core"], "answer": "Mantle"},
    {"question": "What is the national animal of Australia?", "options": ["Koala", "Kangaroo", "Emu", "Dingo"], "answer": "Kangaroo"},
    {"question": "Which blood cells help the body fight infections?", "options": ["Red Blood Cells", "White Blood Cells", "Platelets", "Plasma"], "answer": "White Blood Cells"},
    {"question": "What is the value of 2 to the power of 5?", "options": ["16", "25", "32", "64"], "answer": "32"},
    {"question": "Which device converts electrical energy into mechanical energy?", "options": ["Generator", "Electric Motor", "Transformer", "Battery"], "answer": "Electric Motor"},
    {"question": "Which is the deepest ocean trench in the world?", "options": ["Java Trench", "Tonga Trench", "Mariana Trench", "Puerto Rico Trench"], "answer": "Mariana Trench"},
    {"question": "Who developed the first successful polio vaccine?", "options": ["Louis Pasteur", "Jonas Salk", "Edward Jenner", "Robert Koch"], "answer": "Jonas Salk"},
    {"question": "What does URL stand for?", "options": ["Uniform Resource Locator", "Universal Reference Link", "Unified Resource Language", "Universal Routing Location"], "answer": "Uniform Resource Locator"},
    {"question": "Which mathematical constant represents the ratio of a circle's circumference to its diameter?", "options": ["Euler's Number", "Pi", "Phi", "Infinity"], "answer": "Pi"},
    {"question": "Which metal is liquid at room temperature?", "options": ["Iron", "Copper", "Mercury", "Aluminium"], "answer": "Mercury"}
]

# 2. RANDOMISATION & VARIABLES
selected_questions = random.sample(questions_pool, 10)
current_index = 0
score = 0
selected_option = ""
time_left = 10
timer_id = None

# 3. FILE HANDLING, LOOPS & EXCEPTION HANDLING
def save_score_to_laptop(player_name, final_score):
    try:
        with open("scores.txt", "a") as file:
            file.write(f"{player_name} : {final_score}/10 ({final_score * 10} Coins)\n")
    except Exception as error:
        print("Error saving score:", error)

def get_recent_scores():
    try:
        with open("scores.txt", "r") as file:
            lines = file.readlines()
            board_text = ""
            for line in lines[-5:]:
                board_text = board_text + line
            return board_text
    except FileNotFoundError:
        return "No previous scores yet."

# 4. TIMER, SELECTION & NEXT QUESTION FUNCTIONS
def reset_button_colors():
    btn_a.configure(fg_color="#F3F2FF", text_color="#222222")
    btn_b.configure(fg_color="#F3F2FF", text_color="#222222")
    btn_c.configure(fg_color="#F3F2FF", text_color="#222222")
    btn_d.configure(fg_color="#F3F2FF", text_color="#222222")

def update_timer():
    global time_left, timer_id
    if time_left > 0:
        timer_label.configure(text=f"⏱️ Time Left: {time_left}s")
        time_left = time_left - 1
        timer_id = app.after(1000, update_timer)
    else:
        # When 10s runs out, automatically save selected answer and move to next
        next_question()

def load_question():
    global time_left, timer_id, selected_option
    if timer_id is not None:
        app.after_cancel(timer_id)
        
    selected_option = ""
    reset_button_colors()
    
    q_data = selected_questions[current_index]
    progress_label.configure(text=f"Question {current_index + 1} of 10   |   🪙 Coins: {score * 10}")
    question_label.configure(text=q_data["question"])
    
    btn_a.configure(text="A.  " + q_data["options"][0])
    btn_b.configure(text="B.  " + q_data["options"][1])
    btn_c.configure(text="C.  " + q_data["options"][2])
    btn_d.configure(text="D.  " + q_data["options"][3])
    
    time_left = 10
    update_timer()

def select_answer(option_index, clicked_button):
    global selected_option
    q_data = selected_questions[current_index]
    selected_option = q_data["options"][option_index]
    
    # Reset all buttons to light purple, then highlight the clicked one
    reset_button_colors()
    clicked_button.configure(fg_color="#5A4FCF", text_color="white")

def click_a(): select_answer(0, btn_a)
def click_b(): select_answer(1, btn_b)
def click_c(): select_answer(2, btn_c)
def click_d(): select_answer(3, btn_d)

def next_question():
    global current_index, score
    q_data = selected_questions[current_index]
    
    # Check if the user's selected option is correct before moving on
    if selected_option == q_data["answer"]:
        score = score + 1
        
    current_index = current_index + 1
    
    if current_index < len(selected_questions):
        load_question()
    else:
        finish_quiz()

def finish_quiz():
    global timer_id
    if timer_id is not None:
        app.after_cancel(timer_id)
    timer_label.configure(text="")
    
    player_name = name_entry.get().strip()
    if player_name == "":
        player_name = "Player"
        
    save_score_to_laptop(player_name, score)
    history = get_recent_scores()
    
    btn_a.pack_forget()
    btn_b.pack_forget()
    btn_c.pack_forget()
    btn_d.pack_forget()
    next_btn.pack_forget()
    
    progress_label.configure(text="🎉 QUIZ COMPLETED!")
    question_label.configure(
        text=f"{player_name}, you scored {score}/10 ({score * 10} Coins)!\n\n--- Recent Scores ---\n{history}"
    )
    play_again_btn.pack(pady=20)

def play_again():
    global selected_questions, current_index, score
    selected_questions = random.sample(questions_pool, 10)
    current_index = 0
    score = 0
    
    play_again_btn.pack_forget()
    btn_a.pack(pady=6)
    btn_b.pack(pady=6)
    btn_c.pack(pady=6)
    btn_d.pack(pady=6)
    next_btn.pack(pady=(15, 5))
    load_question()

# 5. GUI DEVELOPMENT
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Super Quiz")
app.geometry("420x680")
app.configure(fg_color="#3B28CC")

progress_label = ctk.CTkLabel(app, text="", font=("Arial", 15, "bold"), text_color="white")
progress_label.pack(pady=(15, 2))

timer_label = ctk.CTkLabel(app, text="⏱️ Time Left: 10s", font=("Arial", 15, "bold"), text_color="#FFD700")
timer_label.pack(pady=(0, 10))

name_entry = ctk.CTkEntry(app, placeholder_text="Enter your name...", width=340, height=36, corner_radius=15)
name_entry.pack(pady=(0, 12))

card = ctk.CTkFrame(app, fg_color="white", corner_radius=25, width=360, height=500)
card.pack(padx=25, pady=5, fill="both", expand=True)

question_label = ctk.CTkLabel(
    card, text="", font=("Arial", 18, "bold"), text_color="#222222", wraplength=300, justify="left"
)
question_label.pack(pady=(25, 20), padx=20)

btn_style = {
    "width": 300, "height": 44, "corner_radius": 22,
    "fg_color": "#F3F2FF", "text_color": "#222222",
    "hover_color": "#5A4FCF", "font": ("Arial", 14, "bold"), "anchor": "w"
}

btn_a = ctk.CTkButton(card, text="", command=click_a, **btn_style)
btn_a.pack(pady=6)

btn_b = ctk.CTkButton(card, text="", command=click_b, **btn_style)
btn_b.pack(pady=6)

btn_c = ctk.CTkButton(card, text="", command=click_c, **btn_style)
btn_c.pack(pady=6)

btn_d = ctk.CTkButton(card, text="", command=click_d, **btn_style)
btn_d.pack(pady=6)

next_btn = ctk.CTkButton(
    card, text="Save & Next ➔", command=next_question,
    width=200, height=42, corner_radius=20, fg_color="#3B28CC", text_color="white", font=("Arial", 14, "bold")
)
next_btn.pack(pady=(15, 5))

play_again_btn = ctk.CTkButton(
    card, text="🔄 Play Again (New Questions)", command=play_again,
    width=260, height=45, corner_radius=22, fg_color="#3B28CC", text_color="white", font=("Arial", 14, "bold")
)

load_question()
app.mainloop()