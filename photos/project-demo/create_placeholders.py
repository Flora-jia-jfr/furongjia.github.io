from PIL import Image, ImageDraw, ImageFont
import os

# Project details
projects = [
    {
        "filename": "diagnosing-datasets.png",
        "title": "Diagnosing\nDatasets",
        "color": (70, 130, 180)  # Steel blue
    },
    {
        "filename": "counting-clues.png",
        "title": "Counting\nClues",
        "color": (60, 179, 113)  # Medium sea green
    },
    {
        "filename": "dataset-shift.png",
        "title": "Dataset\nShift",
        "color": (205, 92, 92)  # Indian red
    },
    {
        "filename": "gpt4mts.png",
        "title": "GPT4MTS",
        "color": (147, 112, 219)  # Medium purple
    }
]

# Create placeholder images
for project in projects:
    # Create image with gradient background
    img = Image.new('RGB', (400, 300), project['color'])
    draw = ImageDraw.Draw(img)
    
    # Add lighter overlay for depth
    overlay = Image.new('RGB', (400, 300), project['color'])
    draw_overlay = ImageDraw.Draw(overlay)
    for i in range(300):
        alpha = int(255 * (i / 300) * 0.3)
        lighter = tuple(min(255, c + alpha) for c in project['color'])
        draw_overlay.line([(0, i), (400, i)], fill=lighter)
    
    img = overlay
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fallback to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Draw title
    bbox = draw.textbbox((0, 0), project['title'], font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (400 - text_width) / 2
    y = (300 - text_height) / 2 - 20
    
    # Draw text with shadow for depth
    draw.text((x+2, y+2), project['title'], fill=(0, 0, 0, 128), font=font)
    draw.text((x, y), project['title'], fill='white', font=font)
    
    # Add "Research Project" subtitle
    subtitle = "Research Project"
    bbox2 = draw.textbbox((0, 0), subtitle, font=small_font)
    sub_width = bbox2[2] - bbox2[0]
    sub_x = (400 - sub_width) / 2
    sub_y = y + text_height + 10
    draw.text((sub_x, sub_y), subtitle, fill='white', font=small_font)
    
    # Save image
    img.save(project['filename'])
    print(f"Created {project['filename']}")

print("\nAll placeholder images created successfully!")
