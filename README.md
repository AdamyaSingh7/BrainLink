# BrainLink: Mind-Powered Question Response System

## Overview  
Brain Link is an innovative project that leverages EEG technology to enable users to answer yes/no questions using brain wave activity. Designed to assist individuals with limited mobility or communication abilities, this system uses non-invasive brain wave analysis to interpret responses through directional thought patterns.

The project is highly customizable, allowing caregivers or administrators to configure personalized question sets in a binary tree structure for dynamic question navigation. It also supports multilingual functionality, providing accessibility for users from diverse linguistic backgrounds.

---

## Features  
- **Non-invasive EEG-based communication**: Interpret brain wave activity for answering yes/no questions.  
- **Dynamic questionnaire**: Questions are stored in a binary tree format and adapt based on user responses.  
- **Multilingual support**: Questions can be presented in various languages as per user preferences.  
- **Customizable**: Easily update the questionnaire to cater to individual needs.  
- **Scalable architecture**: Future enhancements can include more complex question-answer patterns and better signal analysis.  

---

## How It Works  
1. **Hardware Integration**: Uses the Neuphony FlexCap EEG headset to capture brain activity.  
2. **Signal Preprocessing**: Data preprocessing using Python libraries like `pylsl` for accurate signal analysis.  
3. **Custom Model**: Combines CNN and RNN layers built in PyTorch to classify brain activity into three categories.  
4. **Dynamic Question Flow**: Employs binary tree traversal to dynamically present questions based on responses.  
5. **GUI Interaction**: Intuitive interface built using Python’s `Tkinter` library for user interaction and configuration.  

---
## Folder Structure  
- gui.py: main code which starts the application.  
- lslpipe.py: code to fetch data from lslstream.  
- modelTrain3.py: code for Model.  
- qutionConfig.py: code to start application which fills questionnaire.  

