from PIL import Image
import json
import os

def pack_atlas():
    asset_root = "public/assets"
    dist_dir = "dist"
    
    # Ensure dist directory exists
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
        
    master_size = 1024 # Standard 1k texture
    atlas_img = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
    
    # The Manifest (The map for the Game Engine/LLM)
    atlas_data = {
        "frames": {},
        "meta": {
            "image": "spritesheet.png",
            "format": "RGBA8888",
            "size": {"w": master_size, "h": master_size},
            "scale": "1"
        }
    }

    current_x, current_y = 0, 0
    row_h = 0

    # 1. Scan all subdirectories in public/assets (The Distributed Islands)
    asset_folders = [f for f in os.listdir(asset_root) if os.path.isdir(os.path.join(asset_root, f))]
    asset_folders.sort()

    for folder in asset_folders:
        sprite_path = os.path.join(asset_root, folder, "sprite.png")
        if not os.path.exists(sprite_path):
            continue
            
        src = Image.open(sprite_path)
        sw, sh = src.size
        # Pro-logic: Assume horizontal strips where height = frame size
        fw, fh = sh, sh
        count = sw // fw
        
        print(f"Baking {folder}: {count} frames...")

        for i in range(count):
            frame = src.crop((i * fw, 0, (i+1) * fw, fh))
            
            if current_x + fw > master_size:
                current_x = 0
                current_y += row_h
                row_h = 0
            
            if current_y + fh > master_size:
                print("Error: Atlas exceeded master size limit!")
                break
                
            atlas_img.paste(frame, (current_x, current_y))
            
            # Map frames: name_0, name_1 or just name if single frame
            frame_name = f"{folder}_{i}" if count > 1 else folder
            atlas_data["frames"][frame_name] = {
                "frame": {"x": current_x, "y": current_y, "w": fw, "h": fh},
                "sourceSize": {"w": fw, "h": fh},
                "spriteSourceSize": {"x": 0, "y": 0, "w": fw, "h": fh}
            }
            
            row_h = max(row_h, fh)
            current_x += fw

    # 2. Save production artifacts
    atlas_img.save(os.path.join(dist_dir, "spritesheet.png"))
    with open(os.path.join(dist_dir, "spritesheet.json"), "w") as f:
        json.dump(atlas_data, f, indent=2)
    
    print("\nBaking Successful!")
    print(f"Artifacts created in: {dist_dir}/")

if __name__ == "__main__":
    pack_atlas()
