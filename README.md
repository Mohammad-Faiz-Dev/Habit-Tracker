📈 Pixela Habit Tracker
A simple Python project that uses the Pixela API to track daily habits through graphs — directly from your terminal.
It allows you to:

Create a Pixela user account

Create a habit-tracking graph (e.g., cycling, reading, coding)

Post daily data points (called "pixels")

Automatically log today’s progress

(Optional) Update or delete entries using Pixela’s API

🚀 Features
🧑‍💻 User creation via Pixela API

📊 Graph setup with custom units, names, and colors

✅ Daily pixel logging with today's date

🔁 Optional retry mechanism for free-tier limits

🧱 Extensible for CLI tools, GUIs, or schedulers

🛠 Technologies Used
Tech	Why It's Used
Python	Core language for scripting and API interaction
requests	To make HTTP requests to Pixela's API
datetime	To get and format the current date in Pixela's required format
Pixela API	Free habit tracking via RESTful endpoints

📦 Requirements
Python 3.7+

requests module (install with pip install requests)

🔐 Setup (Important!)
Before running the script, you must provide your own:

python
Copy
Edit
GRAPH_ID = "your-graph-id"
USERNAME = "your-username"
TOKEN = "your-secret-token"
These should not be uploaded to GitHub.
Keep them private for security reasons.

✅ How to Use
Create a user (only once)
Uncomment and run the code block that creates a Pixela user with your token and username.

Create a graph (only once)
Define the graph's name, unit, type, and color — then run that block.

Post a pixel
The script logs today's habit data with a specified quantity (e.g., 7.8 km).

🌱 Example Use Case
You want to track your daily cycling distance:

Run the script once to create the graph.

Each day, run it again with updated quantity.

Over time, you’ll see a beautiful graph hosted at https://pixe.la/@yourusername.

📚 Pixela Docs
See full documentation: https://docs.pixe.la/

🤝 Contributing
Pull requests are welcome. Feel free to open an issue if you want to discuss something or add new features (like update/delete pixels, UI, or CLI support).

📜 License
MIT — free to use, modify, and share.
Just don’t upload sensitive data like tokens!

