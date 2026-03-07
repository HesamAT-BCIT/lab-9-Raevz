from flask import session


def get_current_user():
    """Return the logged-in user's UID from the session, or None."""
    if not session.get("logged_in"):
        return None
    return session.get("username")
