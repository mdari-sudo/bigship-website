from PIL import Image
from collections import Counter

def extract_dominant_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = list(image.getdata())
    
    # Count frequency of each color
    color_count = Counter(pixels)
    
    # Get the most common colors
    most_common = color_count.most_common(num_colors)
    
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for (r, g, b), count in most_common]
    return hex_colors

if __name__ == "__main__":
    logo_path = r"C:\Users\ADMIN\Desktop\bigship\frontend\public\bigship-logo.jpg"
    colors = extract_dominant_colors(logo_path)
    with open('logo_colors.txt', 'w') as f:
        f.write("Dominant colors from logo:\n")
        for color in colors:
            f.write(color + '\n')
    print("Colors extracted and saved to logo_colors.txt")
