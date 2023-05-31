# Let's start with uploading a working directory to GitHub

# 1. track your folder 
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ git init 
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"

# 2. stage your changes
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ git add . 
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"

# 3. commit your changes
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ git commit -m "First Commit" 
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"

# 4. create your GitHub repository

# 5. upload the local folder
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ git remote add origin <repo-url>
### --->>>$ git push origin master
### --->>>$ git push --all "upload all branches"
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"

# Now, let's download a project from GitHub

# 1. fork any project to your account
# 2. copy the HTTPS link from the code tab
# 3. open a folder on your local machine and clone the project
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ git clone https://github.com/uodeeb/test01.git
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"

# 4. now, you can see a folder named test01m to work with it
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ cd test01
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"

# if there any changes in the remote project, you can update the project
# using a pull request 
"_--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--__--_--_"
### --->>>$ git pull origin master
