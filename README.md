# 🎨 Hemanth's Photo Colorizer

Bring your old black-and-white images to life with vibrant colors using deep learning! This web application allows you to upload grayscale images and receive fully colorized outputs powered by an autoencoder-based image-to-image translation model.

🌐 **Live Demo:** [https://imagecolorizer-weld.vercel.app](https://imagecolorizer-weld.vercel.app)

---

## 📸 What It Does

This app takes grayscale (black & white) images as input and produces colorized versions using a pre-trained deep learning model. It's useful for:

- Restoring old family photos
- Colorizing historical black & white images
- Enhancing grayscale artwork

---

## 🚀 How It Works

### 🔧 Backend (FastAPI + Deep Learning)

The backend is deployed on [Render](https://render.com) and powered by a Convolutional Autoencoder trained for image colorization.

#### 🧠 Model Overview: Autoencoder for Colorization

Autoencoders are neural networks designed to learn efficient representations of data:

- **Encoder**: Compresses the input grayscale image into a lower-dimensional latent space.
- **Decoder**: Reconstructs the RGB image from the latent representation.

For colorization:
- Input is a **1-channel grayscale image** (L channel from LAB color space).
- The model predicts the missing **a and b channels** (color information).
- Output is a **3-channel RGB image** after merging the L, a, and b channels and converting back to RGB.

This method enables the model to "imagine" plausible color distributions based on context, textures, and object structures.

### 🧪 Inference Flow

1. Grayscale image is uploaded via the frontend.
2. The image is sent to the backend FastAPI server.
3. The server loads the model and processes the image.
4. The resulting colorized image is sent back to the frontend as a JPEG blob.
5. The user sees a side-by-side comparison of the input and output images.

---

## 💻 Frontend (HTML, CSS, JS)

- Built using HTML/CSS/JavaScript
- Responsive, clean UI with modern design
- Upload and view both original and colorized images side-by-side
- Hosted on **Vercel**: [https://imagecolorizer-weld.vercel.app](https://imagecolorizer-weld.vercel.app)

---

## 🧰 Technologies Used

| Layer        | Tech Stack              |
|--------------|--------------------------|
| Frontend     | HTML, CSS, JavaScript    |
| Backend      | FastAPI (Python)         |
| Deep Learning| CNN-based Autoencoder (OpenCV, NumPy, Keras/PyTorch) |
| Hosting      | Vercel (Frontend), Render (Backend) |

---

## 📂 Folder Structure
📁 backend/
├── main.py # FastAPI server
├── colorize.py # Image colorization logic
├── model.py # Model Logic
└── model.pth/ # Saved autoencoder model

📁 frontend/
└──  index.html # UI for uploading and viewing results which include css and js .

📌 Notes
For best results, upload clear black and white portraits or landscapes.

Model predictions are based on general color patterns; results may vary based on image quality and training data.

📧 Contact
Made  by Challapalli Satya Venkata Hemanth

For suggestions or feedback, feel free to open an issue or reach out on GitHub!

🔮 Future Plans
To improve both the performance and accuracy, I plan to:

🔁 Switch to a GAN-based model (e.g., Pix2Pix or DeOldify) for more realistic and vivid colors.

⚡ Add GPU acceleration on the backend to speed up processing time.

🧠 Train on a larger and more diverse dataset for better generalization.

📥 Enable image downloads so users can save the colorized output.

🔍 Add a progress bar or loading spinner for a smoother user experience.

📱 Make the UI more mobile-friendly with drag & drop support.

🧩 Integrate optional color style transfer (e.g., choose vintage or modern coloring styles).


![image](https://github.com/user-attachments/assets/4f30f5b5-9347-4b31-b7bd-79fb5b3de6ab)


![image](https://github.com/user-attachments/assets/c4b95eb9-5906-4001-a8e2-97e96ff9cd0e)

![image](https://github.com/user-attachments/assets/90edeb93-eaed-40b8-a8d9-e54fe621eb9e)

if a clear or proper image is not given the output may look like below 

![image](https://github.com/user-attachments/assets/65a7c015-158b-48e3-b646-39672ce19255)



