from flights import main
import boto3
import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime
import webbrowser
import tempfile
import textwrap
def lambda_handler(event, context):
    #return {
    #    'statusCode': 200,
    #    'body': main()
    #    print(main())
    #}
    #print("I am from Main Hellow World....")
    
    # Environment variables or hard-coded values
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
    sender = "roy777rajat@gmail.com"
    recipient = ["uk.rajatroy@gmail.com","anindita21bakshi@gmail.com"]
    region = "eu-west-1"

    subject = f"Emirates Flight Live Status from CCU to DXB {current_datetime}"

    # Your actual social profile links
    linkedin_url = "https://www.linkedin.com/in/royrajat/"
    medium_url = "https://medium.com/@uk.rajatroy"
    facebook_url = "https://facebook.com/rajat.ray.716/"
    github_url = "https://github.com/roy777rajat"

    # Icon URLs (SVGs or PNGs with transparent background)
    linkedin_icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
    medium_icon = "https://cdn-icons-png.flaticon.com/512/5968/5968885.png"
    facebook_icon = "https://cdn-icons-png.flaticon.com/512/733/733547.png"
    github_icon = "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"

    # Parse JSON
    rows = json.loads(main())
    headers = rows[0].keys()

    # Emirates logo URL
    logo_url = "https://imgur.com/a/5ez0raJ"



    # Email body in HTML
    body_html = textwrap.dedent(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Emirates Flight</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0; padding:0; font-family:Segoe UI, Tahoma, Geneva, Verdana, sans-serif; background:#f5f7fa;">
    <div style="background-color:#d71920; color:white; padding:16px; display:flex; align-items:center;">
        <h2 style="margin:0; font-size:20px;">Emirates Kolkata to Dubai Flight Information {current_datetime}</h2>
    </div>
    <div style="padding:16px; overflow-x:auto;">
        <table style="border-collapse:collapse; width:80%; min-width:500px; font-size:14px;">
            <thead>
                <tr>
                    {"".join(f'<th style="background-color:#d71920; color:white; padding:8px; border:1px solid #ccc; text-align:center;">{header.title()}</th>' for header in headers)}
                </tr>
            </thead>
            <tbody>
                {"".join(
                    "<tr>" + "".join(
                        f'<td style="padding:8px; border:1px solid #ccc; background-color:#ffffff;">{row[header]}</td>'
                        for header in headers
                    ) + "</tr>"
                    for row in rows
                )}
            </tbody>
        </table>
    </div>
    <div style="background-color:#f0f0f0; text-align:center; padding:16px; font-size:13px; color:#555;">
        <p style="margin:0 0 8px 0;">Connect with me:</p>
        <a href="{linkedin_url}" target="_blank" title="LinkedIn"><img src="{linkedin_icon}" alt="LinkedIn" style="width:28px; height:28px; margin:0 6px;"></a>
        <a href="{medium_url}" target="_blank" title="Medium"><img src="{medium_icon}" alt="Medium" style="width:28px; height:28px; margin:0 6px;"></a>
        <a href="{facebook_url}" target="_blank" title="Facebook"><img src="{facebook_icon}" alt="Facebook" style="width:28px; height:28px; margin:0 6px;"></a>
    </div>
</body>
</html>
""")






    # Plain-text fallback
    body_text = "Hello from Lambda!\nThis is a plain-text fallback message."

    # Create SES client
    ses = boto3.client('ses', region_name=region)

    # Send the email
    try:
        response = ses.send_email(
            Source=sender,
            Destination={
                'ToAddresses': recipient
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': body_text,
                        'Charset': 'UTF-8'
                    },
                    'Html': {
                        'Data': body_html,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        # Current Date Time stamp
        print(f"Email sent at {current_datetime}")
        return {
            'statusCode': 200,
            'body': f"Email sent! Message ID: {response['MessageId']}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error sending email: {str(e)}"
        }