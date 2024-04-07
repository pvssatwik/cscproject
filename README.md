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
