from tfw_uplink import TFWUplink
from crypto import PasswordHasher
from model import User
from errors import InvalidCredentialsError, UserExistsError


class UserOps:
    def __init__(self, username, password, db_session):
        self.username = username
        self.password = password
        self.db_session = db_session
        self._uplink = TFWUplink()

    def log(self, message):
        self._uplink.send_message({
            'key': 'message.send',
            'originator': 'webservice',
            'message': message
        })

    def authenticate(self):
        """
        Attempts to authenticate the user.
        Raises an exception on failure, does nothing on success.

        :raises InvalidCredentialsError:
            User does not exist or password provided is invalid
        """
        user = self.db_session.query(User).filter(
            User.username == self.username
        ).first()

        if not user or not PasswordHasher.verify(
                self.password,
                user.passwordhash
        ):
            self.log(
                f'Invalid credentials for '
                f'user "{self.username}"!'
            )
            raise InvalidCredentialsError

        self.log(f'User "{self.username}" logged in!')

    def register(self):
        """
        Attempts to register a user.
        Raises an exception of failure, does nothing on success.

        :raises UserExistsError:
            A user with the provided username already exists
        """
        existing_users = self.db_session.query(User).filter(
            User.username == self.username
        ).all()

        if existing_users:
            raise UserExistsError

        user = User(
            username=self.username,
            passwordhash=PasswordHasher.hash(self.password)
        )
        self.db_session.add(user)

        self.log(f'User "{self.username}" registered!')
