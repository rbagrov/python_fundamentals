# Environment setup

### Steps:
#### 1. Update dist packages
```
sudo apt-get update
```
#### 2. Upgrade dist packages
```
sudo apt-get upgrade
```
#### 3. Install course packages
```
sudo apt-get install git-core python-pip python3-pip virtualenv
```

# GIT setup

### Steps:
#### 0. If completely new to version control and GIT please checkout this quick guide:
[http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/)

#### 1. Check if you have git installed. If not: got back in environment setup
```
rbagrov@rbagrov:~/python_fundamentals$ git --version
git version 2.7.4
```
#### 2. Create account in [GitHub](https://github.com/join?source=header-home). (If you already have: ommit)
#### 3. GIT initial setup (If you already did: ommit):
```
git config --global user.name "Your Name Here"
git config --global user.email the_email_you_just_registerd_with_in_github@example.com
```
#### 4. Clone course repository:
```
git clone https://github.com/rbagrov/python_fundamentals.git
```
#### 5. Checkout (switch to) branch:
```
cd python_fundamentals
git checkout develop
```

# Python environment setup
### Steps
#### 1. Enter in your course local directory and execute
```
virtualenv -p python3 .env
```
#### 2. Enter in your pythin virtual environment
```
source .env/bin/activate
```
#### 3. Install whatever requirements we've setuped
```
pip install -r requirements.txt
```

# Please note what will be our development workflow:
* Always branch from latest develop !
```
git checkout develop
git pull
```
* Name your branches after your issue
```
git checkout -b issue/TAPC-120
```
* Commit descriptive messages with signoff
```
git commit -s -m "Added this, remove that, fixed this, refactored that"
```
* Check what you will push before you push it! Run your tests locally and check git status!
```
git status
```
* Avoid ammending commits
```
git commit --amend -s -m "Some message"
```
* Avoid pushing with force
```
git push origin issue/TAPC-120 -f
```
