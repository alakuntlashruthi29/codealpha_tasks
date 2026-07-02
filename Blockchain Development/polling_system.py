import time

class Poll:
    def __init__(self, title, options, duration_seconds):
        self.title = title
        self.options = options
        self.vote_count = {option: 0 for option in options}
        self.voters = set()
        self.end_time = time.time() + duration_seconds

    def vote(self, voter_address, option):

        if time.time() > self.end_time:
            print("Voting has ended.")
            return

        if voter_address in self.voters:
            print("You have already voted.")
            return

        if option not in self.options:
            print("Invalid option.")
            return

        self.vote_count[option] += 1
        self.voters.add(voter_address)

        print("Vote recorded successfully.")

    def winner(self):

        if time.time() < self.end_time:
            print("Poll is still active.")
            return

        winning_option = max(self.vote_count, key=self.vote_count.get)

        print("\nWinning Option:", winning_option)
        print("Votes:", self.vote_count[winning_option])


# Example
poll = Poll(
    "Favorite Programming Language",
    ["Python", "Java", "C++"],
    20
)

poll.vote("0xABC123", "Python")
poll.vote("0xDEF456", "Java")
poll.vote("0xABC123", "C++")  # Duplicate vote

print("\nWaiting for poll to end...")
time.sleep(20)

poll.winner()