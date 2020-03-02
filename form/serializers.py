from rest_framework import serializers

from form.models import Account


class LoginSerializer(serializers.ModelSerializer):
    email 	= serializers.EmailField(style={'input_type': 'email'})
    password = serializers.CharField(style={'input_type': 'password'},min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def authentication(self):
        email    = self.validated_data['email'],
        password = self.validated_data['password']
        get_user_ditels = Account.objects.filter(email=email[0]).values()
        user_password = get_user_ditels[0].get("password")
        if password == user_password:
            return True
        return False


class RegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['email', 'password']
		extra_kwargs = {
				'password': {'write_only': True,'min_length':8},
		}


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
                    password=self.validated_data['password']
				)
		account.save()
		return account
