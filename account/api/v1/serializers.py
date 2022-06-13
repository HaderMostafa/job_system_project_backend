from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '_all_'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username')
        )

        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError({'detail': 'passwords did not match'})

        user.set_password(self.validated_data.get('password'))
        user.save()

        return user