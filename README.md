🍲 Food Recipe Finder using Vision Transformer (ViT)
This project demonstrates an intelligent Food Recipe Finder that uses Vision Transformer (ViT) to identify dishes from images and instantly fetches recipes using the API Ninjas Recipe API. Simply upload a photo of your food, and the model predicts the dish name and provides a detailed recipe for it — all in one click!

🚀 Project Overview
The Food Recipe Finder combines Computer Vision and Machine Learning to recognize food items and retrieve their corresponding recipes. It uses the Vision Transformer (ViT) from the Hugging Face Transformers library, which represents one of the most powerful architectures for image classification tasks.

Once the image is identified, the app dynamically fetches recipes from the API Ninjas service, providing users with easy cooking instructions, ingredients, and serving information.

🧩 Features
🍕 Upload an image of any common dish (e.g., pizza, burger, sushi, etc.)

🧠 Model predicts the food name using Vision Transformer (ViT)

🔗 Integrates with API Ninjas Recipe API for real-time recipe data

📖 Displays the complete recipe including ingredients, instructions, and servings

🌐 Deployed on Hugging Face Spaces using Gradio

⚡ Lightweight, fast, and easy-to-use interface

🎨 Clean UI with professional design and responsive table styling

## 🛠️ Tech Stack

| Category | Tools & Frameworks |
|----------|-------------------|
| Language | Python |
| Model | Vision Transformer (ViT) |
| Library | Hugging Face Transformers |
| API | API Ninjas Recipe API |
| Interface | Gradio |
| Image Processing | Pillow (PIL) |
| HTTP Requests | Requests |
| Deployment | Hugging Face Spaces |


💻 How It Works
🖼️ Image Upload: The user uploads an image of a food item through the Gradio interface

🤖 Food Identification: The Vision Transformer model processes the image and classifies the dish

🔍 Recipe Fetching: The app calls API Ninjas Recipe API with the predicted food name

📊 Result Display: The recipe information is formatted into an elegant HTML table and displayed

📋 API Integration
This project integrates with API Ninjas Recipe API to fetch detailed recipe information including:

Recipe title and servings

List of ingredients

Step-by-step cooking instructions

🌍 Deployment
The project is deployed on Hugging Face Spaces using Gradio as the interactive front-end.

👉 Live Demo: https://huggingface.co/spaces/tanvirshaikatx/Food-Recipe-Finder

🧪 Use Cases
🍽️ Smart kitchen assistants

📱 Mobile food recognition apps

🧑‍🍳 Recipe recommendation systems

🧠 Educational projects for AI and computer vision

🚀 Demonstration of transformer models beyond NLP

🔍 Food identification and dietary tracking applications

📊 Future Improvements
🔍 Add multilingual recipe support

🍜 Expand food category dataset for global cuisines

🪄 Add voice-based search or text-based recipe generation using LLMs

🎨 Improve explainability using attention maps

💾 Add caching for frequently searched recipes

⭐ User rating system for recipes

📱 Mobile app version with camera integration

👨‍💻 Author
Md. Tanvir Ahmed Shaikat
🎓 B.Sc. in Computer Science and Engineering, Bangladesh University
🧠 Research Interests: Artificial Intelligence, Machine Learning, Computer Vision, NLP
📫 Email: tanvirshaikat40@gmail.com

🔗 Links
🌍 Hugging Face Space: Food Recipe Finder

🔗 API Ninjas: Recipe API Documentation

🏅 Acknowledgment
Hugging Face for the Transformers and Spaces platforms

Google Research for the Vision Transformer model

API Ninjas for providing the Recipe API

Gradio team for simple web deployment

Open-source contributors and datasets

📄 License
This project is open source and available under the MIT License.

⭐ If you find this project helpful, please give it a star on Hugging Face Spaces!


