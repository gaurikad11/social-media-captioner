# 🧊 Social Media Captioner App

Welcome to the **Social Media Captioner App**! 🚀 This web app generates **engaging and platform-specific captions** for your social media posts based on the image you upload and your instructions. Whether you're posting on **LinkedIn**, **Instagram**, or **Twitter**, the app provides **customized captions** in various tones, such as **Professional**, **Funny**, **Sarcastic**, and more, helping you boost your engagement and save time!

## Features

- Upload an image and get an automatic **description**.
- Choose from **multiple platforms** (LinkedIn, Instagram, Twitter) for tailored captions.
- Select the **tone** for your caption, including Cheerful, Professional, Emotional, Funny, etc.
- **Edit** the generated captions directly in the app.

## 👨‍💻 Contributors

- [devyanic11](https://github.com/devyanic11) - Devyani Chavan
- [@gaurikad11](https://github.com/gaurikad11) - Gauri Kad


## Screenshot
![App Screenshot](https://github.com/user-attachments/assets/7e165f92-59ec-4bd0-b125-1d8d64a05950)


## How to Run Locally 🖥️

### Prerequisites

- **Python 3.8+** installed on your machine
- **Pip** (Python package installer)
- Required Python packages (listed below)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/soulkadhi/social-media-captioner.git
    cd social-media-captioner
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Linux/macOS
    .\.venv\Scripts\activate  # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the App

1. **Start the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. The app will open in your default web browser. You can access it at `http://localhost:8501`.

### Uploading an Image

- Once the app is running, you can **upload an image** in the supported formats: **.jpg**, **.jpeg**, **.png**.
- Describe your post and **choose the platform** and tone for your caption.
- The app will generate a **custom caption** tailored to the platform and the image description.

## Example Usage

- **LinkedIn Post**: Upload a professional image, describe your goal, and get a well-crafted LinkedIn post with a catchy intro and a call to action.
- **Instagram Post**: Add an image, select a funny tone, and get a brief and engaging caption perfect for Instagram.
- **Twitter Post**: Stay within the 280-character limit while posting relevant, hashtag-driven content on Twitter.

## Technologies Used

- **Streamlit**: For the web interface
- **LangChain & Ollama**: To generate captions using the **Llama 3.1 model**
- **Pillow (PIL)**: For image processing
- **Python**: Backend and business logic
- **Unsplash API**: For background images in the app

## Contributing

Feel free to fork the repository and submit pull requests! Contributions are always welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out with questions or feedback. Happy captioning! 😊
