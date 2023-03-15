class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {current_question.q_text} (True/False) ")
        self.check_ans(user_ans, current_question.a_text)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print(f"you got it! your score is {self.score}/{self.question_no}")
        else:
            print(f" that's wrong! correct answer is {correct_ans} ")
