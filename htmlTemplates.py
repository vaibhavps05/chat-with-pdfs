css = '''
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 2rem;
}

.chat-message {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    max-width: 80%;
    word-wrap: break-word;
    margin-bottom: 1rem;
}


.chat-message .message {
    flex-grow: 1;
    font-family: 'Arial', sans-serif;
    font-size: 0.95rem;
    line-height: 1.5;
    color: #333;
}

.chat-message.question {
    background-color: #ef7caf;
    align-self: flex-end;
    flex-direction: row-reverse
}

.chat-message.answer {
    background-color: #9b88bf;
    align-self: flex-start;
}

.chat-message .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #ebb1d1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    font-weight: bold;
    color: black;
}

</style>
'''

answer_template = '''
<div class="chat-message answer">
    <div class="avatar">AI</div>
    <div class="message">{{MSG}}</div>
</div>
'''

question_template = '''
<div class="chat-message question">
    <div class="avatar">U</div>
    <div class="message">{{MSG}}</div>
</div>
'''
