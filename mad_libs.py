

print("Let's do some MadLibs!\n")
print("We are going to need a few words from you in order to complete the story.\n")

story = """\nDriving a car can be fun if you follow this {0} advice:
When approaching a {1} on the right, always blow your {2}.
Before making a {3} turn, always stick your {4} out of the window.
Every 2000 miles, have your {5} inspected and your {6} checked.
When approaching a school, watch out for {7} {8}.
Above all, drive {9} The {10} you save may be your own!"""

adjective_zero = input("Adjective:\n")
noun_one = input("\nNoun:\n")
noun_two = input("\nNoun:\n")
adjective_three = input("\nAdjective:\n")
noun_four = input("\nNoun:\n")
noun_five = input("\nNoun:\n")
noun_six = input("\nNoun:\n")
adjective_seven = input("\nAdjective:\n")
noun_eight = input("\nNoun:\n")
adverb_nine = input("\nAdverb:\n")
noun_ten = input("\nNoun:\n")

print(story.format(adjective_zero, noun_one, noun_two, adjective_three, noun_four, noun_five, noun_six, adjective_seven, noun_eight, adverb_nine, noun_ten))