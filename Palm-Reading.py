import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import cv2
import numpy as np

def get_palm_reading(characteristics):
    interpretations = {
        'shape': {
            'square': "A square palm indicates practicality and a grounded nature.",
            'rectangular': "A rectangular palm indicates a strong imagination and creativity."
        },
        'heart_line': {
            'long': "You have a deep capacity for love and emotional fulfillment.",
            'short': "You might struggle with expressing emotions openly."
        },
        'head_line': {
            'curved': "You are flexible in your thinking and adaptable to change.",
            'straight': "You are logical and prefer structured approaches to problems."
        },
        'life_line': {
            'long': "You are likely to have a long and fulfilling life.",
            'short': "You may be more cautious and aware of your health."
        }
    }
    
    reading = []
    
    for feature, value in characteristics.items():
        if feature in interpretations and value in interpretations[feature]:
            reading.append(interpretations[feature][value])
        else:
            reading.append(f"No interpretation found for {feature} = {value}.")
    
    return "\n".join(reading)

def analyze_image(image_path):
    # Example function to analyze palm images
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Could not open the image.")
        return
    
    # Process the image (e.g., converting to grayscale and detecting edges)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Display the processed image using OpenCV
    cv2.imshow('Processed Palm Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Add some feedback based on processed features
    messagebox.showinfo("Image Analysis", "Image processed. Features detected.")

def upload_image():
    file_path = filedialog.askopenfilename(title="Select Palm Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        analyze_image(file_path)

def save_results(characteristics, reading):
    with open("palm_reading_results.txt", "a") as file:
        file.write("Palm Characteristics:\n")
        for feature, value in characteristics.items():
            file.write(f"{feature}: {value}\n")
        file.write("Interpretation:\n")
        file.write(reading + "\n\n")
    
    messagebox.showinfo("Success", "Results saved to palm_reading_results.txt")

def submit_characteristics():
    characteristics = {
        'shape': shape_var.get(),
        'heart_line': heart_line_var.get(),
        'head_line': head_line_var.get(),
        'life_line': life_line_var.get(),
    }

    result = get_palm_reading(characteristics)
    messagebox.showinfo("Palm Reading Interpretation", result)
    save_results(characteristics, result)

def show_help():
    help_text = """Palm Reading Help Section:
1. Select the characteristics of your palm:
   - Shape: Choose between 'Square' and 'Rectangular'.
   - Heart Line: Select 'Long' or 'Short'.
   - Head Line: Choose 'Curved' or 'Straight'.
   - Life Line: Select 'Long' or 'Short'.

2. Upload an image of your palm to analyze its features.

3. Click 'Submit Characteristics' to get your palm reading interpretation.
4. Results will be saved to a text file named 'palm_reading_results.txt'.

"""
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_text_widget = scrolledtext.ScrolledText(help_window, width=50, height=15)
    help_text_widget.insert(tk.END, help_text)
    help_text_widget.config(state=tk.DISABLED)
    help_text_widget.pack()

# Create the main window
root = tk.Tk()
root.title("Palm Reading Application")

# Define variables for input
shape_var = tk.StringVar()
heart_line_var = tk.StringVar()
head_line_var = tk.StringVar()
life_line_var = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Select Palm Shape:").pack()
tk.Radiobutton(root, text="Square", variable=shape_var, value='square').pack()
tk.Radiobutton(root, text="Rectangular", variable=shape_var, value='rectangular').pack()

tk.Label(root, text="Select Heart Line:").pack()
tk.Radiobutton(root, text="Long", variable=heart_line_var, value='long').pack()
tk.Radiobutton(root, text="Short", variable=heart_line_var, value='short').pack()

tk.Label(root, text="Select Head Line:").pack()
tk.Radiobutton(root, text="Curved", variable=head_line_var, value='curved').pack()
tk.Radiobutton(root, text="Straight", variable=head_line_var, value='straight').pack()

tk.Label(root, text="Select Life Line:").pack()
tk.Radiobutton(root, text="Long", variable=life_line_var, value='long').pack()
tk.Radiobutton(root, text="Short", variable=life_line_var, value='short').pack()

tk.Button(root, text="Submit Characteristics", command=submit_characteristics).pack()
tk.Button(root, text="Upload Palm Image", command=upload_image).pack()
tk.Button(root, text="Help", command=show_help).pack()

# Start the GUI event loop
root.mainloop()
