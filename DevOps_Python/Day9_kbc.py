questions = ["what is national bird of india\noptions are: peacock, pegion, owl, sparrow",
             "What is national animal\noptions are: tiger, lion, jackal, wolf",
             "What is national language of india\noptions are: english, hindi, french, german",
             "what is language which made k8s\noptions are: go, shell, python, c/c++",
             "Tell me aws compute service name\noptions are: vpc, eip, efs, ec2",
             "What is service type in k8s within cluster scope intercommunication\noptions are: clusterip, nodeport, loadbalancer, externalservice", 
             "What is default port number of mysql\noptions are: 3304,3305,3306,3309"]
levels = [1000,2000,5000,100000,500000,1000000,2000000]
correctoptions = ["peacock","tiger","hindi","go","ec2","clusterip","3306"]
i = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"question {i} {question} for Rs. {levels[i]}")
    ans = input(f"Enter your options: ")
    if ans.lower() == correctoptions[i]:
        print("right answer you got", levels[i])
    else:
        print("Wrong answer thankyou for playing")
        print(f"your prize money is Rs: {levels[i]}")
        exit()