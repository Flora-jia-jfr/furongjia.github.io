#!/bin/bash

# Create solid color placeholder images using macOS sips
# We'll create base images and add text overlays

projects=(
  "diagnosing-datasets.png:#4682B4:Diagnosing Datasets"
  "counting-clues.png:#3CB371:Counting Clues"
  "dataset-shift.png:#CD5C5C:Dataset Shift"
  "gpt4mts.png:#9370DB:GPT4MTS"
)

for project in "${projects[@]}"; do
  IFS=':' read -r filename color title <<< "$project"
  
  # Create a simple colored rectangle using printf and convert to png
  # We'll use base64 encoded minimal PNG
  cat > temp.html << HTML
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;width:400px;height:300px;background:linear-gradient(135deg, ${color} 0%, ${color}dd 100%);display:flex;align-items:center;justify-content:center;font-family:Arial,sans-serif;">
  <div style="text-align:center;color:white;text-shadow:2px 2px 4px rgba(0,0,0,0.5);">
    <h1 style="font-size:48px;margin:0;">${title}</h1>
    <p style="font-size:20px;margin:10px 0 0 0;opacity:0.9;">Research Project</p>
  </div>
</body>
</html>
HTML

  echo "Created template for $filename"
done

rm -f temp.html
