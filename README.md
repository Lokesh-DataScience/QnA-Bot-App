# ChatBotApp

## Project Overview

ChatBotApp is a python webapp for QnA using Llama-3 model.

## Repository Contents

- **ChatBotApp.py**: Python script that provides a graphical user interface (GUI) using Streamlit to demonstrate the ChatBot.
- **ChatBotCode.ipynb**: Jupyter notebook containing the complete code for ChatBot model.
- **requirements.txt**: List of Python libraries required to run `ChatBotApp.py` and `ChatBotCode.ipynb`.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.12
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Lokesh-DataScience/ChatBotApp.git
    cd ChatBotApp
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Demo

To run the GUI demo of the emotion detection model:

```bash
streamlit run ChatBotApp.py
```
### Usage
- **The ChatBotApp.py scripts open a window displaying the interface of streamlit.**
- **The model will take input from user as query and gives related and relevant.**
- **The ChatBotCode.ipynb notebook can be used to understand and reproduce the ChatBot model.**

### Model Details
- **The LangChain is used for ChatBot is saved in the ChatBotCode.ipynb file.**
- **This model is build to get data from `serpapi-search`, `google-serper` and `wikipedia` as per user query.**

### Contributing
- **Contributions are welcome! Please feel free to submit a Pull Request.**

### Acknowledgements
- **Streamlit for providing the tools for GUI and user interaction.**
- **Langchain for the model training.**

