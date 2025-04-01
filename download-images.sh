#!/bin/bash

# Create images directory if it doesn't exist
mkdir -p images

# Function to download image
download_image() {
    local url=$1
    local output=$2
    echo "Downloading $output..."
    curl -L "$url" -o "images/$output"
}

# Hero Section Images - Updated with telecom-related images
download_image "https://images.unsplash.com/photo-1516387938699-a93567ec168e?w=1920&h=800&fit=crop" "hero-1.jpg"
download_image "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=1920&h=800&fit=crop" "hero-2.jpg"
download_image "https://images.unsplash.com/photo-1539683255143-73a6b838b106?w=1920&h=800&fit=crop" "hero-3.jpg"

# Service Images
download_image "https://images.unsplash.com/photo-1552581234-26160f608093?w=800&h=600&fit=crop" "voice-solution.jpg"
download_image "https://images.unsplash.com/photo-1556155092-490a1ba16284?w=800&h=600&fit=crop" "sms-service.jpg"
download_image "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=600&fit=crop" "cloud-comm.jpg"
download_image "https://images.unsplash.com/photo-1611746872915-64382b5c76da?w=800&h=600&fit=crop" "whatsapp-business.jpg"

# About Page Images
download_image "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=600&fit=crop" "office.jpg"
download_image "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&h=600&fit=crop" "team.jpg"
download_image "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&h=600&fit=crop" "technology.jpg"
download_image "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&h=600&fit=crop" "culture.jpg"

echo "All images have been downloaded!" 