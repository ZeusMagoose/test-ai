from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-UC5tSiq7eSERQaj1pgcpT3BlbkFJ69zR8MFtooVMtraaoG5F'

@app.route('/chat', methods=['GET'])
def chat():
    user_message = request.args.get('message')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
