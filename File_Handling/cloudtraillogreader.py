#code to read CloudTrail logs would go here
import re
def read_cloudtrail_logs():
    file_path = r"C:\Users\GFVM4731\Downloads\python-for-devops\cloudtrail.log"
    with open(file_path, 'r') as file:
        for line in file:
            # print(line.strip())
            # Example regex pattern to find 'ERROR' in logs
            pattern = r"accessKeyId"
            if re.search(pattern, line):
                print("AccessKeyID found",line)



read_cloudtrail_logs()