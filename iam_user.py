import boto3


class IAMUser:
    def __init__(self):
        """
        Initializes an instance of IAMUser class.
        """
        self.iam = boto3.resource("iam")

    def create_user(self, username: str):
        """
        Creates a new IAM user.

        Args:
            username (str): The username of the IAM user.
        """
        user = self.iam.create_user(UserName=username)
        print(f"IAM user created: {username}, with ID {user.id}")

    def delete_user(self, username: str):
        """
        Deletes an IAM user.

        Args:
            username (str): The username of the IAM user.
        """
        user = self.iam.User(username)
        user.delete()
        print(f"IAM user deleted: {username}")

    def list_users(self):
        """
        Lists all IAM users.
        """
        for user in self.iam.users.all():
            print(user.name)

    def add_user_to_group(self, group_name: str, username: str):
        """
        Adds an IAM user to a group.

        Args:
            group_name (str): The name of the group.
            username (str): The username of the IAM user.
        """
        group = self.iam.Group(group_name)
        group.add_user(UserName=username)
        print(f"IAM user added to group: {username} -> {group_name}")

    def remove_user_from_group(self, group_name: str, username: str):
        """
        Removes an IAM user from a group.

        Args:
            group_name (str): The name of the group.
            username (str): The username of the IAM user.
        """
        group = self.iam.Group(group_name)
        group.remove_user(UserName=username)
        print(f"IAM user removed from group: {username} -> {group_name}")

    def list_user_groups(self, username: str):
        """
        Lists the groups that an IAM user belongs to.

        Args:
            username (str): The username of the IAM user.
        """
        groups = self.iam.groups.filter(UserName=username)
        for group in groups:
            print(group.name)
 