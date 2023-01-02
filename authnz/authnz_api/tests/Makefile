
tests: tests-env \
		0000-get-login-csrf \
		0010-login-user \
		0012-get-token \
		0020-logout-user

tests-env:
	env | sort

%:
	sleep 1
	@echo "Running test $@.sh"
	./$@.sh
