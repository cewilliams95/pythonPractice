# Trying to use tkinter to make a basic trivia game
# TODO: Get rid of extra win, stop overusing the shit out of class-wide variables, get question list length and end the game at the end,
#       style the score, center the question somehow and keep the buttons in one spot
import tkinter as tk
import requests
import json
import random
import html

class MainWindow(tk.Toplevel):
    questionNum = 0
    questions = {}
    score = 0
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        master.title("Python Trivia")
        master.geometry("960x768")
        self.scoreLabel = tk.Label(master, text=str(self.score))
        self.scoreLabel.grid(row=4,column=1)
        self.question = tk.Label(master, text="")
        self.question.grid(row=1,columnspan=2)

        self.getQuestions()
        self.writeQuestion(master)
        self.writeAnswers(master)
        
    
    # Create Question
    def writeQuestion(self, master):
        self.question["text"] = html.unescape(self.questions[self.questionNum]['question'])

    # Create answer options
    def writeAnswers(self, master):
        self.answers = self.questions[self.questionNum]['incorrect_answers']
        correct = self.questions[self.questionNum]['correct_answer']
        self.answers.append(correct)
        random.shuffle(self.answers)
        # Create answer buttons
        self.option1 = tk.Button(master, text='A: '+self.answers[0], width=25, command=lambda: self.check(self.answers[0],correct))
        self.option1.grid(row=2,column=1)
        self.option2 = tk.Button(master, text='B: '+self.answers[1], width=25, command=lambda: self.check(self.answers[1],correct))
        self.option2.grid(row=2,column=2)
        self.option3 = tk.Button(master, text='C: '+self.answers[2], width=25, command=lambda: self.check(self.answers[2],correct))
        self.option3.grid(row=3,column=1)
        self.option4 = tk.Button(master, text='D: '+self.answers[3], width=25, command=lambda: self.check(self.answers[3],correct))
        self.option4.grid(row=3,column=2)

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
            if self.answers[i] == ans:
                options[i]["bg"] = "green"
            else:
                options[i]["bg"] = "red"
        self.waithere()
        self.nextQuestion()
        
    def nextQuestion(self):
        self.questionNum += 1
        self.writeQuestion(self.master)
        self.writeAnswers(self.master)

    def getQuestions(self):
        req = requests.get('https://opentdb.com/api.php?amount=10&difficulty=medium&type=multiple')
        data = req.json()
        print(type(data))
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
    # app.after(1000, window.update)
    app.mainloop()

if __name__ == '__main__':
    main()