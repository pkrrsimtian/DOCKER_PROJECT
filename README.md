# DOCKER_PROJECT
#righteducation #docker #vimaldaga #iiec_connect #iiec_rise  

#How To Setup This Environment

Step 1: Install Rhel8 Or Centos8 in physical or Virtual Machine 

Step 2: Configure Local YUM

Step 3: Install DOCKER_CE

      #yum install docker-ce --nobest

Step 4: Start Docker engine by this command

          For Temporary
        #systemctl start docker
         For Permanent
        #systemctl enable docker
        
Step 5: Run These Command To add services or port to firewall

        #firewall-cmd --permanent --zone=public --add-masquerade
        #firewall-cmd --zone=public --add-port=80/tcp
        #firewall-cmd --zone=public --add-port=443/tcp
         Reload firewall to apply permanent rules
        #firewall-cmd --reload
        
Step 6: Download Images by this Command

        #docker pull wordpress:5.1.1-php7.3-apache
        #docker pull mysql:5.7
        #docker pull mongo:4.0
        #docker pull rocket.chat
        
Step 7 :Download My Repository & launch your Environment by TUI program
        
         #git clone https://github.com/pkrrsimtian/DOCKER_PROJECT.git
         #cd DOCKER_PROJECT
         #cd project
         #python3 TUI.py
         
         
