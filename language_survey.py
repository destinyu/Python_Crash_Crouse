from survey import AnnonymousSurvey
question="What language did you first learn to speak?"
my_survey=AnnonymousSurvey(question)
my_survey.show_qusetion()

print("Enter 'q' at any time to quit")
while True:
    response=input("language:")
    if response=='q':
        break
    else:
        my_survey.store_qusetion(response)

print("\nThank you")
my_survey.show_results()