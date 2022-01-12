# Add dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to where file will be located
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Initialize candidates list.
candidate_options = []
# Declare candidate votes dictionary
candidate_votes = {}
# Declare variable that hold an empty string value for the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and Print header row in the CSV file.
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        # Get candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match existing candidate name add to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # start tracking vote count
            candidate_votes[candidate_name] = 0
        # Start adding votes to candidate count.
        candidate_votes[candidate_name] +=1
  # Save audit results to text file.
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print and Save the final vote count to the terminal and text file.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage of each candidate.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print and save each candidate's voter count and percentage to the terminal and text file.
        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, then set winning_count = votes and winning_percent = vote_percentage, winning_candidate = candidate_name.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print and save the winning candidate's results to the terminal and text file.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
