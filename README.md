# ☂️ Umbrella Decision Tool

This interactive Streamlit app demonstrates a decision network based on the classic umbrella example from *Artificial Intelligence: A Modern Approach*. Students can explore expected utility and the value of information using a simple weather forecast scenario.

[https://week10-umbrella-decision-tool.streamlit.app](https://week10-umbrella-decision-tool.streamlit.app)

## 🔧 Features

- Adjust utility values for all outcomes (rain/sun vs. take/leave umbrella)
- Update beliefs based on a weather forecast (Good or Bad)
- Visualize the decision network with Graphviz
- View real-time updates in probabilities and utilities

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/umbrella-decision-tool.git
cd umbrella-decision-tool
```

### 2. Create a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\\Scripts\\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run umbrella_app.py
```

## 📦 Requirements

Dependencies are listed in requirements.txt:

```text
streamlit>=1.0
pandas>=1.0
graphviz>=0.20
```

## 🧠 Educational Use

This tool is ideal for teaching:

- Decision theory
- Bayesian inference
- Value of information

## 📝 License

MIT License. Feel free to use and adapt!