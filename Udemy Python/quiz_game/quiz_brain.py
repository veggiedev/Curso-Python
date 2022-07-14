class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self):
        is_right = True
        current_question = self.question_list[self.question_number]
        
    
    def check_answer(self):
        score = 0
        for item in self.question_list:
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {item.text} (True/False)?: ")    
            if user_answer.capitalize() != item.answer:
                print(f"Wrong answer. The correct answer was '{item.answer}'")
                print(f"Your score was {score}/12")
                continue
            else:
                score += 1
                print("You got it right!")
                print(f"The correct answer was: {item.answer}")
                print(f"Your score is {score}/12")
                continue
