<h1>Welcome to "Lainey" - Create your own Virtual AI Assistant!</h1>
<p>This repository contains a python script which outlines the structure for speech recognition, spoken response, speech to text translation, etc.
It was designed to control my Roku TV through speech, due to a misplaced TV remote, and quickly realized it could be incredibly useful for many things.</p>

<h2>License:</h2>
<p>MIT License
  Copyright (c) <strong>Jake Rawls</strong>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.</p>

<h2><b>Installation</b></h2>
<p>To use this project, follow these steps:</p>

<h2>Clone this repo to your local machine using the following command in your terminal/CMD:</h2>
<code>git clone https://github.com/Jake-Rawls/virtual-AI-assistant.git</code>

<h2>Navigate to the project's directory:</h2>
<code>cd virtual-AI-assistant</code>

<h2>Once in the virtual-AI-assistant directory, the last commands to run are for installing required modules needed for speech recognition:</h2>
<code>pip3 install SpeechRecognition</code>
<code>pip3 install pyttsx3</code>
<code>pip3 install PyAudio</code>

<h2>Lastly, run the script with the following command:</h2>
<code>python3 main.py</code>

<h2>Usage:</h2>
<p>In this example, the program uses the SpeechRecognition library to continuously listen to the user's voice input through a microphone. The recognized text is then immediately spoken using the pyttsx3 library.</p><br>
<p>The recognize_and_speak function initializes the microphone as the audio source and enters an infinite loop. Inside the loop, it listens to the audio input, recognizes the speech using the recognize_google method, and then speaks the recognized text using the speak function.</p><br>
<p>To use this program, run it and speak into the microphone. The program will continuously recognize and speak the words you say in real-time. <span>Note that you may need to adjust the microphone settings and ensure that you have the required dependencies installed (SpeechRecognition and pyttsx3) for the program to work properly</span>.</p>

<h2>Contributing:</h2>
<p>Contributions are welcome! If you'd like to contribute to this project, please follow these steps:</p>
<li>Fork this repository.</li>
<li>Create a new branch.</li>
<li>Make your desired changes.</li>
<li>Commit and push your changes to your forked repository.</li>
<li>Submit a pull request, clearly describing your changes and their purpose.</li>

<h2>Thanks for stopping by!</h2>
<p>If you have any questions or feedback, please feel free to contact me, or submit a PR with any additions.</p>
<p>Also, feel free to modify and customize this template to fit your specific project's needs. You can add or remove sections as necessary. Remember to provide clear and concise instructions to help users understand and utilize your repository effectively.</p>
