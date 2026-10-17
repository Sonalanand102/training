"""
Imagine an API can fail randomly.
Given:
responses = [500, 500, 500, 200]


Simulate retry behavior.
Your program should check each response sequentially.
If response is 200:
Request successful

and stop.
If response is not 200:
Request failed, retrying...

After all attempts fail:
All retry attempts failed

This introduces a real backend concept using only loops + conditions.
"""
responses = [500, 500, 500, 200]

sucessfull = False

for i in responses:
    if i == 200:
        print("request successfull")
        sucessfull = True
        break
    else:
        print("request faiiled, retrying ....")

if not sucessfull:
    print("all attempts failed")

