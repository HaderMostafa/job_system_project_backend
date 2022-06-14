from django.contrib.auth import get_user_model
from rest_framework import serializers

# from tag.serializers import TagSerializer
User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'type', 'allow_mail_notification', 'gender',
                  'date_of_birth', 'tags', 'cv', 'address', 'history']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            password=self.validated_data.get('password'),
            type=self.validated_data.get('type'),
            allow_mail_notification=self.validated_data.get('allow_mail_notification'),
            gender=self.validated_data.get('gender'),
            date_of_birth=self.validated_data.get('date_of_birth'),
            # tags=self.validated_data.get('tags'),
            cv=self.validated_data.get('cv'),
            address=self.validated_data.get('address'),
            history=self.validated_data.get('history'),

        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError({'detail': 'passwords did not match'})
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'allow_mail_notification', 'gender', 'date_of_birth', 'tags', 'cv',
                  'address', 'history']
        depth = 1


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'allow_mail_notification', 'gender', 'date_of_birth', 'tags', 'cv',
                  'address', 'history']
