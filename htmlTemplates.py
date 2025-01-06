css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}

.chat-message .question {
    background-color: #2b313e
    right: 0
}

.chat-message .answer {
    background-color: #475063
    left: 0
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

answer_template = '''
<div class="chat-message answer">
    <div class="message">{{MSG}}</div>
</div>
'''

question_template = '''
<div class="chat-message question"> 
    <div class="message">{{MSG}}</div>
</div>
'''