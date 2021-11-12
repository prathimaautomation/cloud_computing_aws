# Cloud Computing
- Cloud computing is the delivery of on-demand computing services -- from applications to storage and processing power -- typically over the internet and on a pay-as-you-go basis.

## Amazon Web Services (AWS)
- Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

### AWS Global Infrastructure
- The AWS Global Cloud Infrastructure is the most secure, extensive, and reliable cloud platform, offering over 200 fully featured services from data centers globally. Whether you need to deploy your application workloads across the globe in a single click, or you want to build and deploy specific applications closer to your end-users with single-digit millisecond latency, AWS provides you the cloud infrastructure where and when you need it.

### AWS Regions
- AWS has the concept of a Region, which is a physical location around the world where we cluster data centers. We call each group of logical data centers an Availability Zone. Each AWS Region consists of multiple, isolated, and physically separate AZs within a geographic area. 

### AWS Availability Zones (AZs)
- An Availability Zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. AZs give customers the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center.

### Public cloud - Private Cloud and Hybrid Cloud use cases
- IaaS : Infrastructure as a Service examples are DigitalOcean, Linode, Rackspace, Amazon Web Services (AWS), Cisco Metapod, Microsoft Azure, Google Compute Engine (GCE).
- PaaS : Platform as a Service examples are AWS Elastic Beanstalk, Windows Azure, Heroku, Force.com, Google App Engine, Apache Stratos, OpenShift.
- SaaS : Software as a Service examples are Google Workspace, Dropbox, Salesforce, Cisco WebEx, Concur, GoToMeeting.
  
- Cloud Data Centers: With a cloud data center, the actual hardware is managed and run by the cloud company in question, often with the help of a third-party managed services provider. Clients then run their applications and manage their data within a virtual infrastructure that runs on the cloud servers.

## AWS Services
- Elastic Compute Cloud `EC2` : Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment.
- Simple Storage Service `S3` : Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.
- Virtual Private Network `VPC` : 
- Internet Gateway `IG`
- Route Tables `RT`
- Subnets `sn`
- Network Access Control `NACLs`
- Security Groups `SG`
- Cloudwatch `CW`
- Simple Notification Service `SNS`
- Simple Queue Service `SQS`
- Load Balancers `LB` - Application `ALB` - Elastic `ELB` - Network `NLB`
- Autoscaling Groups `ASG`
- Amazon Machine Image `AMI`
- Dynamodb -Mongodb

# Launch ec2 instance

- ssh debugging
```
eval ssh-agent

ssh-add "keyfile.pem"
```
- update and upgrade system
- install nginx
- nginx enabled
- check the public ip globally
```
  sudo apt-get update -y
  sudo apt-get upgrade -y
  sudo apt-get install nginx -y
  sudo apt-get update -y
  sudo systemctl restart nginx
  sudo systemctl enable nginx
```
## 2 tier app deployment on the AWS
![]()

