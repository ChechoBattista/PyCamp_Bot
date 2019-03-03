import logging


logger = logging.getLogger(__name__)


def is_admin(bot, update):
    """Checks if the user is authorized as admin"""
    authorized = ["WinnaZ", "sofide", "ArthurMarduk", "xcancerberox"]
    username = update.message.from_user.username

    if username not in authorized:
        logger.info("{} is not authorized as admin".format(username))
        bot.send_message(
            chat_id=update.message.chat_id,
            text="No estas Autorizadx para hacer esta acción"
        )
        return False
    else:
        logger.info("{} is authorized as admin".format(username))
        return True


def admin_needed(f):
    def wrap(*args):
        bot, update = args
        if is_admin(*args):
            f(*args)
    return wrap
