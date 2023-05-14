import boto3


class EC2Instance:
    def __init__(self):
        """
        Initializes an instance of EC2Instance class.
        """
        self.ec2 = boto3.resource("ec2")

    def create_instance(self, image_id: str, instance_type: str, key_name: str, security_group_ids: list, subnet_id: str):
        """
        Creates a new EC2 instance.

        Args:
            image_id (str): The ID of the AMI to use for the instance.
            instance_type (str): The type of the instance (e.g., 't2.micro').
            key_name (str): The name of the key pair to use for SSH access.
            security_group_ids (list): List of security group IDs to assign to the instance.
            subnet_id (str): The ID of the subnet in which to launch the instance.

        Returns:
            str: The ID of the created instance.
        """
        instance = self.ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            SubnetId=subnet_id,
            MinCount=1,
            MaxCount=1,
        )[0]
        print(f"New EC2 instance created: {instance.id}")
        return instance.id

    def start_instance(self, instance_id: str):
        """
        Starts a stopped EC2 instance.

        Args:
            instance_id (str): The ID of the instance to start.
        """
        instance = self.ec2.Instance(instance_id)
        instance.start()
        print(f"EC2 instance started: {instance_id}")

    def stop_instance(self, instance_id: str):
        """
        Stops a running EC2 instance.

        Args:
            instance_id (str): The ID of the instance to stop.
        """
        instance = self.ec2.Instance(instance_id)
        instance.stop()
        print(f"EC2 instance stopped: {instance_id}")

    def reboot_instance(self, instance_id: str):
        """
        Reboots a running EC2 instance.

        Args:
            instance_id (str): The ID of the instance to reboot.
        """
        instance = self.ec2.Instance(instance_id)
        instance.reboot()
        print(f"EC2 instance rebooted: {instance_id}")

    def terminate_instance(self, instance_id: str):
        """
        Terminates an EC2 instance.

        Args:
            instance_id (str): The ID of the instance to terminate.
        """
        instance = self.ec2.Instance(instance_id)
        instance.terminate()
        print(f"EC2 instance terminated: {instance_id}")

    def describe_instance(self, instance_id: str):
        """
        Describes an EC2 instance.

        Args:
            instance_id (str): The ID of the instance to describe.
        """
        instance = self.ec2.Instance(instance_id)
        response = instance.describe()
        print(response)

    def get_instance_state(self, instance_id: str):
        """
        Retrieves the state of an EC2 instance.

        Args:
            instance_id (str): The ID of the instance.

        Returns:
            str: The current state of the instance.
        """
        instance = self.ec2.Instance(instance_id)
        state = instance.state["Name"]
        print(f"EC2 instance state: {state}")
