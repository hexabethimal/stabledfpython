import requests
import base64
import json
import time

your_api_key_from_runpod = "Copy and Paste your API Key here";
your_server_endpoint_from_runpod = "Copy and Paste your endpoint here"

# Define the API endpoint
url = f"{your_server_endpoint_from_runpod}/run"
status_url = f"{your_server_endpoint_from_runpod}/status"

# Define the JSON payload
payload = {
    "input": {
        #Write your description here for what you want the image to look like
        "prompt": "Show me an image of a dinosaur wearing sunglasses riding a surfboard",
        #Write what you don't want the image to include
        "negative_prompt": "blurry, low quality, deformed, ugly, text, watermark, signature",
        #Specify pixel width and height. Lower values will be slightly cheaper but be less quality.
        "height": 1024,
        "width": 1024,
        #Controls the number of denoising steps during image generation. More steps generally improve image quality but increase processing time. A typical range is 20-50 steps
        "num_inference_steps": 45,
        #Used when applying a refiner model to enhance details in the generated image. It determines how many steps the refiner takes to improve textures and fine details.
        "refiner_inference_steps": 50,
        #How strictly the model follows your prompt. Low values: 1-5. High values: 7-15. Extremely high: 20+. Generally use 7-12. For highly detailed prompts, use 12-16.
        "guidance_scale": 9.5,  
        #Controls the fraction of noise added in the initial step. A higher value means more randomness, which can lead to more abstract or creative results.
        "high_noise_frac": 0.8,        
        "scheduler": "K_EULER",
        "num_images": 1,        
    }
}

# Define headers
headers = {
    "Authorization": f"Bearer {your_api_key_from_runpod}",
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Send request to generate image
response_data = response.json()
request_id = response_data.get("id")

# Poll for status update until no longer "IN_QUEUE"
while True:
    status_response = requests.get(f"{status_url}/{request_id}", headers=headers)
    status_data = status_response.json()
    
    if status_data["status"] == "IN_QUEUE" or status_data["status"] == "IN_PROGRESS":
        print("Still processing... Waiting 5 seconds.")
        time.sleep(5)  # Wait before checking again
    else:        
        print("Processing complete!")
        break  # Exit loop when processing is done

# Extract base64 image once status is updated
try:
    base64_image = status_data["output"]["image_url"].split(",")[1]
    image_data = base64.b64decode(base64_image)

    # Save the image
    with open("output_image.png", "wb") as f:
        f.write(image_data)

    print("Image saved successfully!")
except:
    print(f"Error: {status_data}")