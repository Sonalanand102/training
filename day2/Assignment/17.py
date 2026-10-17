"""
Given:
status_codes = [200, 201, 200, 404, 500, 200, 403, 201]


Print every failed status code.
Expected:
404
500
403

Then print the total number of failed requests.
"""


status_codes = [200, 201, 200, 404, 500, 200, 403, 201]

failed_count = 0

for i in status_codes:
    if i>= 400:
        print(i)
        failed_count += 1

print("total failed request", failed_count)