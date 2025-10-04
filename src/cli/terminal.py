# src/cli/terminal.py
"""
Terminal-based interface for ELIZA chatbot.
Handles user input/output loop and interacts with ElizaInterpreter.
"""

import os
from engine import ScriptLoader, ElizaInterpreter

def main():
    # Build path to the doctor.txt script relative to this file
    script_path = os.path.join(os.path.dirname(__file__), "../scripts/doctor.txt")
    
    # Load the script
    loader = ScriptLoader(script_path)
    script_data = loader.load_script()
    
    # Initialize ELIZA interpreter
    eliza = ElizaInterpreter(script_data)
    
    # Print initial greeting
    print("Eliza: " + eliza.initial)
    
    while True:
        try:
            # Read user input
            user_input = input("> ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in script_data["quit"]:
                print("Eliza: " + eliza.final)
                break
            
            # Generate ELIZA response
            response = eliza.respond(user_input)
            if response:
                print("Eliza: " + response)
        
        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C / Ctrl+D gracefully
            print("\nEliza: " + eliza.final)
            break

if __name__ == "__main__":
    main()
