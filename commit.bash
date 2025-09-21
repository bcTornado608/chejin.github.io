#!/bin/bash

# Get today's date in YYYY-MM-DD format
DATE=$(date +%Y-%m-%d)

# Add all changes
git add --all

# Commit with date as message
git commit -m "Update: $DATE"

# Push to the remote repository
git push
