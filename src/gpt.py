from openai import OpenAI
import datetime

# migration guide: https://github.com/openai/openai-python/discussions/742

api_key = ''
def save_apikey(apikey):
    global api_key
    api_key = apikey

def run_gpt(query):
    #TODO
    pass


# TODO: gpt now has an error. idk why. error message below.
def run_gpt_helloworld():
    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=api_key,
	)
    completion = client.completions.create(model='curie', prompt="This is a test")
    print(datetime.datetime.now(), completion.choices[0].text)
    print(datetime.datetime.now(), dict(completion).choices[0].text)
    print(datetime.datetime.now(), completion.model_dump_json(indent=2))
    
###### error message ######
# Traceback (most recent call last):
#   File "/home/jhkim/ai-edutech/chatgpt_test.py", line 34, in <module>
#     run_gpt_helloworld()
#   File "/home/jhkim/ai-edutech/chatgpt_test.py", line 16, in run_gpt_helloworld
#     completion = client.chat.completions.create(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_utils/_utils.py", line 299, in wrapper
#     return func(*args, **kwargs)
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/resources/chat/completions.py", line 598, in create
#     return self._post(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 1055, in post
#     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 834, in request
#     return self._request(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 865, in _request
#     return self._retry_request(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 925, in _retry_request
#     return self._request(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 865, in _request
#     return self._retry_request(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 925, in _retry_request
#     return self._request(
#   File "/home/jhkim/.local/lib/python3.10/site-packages/openai/_base_client.py", line 877, in _request
#     raise self._make_status_error_from_response(err.response) from None
# openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
############################

# get the question from student and do prompt engineering for gpt
def prompt(question):
    #TODO
	pass	





# def gpt_connection():
# 	api_key = '[AUTH_KEY 입력]'
# 	return api_key

# def run_gpt(query):
# 	openai.api_key = gpt_connection()
# 	messages = [{"role": "", "content": ""}] 
# 	response = openai.ChatCompletion.create(
# 		model = 'gpt-4',
# 		messages = messages
# 	)
# 	msg = response['choices'][0]['message']['content']
# 	return msg
	