#### Setting up new AWS ec2 instance.
- Make sure to be logged in and have location set to ireland
- Setting up a new EC2 instance on AWS
- Navigate to ec2 dashboard and create new instance
- Choose Amazon Machine ubuntu server 16.04 (64-bit(x86) )
- Choose an instance type, we chose Family:t2, Type:t2micro etc
- Install instance details, change subnet to DevOpsStudent default 1a and    auto-assign public ip to enable
- Add storage default settings suffice
- Add Tags, key = Name and Value = devopsbootcamp_prathima_ExtraInfo
- Config Security Group (set up to allow specific access), Create new one with naming convention devopsbootcamp_Yourname_SG_ExtraInfo. type=ssh, port range = 22, source = MyIP.
- To have group access add another rule (inbound rules means you're allowing access to people coming in) and set: type = HTTP, port = 80, source= Anywhere
Because we have enabled public ip that means we need the http for anyone to access.
- Review instance launch. Just check everything is set up correctly
- LAUNCH
- Choose an existing key pair, Select a key pair = devopsbootcamp.pem (This key-file has been sent to us by our supervisor)
- You will be given an instance ID. You can find your instance if you go to ec2 dashboard and type the name of your instance in Filter instances

### SSH into new instance (make sure you have the devopsbootcamp key)
- Select your instance and click on connect. You will be provided with a few options on how to connect
- Go to ssh client
- Copy chmod... command to ensure your key is not publicaly viewable
- Open Gitbash terminal and open directory where devopsbootcamp.pem key is, in my case it is in my ssh folder.
- run `chmod 400 devopsbootcamp.pem` command in ssh directory. Only required to do once for new instance
- Now we need to connect to the machine using the key. Copy example line (ssh -i etc.) and paste in terminal. Allow continue connecting
(Adds key permanently into your hosts file in your machine)

### SSH into existing machine
- Find the instance, select it and press connect
- Copy and past the command in ssh directory

### Start/Stop instance
- Select an instance and select instance state and either select Start instance OR Stop instance

### Copy files from host to instance
- Copy app folder from: /c/Users/Prathima/multi-machine_virtualisation/starter-code to Instace

- In /starter-code directory, run:
`scp -i ~/.ssh/devopsbootcamp.pem -r app/ ubuntu@ec2-18-203-233-158.eu-west-1.compute.amazonaws.com:~/app/`
(The IP above is the public IP for that instance)
```
Where:
scp securly copies files
~/.ssh... is path to where to fetch the file
-r copy all items
app from this current location
ubuntu... copy to specific instance with public ip
:~/app/ where you want to copy it
Once copy complete, you should have app folder in the instance
```
### 2 tier architecture Sparta Global app setup
- Set up 2 instances,named app and db and follow steps from above creating ec1 instance and name them as devops_prathima_app and devops_prathima_db. 
- In app instance
```
#Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

#Install git
sudo apt-get install git -y

#Install nodejs
sudo apt-get install python-software-properties -y
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install nodejs -y

#Install pm2
sudo npm install pm2 -g

#Install nginx
sudo apt-get install nginx

#To allow public access to port 3000
```
- select devops_prathima_app instance in aws and click security -> Security groups -> Edit inbound rules -> add rule
Change port range = 3000, source = Anywhere IPv4
save rule and refresh page

### Open directoy app and run npm start
- To check if app is working, use your app public IP with the port
Reverse Proxy
- In devops_prathima_app instance, go to cd /etc/nginx/sites-available
Change default file to:
server {
    listen 80;

    server_name _;
    location / {
        proxy_pass http://18.203.233.158:3000; # app public ip
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

- Check nginx config `sudo nginx -t`
- Restart nginx `sudo systemctl restart nginx`
- Go to app directory and run `npm install ` & `npm start`

- If you load the app public ip without the post, you should get the app home page

### Install mongodb on devops_prathima_db instance
#### mongodb keys
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927 
echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update -y
sudo apt-get upgrade -y

# Install mongod and multiple packages
sudo apt-get install -y --allow-downgrades mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20

- Go to `cd /etc` and change `bindIp to 0.0.0.0` in `mongod.conf`
`sudo nano mongod.conf`
# Go back to home directory and run
# To restart and enable changes
sudo systemctl restart mongod
sudo systemctl enable mongod

- Good practice to check if mongod is running with: systemctl status mongod
```
### Create persistant variable in devops_prathima_app instance
- Make sure to use db public ip (in this case) to connect db and app
- To create a persistance variable, run: `sudo echo export DB_HOST="mongodb://34.243.86.240:27017/posts" >> ~/.bashrc`
- Need to run the source file to reload the information `source ~/.bashrc`
- To check if varaible exists, run `env` or `printenv DB_HOST`

### To give app access to db port 27017
- Open Security groups for devops_prathima_db instance and edit unbound rules
- Create new rule and change port range=27017 and source=18.203.233.158/32, where the ip is the public app ip
-save new rules

### Run app/posts
- In app terminal, in the app directory open seeds and run `npm install`
- Go back to app directory, run npm start and all should work
- To check it's working: `app_public_ip/posts` in browser

## Dealing with Demand
- Big advantage of AWS and similar cloud services is the ability to scale with traffic
- AWS does provide the ability to automatically scale with demand

#### Start with monitoring with Cloudwatch
- This raises when a level is reached
- Spin up autosclaing group
- A load balancer then rebalances the demand.
- It is also possible to deploy architecture in multiple availability zones to defend against potential data center problems.
- Have to create a listener group that checks machines are up and running.

#### Basics of Setting up monitoring
- When viewing an instance, select monitoring.

- This shows stats such as CPU utlisation percentage, disk write, and so forth

- Can add information to a dashboard, Note: need to enable detailed montioring under manage detailed monitoring * this does cost more, so use with caution

- add the monitoring to a dashboard of choice

- next, in instances, either select the + sign next to your instances "alarm status" field, or enter the alarm creation menu via actions -> monitor and troubleshoot ->Manage CloudWatch Alarms

- Name your alarm, and set the threshold you would like to be notified by

if you have an SNS group already set up, you can link it here

Otherwise, enter the Cloudwatch dashboard and edit the alarm

Add a new SNS group, and add the email addresses you would like to have notified when the alarm is triggered

You should now receive an email asking you to confirm the subscription

Congratulations, AWS will now let you know when your instance triggers an alarm!

Full guide to editing or setting up an alarm here

More on SNS groups here