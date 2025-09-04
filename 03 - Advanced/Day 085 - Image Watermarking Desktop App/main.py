import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarker")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f0f0')

        # Variables
        self.original_image = None
        self.watermarked_image = None
        self.preview_image = None
        self.watermark_text = tk.StringVar(value="Your Website Here")
        self.watermark_size = tk.IntVar(value=36)
        self.watermark_opacity = tk.IntVar(value=128)
        self.watermark_color = "#FFFFFF"
        self.position_var = tk.StringVar(value="bottom-right")

        self.setup_ui()

    def setup_ui(self):
        # Main title
        title_label = tk.Label(self.root, text="Image Watermarker",
                               font=("Arial", 20, "bold"),
                               bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=10)

        # File upload section
        upload_frame = tk.Frame(self.root, bg='#f0f0f0')
        upload_frame.pack(pady=10)

        self.upload_btn = tk.Button(upload_frame, text="Select Image",
                                    command=self.upload_image,
                                    font=("Arial", 12),
                                    bg='#4CAF50', fg='white',
                                    padx=20, pady=5)
        self.upload_btn.pack(side=tk.LEFT, padx=5)

        self.file_label = tk.Label(upload_frame, text="No file selected",
                                   bg='#f0f0f0', fg='#666666')
        self.file_label.pack(side=tk.LEFT, padx=10)

        # Settings frame
        settings_frame = tk.LabelFrame(self.root, text="Watermark Settings",
                                       font=("Arial", 12, "bold"),
                                       bg='#f0f0f0', fg='#333333')
        settings_frame.pack(pady=10, padx=20, fill='x')

        # Text input
        tk.Label(settings_frame, text="Watermark Text:",
                 bg='#f0f0f0').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        text_entry = tk.Entry(settings_frame, textvariable=self.watermark_text,
                              width=30, font=("Arial", 10))
        text_entry.grid(row=0, column=1, padx=5, pady=5)

        # Font size
        tk.Label(settings_frame, text="Font Size:",
                 bg='#f0f0f0').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        size_scale = tk.Scale(settings_frame, from_=12, to=212,
                              orient=tk.HORIZONTAL, variable=self.watermark_size)
        size_scale.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        # Opacity
        tk.Label(settings_frame, text="Opacity:",
                 bg='#f0f0f0').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        opacity_scale = tk.Scale(settings_frame, from_=50, to=255,
                                 orient=tk.HORIZONTAL, variable=self.watermark_opacity)
        opacity_scale.grid(row=2, column=1, sticky='w', padx=5, pady=5)

        # Color picker
        tk.Label(settings_frame, text="Text Color:",
                 bg='#f0f0f0').grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.color_btn = tk.Button(settings_frame, text="Choose Color",
                                   command=self.choose_color,
                                   bg=self.watermark_color, width=15)
        self.color_btn.grid(row=3, column=1, sticky='w', padx=5, pady=5)

        # Position selection
        tk.Label(settings_frame, text="Position:",
                 bg='#f0f0f0').grid(row=4, column=0, sticky='w', padx=5, pady=5)
        position_frame = tk.Frame(settings_frame, bg='#f0f0f0')
        position_frame.grid(row=4, column=1, sticky='w', padx=5, pady=5)

        positions = [("Top Left", "top-left"), ("Top Right", "top-right"),
                     ("Bottom Left", "bottom-left"), ("Bottom Right", "bottom-right"),
                     ("Center", "center")]

        for i, (text, value) in enumerate(positions):
            tk.Radiobutton(position_frame, text=text, variable=self.position_var,
                           value=value, bg='#f0f0f0').grid(row=i // 3, column=i % 3,
                                                           sticky='w', padx=2)

        # Preview and process buttons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)

        self.preview_btn = tk.Button(button_frame, text="Preview Watermark",
                                     command=self.preview_watermark,
                                     font=("Arial", 12),
                                     bg='#2196F3', fg='white',
                                     padx=15, pady=5, state='disabled')
        self.preview_btn.pack(side=tk.LEFT, padx=5)

        self.save_btn = tk.Button(button_frame, text="Save Watermarked Image",
                                  command=self.save_image,
                                  font=("Arial", 12),
                                  bg='#FF9800', fg='white',
                                  padx=15, pady=5, state='disabled')
        self.save_btn.pack(side=tk.LEFT, padx=5)

        # Preview area
        self.preview_frame = tk.LabelFrame(self.root, text="Preview",
                                           font=("Arial", 12, "bold"),
                                           bg='#f0f0f0', fg='#333333')
        self.preview_frame.pack(pady=10, padx=20, fill='both', expand=True)

        self.preview_label = tk.Label(self.preview_frame,
                                      text="Upload an image to see preview here",
                                      bg='white', fg='#666666',
                                      font=("Arial", 14))
        self.preview_label.pack(expand=True, fill='both', padx=10, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
                       ("All files", "*.*")]
        )

        if file_path:
            try:
                self.original_image = Image.open(file_path)
                self.file_label.config(text=f"Selected: {os.path.basename(file_path)}")
                self.preview_btn.config(state='normal')
                self.save_btn.config(state='normal')
                self.show_original_preview()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def show_original_preview(self):
        if self.original_image:
            # Resize image for preview
            display_image = self.original_image.copy()
            display_image.thumbnail((400, 300), Image.Resampling.LANCZOS)

            # Convert to PhotoImage for display
            self.preview_image = ImageTk.PhotoImage(display_image)
            self.preview_label.config(image=self.preview_image, text="")

    def choose_color(self):
        color = colorchooser.askcolor(color=self.watermark_color)
        if color[1]:  # If user didn't cancel
            self.watermark_color = color[1]
            self.color_btn.config(bg=self.watermark_color)

    def get_watermark_position(self, img_width, img_height, text_width, text_height):
        margin = 20
        position = self.position_var.get()

        positions = {
            "top-left": (margin, margin),
            "top-right": (img_width - text_width - margin, margin),
            "bottom-left": (margin, img_height - text_height - margin),
            "bottom-right": (img_width - text_width - margin,
                             img_height - text_height - margin),
            "center": ((img_width - text_width) // 2,
                       (img_height - text_height) // 2)
        }

        return positions.get(position, positions["bottom-right"])

    def create_watermark(self):
        if not self.original_image:
            return None

        # Create a copy of the original image
        watermarked = self.original_image.copy()

        # Create a transparent overlay for the watermark
        overlay = Image.new('RGBA', watermarked.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        # Try to use a better font, fall back to default if not available
        try:
            font = ImageFont.truetype("arial.ttf", self.watermark_size.get())
        except:
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf",
                                          self.watermark_size.get())
            except:
                font = ImageFont.load_default()

        # Get text dimensions
        text = self.watermark_text.get()
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Get position
        x, y = self.get_watermark_position(watermarked.width, watermarked.height,
                                           text_width, text_height)

        # Convert hex color to RGB and add opacity
        color = self.watermark_color.lstrip('#')
        rgb_color = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
        rgba_color = rgb_color + (self.watermark_opacity.get(),)

        # Draw the watermark text
        draw.text((x, y), text, font=font, fill=rgba_color)

        # Composite the overlay onto the original image
        if watermarked.mode != 'RGBA':
            watermarked = watermarked.convert('RGBA')

        watermarked = Image.alpha_composite(watermarked, overlay)

        # Convert back to RGB if original was RGB
        if self.original_image.mode == 'RGB':
            watermarked = watermarked.convert('RGB')

        return watermarked

    def preview_watermark(self):
        try:
            self.watermarked_image = self.create_watermark()

            if self.watermarked_image:
                # Resize for preview
                display_image = self.watermarked_image.copy()
                display_image.thumbnail((400, 300), Image.Resampling.LANCZOS)

                # Convert to PhotoImage for display
                self.preview_image = ImageTk.PhotoImage(display_image)
                self.preview_label.config(image=self.preview_image, text="")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create watermark: {str(e)}")

    def save_image(self):
        if not self.watermarked_image:
            self.preview_watermark()  # Create watermark if not already done

        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"),
                           ("JPEG files", "*.jpg"),
                           ("All files", "*.*")]
            )

            if file_path:
                try:
                    # Save with appropriate format
                    if file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg'):
                        # Convert to RGB for JPEG
                        save_image = self.watermarked_image.convert('RGB')
                        save_image.save(file_path, 'JPEG', quality=95)
                    else:
                        self.watermarked_image.save(file_path)

                    messagebox.showinfo("Success",
                                        f"Watermarked image saved successfully!\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image: {str(e)}")


def main():
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()