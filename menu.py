import pyttsx3
from googlesearch import search
from twilio.rest import Client
import cv2
import numpy as np
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.text import MIMEText
import time
from datetime import datetime
from instagrapi import Client
import time
import psutil
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import pymongo
import os
import time
import json
import urllib.request
import json
import boto3
import os

print()
print("\t\t\t\t---------------------------------------------------------------------------")
print("\t\t\t\t-------------------------welcome to menu tool------------------------------")
print("\t\t\t\t---------------------------------------------------------------------------")
print()

def speaker() :
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50) 
    text=input("enter the sentence you want to spell by your system:  ")
    engine.say(text)
    engine.runAndWait()
    
def search_query():
    query = input("enter the word: ")

    # Search for top 5 results
    results = search(query, num=5, stop=5)

    # Print the URLs
    for result in results:
      print(result)
    
def whatsapp():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='Hello preety',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918709554389'
)

    print(message.sid)
    print("message sent successfully!!")
    
def message():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='Hello preety, this is a test sms!',
    from_='+12054059248',
    to='+918709554389'
)

    print(message.sid)
    print("message sent successfully!!")
    
def call():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    call = client.calls.create(
    twiml='<Response><Say>Hello, this is a test call from Twilio!</Say></Response>',
    from_='+1 205 405 9248',
    to='+918709554389'
)

    print(call.sid)
    print("calling....")
    
    
    
def photo():
    cap = cv2.VideoCapture(0)
    status , photo = cap.read()
    cv2.imshow("preety Photo" , photo)
    print("your photo!!")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
    

