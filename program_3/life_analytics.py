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

                count = input("Add another line? yes/no: ").lower
                if count == "no":
                    break

    def analyze_entries(self):
        mood = []
        word = []
