import tkinter as tk
import random
from time import sleep
from modelTrain3 import NeuralNetwork
import torch
import numpy as np
from pylsl.pylsl import StreamInlet, resolve_stream
import mne

FILENAME = "questions.txt"
RESPONSE_FILENAME = "responses.txt"
file = open(FILENAME, 'r')
questions = file.readlines()
num_questions = len(questions)
for i in range(num_questions) :
    questions[i].rstrip("\n")
    print(questions[i])
index = 0
responses = []

def get_eeg_info():
    ch_names = ['Fp1.', 'Fp2.', 'F3..', 'F4..', 'C3..', 'C4..', 'F7..', 'F8..']
    ch_type = ['eeg'] * 8
    sfreq = 129
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
    return info

def get_streams(name='type', type='EEG'):
    streams = resolve_stream(name, type)
    if len(streams) == 0:
        print("No stream detected. Closing the program. Terminating.")
        exit(1)
    return streams

def get_data_from_stream(inlet: StreamInlet, chunk_size=129):
    samples, _ = inlet.pull_chunk(timeout=1.0, max_samples=chunk_size)
    if len(samples) == 0:
        print("No samples received from connection. Terminating.")
        exit(1)
    data = np.array(samples).T
    return torch.tensor(data, dtype=torch.float32).unsqueeze(0)

def predict_intended_action(model: NeuralNetwork, input_signal):
    with torch.no_grad():
        output = model(input_signal)
        _, prediction = torch.max(output, dim=1)
        action = prediction.item()
    return action

def get_data_and_predict():
    input_signal = get_data_from_stream(inlet)
    action = predict_intended_action(model, input_signal=input_signal)
    return action

def on_left():
    global index
    left_button.config(bg="darkgreen")
    root.update()
    sleep(0.2)
    left_button.config(bg="lightgreen")
    responses.append("LEFT\n")
    print("LEFT button clicked!")
    index += 1
    if (index == num_questions) :
        file = open(RESPONSE_FILENAME, 'w')
        file.writelines(responses)
        root.destroy()


def on_right():
    global index
    right_button.config(bg="darkred")
    root.update()
    sleep(0.2)
    right_button.config(bg="lightcoral")
    responses.append("RIGHT\n")
    print("RIGHT button clicked!")
    index += 1
    if (index == num_questions) :
        file = open(RESPONSE_FILENAME, 'w')
        file.writelines(responses)
        root.destroy()

def no_action():
    print("No action taken")

def gui_loop():
    global root, left_button, right_button, questions
    global index
    root = tk.Tk()
    root.title("Question Window")

    def on_left():
        global index
        left_button.config(bg="darkgreen")
        root.update()
        sleep(0.2)
        left_button.config(bg="lightgreen")
        responses.append("LEFT\n")
        print("LEFT button clicked!")
        index += 1
        if index < num_questions :
            question_label.config(text=questions[index])
            heading_label.config(text=f"QUESTION {index + 1}")
        else :
            file = open(RESPONSE_FILENAME, 'w')
            file.writelines(responses)
            root.destroy()


    def on_right():
        global index
        right_button.config(bg="darkred")
        root.update()
        sleep(0.2)
        right_button.config(bg="lightcoral")
        responses.append("RIGHT\n")
        print("RIGHT button clicked!")
        index += 1
        if index < num_questions :
            question_label.config(text=questions[index])
            heading_label.config(text=f"QUESTION {index + 1}")
        else :
            file = open(RESPONSE_FILENAME, 'w')
            file.writelines(responses)
            root.destroy()

    def no_action():
        print("No action taken")

    def simulate_button_click():
        action = get_data_and_predict()
        print(action)
        match action:
            case 1:
                on_left()
            case 2:
                on_right()
            case 0:
                no_action()

        root.after(1000, simulate_button_click)

    root.geometry("400x300")

    heading_label = tk.Label(root, text=f"QUESTION {index}", font=("Arial", 16))
    heading_label.pack(pady=10)

    question_label = tk.Label(root, text=questions[index], font=("Arial", 12))
    question_label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20, fill="x")

    left_button = tk.Button(button_frame, text="YES", font=("Arial", 14), width=10, height=5, bg="lightgreen", command=on_left)
    left_button.pack(side="left", padx=50, pady=100)

    right_button = tk.Button(button_frame, text="NO", font=("Arial", 14), width=10, height=5, bg="lightcoral", command=on_right)
    right_button.pack(side="right", padx=50, pady=100)

    root.after(1000, simulate_button_click)
    root.mainloop()

    
info = get_eeg_info()
model = NeuralNetwork(3)
model.load_state_dict(torch.load("models\\other_model_3.pth"))
model.eval()

streams = get_streams()
inlet = StreamInlet(streams[0])

def main():
    gui_loop()

if __name__ == "__main__":
    main()