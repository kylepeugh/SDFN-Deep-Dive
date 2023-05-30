# working with Git on local machine
# 1. to start track any folder

"_______________________________________________________________________"
### --->>>$ git init
"_______________________________________________________________________"

# Now, a hidden folder named .Git was created inside of your working directory

# For Git, anything happen inside the working directory is a change even minor
# things like adding or removing a whitespace 
# 2. to create a file inside your working directory 

"_______________________________________________________________________"
### --->>>$ touch main.py
"_______________________________________________________________________"

# 3. now, we can add any code then, stage the changes

"_______________________________________________________________________"
### --->>>$ git add main.py

# to stage all the changes project-wise, use the period

### --->>>$ git add .
"_______________________________________________________________________"

# 4. to save these changes, commit them

"_______________________________________________________________________"
### --->>>$ git commit -m "First Commit"
"_______________________________________________________________________"

# 5. to check all commits 

"_______________________________________________________________________"
### --->>>$ git log

# the log will be multiple lines, to see all commits as one line

### --->>>$ git log --oneline --decorate --graph --all
"_______________________________________________________________________"

# 6. we can use status to check for any changes in your working directory

"_______________________________________________________________________"
### --->>>$ git status
"_______________________________________________________________________"

# 7. to start a new branch of development 

"_______________________________________________________________________"
### --->>>$ git branch new 
"_______________________________________________________________________"

# 8. to go to the new branch

"_______________________________________________________________________"
### --->>>$ git checkout new
"_______________________________________________________________________"

# 9. to chakout to a specific commit, we use the SHA id 

"_______________________________________________________________________"
### --->>>$ git log --oneline --decorate --graph --all
### --->>>$ git checkout f9b19ac
"_______________________________________________________________________"

# 10. to merge two branches master and new

"_______________________________________________________________________"
### --->>>$ git checkout master
### --->>>$ git merge new
"_______________________________________________________________________"
