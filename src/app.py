from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
import warnings
import requests
import gradio as gr

warnings.filterwarnings('ignore')

# Load the pre-trained Vision Transformer model and feature extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# API key for Recipe information
api_key = "raBfmBnGSgfgvyzu2V+xEg==LOUVUAdCYrYk1a3V"

def identify_image(image_path):
    """Identify the food item in the image."""
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]
    food_name = predicted_label.split(",")[0]
    return food_name

def get_recipe(food_name):
    """Get the recipe information of the identified food item."""
    api_url = f"https://api.api-ninjas.com/v1/recipe?query={food_name}"
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        recipe_info = response.json()
    else:
        recipe_info = {"Error": response.status_code, "Message": response.text}
    return recipe_info

def format_recipe_info(recipe_info):
    """Format the recipe information into an HTML table with visible black text on white background."""
    if "Error" in recipe_info:
        return f"<b>Error:</b> {recipe_info['Error']} - {recipe_info['Message']}"

    if not recipe_info or len(recipe_info) == 0:
        return "No recipe information found."

    recipe_data = recipe_info[0]

    # Create formatted HTML
    table = f"""
    <table border="1" style="
        width: 100%; 
        border-collapse: collapse; 
        font-family: Arial; 
        background-color: white; 
        color: black;">
        
        <tr>
            <th colspan="2" style="
                text-align: center; 
                background-color: #ffedcc; 
                color: black;
                padding: 10px;">
                <h2 style='color: black; margin: 0;'>{recipe_data['title']}</h2>
            </th>
        </tr>
        <tr>
            <td style="background-color: white; color: black; padding: 8px;"><b>Servings</b></td>
            <td style="background-color: white; color: black; padding: 8px;">{recipe_data.get('servings', 'N/A')}</td>
        </tr>
        <tr>
            <td style="background-color: white; color: black; padding: 8px;"><b>Ingredients</b></td>
            <td style="background-color: white; color: black; padding: 8px;">{recipe_data.get('ingredients', 'N/A').replace('|', '<br>')}</td>
        </tr>
        <tr>
            <td style="background-color: white; color: black; padding: 8px;"><b>Instructions</b></td>
            <td style="background-color: white; color: black; text-align: justify; padding: 8px;">
                {recipe_data.get('instructions', 'N/A')}
            </td>
        </tr>
    </table>
    """
    return table


def main_process(image_path):
    """Identify the food item and fetch its recipe."""
    food_name = identify_image(image_path)
    recipe_info = get_recipe(food_name)
    formatted_recipe_info = format_recipe_info(recipe_info)
    return f"<h3>Detected Food: {food_name}</h3><br>{formatted_recipe_info}"

def gradio_interface(image):
    return main_process(image)

# Create the Gradio UI
iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Image(type="filepath", label="Upload a Food Image"),
    outputs="html",
    title="🍽️ Food Recipe Finder",
    description="Upload an image of food to automatically identify it and get a delicious recipe!",
    allow_flagging="never"
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
