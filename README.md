# Amazon-Lex-Chatbot-code

### What is Amazon Lex?

> Amazon Lex is an AWS service for building conversational interfaces for applications using voice and text. Amazon Lex provides the deep functionality and flexibility of natural language understanding (NLU) and automatic speech recognition (ASR) so you can build highly engaging user experiences with lifelike, conversational interactions, and create new categories of products.


### Resources for creating own custom bot: 
1. [Using AWS Lambda Function guide](https://docs.aws.amazon.com/lexv2/latest/dg/lambda.html)
2. [Managing conversations](https://docs.aws.amazon.com/lexv2/latest/dg/using-conversations.html)
3. [Testing a bot using the console](https://docs.aws.amazon.com/lexv2/latest/dg/build-test.html)
4. [Examples of Amazon Lex Bots](https://docs.aws.amazon.com/lex/latest/dg/additional-exercises.html)

### Usage of my code
Right now, it just takes one slot by the name of **Location** and then the Lambda function code present in this repo takes that arguement and pass it to an API for which tells the weather of that Location and return a **confirmIntent** message. I created it for test purpose to get idea of how to use Amazon Lex service. 

```Note: ``` api_key is an environment variable in given Lambda code. So do update it in your Lambda console. 
