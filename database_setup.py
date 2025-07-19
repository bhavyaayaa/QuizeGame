import sqlite3

# Connect to the database (creates one if it doesn't exist)
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

# Drop existing table if you want a fresh start
cursor.execute("DROP TABLE IF EXISTS questions")

# Create the questions table
cursor.execute("""
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer TEXT NOT NULL,
    difficulty TEXT NOT NULL
)
""")

# Your 60 questions (20 Easy, 20 Medium, 20 Hard)
questions = [
    # EASY QUESTIONS
    ("What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", "Delhi", "easy"),
    ("Who invented the light bulb?", "Nikola Tesla", "Albert Einstein", "Thomas Edison", "Isaac Newton", "Thomas Edison", "easy"),
    ("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "Mars", "easy"),
    ("How many colors are there in a rainbow?", "5", "6", "7", "8", "7", "easy"),
    ("Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "Blue Whale", "easy"),
    ("What is H2O commonly known as?", "Salt", "Water", "Oxygen", "Hydrogen", "Water", "easy"),
    ("What is the currency of the USA?", "Dollar", "Euro", "Rupee", "Yen", "Dollar", "easy"),
    ("How many legs does a spider have?", "6", "8", "10", "12", "8", "easy"),
    ("Which fruit is known for having its seeds on the outside?", "Apple", "Banana", "Strawberry", "Mango", "Strawberry", "easy"),
    ("Which animal is known as the King of the Jungle?", "Elephant", "Tiger", "Lion", "Leopard", "Lion", "easy"),
    ("How many days are there in a leap year?", "365", "366", "367", "368", "366", "easy"),
    ("What do bees make?", "Milk", "Honey", "Sugar", "Juice", "Honey", "easy"),
    ("Which shape has three sides?", "Square", "Rectangle", "Triangle", "Circle", "Triangle", "easy"),
    ("Which organ pumps blood in our body?", "Brain", "Lungs", "Heart", "Kidney", "Heart", "easy"),
    ("Which part of the plant is underground?", "Stem", "Root", "Leaf", "Flower", "Root", "easy"),
    ("What is the color of the sun?", "Red", "Yellow", "Green", "Blue", "Yellow", "easy"),
    ("Which gas do humans need to breathe?", "Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen", "Oxygen", "easy"),
    ("Which month has 28 days in a common year?", "February", "March", "April", "June", "February", "easy"),
    ("What is the opposite of hot?", "Cold", "Warm", "Heat", "Boil", "Cold", "easy"),
    ("Which insect has colorful wings?", "Ant", "Butterfly", "Bee", "Spider", "Butterfly", "easy"),

    # MEDIUM QUESTIONS
    ("What is the smallest prime number?", "0", "1", "2", "3", "2", "medium"),
    ("Which planet has rings around it?", "Earth", "Saturn", "Mars", "Jupiter", "Saturn", "medium"),
    ("What is the boiling point of water in Celsius?", "90", "95", "100", "105", "100", "medium"),
    ("Which is the longest river in the world?", "Nile", "Amazon", "Ganga", "Yangtze", "Nile", "medium"),
    ("Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", "William Shakespeare", "medium"),
    ("Which metal is liquid at room temperature?", "Gold", "Mercury", "Silver", "Iron", "Mercury", "medium"),
    ("Which part of the body helps in breathing?", "Heart", "Lungs", "Kidney", "Liver", "Lungs", "medium"),
    ("Who discovered gravity?", "Thomas Edison", "Albert Einstein", "Isaac Newton", "Galileo", "Isaac Newton", "medium"),
    ("How many players are there in a cricket team?", "9", "10", "11", "12", "11", "medium"),
    ("Which festival is known as the festival of colors?", "Diwali", "Holi", "Eid", "Christmas", "Holi", "medium"),
    ("What is the national animal of India?", "Lion", "Elephant", "Tiger", "Peacock", "Tiger", "medium"),
    ("What is the square root of 81?", "7", "8", "9", "10", "9", "medium"),
    ("Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci", "medium"),
    ("Which is the highest mountain in the world?", "K2", "Kanchenjunga", "Everest", "Nanda Devi", "Everest", "medium"),
    ("Which is the hardest substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", "Diamond", "medium"),
    ("Who is known as the Father of the Nation in India?", "Bhagat Singh", "Subhas Chandra Bose", "Jawaharlal Nehru", "Mohandas Karamchand Gandhi", "Mohandas Karamchand Gandhi", "medium"),
    ("How many continents are there on Earth?", "5", "6", "7", "8", "7", "medium"),
    ("Which bird can mimic human speech?", "Crow", "Pigeon", "Parrot", "Sparrow", "Parrot", "medium"),
    ("Which vitamin is provided by sunlight?", "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "Vitamin D", "medium"),
    ("Which planet is closest to the Sun?", "Earth", "Mars", "Mercury", "Venus", "Mercury", "medium"),

    # HARD QUESTIONS
    ("What is the powerhouse of the cell?", "Nucleus", "Ribosome", "Mitochondria", "Chloroplast", "Mitochondria", "hard"),
    ("Which gas is most abundant in Earth's atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", "Nitrogen", "hard"),
    ("What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", "Canberra", "hard"),
    ("What is the chemical symbol for gold?", "Au", "Ag", "Gd", "Go", "Au", "hard"),
    ("Which country is known as the Land of the Rising Sun?", "China", "Thailand", "Japan", "South Korea", "Japan", "hard"),
    ("Who developed the theory of relativity?", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", "Albert Einstein", "Albert Einstein", "hard"),
    ("Which is the smallest bone in the human body?", "Femur", "Stapes", "Ulna", "Tibia", "Stapes", "hard"),
    ("How many chambers are there in the human heart?", "2", "3", "4", "5", "4", "hard"),
    ("Which Indian scientist won the Nobel Prize in Physics in 1930?", "C. V. Raman", "Homi Bhabha", "APJ Abdul Kalam", "Vikram Sarabhai", "C. V. Raman", "hard"),
    ("What is the largest organ in the human body?", "Heart", "Liver", "Skin", "Lung", "Skin", "hard"),
    ("Which country hosted the 2016 Summer Olympics?", "China", "Brazil", "UK", "USA", "Brazil", "hard"),
    ("Who wrote the Indian national anthem?", "Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Jawaharlal Nehru", "Rabindranath Tagore", "hard"),
    ("Which is the longest bone in the human body?", "Fibula", "Tibia", "Femur", "Humerus", "Femur", "hard"),
    ("Which planet is known as the Morning Star?", "Mercury", "Venus", "Mars", "Jupiter", "Venus", "hard"),
    ("Who was the first woman Prime Minister of India?", "Pratibha Patil", "Sonia Gandhi", "Indira Gandhi", "Sushma Swaraj", "Indira Gandhi", "hard"),
    ("Which state in India is known as the Spice Garden?", "Kerala", "Tamil Nadu", "Goa", "Karnataka", "Kerala", "hard"),
    ("Which planet has the most moons?", "Saturn", "Jupiter", "Uranus", "Mars", "Saturn", "hard"),
    ("Which is the deepest ocean in the world?", "Indian", "Atlantic", "Southern", "Pacific", "Pacific", "hard"),
    ("Which instrument measures earthquakes?", "Barometer", "Seismograph", "Thermometer", "Altimeter", "Seismograph", "hard"),
    ("Which Mughal emperor built the Taj Mahal?", "Babur", "Akbar", "Shah Jahan", "Aurangzeb", "Shah Jahan", "hard"),
]

# Insert all questions
cursor.executemany("""
INSERT INTO questions (question, option1, option2, option3, option4, answer, difficulty)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", questions)

# Save and close
conn.commit()
conn.close()

print("Database setup complete with all 60 questions.")
