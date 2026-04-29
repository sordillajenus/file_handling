import datetime
from collections import Counter

class LifeAnalytics:
    def __init__ (self, filename):
        self.filename = filename

    def write_entry(self):
        with open (self.filename, "a") as file:

            while True:
                mood = input("What's your mood today?: ")
                entry = input("write about your day today: ")

                word_count = len(entry.split())
                timestamp = datetime.datetime.now()

                file.write(f"[{timestamp}]\n")
                file.write(f"Mood: {mood}\n")
                file.write(f"Words: {word_count}\n")
                file.write(f"Entry: {entry}\n\n")

                repeat = input("Add another line? yes/no: ").lower
                if repeat == "no":
                    break

    def analyze_entries(self):
        moods = []
        word_counts = []

        with open(self.filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("Mood:"):
                mood = line.split(":")[1].strip()
                moods.append(mood)

            elif line.startswith("Words:"):
                count = int(line.split(":")[1].strip())
                word_counts.append(count)

        if not moods:
            print("No data to analyze.")
            return
        
        most_common_words =  most_common_mood = Counter(moods).most_common(1)[0][0]
        average_words = sum(word_counts) / len(word_counts)
        minimum_word_counts = min(word_counts)
        maximum_word_counts = max(word_counts)

        print("\nLIFE ANALYTICS REPORT\n")
        print(f"Total Entries: {len(moods)}")
        print(f"Most Common Mood: {most_common_words}")
        print(f"Average Words per Entry: {average_words:.2f}")
        print(f"Longest Entry: {maximum_word_counts} words")
        print(f"Shortest Entry: {minimum_word_counts} words")




