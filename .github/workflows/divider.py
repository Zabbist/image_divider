import os

from PIL import Image
from tkinter import filedialog, Tk
from tkinter import Button

# Set the initial value of the image variable
image = "img1.png"

# Create the main window
root = Tk()
root.title("Save Image")

# Create a function to save the image
def save_image():
    # Open the save file dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")

    # Check if a file was selected
    if file_path:
        # Open the image
        img = Image.open(image)

        # Save the image to the selected location
        img.save(file_path)

# Create a button to save the image
button = Button(root, text="Save Image", command=save_image)
button.pack()

# Run the main loop
root.mainloop()
