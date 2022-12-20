import requests
import threading

def call_api(thread_name):
  while True:
    url = "https://dev.pron.kidsenglish.vn/recog"
    payload={'target_word': 'apples'}
    files=[
      ('the_file',('20221111133649.wav',open('/home/trandat/project/VIETTEC/pronounciation/CODE/data/origin/apples/20221111133649.wav','rb'),'audio/wav'))
    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(thread_name + response.text)

if __name__ == '__main__':
  thread_1 = threading.Thread(target=call_api, args=("thread_1",))
  thread_2 = threading.Thread(target=call_api, args=("thread_2",))
  thread_3 = threading.Thread(target=call_api, args=("thread_3",))
  thread_4 = threading.Thread(target=call_api, args=("thread_4",))
  thread_1.start()
  thread_2.start()
  thread_3.start()
  thread_4.start()
  thread_1.join()
  thread_2.join()
  thread_3.join()
  thread_4.join()