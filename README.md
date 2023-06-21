# Amazon Rekognition Face Liveness

A sample code to implement Amazon Rekognition Face Liveness to detect real users and deter bad actors using spoofs in seconds during facial verification.

## What is Amazon Rekognition Face Liveness?
[Amazon Rekognition Face Liveness](https://aws.amazon.com/rekognition/face-liveness/) helps you verify that a user going through facial verification is physically present in front of a camera. It detects spoof attacks presented to a camera or trying to bypass a camera. Users can complete a Face Liveness check by taking a short video selfie where they follow a series of prompts intended to verify their presence.

We can easily add Face Liveness to the React web, native iOS, and native Android applications using open-source AWS Amplify SDKs.Face Liveness uses ML models trained on diverse datasets to support high accuracy across user skin tones, ancestries, and devices.

## Architecture

![RekognitionLivenessArchitectureDeveloperGuide_v2.jpg](https://docs.aws.amazon.com/images/rekognition/latest/dg/images/RekognitionLivenessArchitectureDeveloperGuide_v2.jpg)

## Components
Face Liveness uses multiple components:

* AWS Amplify SDK with FaceLivenessDetector component
* AWS SDKs
* AWS Cloud APIs


When we configure our application to integrate with Face Liveness feature, it uses the following API operations:

* CreateFaceLivenessSession - Starts a Face Liveness session, letting the Face Liveness detection model be used in your application. Returns a SessionId for the created session.

* StartFaceLivenessSession - Called by the AWS Amplify FaceLivenessDetector. Starts an event stream containing information about relevant events and attributes in the current session.

* GetFaceLivenessSessionResults - Retrieves the results of a specific Face Liveness session, including a Face Liveness confidence score, reference image, and audit images.

## Prerequisites


```sh
# Setup the AWS CLI
aws configure                                                                     
```

Locally installing on a workstation requires the following steps. 

1. Locally install AWS CDK as the [official documentation](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) describes.
2. [Bootstrap CDK for AWS Account](https://github.com/aws/aws-cdk/blob/master/design/cdk-bootstrap.md) 
3. Install Python >=3.6 from [python.org](http://python.org/)
4. Create a Python virtual environment
  ```sh
  python3 -m venv .venv                                      
  ```

5. Activate virtual environment
  On MacOS or Linux
  ```sh
  source .venv/bin/activate                                       
  ```
  On Windows
  ```sh
    .venv\Scripts\activate.bat                                        
  ```



## Solution Deployment

The [one-click.sh](https://github.com/aws-samples/amazon-rekognition-face-liveness/blob/main/one-click.sh) utility script is the recommended procedure for deploying a Rekognition Face Liveness(rfl) stack into an AWS Account.  It automates every step including installing missing dependency and executing all Out-Of-Band (OOB) operations.  Additionally, there is support for upgrading existing environments and seamlessly handling any future requirements.  


This table enumerates the overridable environment variables.  The deployment script supports deploying multiple stacks within the same account and region (e.g., Prod and Dev in us-east-1).  Additionally, the default settings support 200M unique faces.  Please contact us at rekognition-identity-verification@amazon.com for instructions beyond this threshold.  Lastly, AWS CloudFormation requires the Amazon S3 bucket and deployment region are the same.  When these values differ the *create-stack* command fails with a descriptive error.

```sh

# Customers can deploy multiple instances to the same region (Prod vs Dev)
# If this value is not set then it defaults to 'Rfl-Prod'
# You control this functionality by setting the Landing Zone Name value
export RFL_STACK_NAME=Rfl-Prod

# Running this command will install any dependencies (brew, yum, or apt required)
# After preparing the local machine it will synthesize and deploy into your environment.
./one-click.sh
```


## How do I run the amplify app locally
#First create a .env.local file in the frontend directory with the following contents:

```
REACT_APP_ENV_API_URL=https://YOUR_API_GW_STAGE_URL
REACT_APP_IDENTITYPOOL_ID=AMAZON_COGNITO_IDENTITYPOOL_ID
REACT_APP_REGION=AMAZON_COGNITO_APP_REGION
REACT_APP_USERPOOL_ID=AMAZON_COGNITO_APP_USERPOOL_ID
REACT_APP_WEBCLIENT_ID=AMAZON_COGNITO_APP_WEBCLIENT_ID


```

#Install depedency and start the app

```
npm install
npm start

```


## How is the code organized


- [infra](infra).  CDK Automation for provisioning the environment(s)
  - [facelivenessbackend](infra/facelivenessbackend/).  The RFL backend
  - [frontend](infra/frontend/). React Frontend Web App infra for Amazon Rekognition Face Liveness
- [src](src).  The backing code for Lambdas functions and other compute constructs
  - [liveness-session-result](src/backend/start-liveness-session/).  Backent to start the Face Liveness Session
  - [liveness-session-result](src/backend/liveness-session-result/).  Backent to get the Face Liveness Session Result
  - [frontend](src/frontend).  React Frontend Web App for Amazon Rekognition Face Liveness


