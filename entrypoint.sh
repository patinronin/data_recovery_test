#!/bin/bash

FLAG_FILE="/app/.db_populated"

echo "Starting container..."

# Run populate DB only once
if [ ! -f "$FLAG_FILE" ]; then
    echo "Populating database for the first time..."
    python -m app.main --poblate_db
    
    echo "Creating population flag..."
    touch "$FLAG_FILE"
else
    echo "Database already populated. Skipping..."
fi

# Always run this
echo "Generating results..."
python -m app.main --generate_results_file
