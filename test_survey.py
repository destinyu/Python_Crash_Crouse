import unittest
from survey import AnnonymousSurvey
class TestAnonmyousSurvey(unittest.TestCase):
    """def test_store_single_response(self):
       self.question="What is your favourite language?"
       my_survey=AnnonymousSurvey(self.question)
       my_survey.store_qusetion('English')

       self.assertIn('English',my_survey.responses)

       def test_store_three_responses(self):
        self.question="What is your favourite language?"
        my_survey=AnnonymousSurvey(self.question)
        responses=['C','C++','java']
        for response in responses:
            my_survey.store_qusetion(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
            """

    def setUp(self):
        self.question="What language did you first learn to speak?"
        self.my_survey=AnnonymousSurvey(self.question)
        self.responses=['C','Python','C++']
    def test_store_single_response(self):
        self.my_survey.store_qusetion(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_qusetion(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)





if __name__ == '__main__':
    unittest.main()