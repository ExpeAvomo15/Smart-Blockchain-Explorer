# 🧠 Smart Blockchain Explorer

**Smart Blockchain Explorer** is a lightweight web interface built with Streamlit that allows users to query smart contracts deployed across multiple blockchains using natural language. It leverages the Thirdweb Nebula API to provide intelligent, human-like answers about smart contracts.

## 🚀 Features

* Query smart contracts on over 15 major blockchain networks.
* Ask questions in natural language.
* Optional concise answer mode (<200 characters).
* Clean and user-friendly interface with Streamlit.
* Seamless integration with a powerful AI backend.

## 🛠️ Tech Stack

* **Python 3**
* **Streamlit** for the web interface.
* **Thirdweb Nebula API** for AI-based contract analysis.
* **requests** for HTTP communication.
* **python-dotenv** for environment variable management.

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/smart-blockchain-explorer.git
   cd smart-blockchain-explorer
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your API key:

   ```
   NEBULA_API_KEY=your_secret_key
   ```

## 🧪 Usage

Run the app locally using Streamlit:

```bash
streamlit run app.py
```

Through the interface you can:

* Select a blockchain network.
* Input a smart contract address.
* Ask a question in natural language.
* Choose if you want a short answer.

## 🐳 Docker Usage

1. Build the Docker image:

   ```bash
   docker build -t smart-blockchain-explorer .
   ```

2. Run the container:

   ```bash
   docker run -p 8501:8501 --env-file .env smart-blockchain-explorer
   ```

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application
├── nebula.py           # Nebula API integration logic
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build configuration
├── .dockerignore       # Files to exclude from Docker build
└── .env                # (not included) API keys and environment config
```

## 🔐 Security Notice

* Never commit your `.env` file or your `NEBULA_API_KEY` to source control.
* In production, consider using secrets management tools or environment variables injected via CI/CD.


