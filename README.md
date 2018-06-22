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
