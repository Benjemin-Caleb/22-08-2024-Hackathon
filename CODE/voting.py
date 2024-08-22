import hashlib
import json
import os

VOTE_FILE = "votes.json"

admin_password = "password"

def load_votes():
    if os.path.exists(VOTE_FILE):
        with open(VOTE_FILE, "r") as file:
            return json.load(file)
    else:
        return {'A': 0, 'B': 0, 'C': 0}

def save_votes(votes):
    with open(VOTE_FILE, "w") as file:
        json.dump(votes, file)

votes = load_votes()

def hash_vote(vote):
    """Hashes the vote to ensure it can't be tampered with."""
    return hashlib.sha256(vote.encode()).hexdigest()

def cast_vote(candidate):
    """Casts a vote for a candidate and returns a hash of the vote."""
    if candidate in votes:
        votes[candidate] += 1
        save_votes(votes) 

        return hash_vote(candidate)
    else:
        return "Invalid Candidate"

def display_results():
    """Displays the final voting results in a secure manner."""
    print("Election Results:")
    for candidate, count in votes.items():
        print(f"Candidate {candidate}: {count} votes")

def view_results():
    """Handles result viewing by verifying the admin password."""
    password = input("Enter admin password: ")
    
    if password == admin_password:
        display_results()
    else:
        print("Invalid password. Access denied.")

def voting_system():
    while True:
        print("1. Cast Vote")
        print("2. View Results")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Candidates: A, B, C")
            vote = input("Enter your vote: ").upper()
            vote_hash = cast_vote(vote)
            if "Invalid" not in vote_hash:
                print(f"Your vote has been recorded securely. Vote Hash: {vote_hash}")
            else:
                print(vote_hash)
        elif choice == '2':
            view_results()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    voting_system()
