#!/usr/bin/env python
"""
Image optimization script for Django project.
Converts JPEG/PNG images to WebP and creates responsive variants.
"""
import os
from PIL import Image
from pathlib import Path

# Configuration
MEDIA_DIR = Path(__file__).parent.parent / 'assets' / 'media' / 'vehicles'
RESIZE_SIZES = {
    'small': 400,
    'medium': 600,
    'large': 800
}
QUALITY = 85  # WebP quality (1-100)
JPEG_QUALITY = 85


def optimize_images():
    """Optimize all images in the vehicles directory."""
    
    if not MEDIA_DIR.exists():
        print(f"Media directory not found: {MEDIA_DIR}")
        return
    
    # Get all JPEG/PNG files (exclude already optimized)
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png']:
        image_files.extend(MEDIA_DIR.glob(ext))
    
    # Filter out already-processed variants
    base_images = {
        str(f.stem.replace('_small', '').replace('_medium', '').replace('_large', '')): f
        for f in image_files
        if not any(x in f.name for x in ['_small', '_medium', '_large', '.webp'])
    }
    
    print(f"Found {len(base_images)} base images to optimize")
    
    total_original = 0
    total_optimized = 0
    
    for base_name, filepath in base_images.items():
        print(f"\nProcessing: {filepath.name}")
        
        try:
            # Get original file size
            original_size = filepath.stat().st_size
            total_original += original_size
            
            # Open image
            img = Image.open(filepath)
            
            # Create WebP versions
            for size_name, width in RESIZE_SIZES.items():
                # Calculate height maintaining aspect ratio
                ratio = width / img.width
                height = int(img.height * ratio)
                
                # Resize
                resized = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Save WebP
                webp_name = filepath.stem + f'_{size_name}.webp'
                webp_path = filepath.parent / webp_name
                resized.save(webp_path, 'WEBP', quality=QUALITY)
                webp_size = webp_path.stat().st_size
                
                # Save optimized JPEG
                jpeg_name = filepath.stem + f'_{size_name}.jpg'
                jpeg_path = filepath.parent / jpeg_name
                resized.save(jpeg_path, 'JPEG', quality=JPEG_QUALITY, optimize=True)
                jpeg_size = jpeg_path.stat().st_size
                
                total_optimized += webp_size + jpeg_size
                reduction = ((1 - webp_size / original_size) * 100)
                print(f"  {size_name}: WebP {webp_size:,}B ({reduction:.1f}% reduction)")
        
        except Exception as e:
            print(f"  ERROR: {e}")
    
    if total_original > 0:
        total_reduction = ((1 - total_optimized / total_original) * 100)
        print(f"\nOptimization complete!")
        print(f"Original size: {total_original / 1024 / 1024:.1f} MB")
        print(f"Optimized size: {total_optimized / 1024 / 1024:.1f} MB")
        print(f"Total reduction: {total_reduction:.1f}%")


if __name__ == '__main__':
    optimize_images()
