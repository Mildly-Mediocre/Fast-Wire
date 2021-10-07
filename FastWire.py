from flask import Flask, flash, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"
if __name__ == "__main__":
    app.run()


# def count_files(directory):
#     for filename in os.listdir(directory):
#         if filename.endswith(".csv"): 
#             # print(os.path.join(directory, filename))
#             fileCount += 1
#         else:
#             continue

# def find_priority(directory):
#     for filename in os.listdir(directory):
#         if filename.endswith(".csv"): 
#             # print(os.path.join(directory, filename))
            
#         else:
#             continue
    
