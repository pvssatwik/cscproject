# cscproject
![Screenshot (427)](https://github.com/pvssatwik/cscproject/assets/115912017/0fb19e30-a91f-42d7-8248-5cb43ccbb3d1)
To ensure seamless operation, there are a few essential stages involved in creating a Telegram bot that uses AWS to transform photos to text. In order to communicate with the bot, users must upload photographs to Telegram. These images are then immediately saved in an AWS S3 bucket. When an image is uploaded, Amazon Textract is used to initiate the text extraction process via AWS Lambda functions. This robust service reads the submitted photos, extracts the text, and gets everything ready for processing. After the text has been extracted, the Telegram bot formats it to make it readable before returning it to the users. A user-friendly experience where photographs are swiftly transformed to text and returned to users in a comfortable way is made possible by this seamless integration of services.

SERVICES USED
API GATEWAY:
With the help of AWS's API Gateway service, developers can efficiently design, implement, and maintain APIs—even on a massive scale. It serves as a conduit for communication between applications and backend services, managing functions like rate limitation, authentication, and authorisation. API Gateway streamlines communication by guaranteeing smooth interaction between clients and backend systems with support for both RESTful and WebSocket APIs.
AWS LAMBDA:
Developers can run code on AWS Lambda, a serverless computing platform from Amazon Web Services, without having to provision or manage servers. This software bills users only for the resources they use, dynamically adjusting capacity based on demand. Because of these features, AWS Lambda is perfect for applications that are easily scalable and event-triggered.
S3 BUCKET:
Amazon S3 (Simple Storage Service) is a cloud storage solution provided by AWS, designed to offer scalable, durable, and secure storage for various data types and applications. It includes features such as versioning, encryption, and customizable storage classes to accommodate diverse storage needs.
IAM:
With the help of the AWS service IAM (Identity and Access Management), administrators may securely manage authentication and authorization for users accessing resources.
DYNAMO DB:
AWS's DynamoDB is a fully managed NoSQL database designed for remarkable scalability and performance. It offers low latency, quick access to data, dynamic scaling in response to workload fluctuations, and support for flexible data models. Because of these characteristics, DynamoDB is perfect for a wide range of applications that require easy scaling and quick, reliable storage.
Steps for creating telegram bot that extracts image to text
Go to the S3 service in the AWS Console to begin the process of creating a new bucket. Choose the "Create a Bucket" option under the S3 service. Give the bucket a unique name. If public access is required, make sure that Object Ownership is set up with ACL Enabled and do not tick the Block Public Access option. To maintain track of several versions of stored items, enable bucket versioning. Lastly, to finish the procedure, click the create button. The bucket will be prepared for use upon creation.

![image](https://github.com/pvssatwik/cscproject/assets/115912017/dcb49ba3-4b55-45e5-b76a-02c437ece2f2)

Go to the IAM service in order to start the role creation process in the IAM Console. Next, choose "Create Role." Set the use case to "Lambda" and the trusted entity type to "AWS Service." Next, grant the required access by selecting "S3FullAccess," "AmazonDynamoDBFullAccess," and "LambdaFullAccess." Give the position a distinct and descriptive name that communicates its intended purpose. Finally, to complete the role creation process, click "Create Role".

![image](https://github.com/pvssatwik/cscproject/assets/115912017/36d7aecc-d939-4d18-bbc9-6c289c492c19)

![image](https://github.com/pvssatwik/cscproject/assets/115912017/99b1826b-b764-442f-abd4-58d2ac12f0e4)

Go to the Amazon Lambda Service and choose "Create Function." Give the function a name, select an existing role, set Python as the runtime, and click "Create Function."
Lambda Code that extracts the text from image

![image](https://github.com/pvssatwik/cscproject/assets/115912017/7fa864ba-03ea-4d11-89bf-50892de108c7)

Go to the DynamoDB console and select "Create Table" to begin the process of creating a table in the DynamoDB service. Give the table a name, specify a partition key, then click "Create" to continue.

![image](https://github.com/pvssatwik/cscproject/assets/115912017/f8d60942-59b9-4372-9e71-e6ce152ea433)

![image](https://github.com/pvssatwik/cscproject/assets/115912017/5e13f1f5-4cb0-4369-b8b8-90862b15a120)

![image](https://github.com/pvssatwik/cscproject/assets/115912017/1b7a265a-de0d-4015-b891-83fab312e269)

OUTPUT

![image](https://github.com/pvssatwik/cscproject/assets/115912017/9793888f-fb2e-4574-970b-f0953ce64bb0)

![image](https://github.com/pvssatwik/cscproject/assets/115912017/da3fdf14-3b98-4c05-a4c9-06dc4a199f8d)

CONCLUSION
In conclusion, creating a Telegram bot that uses AWS services to translate photos to text offers a reliable and scalable solution. The functionality of the bot is improved by integrating services like Lambda for serverless computing and S3 for storage. Reliability is increased by AWS's security measures, which are controlled via IAM and error handling/logging through CloudWatch. Because of AWS's scalable and reasonably priced infrastructure, the bot can efficiently manage varying workloads while cutting down on operating expenses. All things considered, building a dependable and effective image-to-text conversion bot for Telegram is made possible by using AWS services.
