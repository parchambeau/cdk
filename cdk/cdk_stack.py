from aws_cdk import (aws_ec2 as ec2, aws_ecs as ecs,aws_ecs_patterns as ecs_patterns, Stack)
from constructs import Construct
import os
from dotenv import load_dotenv
load_dotenv()


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create new VPC
        vpc = ec2.Vpc(self, "MicroservicesProjVPC",
            cidr="10.0.0.0/16",
        )

        # Create Fargate Service w/ load balancer (jaina)
        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MicroServicesProjFargateServiceJaina",
            vpc=vpc,
            cpu=256,                    
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                container_port=80,
                image=ecs.ContainerImage.from_asset(os.environ.get('JAINA_DOCKERFILE_PATH'))), # Build directly from Dockerfile
            memory_limit_mib=512,      
            public_load_balancer=True)  # Make public for access

        # Create Fargate Service w/ load balancer (arthas)
        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MicroServicesProjFargateServiceArthas",
            vpc=vpc,
            cpu=256,                    
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                container_port=80,
                image=ecs.ContainerImage.from_asset(os.environ.get('ARTHAS_DOCKER_FILE_PATH'))), # Build directly from Dockerfile
            memory_limit_mib=512,      
            public_load_balancer=True)  # Make public for access

        # Create Fargate Service w/ load balancer (thrall)
        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MicroServicesProjFargateServiceThrall",
            vpc=vpc,
            cpu=256,                    
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                container_port=80,
                image=ecs.ContainerImage.from_asset(os.environ.get('THRALL_DOCKERFILE_PATH'))), # Build directly from Dockerfile
            memory_limit_mib=512,      
            public_load_balancer=True)  # Make public for access