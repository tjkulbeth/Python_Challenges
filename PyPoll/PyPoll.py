#!/usr/bin/env python
# coding: utf-8

# In[17]:


import csv

row=[]
cand1 = []
cand2 = []
cand3 = []
cand4 = []
data=[]


# In[18]:


filename = "Resources/election_data.csv"
with open (filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
#     for row in csvreader:
#         data.append(row[2])
    data = list(csvreader)
#     print(data)
    


# In[19]:


# Calculate total number of votes
    tot_votes=len(data)


# In[ ]:


for row in data:
    if row[2] == "Khan":
        cand1.append(row) 
    elif row[2] == "Correy":
        cand2.append(row) 
    elif row[2] == "Li":
        cand3.append(row)
    elif row[2] == "O'Tooley":
        cand4.append(row) 


# In[ ]:


print(tot_votes)
cand1_votes = sum(1 for row[0] in cand1)
cand2_votes = sum(1 for row[0] in cand2)
cand3_votes = sum(1 for row[0] in cand3)
cand4_votes = sum(1 for row[0] in cand4)


# In[ ]:


#     Select winner
if len(cand1) > len(cand2) and len(cand1) > len(cand3) and len(cand1) > len(cand4):
    winner = "Khan"
elif len(cand2) > len(cand1) and len(cand2) > len(cand3) and len(cand2) > len(cand4):
    winner = "Correy"
elif len(cand3) > len(cand1) and len(cand3) > len(cand2) and len(cand3) > len(cand4):
    winner = "Li"
elif len(cand4) > len(cand1) and len(cand4) > len(cand2) and len(cand4) > len(cand3):
    winner = "O'Tooley"


# In[ ]:



# Print out Summary
print("Election Results")
print("-----------------------")
print(f"Total Votes: {tot_votes}")
print("-----------------------")
print(f"Khan : {cand1_votes/tot_votes:.2f}% ({len(cand1)})")
print(f"Correy : {cand2_votes/tot_votes:.2f}% ({len(cand2)})")
print(f"Li : {cand3_votes/tot_votes:.2f}% ({len(cand3)})")
print(f"O'Tooley : {cand4_votes/tot_votes:.2f}% ({len(cand4)})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")


# In[ ]:


# Write updated data to a text file
election_results_output = "election_results_output.txt"
with open(election_results_output, 'w') as output:
    output.write(f"Election Results\n")
    output.write(f"-----------------------\n")
    output.write(f"Total Votes: {tot_votes}\n")
    output.write(f"-----------------------\n")
    output.write(f"Khan : {cand1_votes/tot_votes:.2f}% ({len(cand1)})\n")
    output.write(f"Correy : {cand2_votes/tot_votes:.2f}% ({len(cand2)})\n")
    output.write(f"Li : {cand3_votes/tot_votes:.2f}% ({len(cand3)})\n")
    output.write(f"O'Tooley : {cand4_votes/tot_votes:.2f}% ({len(cand4)})\n")  
    output.write(f"-----------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write(f"-----------------------\n")


# In[ ]:




