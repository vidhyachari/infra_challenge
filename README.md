# infra_challenge

### Requirements
* Python3
* pip3
* localstack version 2.0.2

### Prerequisites

* Install LocalStack CLI on your local machine. Installation instructions
https://docs.localstack.cloud/getting-started/installation/#localstack-cli

* Make sure to sign up for AWS account free tier and get AWS key and AWS secret key. setup the creds using **aws credentials** command on your local machine 

* Once LocalStack is up and running, create an S3 bucket by making a POST request to the following URL: http://localhost:4566/2019-12-02/bucket/{bucket_name}

* Create bucket using POST with curl or POSTMAN or use the **create_bucket.py** pyton script that creates the bucket, folders and dummy files

curl -X POST 'http://localhost:4566/s3-vidhya-test''
curl -X POST 'http://localhost:4566/s3-vidhya-test'/deployhash112/' -H 'Content-Length: 0'

### Usage
* Install the python libs via pip
```
pip3 install -r requirements.txt
```

* Run the **cleanup_old_deployments.py** with an argument X such as:
```
python3 cleanup_old_deployments.py 4 --dry-run
```

Note: 
here 4 = # of old deployments to cleanup

* Run unit test with command

``` 
python3 test_cleanup_old_deployments.py 
```

### Questions
1. Where should we run this script? 
* Ideally the script can be run straight from command line/terminal window. The more elegant solution is to hook the script into a CI/CD system like Jenkins. You can create a cron job using a Jenkinsfile as below:

```
    pipeline {
    agent any
    triggers {
        cron('0 0 * * *')  // Run the job at midnight every day
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python /path/to/my/cleanup_old_deployments.py'
            }
        }
    }
}

```

2. How should we test the script before running it production?
* Run the script in a **Test** Environment first. Followed by **Staging** environment. Also a good option would be to take a backup of all the folders before running the script in Production. In case a folder gets accidentally deleted, can recover the same.
The script is codified to use **--dry-run** to ideally simulate what folders will be deleted.

3. If we want to add an additional requirement of deleting deploys older than 30 days while keeping X deployments. What additional changes would you need to make in the script?

* The logic would like something like modifying the main() function to calculate the creation date of each deployment folder and compare it with the current date. If the difference between the two dates is greater than 30 days, then the deployment folder should be deleted.