Here’s a GitHub README.md draft for your project:



 🍽️ Restaurant Name & Menu Generator

This project uses **Google Gemini** and **LangChain** to automatically generate a **fancy restaurant name** and a **menu** based on a chosen cuisine.
It provides an interactive **Streamlit** interface for quick and fun experimentation.

 🚀 Features

* Pick a cuisine (e.g., Indian, Mexican, Italian, etc.)
* Get an AI-generated **unique restaurant name**
* Automatically receive a **menu list** for that restaurant
* Powered by **Google Gemini (via LangChain)** for natural language generation
* Simple **Streamlit web app** interface

---

 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** – Web app framework
* **LangChain** – LLM orchestration
* **Google Gemini API** – AI text generation

---

 📂 Project Structure

```
.
├── main.py                # Streamlit app entry point
├── langchain_helper.py    # LLM logic with LangChain and Gemini
└── requirements.txt       # Python dependencies
```

---

⚙️ Installation & Setup

1️⃣ Clone the repository

```bash
git clone https://github.com/Atharv-M/Restaurant-Name-Generator.git
cd Restaurant-Name-Generator
```

2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Set up Google API Key

* Get your **Google Gemini API key** from [Google AI Studio](https://makersuite.google.com/app/apikey)
* In `langchain_helper.py`, set:

```python
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
```

Or export it as an environment variable:

```bash
export GOOGLE_API_KEY="your_api_key_here"   # Mac/Linux
set GOOGLE_API_KEY="your_api_key_here"     # Windows
```

---

 ▶️ Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

1. Select a **cuisine** from the sidebar.
2. Get a **restaurant name** and menu generated instantly.
3. Enjoy the creativity! 🎉

---

 📸 Screenshot

*(Add screenshot here)*

---

📌 Example Output

**Cuisine:** Italian
**Restaurant Name:** *La Dolce Vita*
**Menu:**

* Margherita Pizza
* Spaghetti Carbonara
* Tiramisu
* Caprese Salad

---

 🤝 Contributing

Pull requests are welcome! If you have ideas for new features (like logo generation or price suggestions), feel free to fork and submit.

---

 📜 License

This project is licensed under the MIT License.

---


