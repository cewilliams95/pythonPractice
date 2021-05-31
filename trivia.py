# Trying to use tkinter to make a basic trivia game
# TODO: End the game properly at the end w/ splash screen,
#       style the score 
import tkinter as tk
import requests
import json
import random
import html

# Main Window class
class MainWindow(tk.Frame):
    questionNum = 0
    questions = {}
    score = 0
    def __init__(self, master):
        master.title("Python Trivia")
        master.geometry("960x568")
        self.master = master
        
        self.question = tk.Label(self.master, text="")
        self.question.place(x=480, y=40, anchor="center")
        
        self.scoreLabel = tk.Label(self.master, text=str(self.score), font=("Arial", 45))
        self.scoreLabel.place(x=480, y=350, anchor="center")

        self.getQuestions()
        self.writeQuestion()
        self.writeAnswers()
        
    
    # Create Question
    def writeQuestion(self):
        self.question["text"] = str(self.questionNum+1) + ". " + html.unescape(self.questions[self.questionNum]['question'])

    # Create answer options
    def writeAnswers(self):
        self.answers = self.questions[self.questionNum]['incorrect_answers']
        correct = self.questions[self.questionNum]['correct_answer']
        self.answers.append(correct)
        random.shuffle(self.answers)
        # Create answer buttons
        self.option1 = tk.Button(
            self.master, 
            text='A: '+html.unescape(self.answers[0]), 
            disabledforeground='white',
            width=25, 
            command=lambda: self.check(self.answers[0], correct))
        self.option1.place(x=480, y=100, anchor="center")
        
        self.option2 = tk.Button(self.master, 
            text='B: '+html.unescape(self.answers[1]), 
            disabledforeground='white',
            width=25, 
            command=lambda: self.check(self.answers[1], correct))
        self.option2.place(x=480, y=150, anchor="center")

        self.option3 = tk.Button(self.master, 
            text='C: '+html.unescape(self.answers[2]), 
            disabledforeground='white',
            width=25, 
            command=lambda: self.check(self.answers[2],correct))
        self.option3.place(x=480, y=200, anchor="center")
        
        self.option4 = tk.Button(self.master, 
            text='D: '+html.unescape(self.answers[3]), 
            disabledforeground='white',
            width=25, 
            command=lambda: self.check(self.answers[3],correct))
        self.option4.place(x=480, y=250, anchor="center")

    # Check if chosen option was correct and update score if so, then reveal & continue
    def check(self, ans, correct):
        success = (ans == correct)
        if(success):
            self.score += 5
            self.scoreLabel["text"] = self.score
            print('Correct!')
        else:
            print('Incorrect...')
        self.revealAnswer()

    # TODO: this sucks but I'm just lazy rn
    # Reveal the answer and move on
    def revealAnswer(self):
        ans = self.questions[self.questionNum]['correct_answer']
        options = [self.option1, self.option2, self.option3, self.option4]
        for i in range(4):
            options[i]["state"] = "disabled"
            if self.answers[i] == ans:
                options[i]["bg"] = "green"
            else:
                options[i]["bg"] = "red"
        self.waithere()
        self.nextQuestion()
    
    # Go to the next question unless you finished
    def nextQuestion(self):
        self.questionNum += 1
        options = [self.option1, self.option2, self.option3, self.option4]
        for btn in options:
            btn["state"] = "normal"
        if self.questionNum >= len(self.questions):
            # TODO: instead destroy the question/answers and highlight the final score w/ a close button on bot
            self.master.destroy()
        else:
            self.writeQuestion()
            self.writeAnswers()

    # Request 10 questions from the opentdb API
    def getQuestions(self):
        req = requests.get('https://opentdb.com/api.php?amount=10&difficulty=medium&type=multiple')
        data = req.json()
        self.questions = data['results']

    # Wait utility func
    def waithere(self):
        var = tk.IntVar()
        self.master.after(2000, var.set, 1)
        print("waiting...")
        self.master.wait_variable(var)

def main():
    app = tk.Tk()
    window = MainWindow(master=app)
    app.mainloop()

if __name__ == '__main__':
    main()