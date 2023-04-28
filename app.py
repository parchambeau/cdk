#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk.cdk_stack import CdkStack
from dotenv import load_dotenv
load_dotenv()


app = cdk.App()
CdkStack(app, "CdkStack",
   env=cdk.Environment(account=os.environ.get('AWS_ACCOUNT_ID'), region=os.environ.get('AWS_REGION'))
)

app.synth()
