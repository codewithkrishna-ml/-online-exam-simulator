#PROJECT-Online Examination System
import time

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, input_email, input_password):
        if self.email == input_email and self.password == input_password:
            print(f"\n Welcome back, {self.name}! Login successfully")
            return True
        return False

class Student(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.my_results = []

    def view_available_exam(self, exam_list):
        print("\n---------------------AVAILABLE EXAMS-----------------------")
        if not exam_list:
            print("No exam are currently available")
            return 
        for idx, exam in enumerate(exam_list, 1):
            print(f"{idx}. [ID: {exam.exam_id}] {exam.title} ({exam.duration} Mins)")
            print("------------------------------------------------------------------")

    def view_past_results(self):
        print("\n-------------------YOUR REPORT CARD----------------------------")
        if not self.my_results:
            print("You have not taken any exams yet.")
            return
        for res in self.my_results:
            print(f"Exam: {res['exam_title']} | Score: {res['score']} | Status: {res['status']}")
            print("-----------------------------------------------------------------")

class Teacher(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def create_exam(self, exam_id, title, duration):
        print(f"\n[System] Exam '{title}' successfully created by prof. {self.name}")
        return Exam(exam_id, title, duration)

class Question:
    def __init__(self, question_id, question_text, option_list, correct_option=1):
        self.question_id = question_id
        self.question_text = question_text
        self.option_list = option_list
        self.correct_option = correct_option

    def display_question(self):
        print(f"\nQ. {self.question_text}")
        for i, option in enumerate(self.option_list, 1):
            print(f"{i}) {option}")

    def check_answer(self, student_answer):
        return str(student_answer).strip() == str(self.correct_option).strip()

class Exam:
    def __init__(self, exam_id, title, duration):
        self.exam_id = exam_id
        self.title = title
        self.duration = duration
        self.questions_list = []

    def add_question(self, question_object):
        self.questions_list.append(question_object)

    def start_exam(self):
        print(f"\n================= EXAM START: {self.title.upper()}=====================")
        print(f"Duration: {self.duration} Minute | Total Question: {len(self.questions_list)}")
        print("Best of luck! The test is starting now...\n")
        time.sleep(1)

        score = 0
        if not self.questions_list:
             print("There are no questions in this exam!")
             return 0
        for idx, q in enumerate(self.questions_list, 1):
             print(f"\n---------- Question {idx} ---------")
             q.display_question()

             ans = input("Select the correct option (1-4): ")
             if q.check_answer(ans):
                 print("correct Answer!")
                 score += 1
             else:
                 print(f"Wrong! the option was {q.correct_option}.")

        print("\n======================== EXAM SUBMITTED====================")
        return score

class OnlineExamSystem:
    def __init__(self):
        self.users = {}
        self.exams = []

    def setup_dummy_data(self):
        teacher = Teacher(101, "Vishal sharma", "teacher@gmail.com", "pass123")
        student = Student(201, "Krishna", "student@gmail.com", "pass456")

        self.users[teacher.email] = teacher
        self.users[student.email] = student

        exam = teacher.create_exam("EX-501", "Python OOPs Quiz", 10)
        q1 = Question(1, "Which OOPs concept is used to hide internal data details?", 
                      ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"], 2)
        q2 = Question(2, "Which keyword is used to call a parent class constructor in Python?", 
                      ["super()", "this()", "parent()", "init()"], 1)

        exam.add_question(q1)
        exam.add_question(q2)
        self.exams.append(exam)

    def run(self):
        self.setup_dummy_data()

        while True:
            print("\n======================================================")
            print("         ONLINE EXAMINATION SYSTEM MENU             ")
            print("====================================================")
            print("1.Login")
            print("2.Exit")
            choice = input("Select an option (1-2): ")

            if choice == "2":
                print("Exiting system. Goodbye!")
                break

            if choice == "1":
                email = input("Enter Email: ")
                password = input("Enter Password: ")

                if email in self.users and self.users[email].login(email, password):
                    user = self.users[email]

                    if isinstance(user, Student):
                        while True:
                            print(f"\n------- STUDENT PANEL ({user.name})---------")
                            print("1.View Available Exams")
                            print("2.Attempts an Exams")
                            print("3.View past Results")
                            print("4.Logout")
                            s_choice = input("Select an option: ")

                            if s_choice == "1":
                                user.view_available_exam(self.exams)
                            elif s_choice == "2":
                                user.view_available_exam(self.exams)
                                if self.exams:
                                    try:
                                        ex_idx = int(input("Enter the exam number you wish to take: "))
                                        if 1 <= ex_idx <= len(self.exams):
                                            selected_exam = self.exams[ex_idx - 1]
                                            final_score = selected_exam.start_exam()
                                            status = "Pass" if final_score >= (len(selected_exam.questions_list)/2) else "Fail"
                                            user.my_results.append({
                                                "exam_title": selected_exam.title,
                                                "score": f"{final_score} / {len(selected_exam.questions_list)}",
                                                "status": status
                                            })
                                        else:
                                            print("Invalid exam choice number.")
                                    except ValueError:
                                        print("Please enter a valid numeric number")
                            elif s_choice == "3":
                                user.view_past_results()
                            elif s_choice == "4":
                                print("Logged out successfully")
                                break

                    elif isinstance(user, Teacher):
                        while True:
                            print(f"\n------------- TEACHER PANEL (prof. {user.name})------------")
                            print("1.Create New Exam")
                            print("2.Logout")
                            t_choice = input("Select an option: ")

                            if t_choice == "1":
                                e_id = input("Enter Exam ID: ")
                                title = input("Enter Exam Title: ")
                                try:
                                    dur = int(input("Enter Duration (in Minutes): "))
                                except ValueError:
                                    print("Invalid input. Defaulting to 10 minutes.")
                                    dur = 10
                                    
                                new_exam = user.create_exam(e_id, title, dur)
                                
                                while True:
                                    add_q = input("Do you want to add a question? (y/n): ")
                                    if add_q.lower() != 'y':
                                        break
                                    q_text = input("Enter question: ")
                                    opts = [input("Opt 1: "), input("Opt 2: "), input("Opt 3: "), input("Opt 4: ")]
                                    correct = input("Correct option (1-4): ")
                                    
                                    new_q = Question(len(new_exam.questions_list) + 1, q_text, opts, correct)
                                    new_exam.add_question(new_q)
                                    
                                self.exams.append(new_exam)
                                print("[System] Exam published successfully!")
                                
                            elif t_choice == "2":
                                print("Logged out successfully")
                                break
                else:
                    print("Invalid email or password.")

if __name__ == "__main__":
    system = OnlineExamSystem()
    system.run()
