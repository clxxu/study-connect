import requests
import json

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Authorization': 'Bearer MmM5YWU5MjQtNDYxMi0zNGU4LWFkMDMtMWUyZjJlZTJjMjlkOnJlZ2lzdHJhcmFwaUBjYXJib24uc3VwZXI=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Origin': 'https://registrar.princeton.edu',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://registrar.princeton.edu/',
    'Accept-Language': 'en-US,en;q=0.9',
}

courses = []

def main():
  r = requests.get('https://api.princeton.edu/registrar/course-offerings/classes/1212', headers=headers)
  
  content = r.json()['classes']
  for classes in content['class']:
    if classes["crosslistings"] not in courses:
      # aesthetically displays courses
      print(classes["crosslistings"])
      courses.append(classes["crosslistings"])
  json_courses = json.dumps(courses)
  # print(json_courses)
  

if __name__ == "__main__":
  main()