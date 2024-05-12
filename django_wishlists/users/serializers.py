from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password as django_validate_password

from users.models import User
import logging

logger = logging.getLogger('M295_logger')


class UserSignupSerializer(ModelSerializer):
    """
    Serializer for user registration. Validates password and accepted_terms_and_conditions.
    """

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password', 'date_of_birth',
                  'accepted_terms_and_conditions']
        extra_kwargs = {'password': {'write_only': True},  # password write only
                        'accepted_terms_and_conditions': {'required': True}}  # terms and conditions required

    def validate_password(self, value):
        """
        Use django's built-in password validation
        """
        django_validate_password(value)
        return value

    def validate_accepted_terms_and_conditions(self, value):
        """
        Check if user has accepted terms and conditions
        :param value: boolean representing whether user has accepted terms and conditions
        :return: True if no error is raised
        :raises: serializers.ValidationError if value is False
        """
        if not value:
            raise serializers.ValidationError('You must accept the terms and conditions.')
        return value

    def create(self, validated_data):
        """
        Create a new user
        :param validated_data: validated data from the serializer
        :return: User object
        """
        user = User.objects.create_user(**validated_data)
        # use set_password to hash the password
        user.set_password(validated_data['password'])
        user.save()
        # log user creation
        logger.info(f'------------------------------------------\n'
                    f'User created successfully:\n'
                    f'{user.__str__()}'
                    f'\n------------------------------------------')
        return user
