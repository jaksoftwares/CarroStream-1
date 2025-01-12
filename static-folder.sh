#!/bin/bash

# Define the list of apps
apps=("home" "about" "services" "accounts" "dashboard" "booking" "payments" "rewards" "faq" "contact" "policies" "tracking" "feedback" "blog")

# Base directory where static files will be created (assuming it already exists)
base_dir="static"

# Loop through each app and create the necessary directories under the existing static folder
for app in "${apps[@]}"; do
    # Create app-specific static subfolders (css, js, images)
    mkdir -p "$base_dir/$app/css" "$base_dir/$app/js" "$base_dir/$app/images"
    echo "Created static folders for app: $app"
done

echo "Static folders created for all apps!"