def image():
    # Create a blank image (height, width, channels)
    height = 500
    width = 500
    channels = 3  # For RGB
    image = np.zeros((height, width, channels), dtype=np.uint8)

    # Define colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Draw a red rectangle
    cv2.rectangle(image, (50, 50), (200, 200), red, -1)  # -1 to fill the rectangle

    # Draw a green circle
    cv2.circle(image, (300, 300), 50, green, -1)  # -1 to fill the circle

    # Draw a blue line
    cv2.line(image, (0, 0), (500, 500), blue, 5)

    # Put some text
    cv2.putText(image, 'Hello, Numpy!', (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    # Display the image
    cv2.imshow('Custom Image', image)
    print("here is your custom image!!")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

    # Save the image
    cv2.imwrite('custom_image.png', image)
    
    
    
    
def email():

    # Replace the following with your details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'preetyprincess2212@gmail.com'
    sender_password = 'xsum hgtk poqm font'
    recipient_email = 'preety04fe@gmail.com'
    subject = 'Subject of the Email'
    body = 'This is the body of the email.'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the email server
    
        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
    
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()
        
        
        
        
def schedule_email():

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'preetyprincess2212@gmail.com'
    sender_password = 'xsum hgtk poqm font'
    recipient_email = 'preety04fe@gmail.com'
    subject = 'Subject of the Email'
    body = 'This is the body of the email.'

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Set the time to send the email
    send_time = datetime(2024, 7, 23, 12, 0, 5)  # Year, Month, Day, Hour, Minute, Second

    # Calculate the delay in seconds
    delay = (send_time - datetime.now()).total_seconds()

    # Wait until the specified time
    time.sleep(max(0, delay))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    
        print("email sent successfully!!")
        
 



def filter_image():
    def capture_photo():
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Error: Could not open webcam.")
                return
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                return
            cap.release()
            return frame
    def apply_filter(image):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            return edges
    def main():
            photo = capture_photo()
            if photo is None:
                return
            filtered_photo = apply_filter(photo)
            cv2.imshow('Original Photo', photo)
            cv2.imshow('Filtered Photo', filtered_photo)
            print("here is your filtered")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    if __name__ == "__main__":
                main()
            
            
            
def insta():
    USERNAME = 'cloud.learner'
    PASSWORD = 'Preety@123'
    IMAGE_PATH = r'C:\Users\HP\Downloads\world.jpeg'
    CAPTION = 'I posted this image using python'

    cl = Client()

    # Login to Instagram
    print("Logging in to Instagram...")
    try:
        cl.login(USERNAME, PASSWORD)
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # Try uploading the photo with retries in case of errors
    max_retries = 5
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            # Post the image with a caption
            print("Uploading photo to Instagram...")
            media = cl.photo_upload(IMAGE_PATH, CAPTION)
            print("Photo uploaded successfully.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Photo upload failed.")

    # Logout from Instagram
    cl.logout()
    print("Logged out from Instagram.")
    
    
    
    
def ram_read():
    # Get the total memory
    total_memory = psutil.virtual_memory().total

    # Get the available memory
    available_memory = psutil.virtual_memory().available

    # Get the used memory
    used_memory = psutil.virtual_memory().used

    # Get the percentage of used memory
    memory_percent = psutil.virtual_memory().percent

    print(f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {available_memory / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory_percent}%")
    
def launch_ec2_instance():
    ec2 = boto3.resource(
        'ec2',
        region_name='us-east-1',  # Specify your region
        aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your actual access key ID
        aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'  # Replace with your actual secret access key
    )
    try:
        instances = ec2.create_instances(
            ImageId='ami-0182f373e66f89c85',  # Replace with your AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='my-new-key-pair'  # Replace with your Key Pair name
        )
        print("EC2 instance launched:", instances)
    except Exception as e:
        print(f"Error launching EC2 instance: {e}")


    
def launch_rhel_instance():
    ec2 = boto3.resource(
        'ec2',
        region_name='us-east-1',  # Replace with your desired AWS region
        aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your Access Key ID
        aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'  # Replace with your Secret Access Key
    )
    try:
        instances = ec2.create_instances(
            ImageId='ami-0182f373e66f89c85',  # Replace with the RHEL AMI ID for the free tier
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',  # Replace with your desired instance type
            KeyName='my-new-key-pair',  # Replace with your key pair name
            SecurityGroupIds=['sg-028cce6448df06b62']  # Replace with your Security Group ID
        )
        print(f"RHEL instance launched: {instances[0].id}")
    except Exception as e:
        print(f"Error launching RHEL instance: {e}")



# Fetch log events
def fetch_log_events(log_group_name, log_stream_name):
    try:
        print("Fetching logs from CloudWatch...")
        
        response = client.filter_log_events(
            logGroupName=log_group_name,
            logStreamNames=[log_stream_name],
            limit=10  # Number of log events to retrieve
        )

        events = response.get('events', [])
        
        if events:
            print(f"Logs successfully retrieved from {log_group_name} and {log_stream_name}:")
            for event in events:
                print(f"Timestamp: {event['timestamp']}, Message: {event['message']}")
            print("Log retrieval completed successfully.")
        else:
            print(f"No logs found in {log_group_name} and {log_stream_name}.")
    
    except Exception as e:
        print(f"Error fetching logs: {e}")


        


def start_transcription(event):
    try:
        # Define the AWS region, S3 bucket, and file key
        bucket_name = 'hellobucket99'  # Replace with your actual bucket name
        object_key = 'hi.mp3.opus'     # Replace with the actual object key
        region_name = 'us-east-1'              # Replace with the correct S3 bucket region

        # Create Transcribe client
        transcribe_client = boto3.client(
            'transcribe',
            region_name=region_name,
            aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your access key
            aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'  # Replace with your secret key
        )
        # Create a unique job name using the current timestamp
        timestamp = int(time.time())
        job_name = f"transcription-{object_key.split('/')[-1].split('.')[0]}-{timestamp}"
        job_uri = f"s3://{bucket_name}/{object_key}"

        # Start the transcription job
        response = transcribe_client.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': job_uri},
            MediaFormat='mp3',  # Ensure the format matches your file type
            LanguageCode='en-US'
        )

        return job_name

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def check_transcription_status(transcribe_client, job_name):
    while True:
        response = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        status = response['TranscriptionJob']['TranscriptionJobStatus']

        if status == 'COMPLETED':
            print("Transcription job completed.")
            return response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        elif status == 'FAILED':
            print("Transcription job failed.")
            return None
        else:
            print("Transcription job still in progress. Checking again in 10 seconds...")
            time.sleep(10)


def get_transcription_text(transcript_uri):
    try:
        # Fetch the transcript from the provided URI
        with urllib.request.urlopen(transcript_uri) as response:
            transcript_data = json.loads(response.read())
            return transcript_data['results']['transcripts'][0]['transcript']

    except Exception as e:
        print(f"Error retrieving transcript: {str(e)}")
        return None





def lambda_handler(event, context):
    try:
        
        # Get the MongoDB URI from environment variables
        mongo_uri = os.getenv('mongodb+srv://preetyprincess2212:preetyprincess2212@cluster0.wxgls.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        # Connect to MongoDB
        client = pymongo.MongoClient(mongo_uri)
        print("Connected to MongoDB successfully!")

        # Access the database and collection
        db = client['Cluster0']  # replace with your database name
        collection = db['sample_mflix.comments']  # replace with your collection name

        # Insert a test document
        result = collection.insert_one({"message": "Hello from AWS Lambda via MongoDB Atlas!"})


        # Retrieve the inserted document
        document = collection.find_one({"_id": result.inserted_id})
        print(f"Retrieved document: {document}")

        # Return a success message with the inserted document
        return {
            'statusCode': 200,
            'body': {
                'inserted_id': str(result.inserted_id),
                'document': str(document)
            }
        }
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': str(e)
        }
    
# Testing locally
if __name__ == "__main__":
    test_event = {}  # Provide a mock event if needed
    test_context = {}  # Provide a mock context if needed
    result = lambda_handler(test_event, test_context)
    print(result)






def upload_file_to_s3(file_path, bucket_name, object_name=None):
    """
    Uploads a file to an S3 bucket.

    :param file_path: Local path to the file to upload
    :param bucket_name: S3 bucket to upload to
    :param object_name: S3 object name. If not specified then file_path is used
    :return: None
    """
    # If S3 object_name was not specified, use file_path
    if object_name is None:
        object_name = r'C:\Users\HP\Documents\New folder\link.txt'

    # Initialize S3 client with explicit credentials (not recommended for production)
    s3_client = boto3.client(
        's3',
        region_name='us-east-1',  # Replace with your AWS region
        aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your Access Key ID
        aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'    # Replace with your AWS secret key
    )



    try:
        # Upload the file
        print(f"Uploading file {file_path} to bucket {bucket_name} with object name {object_name}.")
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded successfully to bucket {bucket_name} as {object_name}.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except Exception as e:
        print(f"An error occurred: {e}")



    
    


def lambda_handler(event, context):
    print("Lambda function started.")
    print(f"Bucket Name: {BUCKET_NAME}, Email File Key: {EMAIL_FILE_KEY}, Sender Email: {SENDER_EMAIL}")

    try:
        # Get the object from S3 (file with email IDs)
        print("Fetching the file from S3...")
        s3_response = s3_client.get_object(Bucket=BUCKET_NAME, Key=EMAIL_FILE_KEY)
        email_data = s3_response['Body'].read().decode('utf-8')
        print(f"File fetched successfully from S3: {EMAIL_FILE_KEY}")


        # Extract email IDs from the file (one per line)
        email_ids = email_data.splitlines()
        print(f"Extracted email IDs: {email_ids}")

        # Send email to each ID
        for email in email_ids:
            if email:  # Only send to valid email lines
                print(f"Sending email to {email}...")
                send_email(email)
                
        print("All emails processed.")
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully processed {len(email_ids)} emails.')
        }
        
    except Exception as e:
        print(f"Error in Lambda function: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing the file or sending emails.')
        }


def send_email(recipient_email):
    try:
        # SES send email
        print(f"Preparing to send email to {recipient_email}...")
        response = ses_client.send_email(
            Source=SENDER_EMAIL,
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Subject': {
                    'Data': 'Your Subject Here',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': 'This is the body of the email. Customize as needed.',
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        print(f"Email sent to {recipient_email}: {response}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")



        

print("press 1: to Print any text and have it spoken aloud.")
print("""press 2: to Search for the top 5 results on Google.
press 3: to Send a WhatsApp message.
press 4: to Send a text message.
press 5: to Make a phone call.
press 6: to Post on Instagram.
press 7: to click a photo.
press 8: to Create a custom image.
press 9: to send an email.
press 10: to Schedule an email to be sent at a specific time.
press 11: to click a photo and apply filters in it.
press 12: to read the ram.
press 13: Launch EC2 Instance.
press 14: Launch RHEL GUI Instance.
press 15: Access Logs from EC2 Instance.
press 16: Upload audio to S3 triggers AWS Transcribe for automatic text conversion.
press 17: Connect to MongoDB using AWS Lambda.
press 18: Upload File to S3.
press 19: Send Emails from S3 File using SES.
press any key to exit""")
while True:
    opt=int(input("enter the option: "))
    if opt==1 :
        speaker()
    elif opt==2 :
        search_query()
    elif opt==3 :
        whatsapp()
    elif opt==4 :
        message()
    elif opt==5 :
        call()
    elif opt==6 :
        insta()
    elif opt==7 :
        photo()
    elif opt==8 :
        image()
    elif opt==9 :
        email()
    elif opt==10 :
        schedule_email()
    elif opt==11 :
        filter_image()
    elif opt==12 :
        ram_read()
    elif opt==13 :
        launch_ec2_instance()
    elif opt==14 :
        launch_rhel_instance()
    elif opt==15 :
        # AWS credentials and region
        aws_access_key_id = 'AKIAQYEI45ZJQVU2VMHI'
        aws_secret_access_key = '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'
        region_name = 'us-east-1'

        # Create a CloudWatch Logs client with explicit credentials and region
        client = boto3.client(
            'logs',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

        # Define the log group and log stream
        log_group_name = 'my-first-loggroup'
        log_stream_name = 'my-first-logstream'

        fetch_log_events(log_group_name, log_stream_name)
    elif opt==16 :
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {
                            'name': 'my-audio-files-bucket'
                        },
                        'object': {
                            'key': 'hi.mp3.opus'
                        }
                    }
                }
            ]
        }
    
        # Initialize the Transcribe client
        transcribe_client = boto3.client(
            'transcribe',
            region_name='us-east-1',  # Replace with your region
            aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your access key
                aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'  # Replace with your secret key
        )

        # Start transcription and get the job name
        job_name = start_transcription(event)
    
        if job_name:
            # Check for the transcription status and get the transcript file URI
            transcript_uri = check_transcription_status(transcribe_client, job_name)

            if transcript_uri:
                # Retrieve the transcription text
                transcription_text = get_transcription_text(transcript_uri)
                print("Transcription Text:")
                print(transcription_text)
            else:
                print("Failed to retrieve transcript.")
        else:
            print("Transcription job failed to start.")


        

    elif opt==17 :
        test_event = {}  # Provide a mock event if needed
        test_context = {}  # Provide a mock context if needed
        result = lambda_handler(test_event, test_context)
        print(result)

    elif opt==18 :
        file_path = r'C:\Users\HP\Documents\New folder\link.txt'  # Replace with your file path
        bucket_name = 'hellobucket88'     # Replace with your bucket name
        object_name = 'link.txt'    # Optional: replace with your desired S3 object name
        upload_file_to_s3(file_path, bucket_name, object_name=None)
    elif opt==19 :
        # Initialize S3 and SES clients with credentials for debugging
        s3_client = boto3.client(
            's3',
            region_name='us-east-1',  # Replace with your AWS region
            aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your Access Key ID
            aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'    # Replace with your AWS secret key
        )

        ses_client = boto3.client(
            'ses',
            region_name='us-east-1',  # Replace with your AWS region
            aws_access_key_id='AKIAQYEI45ZJQVU2VMHI',  # Replace with your Access Key ID
            aws_secret_access_key='PCIkjc6LiYPLRrgvamNFu/LKCVpRRJc9nBI4WZLG'    # Replace with your AWS secret key
        )

        # Environment variables for bucket name and email file path
        BUCKET_NAME = os.environ.get('BUCKET_NAME', 'hellobucket88')
        EMAIL_FILE_KEY = os.environ.get('EMAIL_FILE_KEY', 'email.txt')
        SENDER_EMAIL = os.environ.get('SENDER_EMAIL', 'preetyprincess2212@gmail.com')
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {
                            'name': 'my-audio-files-bucket'
                        },
                        'object': {
                            'key': 'hi.mp3.opus'
                        }
                    }
                }
            ]
        }
        context = {}

        lambda_handler(event, context)
        

    else:
        break