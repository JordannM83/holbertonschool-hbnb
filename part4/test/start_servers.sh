#!/bin/bash

# Script to reset ports, launch servers and insert test data
# Usage: ./start_servers.sh

echo "======================================"
echo "HBnB Server Startup Script"
echo "======================================"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PART4_DIR="$(dirname "$SCRIPT_DIR")"
PART3_DIR="$(dirname "$PART4_DIR")/part3/hbnb"
TEST_DIR="$SCRIPT_DIR"

# Step 1: Kill existing servers
echo -e "\n${YELLOW}[1/6]${NC} Stopping existing servers..."
pkill -f "python run.py" 2>/dev/null
pkill -f "python3 -m http.server 8080" 2>/dev/null
sleep 2
echo -e "${GREEN}✓${NC} Servers stopped"

# Step 2: Check if ports are free
echo -e "\n${YELLOW}[2/6]${NC} Checking ports availability..."
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${RED}✗${NC} Port 5000 is still in use. Killing process..."
    kill -9 $(lsof -t -i:5000) 2>/dev/null
    sleep 1
fi

if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${RED}✗${NC} Port 8080 is still in use. Killing process..."
    kill -9 $(lsof -t -i:8080) 2>/dev/null
    sleep 1
fi
echo -e "${GREEN}✓${NC} Ports 5000 and 8080 are available"

# Step 3: Reset places in database
echo -e "\n${YELLOW}[3/6]${NC} Resetting places in database..."
cd "$PART3_DIR"

# Use Python from part3 virtual environment
source venv/bin/activate

# Copy and run reset script
cp "$TEST_DIR/reset_places.py" "$PART3_DIR/reset_places_temp.py"
python reset_places_temp.py
rm -f reset_places_temp.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Places reset successfully"
else
    echo -e "${RED}✗${NC} Error resetting places"
    exit 1
fi

# Step 4: Insert test data
echo -e "\n${YELLOW}[4/6]${NC} Inserting test data..."
# Copy and run insert script
cp "$TEST_DIR/insert_test_data.py" "$PART3_DIR/insert_test_data_temp.py"
python insert_test_data_temp.py
rm -f insert_test_data_temp.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Test data inserted successfully"
else
    echo -e "${RED}✗${NC} Error inserting test data"
    exit 1
fi

# Step 5: Start backend server
echo -e "\n${YELLOW}[5/6]${NC} Starting backend server (Flask)..."
nohup python run.py > /tmp/backend.log 2>&1 &
BACKEND_PID=$!
sleep 3

# Check if backend is running
if ps -p $BACKEND_PID > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Backend server started (PID: $BACKEND_PID)"
    echo -e "   URL: http://127.0.0.1:5000"
    echo -e "   Logs: /tmp/backend.log"
else
    echo -e "${RED}✗${NC} Failed to start backend server"
    echo -e "   Check logs: tail -f /tmp/backend.log"
    exit 1
fi

# Step 6: Start frontend server
echo -e "\n${YELLOW}[6/6]${NC} Starting frontend server (HTTP)..."
cd "$PART4_DIR"
nohup python3 -m http.server 8080 > /tmp/frontend.log 2>&1 &
FRONTEND_PID=$!
sleep 2

# Check if frontend is running
if ps -p $FRONTEND_PID > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Frontend server started (PID: $FRONTEND_PID)"
    echo -e "   URL: http://127.0.0.1:8080"
    echo -e "   Logs: /tmp/frontend.log"
else
    echo -e "${RED}✗${NC} Failed to start frontend server"
    echo -e "   Check logs: tail -f /tmp/frontend.log"
    exit 1
fi

# Summary
echo -e "\n======================================"
echo -e "${GREEN}All servers started successfully!${NC}"
echo -e "======================================"
echo -e "\nAccess the application at:"
echo -e "  ${GREEN}http://127.0.0.1:8080${NC}"
echo -e "\nAPI documentation:"
echo -e "  http://127.0.0.1:5000/api/v1/"
echo -e "\nTest credentials:"
echo -e "  Admin: admin@hbnb.io / admin1234"
echo -e "  User:  user@hbnb.io / user1234"
echo -e "\nTo stop servers, run:"
echo -e "  pkill -f 'python run.py' && pkill -f 'python3 -m http.server 8080'"
echo -e "\nServer PIDs:"
echo -e "  Backend:  $BACKEND_PID"
echo -e "  Frontend: $FRONTEND_PID"
echo -e "======================================"
