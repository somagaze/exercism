#!/usr/bin/env bash
# Usage: ./setup_exercise.sh <track> <exercise>

TRACK=$1
EXERCISE=$2

if [ -z "$TRACK" ] || [ -z "$EXERCISE" ]; then
    echo "error: missing track or exercise name."
    exit 1
fi

echo "downloading $EXERCISE from the $TRACK track..."
exercism download --track="$TRACK" --exercise="$EXERCISE"

# Navigate to the downloaded directory
cd "$TRACK/$EXERCISE" || exit 1

echo "initializing uv project..."
uv init --lib --quiet

echo "adding pytest..."
uv add pytest --quiet

echo "setup complete for $TRACK/$EXERCISE!"
