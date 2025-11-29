import sys
import os

# Add project root to path
sys.path.append('/home/mb/projects/flix_app')

try:
    from api.service import Auth
    print("Successfully imported Auth class")
    
    auth = Auth()
    print("Successfully instantiated Auth class")
    
    # Check if attributes exist (name mangling applies)
    if hasattr(auth, '_Auth__base_url'):
        print("Attribute _Auth__base_url exists")
    else:
        print("ERROR: Attribute _Auth__base_url missing")
        
    if hasattr(auth, '_Auth__auth_url'):
        print("Attribute _Auth__auth_url exists")
    else:
        print("ERROR: Attribute _Auth__auth_url missing")

    # Check if get_token is a method
    if hasattr(auth, 'get_token') and callable(auth.get_token):
        print("Method get_token exists and is callable")
    else:
        print("ERROR: Method get_token missing or not callable")

except Exception as e:
    print(f"Verification failed with error: {e}")
