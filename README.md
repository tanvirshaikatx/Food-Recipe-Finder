# 🍲 Food Recipe Finder using Vision Transformer (ViT)

This project demonstrates an intelligent **Food Recipe Finder** that uses **Vision Transformer (ViT)** to identify dishes from images and instantly suggest possible **recipes**.  
Simply upload a photo of your food, and the model predicts the dish name and provides a **detailed recipe** for it — all in one click!

---

## 🚀 Project Overview

The **Food Recipe Finder** combines **Computer Vision** and **Machine Learning** to recognize food items and retrieve their corresponding recipes.  
It uses the **Vision Transformer (ViT)** from the **Hugging Face Transformers** library, which represents one of the most powerful architectures for image classification tasks.  

Once the image is identified, the app maps the predicted food class to a pre-stored recipe or dynamically fetches it, providing users with easy cooking instructions.

---

## 🧩 Features

- 🍕 Upload an image of any common dish (e.g., pizza, burger, sushi, etc.)
- 🧠 Model predicts the **food name** using Vision Transformer (ViT)
- 📖 Displays the **complete recipe**, including ingredients and steps
- 🌐 Deployed on **Hugging Face Spaces** using **Gradio**
- ⚡ Lightweight, fast, and easy-to-use interface
- 🖤 Clean UI with professional design and black-font table styling

---

## 🛠️ Tech Stack

| Category | Tools & Frameworks |
|-----------|--------------------|
| **Language** | Python |
| **Model** | Vision Transformer (ViT) |
| **Library** | Hugging Face Transformers |
| **Interface** | Gradio |
| **Deployment** | Hugging Face Spaces |
| **Data Handling** | Pillow, JSON |
| **Environment** | requirements.txt for reproducibility |

---

## 🧠 Model Description

The model uses:
```python
from transformers import ViTFeatureExtractor, ViTForImageClassification

💻 How It Works

🖼️ The user uploads an image of a food item.

🤖 The Vision Transformer model extracts visual features from image patches.

🧩 The model classifies the dish name (e.g., Pizza, Burger, Pasta).

🥣 The app retrieves and displays a detailed recipe corresponding to the predicted dish.

⚡ Results are shown instantly with an elegant black-font table format for readability.



# Clone the repository
git clone https://huggingface.co/spaces/YourUsername/Food-Recipe-Finder
cd Food-Recipe-Finder

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py


🌍 Deployment

The project is deployed on Hugging Face Spaces using Gradio as the interactive front-end.

👉 Live Demo: https://huggingface.co/spaces/tanvirshaikatx/Food-Recipe-Finder

🧪 Use Cases

🍽️ Smart kitchen assistants

📱 Mobile food recognition apps

🧑‍🍳 Recipe recommendation systems

🧠 Educational projects for AI and computer vision

🚀 Demonstration of transformer models beyond NLP

📊 Future Improvements

🔍 Add multilingual recipe support

🍜 Expand food category dataset for global cuisines

🪄 Add voice-based search or text-based recipe generation using LLMs

🎨 Improve explainability using attention maps

☁️ Connect with external recipe APIs for dynamic updates

👨‍💻 Author

Md. Tanvir Ahmed Shaikat
🎓 B.Sc. in Computer Science and Engineering, Bangladesh University
🧠 Research Interests: Artificial Intelligence, Machine Learning, Computer Vision, NLP
📫 Email: tanvirshaikat40@gmail.com

🔗 Portfolio: Coming Soon
🌍 Hugging Face: YourUsername

🏅 Acknowledgment

Hugging Face for the Transformers and Spaces platforms

Gradio team for simple web deployment

Open-source contributors and datasets

Google Colab for model training support
